# Decouple an abstraction from its implementation 
# so that the two can vary independently.
# Use when you want to avoid binding between abstraction
#  and its implementation if, for example, each of them must be selected in runtime.

class Printer:
    def __init__(self, ink):
        self.ink = ink

class EpsonPrinter(Printer):
    def printStr(self):
        return 'Printer: Epson, Ink: ' + self.ink.get()

class HPprinter(Printer):

    def printStr(self):
        return 'Printer: HP, Ink: ' + self.ink.get()

class Ink:
    def __init__(self, type):
        self.type = type

    def get(self):
        return self.type

class ArcrylicInk(Ink):
    def __init__(self):
        Ink.__init__(self, 'acrylic-based')

class AlcoholInk(Ink):
    def __init__(self):
        Ink.__init__(self, 'acohol-based')


def main():
    print(HPprinter(ArcrylicInk()).printStr())
    print(EpsonPrinter(AlcoholInk()).printStr())

if __name__ == "__main__":
    main()