# Encapsulate a request as an object, thereby letting 
# you parameterize clients with different requests, 
# queue or log requests, and support undoable operations.

# Use when you have a queue of requests to handle or 
# you want to log them. Also when you want to have 
# an undo action.


class Cockpit:
    def __init__(self, instruction):
        self.instruction = instruction

    def execute(self):
        self.instruction.execute()


class Turbine:
    def __init__(self):
        self.speed = 0
        self.state = False
    
    def on(self):
        self.speed = 100
        self.state = True
    
    def off(self):
        self.speed = 0
        self.state = False
    
    def speedDown(self):
        if self.state == False:
            return
        
        self.speed -= 100


    def speedUp(self):
        if self.state == False:
            return
        
        self.speed += 100


class OnInstruction:
    def __init__(self, turbine):
        self.turbine = turbine

    def execute(self):
        return self.turbine.on()
        
class OffInstruction:
    def __init__(self, turbine):
        self.turbine = turbine

    def execute(self):
        return self.turbine.off()


class SpeedUpInstruction:
    def __init__(self, turbine):
        self.turbine = turbine

    def execute(self):
        return self.turbine.speedUp()

class SpeedDownInstruction:
    def __init__(self, turbine):
        self.turbine = turbine

    def execute(self):
        return self.turbine.speedDown()

        
def main():
    turbine = Turbine()
    turbine.on()
    turbine.speedUp()

    Cockpit(SpeedUpInstruction(turbine)).execute()

if __name__ == "__main__":
    main()
        