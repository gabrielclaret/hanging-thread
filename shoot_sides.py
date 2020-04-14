from game import g_game
from projectile import Projectile
from shoot import Shoot
import utils

class ShootSides(Shoot):
    def fire(self):
        shooter_attack = self.shooter.attack

        shooter_x = self.shooter.direction == utils.LEFT and self.shooter.rect.left or self.shooter.rect.right
        shooter_y = self.shooter.rect.top

        new_projectile_left = Projectile(shooter_attack, shooter_x + (utils.LEFT * self.width), shooter_y + self.height, self.range, self.speed, self.color, self.width, self.height, utils.LEFT, self.shooter, self.sprite)
        
        shooter_x = self.shooter.rect.right
        
        new_projectile_right = Projectile(shooter_attack, shooter_x + (utils.RIGHT * self.width), shooter_y + self.height, self.range, self.speed, self.color, self.width, self.height, utils.RIGHT, self.shooter, self.sprite)