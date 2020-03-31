import pygame
import pygame_gui
import utils
from pygame_gui.elements.ui_text_box import UITextBox

def draw(coef, manager):
    weight = ["LIGHT", "NORMAL", "MEDIUM", "HEAVY"]
    weightColors = [('#00FF00'), ('#BFFF00'), ('#EDF500'), ('#FF0000')]
    weightText = 'Thread Tension: <font face=Montserrat size=4 color=%s>%s</font>' % (weightColors[coef], weight[coef])

    UITextBox(weightText,
              pygame.Rect((120, 25), (220, 50)),
              manager=manager)
