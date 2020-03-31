from game import g_game
from hanging_thread import HangingThread
import pygame
from monster import Monster
from leveler import Leveler 
from player import Player
from shoot_front import ShootFront
import utils
from walk_follow import WalkFollow
from walk_symmetrical import WalkSymmetrical
from walk_still import WalkStill
import pygame_gui
import ui

def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((utils.WINDOW_WIDTH, utils.WINDOW_HEIGHT))
    pygame.display.set_caption("Hanging by a Thread")
    manager = pygame_gui.UIManager((utils.WINDOW_WIDTH, utils.WINDOW_HEIGHT), 'data/themes/theme_1.json')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(manager.get_theme().get_colour(None, None, 'dark_bg'))

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
    p1 = Leveler(0, 950, (35, 30, 15), 1000, 50)
    p2 = Leveler(0, 100, (35, 30, 15), 50, 900)   #left
    p3 = Leveler(950, 100, (35, 30, 15), 50, 900) #right
    p4 = Leveler(0, 100, (35, 30, 15), 1000, 50)  #top
    p5 = Leveler(400, 800, (35, 30, 15), 200, 50) #platform
    #p6 = Leveler(600, 600, (0, 0, 255), 200, 100, None, True, 5, utils.RIGHT, True, WalkSymmetrical(100))

    t1 = HangingThread(490, 0, 0, (255, 255, 0), 20, 100)
    t1.start_damage()

    #m1 = Monster(700, 800, 0, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.LEFT, 1000, ShootFront(500, 3, (0, 0, 0), 10, 10), WalkStill())
    #m1 = Monster(700, 800, 4, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, utils.LEFT, 1000, ShootFront(500, 10, (0, 0, 0), 10, 10), WalkSymmetrical(50))
    #x, y, speed, color, width, height, direction, attack, max_health_points, shoot_cooldown, shoot_pattern, walk_pattern, horizontal = True, immortal = False, collision_behavior = utils.DO_NOT_IGNORE
    m1 = Monster(700, 800, 4, (0, 255, 0), utils.PLAYER_WIDTH, utils.PLAYER_HEIGHT, 80, 
                 utils.LEFT, 1, 100, utils.SHOOT_COOLDOWN, ShootFront(500, 10, (0, 0, 0), 10, 10), WalkStill())
    m1.teleport(700, 800)
    
    while g_game.running:
        clock.tick(60)/1000.0
        
        coefficient = 2 #get weight_coefficient do hanging_thread.py

        screen.blit(background, (0, 0))
        ui.draw(coefficient, manager)
        manager.draw_ui(screen)

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

        if g_game.monster_weight == 0:
            print("Level cleared!")

        if not g_game.hanging_threads:
            player.die()

        pygame.display.flip()

if __name__ == "__main__":
    main()