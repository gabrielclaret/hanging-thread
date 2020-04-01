from game import g_game
import pygame 
import utils

class UI():
    def __init__(self, font):
        #test purposes
        self.count = 0

        self.weight_text = None
        self.weight_text_1 = None
        self.weight_text_render = None
        self.weight_text_render_1 = None

        self.font = font
        self.weight = ["LIGHT", "NORMAL", "MEDIUM", "HEAVY", "VERY HEAVY"]
        self.weight_colors = ['green', 'yellow', 'orange', 'red', 'crimson']
        
        self.update_text()

    def update_text(self):
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

        self.weight_text = 'Thread Tension: '
        self.weight_text_1 = self.weight[weight_coefficient]
        self.weight_text_render = self.font.render(self.weight_text, True, pygame.Color(255, 255, 255))
        self.weight_text_render_1 = self.font.render(self.weight_text_1, True, pygame.Color(self.weight_colors[weight_coefficient]))
        

    def render(self, posx, posy, screen):
        self.update_text()
        screen.blit(self.weight_text_render, self.weight_text_render.get_rect(centerx=posx-125, centery=posy))
        screen.blit(self.weight_text_render_1, self.weight_text_render_1.get_rect(centerx=posx, centery=posy))
