from game import g_game
from game_object import GameObject
import pygame
import utils
from walk_still import WalkStill

class Leveler(GameObject):
    def __init__(self, x, y, color, width, height, speed = 0, direction = 0, max_health_points = 1, horizontal = True, immortal = True, collision_behavior = utils.DO_NOT_IGNORE, walk_pattern = WalkStill(), sprite = "data/sprites/player.png"):
        super().__init__(x, y, speed, color, width, height, direction, horizontal, max_health_points, immortal, collision_behavior, sprite)

        self.walk_pattern = walk_pattern
        self.walk_pattern.walker = self

        self.on_top = []

    def update(self):
        self.walk_pattern.step()
        #print("Leveler:" + "left " + str(self.rect.left) + " top " + str(self.rect.top) + " id " + str(self.id))
        old_rect = self.rect
        new_rect = self.rect.move(self.move_pos)
        #@if self.speed > 0:
           # print("Old: ", old_rect)
           #print("New: ", new_rect)
        collision = False

        for obj in g_game.objects.values():
            obj_rect = obj.rect

            if obj is self or not isinstance(obj, Leveler) or not new_rect.colliderect(obj_rect) or isinstance(self.walk_pattern, WalkStill):
                continue

            if old_rect.bottom <= obj_rect.top < new_rect.bottom:
                # Coming from above

                new_rect.bottom = obj_rect.top
            elif new_rect.top < obj_rect.bottom <= old_rect.top:
                # Coming from below

                new_rect.top = obj_rect.bottom
            elif new_rect.left < obj_rect.left:
                # Coming from left

                new_rect.right = obj_rect.left
            else:
                # Coming from right

                new_rect.left = obj_rect.right

            collision = True

            break

        if not collision:
            for obj in self.on_top:
                obj.move_as(self)
        else:
            self.direction *= -1
            self.walk_pattern.steps_remaining = self.walk_pattern.steps

        self.rect = new_rect

        pygame.event.pump()
            

