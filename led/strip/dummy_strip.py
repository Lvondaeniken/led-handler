from led.led_interface import LedInterface
from led.color import LedColor


class DummyStrip(LedInterface):
    def __init__(self):
        print("starting dummy strip")

    def setPixelColor(self, index: int, color: LedColor):
        pass

    def show(self):
        pass
