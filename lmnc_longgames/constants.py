from pygame import USEREVENT

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Events
BUTTON_PRESSED = USEREVENT + 1
BUTTON_RELEASED = USEREVENT + 2
ROTATED_CW = USEREVENT + 3
ROTATED_CCW = USEREVENT + 4

#System
MAX_MENU_INACTIVE_TIME = 60

#Controllers
CONTROLS = 0
P1 = 1
P2 = 2

# Buttons
ROTARY_PUSH = 0
BUTTON_A = 1
BUTTON_B = 2

BUTTON_RESET=30
BUTTON_MENU=31

PIN_RESET_RELAY=19