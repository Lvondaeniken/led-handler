from led.led_manager import LedManager
from led.led_event import LedEvent
from led.animations import LedAnimations
from led.elements import LedElements
from led.color import LedColor

if __name__ == "__main__":
    led = LedManager(debug=True)
    led.run()
    color = LedColor(255, 0, 0)
    bg = LedColor(0, 0, 0)
    element = LedElements.BUMPER1
    animation = LedAnimations.SWITCH

    led.send_event(LedEvent(animation, element, color, bg, 1000))
