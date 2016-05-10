from Remote import Remote
from TV import TV
from DVD import DVD


class User(object):

    tv_remote = Remote
    dvd_remote = Remote

    def __init__(self, name):
        self.name = name

    def tv_switch(self, command):
        if command == "volume up":
            return self.tv_remote.volume_up(TV)
        elif command == "volum down":
            return self.tv_remote.volume_down(TV)
        elif command == "next":
            return self.tv_remote.channel_up(TV)
        elif command == "previous":
            return self.tv_remote.channel_down(TV)
        elif command == "tv_mood":
            return self.tv_remote.display_channel(TV)
        elif command == "dvd_mood":
            return self.tv_remote.display_dvd(TV)
        elif command == "off":
            return self.tv_remote.tv_off(TV)

    def dvd_switch(self, command):
        if command == "volume up":
            self.dvd_remote.volume_up(DVD)
        elif command == "volum down":
            self.dvd_remote.volume_down(DVD)
        elif command == "next section":
            self.dvd_remote.channel_up(DVD)
        elif command == "previous section":
            self.dvd_remote.channel_down(DVD)
        elif command == "load":
            self.dvd_remote.insert_dvd(DVD)
        elif command == "play":
            self.dvd_remote.play_dvd(DVD)
        elif command == "pause":
            self.dvd_remote.pause_dvd(DVD)
        elif command == "off":
            self.dvd_remote.dvd_off(DVD)
        return