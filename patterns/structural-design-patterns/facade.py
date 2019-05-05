# Provide a unified interface to a set of interfaces in a subsystem. 
# Facade defines a higher-level interface that makes the subsystem easier to use.

# Use when you want to provide a simple interface to a complex subsystem.

class ShopPattern:
    def __init__(self):
        self.discount = Discount()
        self.shipping = Shipping()
        self.fees = Fees()

    def calc(self, price):
        price = self.discount.calc(price)
        price += self.fees.calc(price)
        price += self.shipping.calc()
        
        return price

class Discount:
    def calc(self, value):
        return value * 0.9

class Shipping:
    def calc(self):
        return 5

class Fees:
    def calc(self, value):
        return value * 1.05

def main():
    shop = ShopPattern()
    print(shop.calc(6))

if __name__ == "__main__":
    main()