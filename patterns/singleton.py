# Ensure a class has only one instance and provide a global point of access to it.

# Use when there must by only one instance of a class.

class Person:
    __instance = None
    @staticmethod
    def getInstance():
        if Person.__instance == None:
            Person()
        return Person.__instance

    def __init__(self):
        if Person.__instance != None:
            raise Exception("This class is a singleton!")
        
        Person.__instance = self

def main():
    p = Person()
    print p
    
    same_p = p.getInstance()
    print same_p

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

    
