from game import g_game
from hanging_thread import HangingThread
import pygame
from monster import Monster
from leveler import Leveler 
import xml_parser
from player import Player
import random
from shoot_front import ShootFront
from shoot_sides import ShootSides
from ui import UI
import utils
from walk_follow import WalkFollow
from walk_symmetrical import WalkSymmetrical
from walk_still import WalkStill

def generate_level(player):

    pygame.mixer.music.stop()

    song = random.choice(utils.SONGS)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)

    g_game.objects = {id: obj for id, obj in g_game.objects.items() if not isinstance(obj, Leveler)}

    next_level_index = random.randint(0, len(g_game.parsed_levels) - 1)
    print(len(g_game.parsed_levels))
    while next_level_index == g_game.last_level_index:
        next_level_index = random.randint(0, len(g_game.parsed_levels) - 1)
    g_game.last_level_index = next_level_index
    print("nextlevel: " + str(next_level_index))
    next_level = g_game.parsed_levels[next_level_index]
    
    player_start_x = next_level["startx"]
    player_start_y = next_level["starty"]
    
    levelers = next_level["levelers"]
    monsters = next_level["monsters"]

    for leveler in levelers:
        walk_pattern = leveler["walk_pattern"]
        try:
            leveler_walk = {
                "follow":      WalkFollow,
                "symmetrical": WalkSymmetrical,
                "still":       WalkStill
            }[walk_pattern]
        except KeyError:
            print(f"Unsupported walk pattern for platform at level {next_level_index}: {walk_pattern}")

            continue

        if walk_pattern != "follow":
            leveler_walk_obj = leveler_walk(leveler["walk_steps"])
            print("AAAAAAAAAAAAAAAAAAAAAAAAA TIPO: " + str(type(leveler_walk_obj)))
        else:
            leveler_walk_obj = leveler_walk(player, leveler["walk_steps"])

        Leveler(
            leveler["startx"], leveler["starty"], leveler["look_color"],
            leveler["look_width"], leveler["look_height"], leveler["speed"],
            leveler["walk_direction"], leveler["health"], leveler["walk_horizontal"], 
            leveler["immortal"], leveler["collision"], leveler_walk_obj,
            leveler["look_sprite"]
        )

    for monster_instance in monsters:
        monster = g_game.parsed_monsters[monster_instance["name"]]

        walk_pattern = monster["walk_pattern"]
        shoot_pattern = monster["shoot_pattern"]

        try:
            monster_walk = {
                "follow":      WalkFollow,
                "symmetrical": WalkSymmetrical,
                "still":       WalkStill
            }[walk_pattern]

            monster_shoot = {
                "front": ShootFront,
                "sides": ShootSides
            }[shoot_pattern]
        except KeyError:
            print(f"Unsupported walk or shoot pattern for monster at level {next_level_index}: {walk_pattern} [walk], {shoot_pattern} [shoot]")

            continue

        monster_shoot_obj = monster_shoot(monster["shoot_range"], 
                                          monster["shoot_speed"], 
                                          monster["shoot_color"], 
                                          monster["shoot_width"], 
                                          monster["shoot_height"],
                                          "data/sprites/player.png")

        if walk_pattern != "follow":
            monster_walk_obj = monster_walk(monster["walk_steps"])
        else:
            monster_walk_obj = monster_walk(player, monster["walk_steps"])

        Monster(
            monster_instance["startx"], monster_instance["starty"], monster["speed"],
            monster["look_color"], monster["look_width"], monster["look_height"],
            monster["weight"], monster["walk_direction"], monster["attack"], 
            monster["health"], monster["shoot_cooldown"], monster_shoot_obj,
            monster_walk_obj, monster["walk_horizontal"], monster["immortal"],
            monster["collision"], monster["look_sprite"]
        )

    player.reinit(player_start_x, player_start_y)

    player_bonus = g_game.status_coefficient - utils.PLAYER_STATUS_PENALTY

    player.attack *= player_bonus
    player.max_health_points *= player_bonus

    player.lose_health(-(player.max_health_points * utils.PLAYER_HEALTH_RECOVER)) 

    g_game.status_coefficient += utils.STATUS_INCREASE_PER_LEVEL

def main():
    pygame.init()

    clock = pygame.time.Clock()

    font = pygame.font.Font("data/fonts/Montserrat-Regular.ttf", 20)
    ui = UI(font)
    screen = pygame.display.set_mode((utils.WINDOW_WIDTH, utils.WINDOW_HEIGHT))
    pygame.display.set_caption("Hanging by a Thread")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((69, 69, 69))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    player = Player(0, 0, utils.PLAYER_SPEED, (255, 0, 0), utils.PLAYER_WIDTH,
                    utils.PLAYER_HEIGHT, utils.RIGHT, utils.PLAYER_INITIAL_ATTACK, 
                    utils.PLAYER_INITIAL_HEALTH, utils.SHOOT_COOLDOWN, 
                    ShootFront(utils.SHOOT_RANGE, utils.SHOOT_SPEED, utils.SHOOT_COLOR, utils.SHOOT_WIDTH, utils.SHOOT_HEIGHT))

    
    HangingThread(790, 0, 0, (255, 255, 0), 20, 100)
    HangingThread(860, 0, 0, (255, 255, 0), 20, 100)
    (HangingThread(720, 0, 0, (255, 255, 0), 20, 100)).start_damage()

    generate_level(player)

    while g_game.running:
        clock.tick(60)/1000.0
        screen.blit(pygame.transform.scale(pygame.image.load("data/sprites/bg.jpg"), (utils.WINDOW_WIDTH, utils.WINDOW_HEIGHT)), (0, 0))
        ui.render(250, 50, screen)

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

        # TODO fuck this error, too lazy to fix -> pygame.error: Surfaces must not be locked during blit
        #      exception handler just as band-aid
        try:
            g_game.sprite_group.update()
            g_game.sprite_group.draw(screen)
        except:
            print("Platform")
            pass

        if g_game.monster_weight == 0:
            generate_level(player)

        if not g_game.hanging_threads:
            player.die()

        pygame.display.flip()

if __name__ == "__main__":
    xml_parser.parse_monsters()
    xml_parser.parse_levels()

    main()