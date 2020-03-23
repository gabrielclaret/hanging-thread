from game import g_game
import pygame
from monster import Monster
from leveler import Leveler 
from player import Player
from shoot_front import ShootFront
import utils
from walk_symmetrical import WalkSymmetrical
from walk_still import WalkStill

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
    
    #monster = Monster(700, 900, 0, (0, 255, 0), 150, 100, utils.RIGHT, 1, ShootFront(500, 5, (0, 0, 0), 10, 10), WalkStill(0))
    #monster.teleport(700, 900)

    #x, y, color, width, height, collision_behavior = None, immortal = True, speed = 0, direction = None, horizontal = True, walk_pattern = WalkStill()
    p1 = Leveler(0, 900, (0, 0, 255), 1000, 100)
    p2 = Leveler(0, 0, (0, 0, 255), 100, 1000)
    p3 = Leveler(900, 0, (0, 0, 255), 100, 1000)
    p4 = Leveler(0, 0, (0, 0, 255), 1000, 100)
    #p5 = Leveler(400, 800, (0, 0, 255), 200, 200)
    #p6 = Leveler(600, 600, (0, 0, 255), 200, 100, None, True, 5, utils.RIGHT, True, WalkSymmetrical(5))

    #m1 = Monster(700, 800, 0, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.LEFT, 1000, ShootFront(500, 3, (0, 0, 0), 10, 10), WalkStill())
    m1 = Monster(700, 800, 4, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.LEFT, 1000, ShootFront(0, 0, (0, 0, 0), 0, 0), WalkSymmetrical(50))
    m1.teleport(700, 800)

    while g_game.running:
        clock.tick(60)

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_game.running = False

                break

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:

            if not player.stunned:
                player.move(utils.LEFT)

        elif player.state == utils.MOVING and player.direction == utils.LEFT:
            player.move_pos = [0, 0]
            player.state = utils.STILL

        if pressed[pygame.K_RIGHT]:

            if not player.stunned:
                player.move(utils.RIGHT)

        elif player.state == utils.MOVING and player.direction == utils.RIGHT:
            player.move_pos = [0, 0]
            player.state = utils.STILL

        if player.leveler is not None and not player.stunned:
            if pressed[pygame.K_UP]:
                player.jump()
            elif pressed[pygame.K_DOWN] and player.leveler.collision_behavior == utils.IGNORE_EXCEPT_ABOVE:
                player.teleport(y = player.leveler.rect.bottom)

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            obj.update()
            obj.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()