import random
import items
import world
import util



class Player():
    def __init__(self):
        self.inventory = [items.Light_Saber(), items.Gold(15)]
        self.hp = 100
        self.maxHp = 100
        self.location_x, self.location_y = world.Spaceship
        self.victory = False
        self.experience = 0
        self.level = 1
        self.nextLevelUp = 100
        self.chosenWPN = None
        self.CurrentWpn = self.inventory[0]
    def status (self):
        print (" You are level",self.level)
        print(" Current HP: ",self.hp)
        print(" Total XP: ",self.experience)
        print(" XP until next level up: {} XP\n". format (self.nextLevelUp - self.experience))
        
    def equip(self):
        print("These are the weapons you have in your inventory")

        Weapon_list = []
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                Weapon_list.append(item)
        i = 1
        for Weapon in Weapon_list:
            print(i,". ", Weapon.name, sep='')
            i+= 1
        while True:
            itemChoice = int(input("\n Select the weapon: ")) - 1
            if itemChoice not in range (0,len(Weapon_list)):
                print("\n Invalid weapon choice")
                continue
            break
        print('\n')
        print(Weapon_list[itemChoice].name,"equipped.\n")
        self.CurrentWpn = Weapon_list[itemChoice]


    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    def print_helth(self):
        print("your reaming health is",self.hp)
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
         if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
            self.experience += 50
            self.level += 1

            if self.level >= 2:
                print("You reached new level, you now have xp of {}".format(self.experience))


        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)

    def heal(self):
        print("\nThese are the potions you currently possess.\n")
        potion_list = []
        for potion in self.inventory:
            if isinstance(potion, items.Potions):
                if potion.amt <= 0:
                    self.inventory.remove(potion)
                    continue
                else:
                    potion_list.append(potion)
        i = 1
        for potion in potion_list:
            print(i, ". ", potion.name, sep="")
            i+=1
        while True:
            if len(potion_list) == 0:
                print("You have no potions.")
                # pause()
                return None

            itemChoice = int(input("""\nSelect a potion: """)) - 1
            if itemChoice not in range(0, len(potion_list)):
                print("\nInvalid choice")
                continue
            break
        self.healToPlayer(itemChoice, potion_list)

    def healToPlayer(self, itemChoice, potion_list):
        chosenPotion = potion_list[itemChoice]
        print("You ware healed for {}".format(chosenPotion.health))
        self.hp = self.hp + chosenPotion.health
        chosenPotion.amt = chosenPotion.amt -1
        if chosenPotion.amt == 0:
            self.inventory.remove(chosenPotion)
        #sound
            util.HealSound()

        if self.maxHp < self.hp:
            self.hp = self.maxHp


