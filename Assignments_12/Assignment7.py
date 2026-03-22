# @staticmethod and @classmethod
#
# Concepts demonstrated:
#   @staticmethod  : belongs to the class, no access to self or cls
#                    used for utility functions logically grouped with a class
#   @classmethod   : receives class (cls) as first argument instead of instance
#                    used for alternative constructors and class-level operations
#   __init__       : regular instance method for comparison

class Temperature:
    strUnit = "Celsius"  # class variable

    def __init__(self, fltValue):
        self.fltValue = fltValue

    # --- @staticmethod: utility conversion, needs no class or instance ---
    @staticmethod
    def CelsiusToFahrenheit(fltCelsius):
        return (fltCelsius * 9 / 5) + 32

    @staticmethod
    def FahrenheitToCelsius(fltFahrenheit):
        return (fltFahrenheit - 32) * 5 / 9

    @staticmethod
    def CelsiusToKelvin(fltCelsius):
        return fltCelsius + 273.15

    # --- @classmethod: alternative constructor (creates object from Fahrenheit) ---
    @classmethod
    def FromFahrenheit(cls, fltFahrenheit):
        fltCelsius = cls.FahrenheitToCelsius(fltFahrenheit)
        return cls(fltCelsius)

    # --- @classmethod: change class-level unit label ---
    @classmethod
    def SetUnit(cls, strNewUnit):
        cls.strUnit = strNewUnit

    def Display(self):
        print("Temperature : %.2f %s" % (self.fltValue, Temperature.strUnit))


class Counter:
    intCount = 0  # tracks how many objects exist

    def __init__(self, strLabel):
        self.strLabel = strLabel
        Counter.intCount += 1

    # @classmethod to read/reset the class variable
    @classmethod
    def GetCount(cls):
        return cls.intCount

    @classmethod
    def ResetCount(cls):
        cls.intCount = 0

    # @staticmethod: pure utility, no class/instance needed
    @staticmethod
    def IsValidLabel(strLabel):
        return len(strLabel) > 0 and strLabel.isalpha()

    def Display(self):
        print("Counter Label :", self.strLabel)


def main():
    print("=== Temperature: @staticmethod conversions ===")
    print("25°C in Fahrenheit : %.2f" % Temperature.CelsiusToFahrenheit(25))
    print("77°F in Celsius    : %.2f" % Temperature.FahrenheitToCelsius(77))
    print("25°C in Kelvin     : %.2f" % Temperature.CelsiusToKelvin(25))

    print()
    print("=== Temperature: @classmethod alternative constructor ===")
    objTemp1 = Temperature(100.0)           # from Celsius directly
    objTemp2 = Temperature.FromFahrenheit(212.0)  # from Fahrenheit
    objTemp1.Display()
    objTemp2.Display()

    print()
    print("=== Temperature: @classmethod changing class variable ===")
    Temperature.SetUnit("°C")
    objTemp1.Display()

    print()
    print("=== Counter: @classmethod and @staticmethod ===")
    print("Is 'Alpha' valid label?", Counter.IsValidLabel("Alpha"))
    print("Is '123'   valid label?", Counter.IsValidLabel("123"))

    objC1 = Counter("Alpha")
    objC2 = Counter("Beta")
    objC3 = Counter("Gamma")

    print("Total counters created:", Counter.GetCount())

    Counter.ResetCount()
    print("After reset, count is:", Counter.GetCount())

    objC1.Display()
    objC2.Display()
    objC3.Display()

if __name__ == "__main__":
    main()
