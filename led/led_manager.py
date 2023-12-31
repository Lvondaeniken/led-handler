from multiprocessing import Process, Queue
from time import sleep
from led.led_event import LedEvent
from led.color import LedColor
from led.elements import LedElements
from led.strip.strip import get_strip
from led.conf import LED_GROUPS
from led.time_base import TIMEBASE_MS


class LedManager(Process):
    def startup(self, debug: bool = False):
        self.debug = debug
        self.deamon = True
        self.toManager = Queue()
        self.fromManager = Queue()
        self.start()

    def send_event(self, event: LedEvent):
        self.toManager.put(event)

    def run(self):
        self.led_groups = LED_GROUPS
        self.leds = get_strip(debug=self.debug)

        while True:
            sleep(TIMEBASE_MS / 1000)
            self.check_new_events()
            self.update_leds()

    def update_leds(self):
        next_frame: list[LedColor] = []
        for group in self.led_groups.values():
            next_frame.extend(group.get_next_frame())
        for i in range(len(next_frame)):
            self.leds.setPixelColor(i, next_frame[i])
        self.leds.show()

    def check_new_events(self):
        while not self.toManager.empty():
            event: LedEvent = self.toManager.get()
            if event.target == LedElements.ALL:
                for group in self.led_groups.values():
                    group.add_event(event)
            else:
                self.led_groups[event.target].add_event(event)
