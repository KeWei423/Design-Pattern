from User import User
from DVD import DVD
from TV import TV
from unittest import TestCase
import unittest


class TestUser(TestCase):

    def test_user_tv(self):
        john = User("John")
        command = "tv_mood"
        john.tv_switch(command)

        self.assertEquals(john.name, "John")
        self.assertEquals(john.tv_switch(command), TV.tv_display(TV))

    def test_user_dvd(self):
        john = User("John")
        command = "pause"
        john.dvd_switch(command)

        self.assertEquals(john.dvd_switch(command), DVD.pause(DVD))




if __name__ == "____name__":
    unittest.main