from EntertainmentDevice import EntertainmentDevice
from TV import TV
from DVD import DVD


class Remote(object):
    def __init__(self, device):
        self.device = EntertainmentDevice()
        return

    def volume_up(self):
        self.device.volume_up(self.device)
        return self.device.volume

    def volume_down(self):
        self.device.volume_down(self.device)
        return self.device.volume

    def channel_up(self):
        self.device.channel_up(self)
        return self.device.channel

    def channel_down(self):
        self.device.channel_down(self)
        return self.device.channel

    def display_channel(self):
        device = TV
        device.tv_display(device)
        return

    def display_dvd(self):
        device = TV
        device.dvd_display(device)
        return

    @staticmethod
    def insert_dvd(self):
        print("Insert DVD")
        return

    def play_dvd(self):
        device = DVD
        device.read_dvd(device)
        return

    def pause_dvd(self):
        device = DVD
        device.pause(DVD)
        return

    def tv_off(self):
        device = TV()
        device.off()
        return

    def dvd_off(self):
        device = DVD()
        device.off()
        return
