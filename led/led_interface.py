from abc import ABC
from led.color import LedColor


class LedInterface(ABC):
    def setPixelColor(self, index: int, color: LedColor):
        ...

    def show(self):
        ...
