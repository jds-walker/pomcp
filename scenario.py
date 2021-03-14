from parser import Parser
from simulator import Simulator
from random import choice, choices

class Scenario(Simulator):

        action = None
        observation = None
        state = None
        reward = None

        def __init__(self, scenario):
            self.p = Parser(scenario)
            self.States, self.Terminal, self.Actions, self.Observations, self.decay, self.discount  = self.p.getScenario()


        def startState(self):
          
            startState = { state.name : state.value[state.name]['initial_value'] if state.value[state.name]['initial_value'] in state.value[state.name]['values'] else choice(state.value[state.name]['values']) for state in self.States }
            return(startState)

        def allActions(self):
            return [action.name for action in self.Actions]
        
        def restart(self):
            pass

        def generate(self, state, action):
            
            # if state['terminal'] == True:
            #     raise NameError("Already terminal")
            
            transition = self.Actions[action].value[action]
            cost  = transition['cost']
            observation = None
            precondition = transition['preconditions']
            prob_success = transition['prob_success']
            success = transition['effects']['success']
            failure = transition['effects']['failure']

            # get new state and observation depending on preconditions
            if precondition.items() <= state.items():
                success = choices([success, failure], [prob_success, 1-prob_success])[0]
                state.update(success['next_state']) 
                observation = success['observation']                   
            else: 
                state.update(failure['next_state']) 
                observation = failure['observation']                   

            
            if state['terminal'] == True:
                cost -= self.Terminal.terminal.value['terminal']['reward']
            if state['exploited'] == True:
                state['terminal'] = True
                cost -= self.Terminal.exploited.value['exploited']['reward']
            
            if len(observation) == 0:
                observation = "No-Observation"
            else: 
                # observation_space:
                #     non_state_obs:
                #         port_obs: &id001
                #         - open
                #         - closed
                #     state_obs:
                #     - os

                for o in observation:

                    try:
                        if observation[o] == "actual":
                            observation = state[o]
                        else:
                            state[o]
                            observation = "No-Observation"
                    except:
                        observation = action + observation[o]
            
            return (state, observation, -cost)


