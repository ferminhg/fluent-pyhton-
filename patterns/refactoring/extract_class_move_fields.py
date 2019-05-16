import warnings

class Pet:
    def __init__(self, name, age, *,
                 has_scales=False,
                 lays_eggs=False,
                 drinks_milk=False):
        self.name = name
        self.age = age
        self.treats_eaten = 0
        self.has_scales = has_scales
        self.lays_eggs = lays_eggs
        self.drinks_milk = drinks_milk

    def give_treats(self, count):
        self.treats_eaten += count
    
    @property
    def needs_head_lamp(self):
        return (
            self.has_scales and 
            self.lays_eggs and
            not self.drinks_milk)

# Step 1: extract animal from pet
class Animal:
    def __init__(self, *,
                has_scales=False,
                lays_eggs=False,
                drinks_milk=False):
        self.has_scales = has_scales
        self.lays_eggs = lays_eggs
        self.drinks_milk = drinks_milk

# step2: add / intro parameter object 
class Pet:
    def __init__(self, name, age,
                 animal=None, **kwargs):
        if kwargs and animal is not None:
            raise TypeError('Mixed usage')
        if animal is None:
            warnings.warn('Shold use Animal')
            animal = Animal(**kwargs)
        self.animal = animal
        self.name = name
        self.age = age
        self.treats_eaten = 0

    def give_treats(self, count):
        self.treats_eaten += count
    
    @property
    def needs_head_lamp(self):
        return (
            self.animal.has_scales and 
            self.animal.lays_eggs and
            not self.animal.drinks_milk)

    @property
    def has_scales(self):
        warnings.warn('use animal attribute')
        return self.animal.has_scales

    @property
    def lay_eggs(self):
        warnings.warn('use animal attribute')
        return self.animal.lays_eggs

    @property
    def drinks_milk(self):
        warnings.warn('use animal attribute')
        return self.animal.drinks_milks


animal = Animal(has_scales=True, lays_eggs=True)
pet = Pet('Gregory', 3, animal)

pet = Pet('Gregory', 3, has_scales=True, lays_eggs=True)
