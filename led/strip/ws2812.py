from led.led_interface import LedInterface
from led.color import LedColor
import rpi_ws281x as ws


class WS2812(LedInterface):
    def __init__(self):
        self.led_count = 120  # Number of LED pixels.
        self.led_pin = 18  # GPIO pin connected to the pixels (18 uses PWM!).
        # LED signal frequency in hertz (usually 800khz)
        self.led_freq_hz = 800000
        self.led_dma = 10  # DMA channel to use for generating signal (try 10)
        self.led_brightness = 20  # Set to 0 for darkest and 255 for brightest
        # True to invert the signal (when using NPN transistor level shift)
        self.led_invert = False
        self.led_channel = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.strip = ws.PixelStrip(
            self.led_count,
            self.led_pin,
            self.led_freq_hz,
            self.led_dma,
            self.led_invert,
            self.led_brightness,
            self.led_channel,
        )
        self.strip.begin()

    def setPixelColor(self, index: int, color: LedColor):
        c = ws.Color(color.red, color.green, color.blue)
        self.strip.setPixelColor(index, c)

    def show(self):
        self.strip.show()
