# Allow an object to alter its behavior when its internal state changes. 
# The object will appear to change its class.

# Use when the object's behaviour depends on its state and its 
# behaviour changes in run-time depends on that state.

class OrderStatus(object):
    def __init__(self, name, nextStatus):
        self.name = name
        self.nextStatus = nextStatus

    def next(self):
        return self.nextStatus()


class WaitingForPayment(OrderStatus):
    def __init__(self):
        return super(WaitingForPayment, self).__init__('waitingForPayments', Shipping)

class Shipping(OrderStatus):
    def __init__(self):
        return super(Shipping, self).__init__('shipping', Delivered)

class Delivered(OrderStatus):
    def __init__(self):
        return super(Delivered, self).__init__('delivered', Delivered)


class Order():
    def __init__(self):
        self.pattern = WaitingForPayment()
    
    def nextPattern(self):
        self.pattern = self.pattern.next()


def main():
    order = Order()
    order.nextPattern()
    order.nextPattern()
    order.nextPattern()
    order.nextPattern()


if __name__ == "__main__":
    main()