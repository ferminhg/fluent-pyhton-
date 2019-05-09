#Define a one-to-many dependency between objects so that when one object 
# changes state, all its dependents are notified and updated automatically.

# Use when a change to one object requires changing others.

class Product():
    def __init__(self):
        self.price = 0
        self.actions = []
    
    def setBasePrice(self, val):
        self.price = val
        self.notifyAll()

    def register(self, observer):
        self.actions.append(observer)
    
    def unregister(self, observer):
        self.actions.remove(observer)

    
    def notifyAll(self):
        return [el.update(self) for el in self.actions]
    

class Fees:
    def update(self, product):
        product.price = product.price * 1.2
    

class Profit:
    def update(self, product):
        product.price = product.price * 2


def main():
    product = Product()
    product.register(Fees())
    product.register(Profit())
    product.setBasePrice(5)

if __name__ == "__main__":
    main()