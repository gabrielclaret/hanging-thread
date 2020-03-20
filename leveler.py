from game import g_game
from game_object import GameObject
import pygame
from walk_still import WalkStill

class Leveler(GameObject):
    def __init__(self, x, y, color, width, height, collision_behavior = None, immortal = True, speed = 0, direction = 0, horizontal = True, walk_pattern = WalkStill()):
        super(Leveler, self).__init__(x, y, speed, color, width, height, direction, horizontal, collision_behavior, immortal)

        self.walk_pattern = walk_pattern
        self.walk_pattern.walker = self

        self.on_top = []

    def update(self):
        self.walk_pattern.step()

        old_rect = self.rect
        new_rect = self.rect.move(self.move_pos)

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
            

