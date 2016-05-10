import abc


class EntertainmentDevice(object):
    __metaclass__ = abc.ABCMeta

    volume = 10
    channel = 1

    def __init__(self):
        pass

    def volume_up(self):
        self.volume += 1
        print("Volume: {0}".format(self.volume) )

    def volume_down(self):
        self.volume -= 1
        print("Volume: {0}".format(self.volume))
        return

    def channel_up(self):
        self.channel += 1
        print("Channel: {0}".format(self.channel))
        return

    def channel_down(self):
        self.channel -= 1
        print("Channel: {0}".format(self.channel))
        return

    def on(self):
        pass

    def off(self):
        pass
