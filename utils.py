import time

# Songs played randomly at each level
SONGS = ("data/songs/tunak.mp3", "data/songs/cosita.mp3", "data/songs/popotao.mp3")

# Window dimensions constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# Monster and player status increase per level (/ 100)
STATUS_INCREASE_PER_LEVEL = 0.05

# Player status STATUS_INCREASE_PER_LEVEL penalty (/ 100)
PLAYER_STATUS_PENALTY = 0.015

# Player health recover per level (/ 100)
PLAYER_HEALTH_RECOVER = 0.35

# Thread constant (interval in ms)
THREAD_MAX_HEALTH_POINTS = 100
THREAD_DAMAGE_INTERVAL = 10000
THREAD_DAMAGE_PER_INTERVAL = 100
THREAD_LIGHT = 0
THREAD_NORMAL = 1
THREAD_MEDIUM = 2
THREAD_HEAVY = 3
THREAD_VERY_HEAVY = 4

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
DO_NOT_IGNORE = 0
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

# Player status constants
PLAYER_INITIAL_ATTACK = 20
PLAYER_INITIAL_HEALTH = 100
PLAYER_SPEED = 10

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