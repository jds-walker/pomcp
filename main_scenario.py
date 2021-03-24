from scenario import Scenario
from node import Node
import random
import logging
from datetime import datetime

def main():
    logging.basicConfig(filename="./logs/" + str(datetime.now()) + '.txt', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    discounted_rewards = {}

    for c in [50]:


        logging.debug('c: %s', c)
        discounted_rewards[c] = {'rewards': [], 'errors': []}
        
        for _ in range(100):

            seed = random.random()
            # seed = 0.6298475305903174 #error_seed c = 1000
            # seed = 0.5738201070552149 # error_seed c = 100
            logging.debug('seed: %s', seed)
            random.seed(seed)

            scenario = Scenario('./scenario/es1_red_d.yaml')

            actual_state = scenario.startState()
            particles = 5000
            gamma = 0.9
            train = 2000


            logging.debug('actual start state: %s, particles: %s, gamma: %s, c: %s, train: %s', actual_state, particles, gamma, c, train)

            tree = Node(scenario, actual_state=actual_state, particles=particles, gamma=gamma, c=c)

            rewards = 0

            while tree.actual_state['terminal'] == False:

                # train
                try: 
                    for _ in range(2000):
                        tree.select()
                except Exception: 
                    logging.debug('training exception: %s', Exception)
                    discounted_rewards[c]['errors'].append(seed)
                    break

                # actual act
                # particle update is done as part of the real step. 
                # Get next belief (function) take current particles - get action and observation -> from there generate next set of particles
                try:
                    tree, reward = tree.act()
                    print(round(reward,2))
                    rewards = rewards + reward
                except Exception:  
                    logging.debug('real action exception: %s', Exception)
                    discounted_rewards[c]['errors'].append(seed)
                    break
                

            # Get average over at least 100 runs (average - total discounted reward - 95% confidence interval)
            # Hyperparameters (c = 100, 200, ... , 1000)
            # keep logs of every state / action 
            # set random seed in one place that makes the scenario determinstic (e.g time(now)) - random until we want to check
            # Generate new belief state when no real observation in tree. 

            print(f"total rewards {rewards}")
            discounted_rewards[c]['rewards'].append(rewards)
        logging.debug(discounted_rewards)
        print(discounted_rewards)
        

if __name__ ==  '__main__':
    main()
