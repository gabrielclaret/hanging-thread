from game_object import GameObject
import pygame

class Leveler(GameObject):
    def __init__(self, x, y, color, width, height, collision_behavior = None, immortal = True):
        super(Leveler, self).__init__(x, y, color, width, height, collision_behavior, immortal)

    def update(self):
        pass