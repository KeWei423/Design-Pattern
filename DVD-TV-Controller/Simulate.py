from User import User
from Remote import Remote

# Situation: pretend that the tv is already on and Alice is watchng TV right now

class Simulation(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def run(self):
        print("Tv is on")
        alice = User("Alice")
        alice.tv_switch("volume up")
        alice.tv_switch("next")
        alice.tv_switch("next")

        print("\n")
        print("{} wants to watch DVD now".format(alice.name))
        alice.tv_switch("dvd_mood")
        alice.dvd_switch("load")
        alice.dvd_switch("play")

        print("\n")
        print("It's time for {} to go to bed".format(alice.name))
        alice.dvd_switch("pause")
        alice.dvd_switch("off")
        alice.tv_switch("tv_mood")
        alice.tv_switch("off")


