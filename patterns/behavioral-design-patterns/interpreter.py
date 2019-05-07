# Given a language, define a representation for its 
# grammar along with an interpreter that uses the representation 
# to interpret sentences in the language.

# Use when you want to interpret given language and you can 
# represent statements as an abstract syntax trees.


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def pattern(self):
        return self.left.pattern() + self.right.pattern()


class Min:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def pattern(self):
        return self.left.pattern() - self.right.pattern()


class Num:
    def __init__(self, val):
        self.val = val

    def pattern(self):
        return self.val

def main():
    print(Sum(Num(1), Num(2))).pattern();
    print(Min(Num(1), Num(2))).pattern();
    
if __name__ == "__main__":
    main()