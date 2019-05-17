import warnings

# Step 1: extract age from pet


class Animal:
    def __init__(self, age=None, *,
                 has_scales=False,
                 lays_eggs=False,
                 drinks_milk=False):
        if age is None:
            warnings.warn('age not specified')
        self.age = age
        self.has_scales = has_scales
        self.lays_eggs = lays_eggs
        self.drinks_milk = drinks_milk

# step2: add / intro parameter object


class Pet:
    def __init__(self, name, maybe_age, maybe_animal=None):
        if maybe_animal is not None:
            warnings.warn('Put age on animal')
            self.animal = maybe_animal
            self.animal.age = maybe_age
        else:
            self.animal = maybe_age

        self.name = name
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

    @property
    def age(self):
        warnings.warn('use animal attribute')
        return self.animal.age

    @age.setter
    def age(self, new_age):
        warnings.warn('Assign animal.age')
        self.animal.age = new_age


animal = Animal(3, has_scales=True, lays_eggs=True)
pet = Pet('Gregory', animal)
