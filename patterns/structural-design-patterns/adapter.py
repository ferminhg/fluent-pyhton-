# Convert the interface of a class into another 
# interface clients expect. Adapter lets classes
# work together that couldn't otherwise because 
# of incompatible interfaces.

# Use when you want to use existing class but its 
# interface does not match the one you need.
class Soldier:
    def __init__(self, level):
        self.level = level

    def attack(self):
        return self.level * 1

class Jedi:
    def __init__(self, level):
        self.level = level
    
    def attackWithSaber(self):
        return self.level * 100

class JediPattern:
    def __init__(self, jedi):
        self.jedi = jedi

    def attack(self):
        return self.jedi.attackWithSaber()

def main():
    army = [Soldier(10), JediPattern(Jedi(10))]

    for soldier in army:
        print(soldier.attack())

if __name__ == "__main__":
    main()