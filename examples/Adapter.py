# Adaptee interface
class EuropeanSocket:
    def voltage(self): pass

    def live(self): pass
    def neutral(self): pass
    def earth(self): pass


class Socket(EuropeanSocket):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class USSocket:
    def voltage(self): pass

    def live(self): pass
    def neutral(self): pass


class Adapter(USSocket):
    _socket = None

    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self._socket.live()

    def neutral(self):
        return self._socket.neutral()


class ElectricKettle:
    #plug in
    _power = None

    def __init__(self, power):
        self._power = power

    def boil(self):
        if self._power.voltage() > 110:
            print ("Kettle on fire! ")
        else:
            if self._power.live() == 1 and self._power.neutral() == -1:
                print ("Coffee time!")
            else:
                print ("No Power")



def main():
    #plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    #make coffee
    kettle.boil()


if __name__ == "__main__":
    main()