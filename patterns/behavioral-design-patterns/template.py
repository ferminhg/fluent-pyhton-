# Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. 
# Template Method lets subclasses redefine certain steps of an algorithm without changing 
# the algorithm's structure.

# Use when you have to define steps of the algorithm once and let subclasses 
# to implement its behaviour.

class Tax(object):
    def calc(self, value):
        if (value >= 1000):
            value = self.overThousand(value)

        return self.complementaryFee(value)
    
    def complementaryFee(self, value):
        return value + 10


class Tax1(Tax):
    def __init__(self):
        return super(Tax1, self).__init__()

    def overThousand(self, value):
        return value * 1.1

class Tax2(Tax):
    def __init__(self):
        return super(Tax2, self).__init__()
    
    def overThousand(self, value):
            return value * 1.2

def main():
    tax1 = Tax1()
    tax2 = Tax2()

    print(tax1.calc(1111))
    print(tax2.calc(1111))

if __name__ == '__main__':
    main()
    