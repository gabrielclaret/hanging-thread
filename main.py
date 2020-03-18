from game import g_game
import pygame
from monster import Monster
from gplatform import Platform 
from player import Player
from shoot_front import ShootFront
import utils
from walk_still import WalkStill

def draw(obj):
    if obj.rect is None or obj.color is None:
        return

    screen = pygame.display.get_surface()

    pygame.draw.rect(screen, obj.color or (0, 0, 0), obj.rect)

def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((utils.WINDOW_WIDTH, utils.WINDOW_HEIGHT))
    pygame.display.set_caption("Hanging by a Thread")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    #x, y, speed, color, width, height, direction
    player = Player(200, 800, 10, (255, 0, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.RIGHT)
    player.teleport(200, 800)
    
    #x, y, speed, color, width, height, direction, shoot_cooldown, shoot_pattern, walk_pattern
    #range, speed, color, width, height
    #steps, speed
    
    #monster = Monster(700, 900, 8, (0, 255, 0), 150, 100, utils.RIGHT, 1, ShootFront(500, 5, (0, 0, 0), 10, 10), WalkStill(0, 0))
    #monster.teleport(700, 900)

    #x, y, width, height, color
    p = Platform(0, 900, 1000, 100, (0, 0, 255))
    p2 = Platform(0, 0, 100, 1000, (0, 0, 255))
    p3 = Platform(900, 0, 100, 1000, (0, 0, 255))
    p4 = Platform(0, 0, 1000, 100, (0, 0, 255))

    while g_game.running:
        clock.tick(60)

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_game.running = False

                break

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.move_left()
        elif player.state == utils.MOVING and player.direction == utils.LEFT:
            player.move_pos = [0, 0]
            player.state = utils.STILL

        if pressed[pygame.K_RIGHT]:
            player.move_right()
        elif player.state == utils.MOVING and player.direction == utils.RIGHT:
            player.move_pos = [0, 0]
            player.state = utils.STILL

        if pressed[pygame.K_UP] and not player.jumping:
            player.jump()

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            obj.update()
            obj.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()