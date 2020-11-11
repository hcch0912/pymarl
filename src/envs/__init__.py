from functools import partial
# from smac.env import MultiAgentEnv, StarCraft2Env
import gym 
import ma_gym
from envs.multiagentenv import MultiAgentEnv
from envs.grid_env import GridEnv
import sys
import os

def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)



REGISTRY = {}
# REGISTRY["sc2"] = partial(env_fn, env=StarCraft2Env)
REGISTRY["grid_world"] = partial(env_fn, env = GridEnv)

if sys.platform == "linux":
    os.environ.setdefault("SC2PATH",
                          os.path.join(os.getcwd(), "3rdparty", "StarCraftII"))
