class Game:
    def __init__(self):
        self.hanging_threads = []
        self.monster_weight = 0
        self.objects = {}
        self.running = True

global g_game
g_game = Game()