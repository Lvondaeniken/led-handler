from led.animations import AnimationInterface
from led.color import LedColor
from led.time_base import TIMEBASE_MS


class WalkingLight(AnimationInterface):
    def __init__(self, duration_s, led_count, color: LedColor):
        self.color = color
        self.duration_s = duration_s
        self.led_count = led_count
        self.frame_counter = 0
        self.frames_to_survive = self.duration_s * 1000 / TIMEBASE_MS
        self.frames_per_led = self.frames_to_survive / self.led_count
        self.on_index = 0
        self.background_color = LedColor(0, 0, 0)
        self.led_states = []
        for _ in range(self.led_count):
            self.led_states.append(self.background_color)

    def set_background(self, color):
        self.background_color = color
        for i in range(self.led_count):
            self.led_states[i] = self.background_color

    def get_next_frame(self):
        self.frame_counter += 1
        if self.frame_counter == self.frames_per_led:
            self.on_index += 1
            self.frame_counter = 0
        self.led_states[self.on_index] = self.color
        if self.on_index > 0:
            self.led_states[self.on_index - 1] = self.background_color
        return self.led_states
