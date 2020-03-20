from abc import ABC, abstractmethod

class Walk:
    def __init__(self, steps = 0):
        self.steps = self.steps_remaining = steps

        self.walker = None

    @abstractmethod
    def step(self):
        pass