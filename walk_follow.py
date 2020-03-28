from game import g_game
from pygame.math import Vector2
import utils
from walk import Walk

class WalkFollow(Walk):
    def __init__(self, target, steps = 0):
        super().__init__(steps)

        self.target = target

    def step(self):
        walker_direction = self.walker.direction
        target_direction = self.target.direction

        origin_id = self.walker.id
        target_id = self.target.id

        walker_rect = self.walker.rect
        target_rect = self.target.rect

        walker_origin = walker_direction == utils.LEFT and (walker_rect.left, walker_rect.top) or (walker_rect.right, walker_rect.top)
        target_origin = target_rect.x > walker_rect.x and (target_rect.left, target_rect.top) or (target_rect.right, target_rect.top)

        if walker_rect.bottom <= target_rect.bottom and not ray_cast(walker_origin, origin_id, target_origin, target_id) and not self.target.invencible:
            self.walker.move(target_rect.x < walker_rect.x and utils.LEFT or utils.RIGHT)
        else:
            direction = self.walker.direction

            if self.steps_remaining == 0:
                direction *= -1
                self.steps_remaining = self.steps

            self.walker.move(direction)
            
            self.steps_remaining -= 1

def ray_cast(origin, origin_id, target, target_id):
    # https://stackoverflow.com/questions/45389563/how-to-get-coordinates-area-of-collision-in-pygame

    origin_vector = Vector2(origin)
    target_vector = Vector2(target)

    if origin_vector == target_vector:
        return

    current_pos = Vector2(origin)

    heading = target_vector - origin_vector

    direction = heading.normalize()

    for _ in range(int(heading.length())):
        current_pos += direction

        old_obj = g_game.objects.copy()
        for obj in old_obj.values():
            if obj.rect.collidepoint(current_pos) and obj.id != origin_id and obj.id != target_id and not obj.collision_behavior == utils.IGNORE_ALWAYS:
                return True

    return False