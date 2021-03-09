import yaml
from enum import Enum

class Parser(): 

    def __init__(self, scenario):
        self.scenario = scenario 

    def getScenario(self):
        with open(self.scenario) as stream:
            documents = yaml.safe_load(stream)

            States = Enum('States', {k : {k : v} for k, v in documents['state_space'].items()})
            Terminal = Enum('Terminal', {k : {k : v} for k, v in documents['terminal_states'].items()})
            Observations = Enum('Observations', {k : {k : v} for k, v in documents['observation_space'].items()})
            Actions = Observations = Enum('Actions', {k : {k : v} for k, v in documents['action_space'].items()})            

            description = documents['description']
            decay = documents['decay_step']
            discount = documents['discount']

            return States, Terminal, Actions, Observations, decay, discount

        



