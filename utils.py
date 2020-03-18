import time

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

GRAVITY_UPWARDS = 25
GRAVITY_DOWNWARDS = 30

LEFT = -1
RIGHT = 1

STILL = 0
MOVING = 1

PLAYER_WIDTH = 150
PLAYER_HEIGHT = 100

JUMP_HEIGHT = 300

def current_milli_time():
    return int(round(time.time() * 1000))