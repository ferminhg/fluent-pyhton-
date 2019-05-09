# Represent an operation to be performed on the elements of an object structure. 
# Visitor lets you define a new operation without changing 
# the classes of the elements on which it operates.

# Use when an object structure includes many classes and you want to perform 
# an operations on the elements of that structure that depend on their classes.


def bonusPatter(employee):
    if isinstance(employee, Manager):
        employee.bonus = employee.salary * 2
        pass
    if isinstance(employee, Developer):
        employee.bonus = employee.salary
        pass
    # raise TypeError, "employee must be a Employee instance"

class Employee(object):
    def __init__(self, salary):
        self.bonus = 0
        self.salary = salary
    
    def accept(self, item):
        item(self)


class Manager(Employee):
    def __init__(self, salary):
        return super(Manager, self).__init__(salary)

class Developer(Employee):
    def __init__(self, salary):
        return super(Developer, self).__init__(salary)

def main():
    manager = Manager(10000)
    manager.accept(bonusPatter)
    
    developer = Developer(10000)
    developer.accept(bonusPatter)

if __name__ == "__main__":
    main()