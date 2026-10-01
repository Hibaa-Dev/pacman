from abc import ABC, abstractmethod
from Typing import Tuple


class Entity(ABC):

    def __init__(self, lives) -> None:
        self.position: Tuple(int, int) = (0, 0)
        self.lives: int = lives
        self.score: int = 0
        self.direction: str = ''

    @abstractmethod
    def moveEntity(self, direction: str):
        pass

    @abstractmethod
    def decreaseLife():
        pass

    @abstractmethod
    def increaseScore():
        pass
