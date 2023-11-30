from led.color import LedColor
from led.animations import LedAnimations
from led.elements import LedElements

from dataclasses import dataclass


@dataclass
class LedEvent:
    animation: LedAnimations
    target: LedElements
    color: LedColor
    background: LedColor
    duration: int

    def get_target(self) -> LedElements:
        return self.target

    def get_color(self) -> LedColor:
        return self.color
