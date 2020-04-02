from game import g_game
from game_object import GameObject
from leveler import Leveler
import pygame
import utils

class Creature(GameObject):
    def __init__(self, x, y, speed, color, width, height, direction, attack, max_health_points, shoot_cooldown, shoot_pattern, horizontal = True, immortal = False, collision_behavior = utils.DO_NOT_IGNORE):
        attack *= g_game.status_coefficient
        max_health_points *= g_game.status_coefficient

        super().__init__(x, y, speed, color, width, height, direction, horizontal, max_health_points, immortal, collision_behavior)

        self.speed = speed
        self.attack = attack
        self.shoot_cooldown = shoot_cooldown

        self.shoot_pattern = shoot_pattern
        self.shoot_pattern.shooter = self

        self.internal_cooldown = utils.current_milli_time()

        self.total_jump = self.knockback_total_distance = self.knockback_direction = 0

        self.reinit(x, y)

    def reinit(self, x, y):
        self.leveler = None
        self.stunned = False
        self.total_jump = 0
        
        if self.direction == utils.LEFT:
            self.rect.midleft = self.area.midleft
        elif self.direction == utils.RIGHT:
            self.rect.midright = self.area.midright

        self.teleport(x, y)

    def teleport(self, x = -1, y = -1):
        self.rect.x = x > -1 and x or self.rect.x
        self.rect.y = y > -1 and y or self.rect.y

    def knock_back(self, total_distance, direction):
        self.knockback_total_distance = total_distance
        self.knockback_direction = direction

        self.stunned = True

    def make_invencible(self, duration):
        self.invencible = True
        self.invencible_duration = utils.current_milli_time() + duration

    def update(self):
        if (utils.current_milli_time() - self.invencible_duration) >= 0:
            self.invencible = False

        if self.total_jump > 0:
            self.move_pos[1] = -utils.GRAVITY_UPWARDS
            self.total_jump -= utils.GRAVITY_UPWARDS
        elif self.leveler is None:
            self.move_pos[1] = utils.GRAVITY_DOWNWARDS

        if self.knockback_total_distance > 0:
            self.move_pos[0] = self.knockback_direction * utils.KNOCKBACK_PER_FRAME

            self.knockback_total_distance -= utils.KNOCKBACK_PER_FRAME
            
            if self.knockback_total_distance <= 0:
                self.stunned = False

        old_rect = self.rect
        new_rect = self.rect.move(self.move_pos)

        self.move_pos = [0, 0]

        collision = [False, None]
        
        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            obj_rect = obj.rect

            if obj is self or not new_rect.colliderect(obj_rect) or self.collision_behavior == utils.IGNORE_ALWAYS or obj.collision_behavior == utils.IGNORE_ALWAYS:
                if self.leveler is obj:
                    obj_rect_raised = obj_rect.copy()
                    obj_rect_raised.top -= 1

                    if not new_rect.colliderect(obj_rect_raised):
                        self.leveler.on_top.remove(self)
                        self.leveler = None

                continue

            if isinstance(obj, Leveler):
                if old_rect.bottom <= obj_rect.top < new_rect.bottom:
                    # Coming from above

                    # Keep whole object stored in case destroyable levelers are implemented in the future.
                    # UPDATE: Leveler object is now being used to handle levelers where collisions only happen above.
                    
                    self.leveler = obj
                    obj.on_top.append(self)
                        
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

            collision = [True, obj]

            break

        self.rect = new_rect

        pygame.event.pump()

        return collision