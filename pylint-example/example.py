"""
Pylint Tutorial
install: 
$pip install pylint
execute:
$pylint example.py
"""

#pylint: disable=too-few-public-methods
class Car:
    """Example class"""
    def __init__(self, color):
        self.color = color

MY_CAR = Car('blue')

def crash(car1, car2=None): #pylint: disable=unused-argument
    """Crash function"""
    car1.color = 'burnt'

crash(Car('red'))
