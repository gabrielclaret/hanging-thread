from creature import Creature
import utils

class Player(Creature):
    def jump(self):
        self.is_in_platform = False
        self.jumping = True
        self.total_jump = utils.JUMP_HEIGHT