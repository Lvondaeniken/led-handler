from abc import ABC
from led.color import LedColor
from typing import Optional
from enum import Enum, auto


class LedAnimations(Enum):
    SWITCH = auto()
    BLINK = auto()
    WALK = auto()
    RAINBOW = auto()


class AnimationInterface(ABC):

    def get_next_frame(self) -> Optional[list[LedColor]]:
        ...
