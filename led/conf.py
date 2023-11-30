from led.led_event import LedElements
from led.led_group import LedGroup

TIMEBASE_MS = 20

LED_GROUPS = {
    LedElements.BALLSHOOTER: LedGroup(24),
    LedElements.PIPES: LedGroup(63),
    LedElements.BOTTLE: LedGroup(1),
    LedElements.BUMPER1: LedGroup(12),
    LedElements.BUMPER2: LedGroup(12),
    LedElements.BUMPER3: LedGroup(12),
    LedElements.TARGET1: LedGroup(3),
    LedElements.TARGET2: LedGroup(3),
    LedElements.TARGET3: LedGroup(3),
}
