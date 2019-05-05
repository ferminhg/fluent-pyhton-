# Use sharing to support large numbers of fine-grained 
# objects efficiently.

# Use when an application uses a lot of small objects 
# and their storing is expensive or their identity 
# is not important.


class Color:
    def __init__(self, name):
        self.name = name

class colorCreator:
    def __init__(self):
        self.colors = {}

    def create(self, name):
        if self.colors.has_key(name) :
            return self.colors[name]

        self.colors[name] = Color(name)
        return self.colors.get(name)

def main():
    creator = colorCreator()
    black = creator.create('black')
    red = creator.create('red')
    print(black)
    print (creator.create('black'))

if __name__ == "__main__":
    main()