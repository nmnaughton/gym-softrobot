import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ReachEnv(gym.Env):
    metadata = {'render.modes': ['rgb', 'human']}

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass

    def close(self):
        pass
