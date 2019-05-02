# Specify the kind of objects to create using a 
# prototypical instance, and create new objects 
# by copying this prototype.
# Use when classes to instantiate are available 
# only in runtime.

class Sheep:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def clone(self):
        return Sheep(self.name, self.weight)

def main():
    original_sheep = Sheep('Wop', 12)
    clone_sheep = original_sheep.clone()
    print(clone_sheep.name)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
