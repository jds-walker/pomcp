import yaml
from enum import Enum
from simulator import Simulator
from random import choice

class Parser(): 

    def __init__(self, scenario):
        self.scenario = scenario 

    def getScenario(self):
        with open(self.scenario) as stream:
            documents = yaml.safe_load(stream)

            States = Enum('States', {k : {k : v} for k, v in documents['state_space'].items()})


            states = {state.name : state.value[state.name]['initial_value'] if state.value[state.name]['initial_value'] in state.value[state.name]['values'] else choice(state.value[state.name]['values']) for state in States}
            print(states)

            # States = Enum('States', )


            # for state in States:
            #     state = Enum(State, doccuments['state_space'][state.name])
            #     print(state)

            # return States                

    

    class Scenario(Simulator):

        action = None
        observation = None
        state = None
        reward = None

        # def startState(self):
        #     state = {k : v for k, v in States.items()}
        #     return choice([State.TIGERLEFT, State.TIGERRIGHT])

    #     def allActions(self) -> [Action]:
    #         return [Action.LISTEN, Action.OPENLEFT, Action.OPENRIGHT]

    #     def restart(self):
    #         pass

    #     def generate(self, s: State, a: Action) -> (State, Observation, Reward):
    #         if s == State.TIGERRIGHT and a == Action.OPENRIGHT:
    #             self.state = self.startState()
    #             self.observation = Observation.TIGERRIGHT
    #             self.reward = Reward.INCORRECT.value
    #             return (self.state, self.observation, self.reward)
    #         if s == State.TIGERRIGHT and a == Action.OPENLEFT:
    #             self.state = self.startState()
    #             self.observation = Observation.TIGERRIGHT
    #             self.reward = Reward.CORRECT.value
    #             return (self.state, self.observation, self.reward)
    #         if s == State.TIGERRIGHT and a == Action.LISTEN:
    #             self.state = s
    #             self.observation = choices([Observation.GROWLRIGHT, Observation.GROWLLEFT],weights=[0.85, 0.15])[0]
    #             self.reward = Reward.LISTEN.value
    #             return (self.state, self.observation, self.reward)
    #         if s == State.TIGERLEFT and a == Action.OPENRIGHT:
    #             self.state = self.startState()
    #             self.observation = Observation.TIGERRIGHT
    #             self.reward = Reward.CORRECT.value
    #             return (self.state, self.observation, self.reward)
    #         if s == State.TIGERLEFT and a == Action.OPENLEFT:
    #             self.state = self.startState()
    #             self.observation = Observation.TIGERRIGHT
    #             self.reward = Reward.INCORRECT.value
    #             return (self.state, self.observation, self.reward)
    #         if s == State.TIGERLEFT and a == Action.LISTEN:
    #             self.state = s
    #             self.observation = choices([Observation.GROWLRIGHT, Observation.GROWLLEFT],weights=[0.15, 0.85])[0]
    #             self.reward = Reward.LISTEN.value
    #             return (self.state, self.observation, self.reward)

     

p = Parser(scenario='./scenario/es1_red_d.yaml')
p.getScenario()