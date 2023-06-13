import datetime
import time
from typing import Optional, Union

import chimerapy as cp
import cv2
import imutils
import numpy as np
from chimerapy_orchestrator import sink_node, source_node


@source_node(name="ChimeraPyTutorial_Video")
class Video(cp.Node):
    """A generic video capture node.

    This can be used to capture a local webcam or a video from the local file system

    Parameters
    ----------
    name : str, optional (default: 'VideoNode')
        The name of the node
    width: int, optional (default: 640)
        The width of the video
    height: int, optional (default: 480)
        The height of the video
    video_src: Union[str, int], optional (default: 0)
        The video source. This can be a local file path or a webcam index
    frame_rate: int, optional (default: 30)
        The frame rate of the video, in frames per second
    frame_key: str, optional (default: 'frame')
        The key to use for the frame in the data chunk
    include_meta: bool, optional (default: False)
        Whether to include the metadata in the data chunk
    loop: bool, optional (default: False)
        Whether to loop the video when it reaches the end
    **kwargs
        Additional keyword arguments to pass to the Node constructor

    Notes
    -----
        The frame_rate is not guaranteed to be exact. It is only a best effort.

    ToDo: Research and Implement a proper frame rate limiter
    """

    def __init__(
        self,
        video_src: Union[str, int] = 0,
        name: str = "VideoNode",
        width: Optional[int] = 640,
        height: Optional[int] = 480,
        frame_rate: int = 30,
        frame_key: str = "frame",
        include_meta: bool = False,
        loop: bool = False,
        **kwargs,
    ) -> None:
        self.video_src = video_src
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.include_meta = include_meta
        self.frame_key = frame_key
        self.cp: Optional[cv2.VideoCapture] = None
        self.frame_count = 0
        self.sleep_factor = 0.95
        self.debug = kwargs.get("debug", False)
        self.loop = loop
        super().__init__(name=name, **kwargs)

    def setup(self) -> None:
        self.cp = cv2.VideoCapture(self.video_src)
        self.frame_count = 0

    def step(self) -> cp.DataChunk:
        data_chunk = cp.DataChunk()
        ret, frame = self.cp.read()

        if not ret:
            if self.loop:
                self.logger.info("Restarting video")
                if isinstance(self.video_src, str) and self.video_src.startswith(
                    "http"
                ):
                    self.cp.release()
                    self.cp = cv2.VideoCapture(self.video_src)
                else:
                    self.cp.set(cv2.CAP_PROP_POS_FRAMES, 0)

                ret, frame = self.cp.read()
            else:
                self.logger.error("Could not read frame from video source")
                h = self.height or 480
                w = self.width or 640
                frame = np.zeros((h, w, 3), dtype=np.uint8)
                cv2.putText(
                    frame,
                    "Read Error",
                    (h // 2, w // 2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )

        if self.width or self.height:
            frame = imutils.resize(frame, width=self.width, height=self.height)

        if self.debug:
            cv2.imshow(
                f"{self.name}_{self.id[0:6]}", frame
            )  # Will the window name be unique?
            cv2.waitKey(1)

        data_chunk.add(self.frame_key, frame, "image")

        if self.include_meta:
            data_chunk.add(
                "metadata",
                {
                    "width": self.width,
                    "height": self.height,
                    "source_id": self.id,
                    "source_name": self.name,
                    "frame_rate": self.frame_rate,
                    "frame_count": self.frame_count,
                    "belongs_to_video_src": bool(ret),
                },
            )

        # Sleeping
        if self.frame_count == 0:
            self.initial = datetime.datetime.now()
        else:
            current_datetime = datetime.datetime.now()
            delta = (current_datetime - self.initial).total_seconds()
            expected = self.frame_count / self.frame_rate
            sleep_time = expected - delta
            time.sleep(max(self.sleep_factor * sleep_time, 0))

        # Update
        self.frame_count += 1

        return data_chunk

    def teardown(self) -> None:
        self.cp.release()
        if self.debug:
            cv2.destroyAllWindows()
