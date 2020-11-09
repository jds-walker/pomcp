from abc import ABC, abstractmethod


class Simulator(ABC):

    @property
    @abstractmethod
    def action(self):
        pass

    @property
    @abstractmethod
    def state(self):
        pass

    @property
    @abstractmethod
    def observation(self):
        pass

    @property
    @abstractmethod
    def reward(self):
        pass

    @abstractmethod
    def startState(self) -> state:
        pass

    @abstractmethod
    def allActions(self) -> []:
        pass

    @abstractmethod
    def generate(self, s: state, a: action) -> (state, observation, reward):
        pass

    @abstractmethod
    def restart(self) -> None:
        pass