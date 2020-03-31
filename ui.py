import pygame 

class UI():
    def __init__(self, font):
        #test purposes
        self.count = 0

        self.weight_text = None
        self.weight_text_1 = None
        self.weight_text_render = None
        self.weight_text_render_1 = None

        self.font = font
        self.weight = ["LIGHT", "NORMAL", "MEDIUM", "HEAVY"]
        self.weight_colors = ['green', 'yellow', 'orange', 'red']
        self.coefficient = 3
        
        self.update_text()

    def update_text(self):
        #self.coefficient = foo.getCoefficient()

        #testing coefficient changes
        self.count+=1
        if(self.count >= 300):
            self.coefficient += 1
            self.count = 0
            if(self.coefficient > 3):
                self.coefficient = 0
        #test block end

        self.weight_text = 'Thread Tension: '
        self.weight_text_1 = self.weight[self.coefficient]
        self.weight_text_render = self.font.render(self.weight_text, True, pygame.Color(255, 255, 255))
        self.weight_text_render_1 = self.font.render(self.weight_text_1, True, pygame.Color(self.weight_colors[self.coefficient]))
        

    def render(self, posx, posy, screen):
        self.update_text()
        screen.blit(self.weight_text_render, self.weight_text_render.get_rect(centerx=posx-125, centery=posy))
        screen.blit(self.weight_text_render_1, self.weight_text_render_1.get_rect(centerx=posx, centery=posy))
