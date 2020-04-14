from abc import ABC, abstractmethod

class Shoot(ABC):
    def __init__(self, range, speed, color, width, height, sprite = "data/sprite/top_box.png"):
        self.range = range
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.sprite = sprite
        self.shooter = None

    @abstractmethod
    def fire(self):
        pass