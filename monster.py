from creature import Creature
from game import g_game
import pygame
from threading import Thread
import utils

class Monster(Creature):
    def __init__(self, x, y, speed, color, width, height, direction, shoot_cooldown, shoot_pattern, walk_pattern, horizontal = True, collision_behavior = None, immortal = False):
        super(Monster, self).__init__(x, y, speed, color, width, height, direction, shoot_cooldown, shoot_pattern, horizontal, collision_behavior, immortal)

        self.walk_pattern = walk_pattern
        self.walk_pattern.walker = self

        self.clock = pygame.time.Clock()

        thread = Thread(target = self.__think)
        thread.start()

    def update(self):
        collision = super(Monster, self).update()

        if not collision[0]:
            return

        collided_creature = collision[1]

        if self.walk_pattern.steps_remaining > 0:
            self.direction *= -1
            self.walk_pattern.steps_remaining = self.walk_pattern.steps

    def __think(self):
        while g_game.running:
            self.walk_pattern.step()

            if (utils.current_milli_time() - self.internal_cooldown) >= 0:
                self.shoot_pattern.fire()

                self.internal_cooldown = utils.current_milli_time() + self.shoot_cooldown

            self.clock.tick(60)