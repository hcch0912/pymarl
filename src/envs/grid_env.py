from envs.multiagentenv import MultiAgentEnv
import gym 
import ma_gym

class GridEnv(MultiAgentEnv):
    def __init__(self, **args):
        self.env = gym.make(args["env_name"])
        self.episode_limit = 1000
        if args["env_name"] == "Checkers-v0":
            self.n_agents = 2 
        elif args["env_name"] == "Switch4-v0":
            self.n_agents = 4
    def step(self, actions):
        return self.env.actions()

    def get_obs(self):
        """ Returns all agent observations in a list """
        return self.env.get_agent_obs()


    def get_obs_agent(self, agent_id):
        """ Returns observation for agent_id """
        return self.env.get_agent_obs()

    def get_obs_size(self):
        """ Returns the shape of the observation """
        return self.env.observation_space._agents_observation_space[0].shape

    def get_state(self):
        return self.env.get_agent_obs()

    def get_state_size(self):
        """ Returns the shape of the state"""
        return self.env.observation_space._agents_observation_space[0].shape

    def get_avail_actions(self):
       	return [self.get_avail_agent_actions(i) for i in range(self.n_agents)]

    def get_avail_agent_actions(self, agent_id):
        """ Returns the available actions for agent_id """
        return [1.0] * 5 

    def get_total_actions(self):
        """ Returns the total number of actions an agent could ever take """
        # TODO: This is only suitable for a discrete 1 dimensional action space for each agent
        return 5

    def reset(self):
        """ Returns initial observations and states"""
        return self.env.reset()

    def render(self):
        return self.env.render()

    def close(self):
        self.env.close()

    def seed(self):
        self.env.see()

    def save_replay(self):
        print("not implemented")

    def get_env_info(self):
        env_info = {"state_shape": self.get_state_size(),
                    "obs_shape": self.get_obs_size(),
                    "n_actions": self.get_total_actions(),
                    "n_agents": self.n_agents,
                    "episode_limit": self.episode_limit}
        return env_info
