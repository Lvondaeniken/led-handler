from typing import Optional
from led.animations import AnimationInterface
from led.color import LedColor
from led.time_base import TIMEBASE_MS


class BlinkingLight(AnimationInterface):
    def __init__(
        self,
        duration_s: int,
        freq_hz: int,
        led_count: int,
        color: LedColor,
        background: LedColor,
    ):
        self._color = color
        self._frames_to_survive = round(duration_s * 1000 / TIMEBASE_MS)
        self._half_period_frames = round(1000 / (2 * freq_hz * TIMEBASE_MS))
        self._led_count = led_count
        self._frame_counter = 0
        self._background_color = background
        self._led_states: list[LedColor]
        self._set_to_color(self._background_color)

    def __repr__(self):
        return (
            f"{self._frames_to_survive=}"
            f"{self._half_period_frames=}"
            f"{self._background_color=}"
            f"{self._color=}"
        )

    def get_next_frame(self) -> Optional[list[LedColor]]:
        if self._done():
            return None
        elif self._is_last_frame():
            self._set_to_color(LedColor(0, 0, 0))
            self._frame_counter += 1
        else:
            # check if half period has past
            if self._frame_counter % self._half_period_frames == 0:
                # check if it is an even or odd half period
                if (self._frame_counter / self._half_period_frames) % 2 == 0:
                    self._set_to_color(self._color)
                else:
                    self._set_to_color(self._background_color)
            self._frame_counter += 1
        return self._led_states

    def _done(self):
        return self._frame_counter > self._frames_to_survive

    def _is_last_frame(self):
        return self._frame_counter == self._frames_to_survive

    def _set_to_color(self, color: LedColor) -> None:
        led: list[LedColor] = []
        for _ in range(self._led_count):
            led.append(color)
        self._led_states = led
