import time

# Window dimensions constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# Gravity constants
GRAVITY_UPWARDS = 25
GRAVITY_DOWNWARDS = 30

# Collision behavior constants
IGNORE_ALWAYS = 1
IGNORE_EXCEPT_ABOVE = 2

# Direction constants
LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1

# Movement constants
STILL = 0
MOVING = 1

# Player dimensions constants
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 100

# Jump height constant
JUMP_HEIGHT = 250

def current_milli_time():
    return int(round(time.time() * 1000))