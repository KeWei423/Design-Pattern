from TV import TV
from unittest import TestCase
import unittest


class TestTV(TestCase):

    def test_volume(self):
        tv = TV
        tv.volume_up(tv)
        tv.volume_down(tv)

        self.assertEquals(tv.volume_up(tv), tv.volume)
        self.assertEquals(tv.volume_down(tv), TV.volume_down(TV))

    def test_channel(self):
        tv = TV
        tv.channel_up(tv)
        tv.channel_down(tv)

        self.assertEquals(tv.channel_up(tv), tv.channel)
        self.assertEquals(tv.channel_down(tv), tv.channel)


    def test_screen(self):
        tv = TV
        tv.tv_display(tv)
        tv.dvd_display(tv)

        self.assertEquals(tv.tv_display(tv), TV.tv_display(TV))
        self.assertEquals(tv.dvd_display(tv), TV.dvd_display(TV))


if __name__ == "____name__":
    unittest.main