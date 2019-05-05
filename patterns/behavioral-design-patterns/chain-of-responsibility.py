# Avoid coupling the sender of a request to its receiver 
# by giving more than one object a chance to handle 
# the request. Chain the receiving objects and pass 
# the request along the chain until an object handles it.

# Use when more than one object can handle a request and 
# that information is known in runtime.

from functools import reduce

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def addProduct(self, product):
        self.products.append(product)

class Discount:
    def calc(self, products):
        ndiscount = NumberDiscount()
        pdiscount = PriceDiscount()
        none = NoneDiscout()

        ndiscount.setNext(pdiscount)
        pdiscount.setNext(none)

        return ndiscount.execute(products)

class NumberDiscount:
    def __init__(self):
        self.next = None
    
    def setNext(self, fn):
        self.next = fn

    def execute(self, products):
        result = 0
        if len(products) > 3:
            result = 0.05
        return result + self.next.execute(products)

class PriceDiscount:
    def __init__(self):
        self.next = None
    
    def setNext(self, fn):
        self.next = fn

    def execute(self, products):
        result = 0
        total = reduce((lambda x, y: x + y), products)

        if total >= 500 :
            result = 0.1
        
        return result + self.next.execute(products)

class NoneDiscout:
    def execute(self, products):
        return 0


def main():
    products = [ 1000, 150, 200, 10]
    discount_calculated = Discount().calc(products)
    print(discount_calculated)

if __name__ == "__main__":
    main()