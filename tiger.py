from simulator import Simulator
from enum import Enum, auto
from random import choices, choice

class Action(Enum):
    OPENLEFT = auto()
    OPENRIGHT = auto()
    LISTEN = auto()

class Observation(Enum):
    TIGERRIGHT = auto()
    TIGERLEFT = auto()
    GROWLLEFT = auto()
    GROWLRIGHT = auto()

class State(Enum):
    TIGERRIGHT = auto()
    TIGERLEFT = auto()

class Reward(Enum):
    CORRECT = 10
    INCORRECT = -100
    LISTEN = -1


class Tiger(Simulator):

    action = None
    observation = None
    state = None
    reward = None

    def startState(self):
        return choice([State.TIGERLEFT, State.TIGERRIGHT])

    def allActions(self) -> [Action]:
        return [Action.LISTEN, Action.OPENLEFT, Action.OPENRIGHT]

    def restart(self):
        pass

    def generate(self, s: State, a: Action) -> (State, Observation, Reward):
        if s == State.TIGERRIGHT and a == Action.OPENRIGHT:
            self.state = self.startState()
            self.observation = Observation.TIGERRIGHT
            self.reward = Reward.INCORRECT.value
            return (self.state, self.observation, self.reward)
        if s == State.TIGERRIGHT and a == Action.OPENLEFT:
            self.state = self.startState()
            self.observation = Observation.TIGERRIGHT
            self.reward = Reward.CORRECT.value
            return (self.state, self.observation, self.reward)
        if s == State.TIGERRIGHT and a == Action.LISTEN:
            self.state = s
            self.observation = choices([Observation.GROWLRIGHT, Observation.GROWLLEFT],weights=[0.85, 0.15])[0]
            self.reward = Reward.LISTEN.value
            return (self.state, self.observation, self.reward)
        if s == State.TIGERLEFT and a == Action.OPENRIGHT:
            self.state = self.startState()
            self.observation = Observation.TIGERRIGHT
            self.reward = Reward.CORRECT.value
            return (self.state, self.observation, self.reward)
        if s == State.TIGERLEFT and a == Action.OPENLEFT:
            self.state = self.startState()
            self.observation = Observation.TIGERRIGHT
            self.reward = Reward.INCORRECT.value
            return (self.state, self.observation, self.reward)
        if s == State.TIGERLEFT and a == Action.LISTEN:
            self.state = s
            self.observation = choices([Observation.GROWLRIGHT, Observation.GROWLLEFT],weights=[0.15, 0.85])[0]
            self.reward = Reward.LISTEN.value
            return (self.state, self.observation, self.reward)