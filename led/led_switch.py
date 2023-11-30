from led.animations import AnimationInterface
from led.color import LedColor
from typing import Optional


class LedSwitch(AnimationInterface):
    def __init__(self, color: LedColor, led_count: int):
        self.color = color
        self.led_count = led_count
        self.done = False

    def get_next_frame(self) -> Optional[list[LedColor]]:
        ret = []
        if self.done is False:
            for _ in range(self.led_count):
                ret.append(self.color)
            self.done = True
            return ret
        else:
            return None
