from creature import Creature
from game import g_game
import pygame
from threading import Thread
import utils

SHOOT_AHEAD = 0
SHOOT_BOTH_SIZES = 1

'''
WALK_STILL = 0
WALK_FOLLOW = 1
WALK_SYMMETRICAL = 2
'''

class Monster(Creature):
    def __init__(self, x, y, speed, color, width, height, direction, shoot_cooldown, shoot_pattern, walk_pattern, collision_behavior = None):
        super(Monster, self).__init__(x, y, speed, color, width, height, direction, collision_behavior)

        self.internal_cooldown = utils.current_milli_time() + shoot_cooldown
        self.shoot_cooldown = shoot_cooldown

        self.shoot_pattern = shoot_pattern
        self.shoot_pattern.shooter = self

        self.walk_pattern = walk_pattern
        self.walk_pattern.walker = self

        self.clock = pygame.time.Clock()

        thread = Thread(target = self.__think)
        thread.start()

    def __think(self):
        while g_game.running:
            self.walk_pattern.step()

            if (utils.current_milli_time() - self.internal_cooldown) >= self.shoot_cooldown:
                self.shoot_pattern.fire()

                self.cooldown = utils.current_milli_time() + self.shoot_cooldown

            self.clock.tick(60)