from DVD import DVD
from unittest import TestCase
import unittest


class TestTV(TestCase):

    def test_volume(self):
        dvd = DVD
        dvd.volume_up(dvd)
        dvd.volume_down(dvd)

        self.assertEquals(dvd.volume_up(dvd), DVD.volume)
        self.assertEquals(dvd.volume_down(dvd), DVD.volume)

    def test_channel(self):
        dvd = DVD
        dvd.channel_up(dvd)
        dvd.channel_down(dvd)

        self.assertEquals(dvd.channel_up(), DVD.channel)
        self.assertEquals(dvd.channel_down(), DVD.channel)

    def test_play_pause(self):
        dvd = DVD
        dvd.play(dvd)
        dvd.pause(dvd)

        self.assertEquals(dvd.play(dvd), DVD.play(DVD))
        self.assertEquals(dvd.pause(dvd), DVD.pause(DVD))

    def test_read(self):
        dvd = DVD
        dvd.read_dvd(dvd)

        self.assertEquals(dvd.read_dvd(dvd), DVD.read_dvd(DVD))

if __name__ == "____name__":
    unittest.main