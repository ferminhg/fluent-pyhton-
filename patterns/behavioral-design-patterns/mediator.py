# Define an object that encapsulates how a set of objects interact. 
# Mediator promotes loose coupling by keeping objects from referring 
# to each other explicitly, and it lets you vary their interaction independently.

# Use when a set of objects communicate in structured but complex ways.

class TrafficTower:
    def __init__(self):
        self.airplanes = []

    def requestPositions(self):
        return list(map(lambda airplane: airplane.position, self.airplanes))
    
class Airplane:
    def __init__(self, position, trafficTower):
        self.position = position
        self.trafficTower = trafficTower
        self.trafficTower.airplanes.append(self)
    
    def requestPositions(self):
        self.trafficTower.requestPositions()


def main():
    airplane = Airplane(10, TrafficTower())
    #FIX why don't return list
    print(airplane.requestPositions())

if __name__ == "__main__":
    main()