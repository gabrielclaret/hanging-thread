from game import g_game
from game_object import GameObject
import pygame
import utils

class Creature(GameObject):
    def __init__(self, x, y, speed, color, width, height, direction):
        super(Creature, self).__init__()

        screen = pygame.display.get_surface()

        self.rect = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        self.area = screen.get_rect()

        self.speed = speed
        self.color = color
        self.direction = direction

        self.state = utils.STILL
        self.jumping = False
        self.is_in_platform = False

        self.__reinit()

        g_game.objects[self.id] = self

    def __reinit(self):
        self.move_pos = [0, 0]
        self.total_jump = 0

        if self.direction == utils.LEFT:
            self.rect.midleft = self.area.midleft
        elif self.direction == utils.RIGHT:
            self.rect.midright = self.area.midright

    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_left(self):
        self.move_pos[0] = -self.speed
        self.direction = utils.LEFT
        self.state = utils.MOVING

    def move_right(self):
        self.move_pos[0] = self.speed
        self.direction = utils.RIGHT
        self.state = utils.MOVING

    def update(self):
        if self.total_jump > 0:
            self.move_pos[1] = -utils.GRAVITY_UPWARDS
            self.total_jump -= utils.GRAVITY_UPWARDS
        elif self.jumping:
            self.move_pos[1] = utils.GRAVITY_DOWNWARDS

        new_rect = self.rect.move(self.move_pos)

        collide = False
        is_in_platform = False

        test_ground = new_rect.copy()
        test_ground.bottom += 1
        
        for obj in g_game.objects.values():
            if obj is self:
                continue

            if test_ground.colliderect(obj.rect):
                is_in_platform = True

                self.is_in_platform = True

            if not new_rect.colliderect(obj.rect):
                continue

            if self.jumping:
                if self.total_jump > 0:
                    self.total_jump = 0
                else:
                    self.is_in_platform = True

                    self.jumping = False
                    self.move_pos[1] = 0
                    
                    new_rect.y = obj.rect.y - 100

                    self.rect = new_rect

            collide = True
            break

        if not is_in_platform and self.is_in_platform:
            self.is_in_platform = False

        if not self.is_in_platform and not self.jumping:
            new_rect.move_ip((0, utils.GRAVITY_DOWNWARDS)) 

        if not collide:
            self.rect = new_rect

        pygame.event.pump()