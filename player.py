from creature import Creature
from monster import Monster
import utils

class Player(Creature):
    def update(self):
        collision = super(Player, self).update()

        if not collision[0]: 
            return

        collided_creature = collision[1]

        if isinstance(collided_creature, Monster):
            # invencible
            pass

    def jump(self):
        self.total_jump = utils.JUMP_HEIGHT