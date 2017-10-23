import numpy as np 
import random

class Agent(object):
	'''
	base class
	'''
	def __init__(self, num_states, num_actions, discount_factor=0.9):
		self.num_states = num_states
		self.num_actions = num_actions
		self.discount_factor = discount_factor
		self.last_state = None
		self.last_action = None


class QLearningAgent(Agent):
    def __init__(self,  learning_rate =0.01, epsilon =0.1, value=0,**kwargs):
        super(QLearningAgent, self).__init__(**kwargs)
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.value = value

        self.value_table = np.full((self.num_states, self.num_actions), self.value) # q table

    
    # update q function with sample <s, a, r, s'>
    def learn(self, state, action, reward, next_state):
        current_q = self.value_table[state][action]
        # using Bellman Optimality Equation to update q function
        new_q = reward + self.discount_factor * max(self.value_table[next_state])
        self.value_table[state][action] += self.learning_rate * (new_q - current_q)

    # get action for the state according to the q function table
    # agent pick action of epsilon-greedy policy
    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            # take random action
            action = np.random.choice(self.actions)
        else:
            # take action according to the q function table
            state_action = self.value_table[state]
            action = self.arg_max(state_action)
        return action

    @staticmethod
    def arg_max(state_action):
        max_index_list = []
        max_value = state_action[0]
        for index, value in enumerate(state_action):
            if value > max_value:
                max_index_list.clear()
                max_value = value
                max_index_list.append(index)
            elif value == max_value:
                max_index_list.append(index)
        return random.choice(max_index_list)