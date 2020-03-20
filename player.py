from creature import Creature
import utils

class Player(Creature):
    def jump(self):
        self.total_jump = utils.JUMP_HEIGHT