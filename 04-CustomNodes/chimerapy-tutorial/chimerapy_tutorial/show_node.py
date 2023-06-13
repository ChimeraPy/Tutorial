from typing import Any, Dict, Optional, Tuple

import chimerapy as cp
import cv2
import numpy as np
from chimerapy_orchestrator import sink_node


@sink_node(name="ChimeraPyTutorial_ShowWindows")
class ShowWindows(cp.Node):
    """A node to show the video/images in a window.

    Parameters
    ----------
    name : str, optional (default: 'ShowWindow')
        The name of the node
    frames_key: str, optional (default: 'frame')
        The key to use for the frame in the data chunk
    **kwargs
        Additional keyword arguments to pass to the Node constructor
    """

    def __init__(
        self,
        name: str = "ShowWindow",
        frames_key: str = "frame",
        window_xy: Optional[Tuple[int, int]] = None,
        **kwargs,
    ) -> None:
        self.frames_key = frames_key
        self.window_xy = np.array(window_xy, dtype=int) if window_xy else None
        super().__init__(name=name, **kwargs)

    def step(self, data_chunks: Dict[str, cp.DataChunk]) -> None:
        for idx, (name, data_chunk) in enumerate(data_chunks.items()):
            frame = data_chunk.get(self.frames_key)["value"]
            maybe_metadata = data_chunk.get("metadata")
            window_id = self._get_window_id(
                name, maybe_metadata["value"] if maybe_metadata else None
            )

            cv2.imshow(window_id, frame)
            cv2.waitKey(1)

    def _get_window_id(self, src_name: str, metadata: Optional[Dict[str, Any]]) -> str:
        """Get the window id for the window to be shown."""
        window_id = src_name
        if metadata:
            src_id = metadata.get("source_id", "")
            if src_id:
                window_id = f"{src_name}_{src_id[0:6]}"

        return window_id

    def teardown(self) -> None:
        cv2.destroyAllWindows()
