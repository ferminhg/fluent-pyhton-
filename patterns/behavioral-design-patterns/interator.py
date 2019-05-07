# Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

# Use when you want to access object's content without knowing how it is internally represented.

class Pattern:
    def __init__(self, elements):
        self.index = 0
        self.elements = elements
    
    def next(self):
        element = self.elements[self.index]
        self.index += 1
        return element

    def hastNext(self):
        return self.index < len(self.elements)


def main():
    listNumbers = Pattern([1, 2, 3])
    print(listNumbers.next())

if __name__ == "__main__":
    main()