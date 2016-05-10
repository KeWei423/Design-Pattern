from Remote import Remote
from TV import TV
from DVD import DVD
from unittest import TestCase
import unittest


class TestTV(TestCase):

    def test_remote_tv(self):
        remote = Remote
        remote.volume_down(TV)
        remote.channel_down(TV)
        remote.channel_up(TV)

        self.assertEquals(remote.volume_down(TV), TV.volume)
        self.assertEquals(remote.channel_down(TV), TV.channel)
        self.assertEquals(remote.channel_up(TV), TV.channel)


    def test_remote_dvd(self):
        remote = Remote
        remote.channel_down(DVD)
        remote.channel_up(DVD)
        remote.volume_up(DVD)
        remote.volume_down(DVD)

        self.assertEquals(remote.volume_down(DVD), DVD.volume)
        self.assertEquals(remote.volume_up(DVD), DVD.volume)
        self.assertEquals(remote.channel_down(DVD), DVD.channel)
        self.assertEquals(remote.channel_up(DVD), DVD.channel)

    def test_screen(self):
        remote = Remote
        remote.display_channel(TV)
        remote.display_dvd(TV)

        self.assertEquals(remote.display_channel(TV), TV.tv_display())

        self.assertEquals(remote.display_channel(TV), TV.dvd_display())

    def test_dvd(self):
        remote = Remote
        remote.play_dvd(DVD)
        remote.pause_dvd(DVD)

        self.assertEquals(remote.play_dvd(DVD), DVD.play(DVD))
        self.assertEquals(remote.pause_dvd(DVD), DVD.pause(DVD))


if __name__ == "____name__":
    unittest.main