from led.strip.dummy_strip import DummyStrip


def get_strip(debug: bool = True):
    if debug is True:
        return DummyStrip()
    else:
        from led.strip.ws2812 import WS2812
        return WS2812()
