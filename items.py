# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt):
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Potions(Item):

    def __init__(self, name, description, value, health, amt):
        self.amt = amt  # attribute of the Gold class
        self.health = health
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealth: {}".format(self.name, self.description, self.value, self.health, self.amt)


class SmallPotion(Potions):
    def __init__(self):
        super().__init__(name="Small Postion", description="A Small Postion", value = 2, health=30, amt = 1)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

 
class Light_Saber(Weapon):
    def __init__(self):
        super().__init__(name="Light Saber",
                         description="A Light Saber.",
                         value=50,
                         damage=30)
class Projectile(Weapon):
    def __init__(self, name, description, value, damage, ammo):
        self.ammo = ammo
        self.damage = damage

        super().__init__(name, description, value, damage)
    def __str__(self):
        return "{}\n=====\n{}\n Value: {} \n Damage : {} \n Ammo : {}"\
            .format(self.name, self.description, self.value, self.damage, self.ammo)

class LaserGun(Projectile):
    def __init__(self):
        super().__init__(name="LaserGun",
                         description= "A Laser Gun",
                         value= 2,
                         damage= 60,
                         ammo=5)
    def sound(self):
        pass