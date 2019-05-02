# Compose objects into tree structures to represent 
# part-whole hierarchies. Composite lets clients treat 
# individual objects and compositions of objects uniformly.

# Use when you want to represent hierarchies of objects.

class Equipment:
    price = 0
    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

class Pattern(Equipment):
    equipments = []
    def __init__(self):
        self.equipments = []
    
    def add(self, equipment):
        self.equipments.append(equipment)
    
    def getPrice(self):
        return sum([i.price for i in self.equipments])

class Cabbinet(Pattern):
    def __init__(self):
        self.setName('cabbinet')

class FloppyDisk(Pattern):
    def __init__(self):
        self.setName('Floppy Disk')
        self.price = 70

class HardDrive(Pattern):
    def __init__(self):
        self.setName('Hard Drive')
        self.price = 250

class Memory(Pattern):
    def __init__(self):
        self.setName('memory')
        self.price = 280

def main():
    computer = Pattern()

    computer.add(FloppyDisk())
    computer.add(HardDrive())
    computer.add(Memory())

    print(computer.getPrice())

if __name__ == "__main__":
    main()