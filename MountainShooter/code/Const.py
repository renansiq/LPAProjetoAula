# C
import pygame as pg

COLOR_ORANGE = (225, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# #I
# IMAGE_LEVEL = {'Level1Bg': 7}

# E
EVENT_ENEMY = pg.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1,
                }
PLAYER_KEY_UP = {'Player1': pg.K_UP,
                 'Player2': pg.K_w}
PLAYER_KEY_DOWN = {'Player1': pg.K_DOWN,
                   'Player2': pg.K_s}
PLAYER_KEY_LEFT = {'Player1': pg.K_LEFT,
                   'Player2': pg.K_a}
PLAYER_KEY_RIGHT = {'Player1': pg.K_RIGHT,
                    'Player2': pg.K_d}
