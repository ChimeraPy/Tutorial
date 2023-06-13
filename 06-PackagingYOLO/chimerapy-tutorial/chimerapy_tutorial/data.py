import numpy as np
from typing import List, Optional

from dataclasses import dataclass, field


@dataclass
class Frame:
    image: np.ndarray
    label: str
    bounding_boxes: Optional[List[np.ndarray]] = field(default=None)