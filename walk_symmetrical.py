from walk import Walk

class WalkSymmetrical(Walk):
    def step(self, direction):
        if self.steps == 0:
            direction *= -1
            self.steps_remaining = self.steps

        move_pos = (direction * self.speed, 0)

        self.steps_remaining -= 1

        return (move_pos, direction)