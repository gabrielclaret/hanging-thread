from game import g_game
from game_object import GameObject
#from projectile import Projectile
import pygame
import utils

count = 0

class Creature(GameObject):
    def __init__(self, x, y, speed, color, width, height, direction, collision_behavior = None):
        super(Creature, self).__init__(x, y, color, width, height, collision_behavior)

        self.speed = speed
        self.direction = direction

        self.state = utils.STILL

        self.total_jump = 0

        self.leveler = None

        self.__reinit()

    def __reinit(self):
        self.move_pos = [0, 0]
        self.total_jump = 0

        if self.direction == utils.LEFT:
            self.rect.midleft = self.area.midleft
        elif self.direction == utils.RIGHT:
            self.rect.midright = self.area.midright

    def teleport(self, x = -1, y = -1):
        self.rect.x = x > -1 and x or self.rect.x
        self.rect.y = y > -1 and y or self.rect.y

    def move(self, direction):
        self.move_pos[0] = direction * self.speed
        self.direction = direction
        self.state = utils.MOVING

    def update(self):
        global count
        if self.total_jump > 0:
            self.move_pos[1] = -utils.GRAVITY_UPWARDS
            self.total_jump -= utils.GRAVITY_UPWARDS
        elif self.leveler is None:
            self.move_pos[1] = utils.GRAVITY_DOWNWARDS

        old_rect = self.rect
        new_rect = self.rect.move(self.move_pos)

        self.move_pos[1] = 0
        
        for obj in g_game.objects.values():
            if obj is self:
                continue

            obj_rect = obj.rect

            if not new_rect.colliderect(obj_rect) or self.collision_behavior == utils.IGNORE_ALWAYS or obj.collision_behavior == utils.IGNORE_ALWAYS:
                if self.leveler is obj:
                    obj_rect_raised = obj_rect.copy()
                    obj_rect_raised.top -= 1

                    if not new_rect.colliderect(obj_rect_raised):
                        self.leveler = None

                continue

            if old_rect.bottom <= obj_rect.top < new_rect.bottom:
                # Coming from above

                # Keep whole object stored in case destroyable levelers are implemented in the future.
                # UPDATE: Leveler object is now being used to handle levelers where collisions only happen above.
                self.leveler = obj

                new_rect.bottom = obj_rect.top
            elif obj.collision_behavior == utils.IGNORE_EXCEPT_ABOVE: continue
            elif new_rect.top < obj_rect.bottom <= old_rect.top:
                # Coming from below

                new_rect.top = obj_rect.bottom
            elif new_rect.left < obj_rect.left:
                # Coming from left

                new_rect.right = obj_rect.left
            else:
                # Coming from right

                new_rect.left = obj_rect.right

            # Player is jumping
            if self.total_jump > 0:
                # Stop jumping
                self.total_jump = 0

            break

        self.rect = new_rect

        pygame.event.pump()