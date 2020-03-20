from game import g_game
from projectile import Projectile
from shoot import Shoot
import utils

class ShootSides(Shoot):
    def fire(self):
        shooter_x = self.shooter.direction == utils.LEFT and self.shooter.rect.left or self.shooter.rect.right
        shooter_y = self.shooter.rect.top

        new_projectile_left = Projectile(shooter_x + (utils.LEFT * self.width), shooter_y + self.height, self.range, self.speed, self.color, self.width, self.height, utils.LEFT, self.shooter)
        
        shooter_x = self.shooter.rect.right
        
        new_projectile_right = Projectile(shooter_x + (utils.RIGHT * self.width), shooter_y + self.height, self.range, self.speed, self.color, self.width, self.height, utils.RIGHT, self.shooter)