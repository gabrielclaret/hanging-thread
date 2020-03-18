from abc import ABC, abstractmethod

class Shoot(ABC):
    def __init__(self, range, speed, color, width, height):
        self.range = range
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height

        self.shooter = None

    @abstractmethod
    def fire(self):
        pass