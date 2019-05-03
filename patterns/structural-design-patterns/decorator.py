# Attach additional responsibilities to an object dynamically. 
# Decorators provide a flexible alternative to subclassing 
# for extending functionality.

# Use when you want to add extensions to an object 
# in runtime without affecting other objects.


class Pasta:
    def __init__(self):
        self.price = 0
    
    def getPrice(self):
        return self.price

class Penne(Pasta, object):
    def __init__(self):
        Pasta.__init__(self)
        self.price = 8


class PastaPattern(Pasta, object):
    def __init__(self, pasta):
        Pasta.__init__(self)
        self.pasta = pasta

    def getPrice(self):
        return self.pasta.getPrice() + 1.3

class SaucePattern(PastaPattern, object):
    def __init__(self, pasta):
        PastaPattern.__init__(self, pasta)
    
    def getPrice(self):
        return super(SaucePattern, self).getPrice() + 5
    
class CheesePattern(PastaPattern, object):
    def __init__(self, pasta):
        PastaPattern.__init__(self, pasta)
    
    def getPrice(self):
        return super(CheesePattern, self).getPrice() + 3

def main():
    pasta_penne = PastaPattern(Penne())
    print(pasta_penne.getPrice())
    pasta_penne_sauce = SaucePattern(Penne())
    print(pasta_penne_sauce.getPrice())
    pasta_penne_cheese = CheesePattern(Penne())
    print(pasta_penne_cheese.getPrice())



if __name__ == "__main__":
    main()

    