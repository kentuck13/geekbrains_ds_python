from datetime import datetime
import time


class TrafficLight:
    _color = 'red'

    def running(self):
        while True:
            print('Current traffic color is: %s' % self._color)
            if self._color == 'red':
                time.sleep(7)
                self._color = 'yellow'
            elif self._color == 'yellow':
                time.sleep(2)
                self._color = 'green'
            else:
                time.sleep(5)
                self._color = 'red'


TrafficLight().running()
