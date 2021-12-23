import items, enemies, actions, world, util
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.visited = 0
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewHealth())
        moves.append(actions.Heal())
 
        return moves


class Spaceship(MapTile):
    visited = 0
    def intro_text(self):

        if self.visited == 0:
            self.visited = self.visited + 1
            util.introart()
            return """
            You woke up in an abandoned Spaceship with strobing lights on the wall, and there are broken wires everywhere. 
            Four paths are visible, each equally dangerous and mysterious. There's a chance you might find the portal to Earth.
            """
        else:
            return""" 
            
            You already visited this room, move forward.
            
            """""


    def modify_player(self, player):
        #Room has no action on player
        pass


class Second_Spaceship(MapTile):
    visited = 0

    def intro_text(self):

        if self.visited == 0:
            self.visited = self.visited + 1

            return """
            You find yourself in an New Spaceship with strobing lights on the wall, and there are broken wires everywhere. 
            Four paths are visible, each equally dangerous and mysterious. There's a chance you might find the portal to Earth.
            """
        else:
            return """ 

            You already visited this room, move forward.

            """""

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.equip()]
        else:
            return self.adjacent_moves()

class EmptyPassage(MapTile):
    def intro_text(self):
        return """
        You are in an empty passage on the spaceship. Keep moving forward.
        
        
        """
 
    def modify_player(self, player):
        pass
 
class AlienRoom(EnemyRoom):

    def __init__(self, x, y):
        super().__init__(x, y, enemies.Alien())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Alien jumps down from its layer in front of you!
            """
        else:
            return """
            The corpse of a dead Alien rots on the ground.
            """


class CreatureRoom(EnemyRoom):

    def __init__(self, x, y):
        super().__init__(x, y, enemies.Creature())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             You found an Unknown Creature front of you!
             """
        else:
            return """
             The corpse of a dead Creature is on the ground.
             """


class FindLaserGun(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.LaserGun())

    visited  = 0
    def intro_text(self):

        if self.visited == 0:
            self.visited = self.visited + 1


            return """
            
               You notice a gun lying on the ground,
                It's a Laser Gun! You pick it up.
                
                """
        else:
            return """ 

             You already visited this room, move forward.

             """""


class FindPotionRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.SmallPotion())

    visited = 0

    def intro_text(self):

        if self.visited == 0:
            self.visited = self.visited + 1

            return """

                Your notice something shiny in the corner.
                It's a  Small Potion! You pick it up. and use it to heal yourself!

                """
        else:
            return """ 

             You already visited this room, move forward.

             """""


class FindLightsaber(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.LaserGun())
        util.Saberart()
    visited = 0

    def intro_text(self):

        if self.visited == 0:
            self.visited = self.visited + 1

            return """

               You notice something shiny in the corner...
                 It's a Light Saber! You pick it up.

                """
        else:
            return """ 

             You already visited this room, move forward.

             """""


class Portal(MapTile):
    util.Portal()
    def intro_text(self):
        return """
         Suddenly, you notice the light flashing brightly.

        Finally, You found the portal to the earth!!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
