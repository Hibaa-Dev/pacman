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
