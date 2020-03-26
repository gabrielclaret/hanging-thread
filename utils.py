import time

# Window dimensions constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# Gravity constants
GRAVITY_UPWARDS = 25
GRAVITY_DOWNWARDS = 30

# Knockback constants
KNOCKBACK_TOTAL = 50
KNOCKBACK_PER_FRAME = 5

# Invencible state duration (ms)
# Triggered when player collides with monster
INVENCIBLE_DURATION = 1000

# Collision behavior constants
IGNORE_ALWAYS = 1
IGNORE_EXCEPT_ABOVE = 2

# Direction constants
LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1

# Player dimensions constants
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 100

# Player shoot constants (cooldown in ms)
SHOOT_COOLDOWN = 500
SHOOT_RANGE = 500
SHOOT_SPEED = 10
SHOOT_COLOR = (0, 0, 0)
SHOOT_WIDTH = 10
SHOOT_HEIGHT = 10

# Jump height constant
JUMP_HEIGHT = 250

def current_milli_time():
    return int(round(time.time() * 1000))