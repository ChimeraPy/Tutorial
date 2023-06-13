import time

import cv2
import chimerapy as cp
from typing import Union, Optional, Dict
from .data import Frame

from chimerapy_orchestrator import source_node, sink_node


@source_node(name="chimerapy_tutorial.VideoNode")
class VideoNode(cp.Node):
    def __init__(
        self,
        name: str = "VideoNode",
        frame_rate: int = 30,
        video_src: Union[int, str] = 0,
        debug: Optional[str] = None,
    ):
        self.video = None
        self.video_src = video_src
        self.frame_rate = frame_rate
        super().__init__(name=name, debug=debug)

    def prep(self):
        self.video = cv2.VideoCapture(self.video_src)

    def step(self) -> cp.DataChunk:
        time.sleep(1 / self.frame_rate)
        ret, frame = self.video.read()
        if not ret:
            return None
        if self.debug:
            cv2.imshow(self.name, frame)
            cv2.waitKey(1)

        ret_chunk = cp.DataChunk()
        ret_chunk.add(
            "frame",
            Frame(
                image=frame,
                label=f"{self.name}",
            ),
        )

        return ret_chunk

    def teardown(self):
        self.video.release()


@sink_node(name="chimerapy_tutorial.ShowWindow")
class ShowWindow(cp.Node):
    def __init__(
        self,
        name: str = "ShowWindow",
        frames_key: str = "frame",
        debug: Optional[str] = None,
    ):
        self.frames_key = frames_key
        super().__init__(name=name, debug=debug)

    def step(self, data_chunks: Dict[str, cp.DataChunk]) -> cp.DataChunk:
        for name, data_chunk in data_chunks.items():
            frame: Frame = data_chunk.get(self.frames_key)["value"]
            cv2.imshow(frame.label, frame.image)
            cv2.waitKey(1)


if __name__ == "__main__":
    video_node = VideoNode(video_src="./TestData/test1.mp4", debug="step")
    video_node.prep()
    time_now = time.time()
    while True:
        video_node.step()
        if time.time() - time_now > 10:
            break
    video_node.shutdown()
