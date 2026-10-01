from enum import Enum


class GameState(Enum):
    MENU = 'Menu'
    PLAY = 'Play'
    CONTINUE = 'continue'
    INSTRUCTIONS = 'Instructions'
    EXIT = 'Exit'
    PAUSE = 'Pause'
    WIN = 'Win'
    LOSE = 'Lose'


VIRTUAL_W = 2080
VIRTUAL_H = 1136
GAME_STATE = GameState.MENU