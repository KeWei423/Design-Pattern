class Cup:
    color = ""

    # the factory method
    def getCup(cupColor):
        if (cupColor == "red"):
            return RedCup()
        elif (cupColor == "blue"):
            return BlueCup()
        else:
            return None

class RedCup(Cup):
    color = "red"

class BlueCup(Cup):
    color = "blue"

#Test
redCup = Cup.getCup("red")
print( "%s(%s)" % (redCup.color, redCup.__class__.__name__))

blueCup = Cup.getCup("blue")
print ("%s(%s)" % (blueCup.color, blueCup.__class__.__name__))