class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Creature(Enemy):
    def __init__(self):
        super().__init__(name="Unknown Creature", hp=80, damage=15)

class Alien(Enemy):
    def __init__(self):
        super().__init__(name="Alien", hp=50, damage=15)