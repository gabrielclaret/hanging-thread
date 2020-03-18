from abc import ABC, abstractmethod

class Walk:
    def __init__(self, steps, speed):
        self.steps = self.steps_remaining = steps
        self.speed = speed

    @abstractmethod
    def step(self, direction):
        pass