from EntertainmentDevice import EntertainmentDevice
from unittest import TestCase
import unittest


class TestEntertainmentClass(TestCase):

    def test_volume(self):
        device = EntertainmentDevice
        device.volume_up(device)
        device.volume_down(device)

        self.assertEquals(device.volume_up(device), EntertainmentDevice.volume)

        self.assertEquals(device.volume_down(device), EntertainmentDevice.volume)


    def test_channel(self):
        device = EntertainmentDevice
        device.channel_up(device)
        device.channel_down(device)

        self.assertEquals(device.channel_up(device), EntertainmentDevice.channel)
        self.assertEquals(device.channel_down(device), EntertainmentDevice.channel)


if __name__ == "____name__":
    unittest.main