from EntertainmentDevice import EntertainmentDevice


class TV(EntertainmentDevice):

    device_on = False
    device = EntertainmentDevice

    def __init__(self):
        self.device_on = True
    
    def volume_up(self):
        print("TV: ")
        super(TV, self).volume_up(EntertainmentDevice)
        return EntertainmentDevice.volume
    
    def volume_down(self):
        super(TV, self).volume_down(EntertainmentDevice)

    def channel_up(self):
        super(TV, self).channel_up(EntertainmentDevice)
        return EntertainmentDevice.channel

    def channel_down(self):
        super(TV, self).channel_down(EntertainmentDevice)
        return EntertainmentDevice.channel

    @staticmethod
    def tv_display(self):
        print("tv channel")

    @staticmethod
    def dvd_display(self):
        print("dvd channel")
    
    def off(self):
        self.device_on = False
        if self.device_on == False:
            print("TV is turned off")