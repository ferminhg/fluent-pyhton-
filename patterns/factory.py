# Define an interface for creating an object, 
# but let subclasses decide which class to instantiate. 
# Factory Method lets a class defer instantiation 
# to subclasses.

# use when a class wants its subclasses to decide 
# which object to create.

class TeslaPattern:
    def create(self, type):
        if type == 'ModelX':
            return Tesla(type, 108000, 300)
        if type == 'ModelS':
            return Tesla(type, 111000, 320)

class Tesla:
    def __init__(self, model, price, maxSpeed):
        self.model = model
        self.price = price
        self.maxSpeed = maxSpeed


def main():
    factory = TeslaPattern()
    teslaX = factory.create('ModelX')
    print(teslaX.model)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

