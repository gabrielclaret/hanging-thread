from creature import Creature
from monster import Monster
import utils

class Player(Creature):
    def jump(self):
        self.total_jump = utils.JUMP_HEIGHT

    def update(self):
        collision = super(Player, self).update()

        if not collision[0]: 
            return

        collided_creature = collision[1]

        if isinstance(collided_creature, Monster) and not self.invencible:
            # lose hp
            # self.lose_hp

            self.knock_back(utils.KNOCKBACK_TOTAL, self.direction * -1)
            self.make_invencible(utils.INVENCIBLE_DURATION)