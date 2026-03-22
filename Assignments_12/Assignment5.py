# Multiple Inheritance and Method Resolution Order (MRO)
#
# Concepts demonstrated:
#   Multiple inheritance : class inherits from two or more parent classes
#   MRO                  : Python resolves method calls left-to-right (C3 linearisation)
#   __mro__              : inspect the resolution order at runtime
#   Mixin pattern        : small reusable classes added via multiple inheritance

# --- Base classes ---
class Flyable:
    def Move(self):
        return "Flying through the air"

    def Describe(self):
        return "I can fly"


class Swimmable:
    def Move(self):
        return "Swimming through water"

    def Describe(self):
        return "I can swim"


class Walkable:
    def Move(self):
        return "Walking on land"

    def Describe(self):
        return "I can walk"


# --- Single parent ---
class Bird(Flyable):
    def __init__(self, strName):
        self.strName = strName

    def Display(self):
        print("Bird     :", self.strName)
        print("Movement :", self.Move())


# --- Multiple inheritance: Duck can fly, swim, and walk ---
class Duck(Flyable, Swimmable, Walkable):
    def __init__(self, strName):
        self.strName = strName

    # Python picks Flyable.Move() first (left-to-right MRO)
    # We override to combine all abilities
    def Move(self):
        return "Flying, swimming, and walking"

    def Display(self):
        print("Duck     :", self.strName)
        print("Movement :", self.Move())
        print("Flyable  :", Flyable.Describe(self))
        print("Swimmable:", Swimmable.Describe(self))
        print("Walkable :", Walkable.Describe(self))


# --- Mixin pattern ---
class LogMixin:
    def Log(self, strMessage):
        print("[LOG] %s : %s" % (self.__class__.__name__, strMessage))


class Fish(Swimmable, LogMixin):
    def __init__(self, strName):
        self.strName = strName

    def Display(self):
        self.Log("Display called")
        print("Fish     :", self.strName)
        print("Movement :", self.Move())


def main():
    print("=== Bird (single inheritance) ===")
    objBird = Bird("Eagle")
    objBird.Display()

    print()
    print("=== Duck (multiple inheritance) ===")
    objDuck = Duck("Donald")
    objDuck.Display()

    print()
    print("=== Fish (Swimmable + LogMixin) ===")
    objFish = Fish("Nemo")
    objFish.Display()

    print()
    print("=== MRO of Duck ===")
    for cls in Duck.__mro__:
        print(" ->", cls)

if __name__ == "__main__":
    main()
