from game import g_game
from game_object import GameObject
import utils

class HangingThread(GameObject):
    def __init__(self, x, y, speed, color, width, height):
        super().__init__(x, y, speed, color, width, height, utils.LEFT, None, utils.THREAD_MAX_HEALTH_POINTS, True)

        g_game.hanging_threads.append(self)

    def start_damage(self):
        self.immortal = False

        self.internal_scheduler = utils.current_milli_time() + utils.THREAD_DAMAGE_INTERVAL

    def die(self):
        super().die()

        remaining_hanging_threads = g_game.hanging_threads

        remaining_hanging_threads.pop()

        if remaining_hanging_threads:
            new_front = remaining_hanging_threads[-1]

            new_front.start_damage()

    def update(self):
        if self.immortal or (utils.current_milli_time() - self.internal_scheduler) < 0:
            return

        weight_coefficient = -1
        
        monster_weight = g_game.monster_weight
        if monster_weight <= 100:
            weight_coefficient = utils.THREAD_LIGHT
        elif monster_weight <= 150:
            weight_coefficient = utils.THREAD_NORMAL
        elif monster_weight <= 200:
            weight_coefficient = utils.THREAD_MEDIUM
        elif monster_weight <= 250:
            weight_coefficient = utils.THREAD_HEAVY
        else:
            weight_coefficient = utils.THREAD_VERY_HEAVY

        next_interval = utils.THREAD_DAMAGE_INTERVAL - (weight_coefficient * 2000)

        self.lose_health(utils.THREAD_DAMAGE_PER_INTERVAL)

        self.internal_scheduler = utils.current_milli_time() + next_interval