from game import g_game
from projectile import Projectile
from shoot import Shoot
import utils

class ShootFront(Shoot):
    def fire(self):
        shooter_x = self.shooter.direction == utils.LEFT and self.shooter.rect.left or self.shooter.rect.right
        shooter_y = self.shooter.rect.top
        direction = self.shooter.direction

        new_projectile = Projectile(shooter_x + (direction * self.width), shooter_y + self.height, self.range, self.speed, self.color, self.width, self.height, direction, self.shooter)