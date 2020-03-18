from walk import Walk

class WalkSymmetrical(Walk):
    def step(self):
        direction = self.walker.direction

        if self.steps == 0:
            direction *= -1
            self.steps_remaining = self.steps

        self.walker.move(direction)
        self.steps_remaining -= 1