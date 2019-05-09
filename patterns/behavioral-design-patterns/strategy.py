# Define a family of algorithms, encapsulate each one, and make them interchangeable. 
# Strategy lets the algorithm vary independently from clients that use it.

# Use when you have many classes that differ in their behaviour. Strategies allow 
# to configure a class with one of many behaviours.


class ShoppingCart():
    def __init__(self, discount):
        self.discount = discount
        self.amount = 0

    def checkout(self):
        return self.discount(self.amount)
    
    def setAmount(self, amount):
        self.amount = amount

def guestPattern(amount):
    return amount

def regularPattern(amount):
    return amount * 0.9

def premiumPattern(amount):
    return amount * 0.8

def main():
    cart = ShoppingCart(regularPattern)
    cart.setAmount(10)

    print(cart.checkout())

if __name__ == '__main__':
    main()
    

