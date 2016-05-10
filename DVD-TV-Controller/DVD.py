from EntertainmentDevice import EntertainmentDevice
from time import sleep

class DVD(EntertainmentDevice):

    device_on = False
    _play = False
    _pause = True

    def __init__(self):
        self.device_on = True

    def volume_up(self):
        super(DVD, self).volume_up(EntertainmentDevice)

    def volume_down(self):
        super(DVD, self).volume_down(EntertainmentDevice)

    def next(self):
        super(DVD, self).channel_up(EntertainmentDevice)

    def previous(self):
        super(DVD, self).channel_down(EntertainmentDevice)

    def play(self):
        self._play = True
        print("Playing DVD")
        self._pause = False

    def pause(self):
        self._pause = True
        print("Pause DVD")
        self._play = False

    def read_dvd(self):
        print("DVD Reading...")
        sleep(0.5)
        self.play(self)

    def off(self):
        self.device_on = False
        if self.device_on == False:
            print("DVD is turned off")
