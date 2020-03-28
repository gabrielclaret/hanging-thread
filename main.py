from game import g_game
import pygame
from monster import Monster
from leveler import Leveler 
from player import Player
from shoot_front import ShootFront
import utils
from walk_follow import WalkFollow
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

    #x, y, speed, color, width, height, direction, attack, max_health_points, shoot_cooldown, shoot_pattern, horizontal = True, immortal = False, collision_behavior = utils.DO_NOT_IGNORE
    player = Player(200, 800, utils.PLAYER_SPEED, (255, 0, 0), utils.PLAYER_WIDTH,
                    utils.PLAYER_HEIGHT, utils.RIGHT, utils.PLAYER_INITIAL_ATTACK, 
                    utils.PLAYER_INITIAL_HEALTH, utils.SHOOT_COOLDOWN, 
                    ShootFront(utils.SHOOT_RANGE, utils.SHOOT_SPEED, utils.SHOOT_COLOR, utils.SHOOT_WIDTH, utils.SHOOT_HEIGHT))
    player.teleport(200, 800)
    
    #x, y, speed, color, width, height, direction, shoot_cooldown, shoot_pattern, walk_pattern
    #range, speed, color, width, height
    #steps, speed
    
    #monster = Monster(700, 900, 0, (0, 255, 0), 150, 100, utils.RIGHT, 1, ShootFront(500, 5, (0, 0, 0), 10, 10), WalkStill(0))
    #monster.teleport(700, 900)

    #x, y, color, width, height, speed = 0, direction = 0, max_health_points = 1, horizontal = True, immortal = True, collision_behavior = utils.DO_NOT_IGNORE, walk_pattern = WalkStill()
    p1 = Leveler(0, 900, (0, 0, 255), 1000, 100)
    p2 = Leveler(0, 0, (0, 0, 255), 100, 1000)
    p3 = Leveler(900, 0, (0, 0, 255), 100, 1000)
    p4 = Leveler(0, 0, (0, 0, 255), 1000, 100)
    p5 = Leveler(400, 700, (0, 0, 255), 200, 100)
    #p6 = Leveler(600, 600, (0, 0, 255), 200, 100, None, True, 5, utils.RIGHT, True, WalkSymmetrical(100))

    #m1 = Monster(700, 800, 0, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.LEFT, 1000, ShootFront(500, 3, (0, 0, 0), 10, 10), WalkStill())
    #m1 = Monster(700, 800, 4, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.LEFT, 1000, ShootFront(500, 10, (0, 0, 0), 10, 10), WalkSymmetrical(50))
    #x, y, speed, color, width, height, direction, attack, max_health_points, shoot_cooldown, shoot_pattern, walk_pattern, horizontal = True, immortal = False, collision_behavior = utils.DO_NOT_IGNORE
    m1 = Monster(700, 800, 4, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, 
                 utils.LEFT, 1, 100, utils.SHOOT_COOLDOWN, ShootFront(500, 10, (0, 0, 0), 10, 10), WalkStill())
    m1.teleport(700, 800)

    while g_game.running:
        clock.tick(60)

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.die()

                break

        if not player.stunned:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                player.move(utils.LEFT)

            if pressed[pygame.K_RIGHT]:
                player.move(utils.RIGHT)

            if player.leveler is not None:
                if pressed[pygame.K_UP]:
                    player.jump()
                elif pressed[pygame.K_DOWN] and player.leveler.collision_behavior == utils.IGNORE_EXCEPT_ABOVE:
                    player.teleport(y = player.leveler.rect.bottom)

            if pressed[pygame.K_SPACE]:
                if (utils.current_milli_time() - player.internal_cooldown) >= 0:
                    player.shoot_pattern.fire()

                    player.internal_cooldown = utils.current_milli_time() + player.shoot_cooldown

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            obj.update()
            obj.draw()

        if g_game.monster_count == 0:
            print("Level cleared!")

        pygame.display.flip()

if __name__ == "__main__":
    main()