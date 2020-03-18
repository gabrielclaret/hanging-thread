from game import g_game
from projectile import Projectile
from shoot import Shoot
import utils

class ShootSides(Shoot):
    def fire(self):
        shooter_x = self.shooter.direction == utils.LEFT and self.shooter.rect.left or self.shooter.rect.right
        shooter_y = self.shooter.rect.top

        new_projectile_left = Projectile(self.range, self.speed, self.color, self.width, self.height, shooter_x + (utils.LEFT * self.width), shooter_y + self.height, utils.LEFT, self.shooter)
        
        shooter_x = self.shooter.rect.right
        
        new_projectile_right = Projectile(self.range, self.speed, self.color, self.width, self.height, shooter_x + (utils.RIGHT * self.width), shooter_y + self.height, utils.RIGHT, self.shooter)

        g_game.objects[new_projectile_left.id] = new_projectile_left
        g_game.objects[new_projectile_right.id] = new_projectile_right