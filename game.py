class Game:
    def __init__(self):
        self.hanging_threads = []
        self.monster_weight = 0
        self.objects = {}
        self.parsed_levels = []
        self.parsed_monsters = {}
        self.running = True
        self.status_coefficient = 1
        

global g_game
g_game = Game()