# Provide a surrogate or placeholder for another object to control access to it.

class Car:
    def drive(self):
        return 'driving'

class CarPattern:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        if self.driver.age < 18:
            return 'too young to drive'
        return Car().drive()

class Driver:
    def __init__(self, age):
        self.age = age
    
def main():
    print(CarPattern(Driver(18)).drive())
    print(CarPattern(Driver(11)).drive())

if __name__ == "__main__":
    main()