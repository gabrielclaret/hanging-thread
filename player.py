from creature import Creature
from game import g_game
from monster import Monster
import utils

class Player(Creature):
    def jump(self):
        self.total_jump = utils.JUMP_HEIGHT

    def die(self):
        print("Game over!")

        g_game.objects.clear()
        g_game.running = False

    def update(self):
        collision = super().update()

        if not collision[0]: 
            return

        collided_creature = collision[1]

        if isinstance(collided_creature, Monster) and not self.invencible:
            self.lose_health(collided_creature.attack)

            self.knock_back(utils.KNOCKBACK_TOTAL, self.direction * -1)
            self.make_invencible(utils.INVENCIBLE_DURATION)