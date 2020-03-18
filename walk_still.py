from walk import Walk

class WalkStill(Walk):
    def step(self, direction):
        return ((0, 0), direction)