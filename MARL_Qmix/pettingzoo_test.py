# library imports
from stable_baselines3.ppo import CnnPolicy
from stable_baselines3 import PPO
from pettingzoo.butterfly import pistonball_v6
import supersuit as ss

# Set up Pistonball environment
env = pistonball_v6.parallel_env(n_pistons=20, time_penalty=-0.1, continuous=True, random_drop=True, random_rotate=True, ball_mass=0.75, ball_friction=0.3, ball_elasticity=1.5, max_cycles=125)

# Change to greyscale color and smaller size to make it faster
env = ss.color_reduction_v0(env, mode='B')
env = ss.resize_v1(env, x_size=84, y_size=84)

# Stack the frames to let network know how fast the ball is going
env = ss.frame_stack_v1(env, 3)

# Set up multi-agent environment
env = ss.pettingzoo_env_to_vec_env_v1(env)

# Run multiple environment at same time to speed up training
env = ss.concat_vec_envs_v1(env, 8, num_cpus=4, base_class='stable_baselines3')

# Learning and Saving
model = PPO(CnnPolicy, env, verbose=3, gamma=0.95, n_steps=256, ent_coef=0.0905168, learning_rate=0.00062211, vf_coef=0.042202, max_grad_norm=0.9, gae_lambda=0.99, n_epochs=5, clip_range=0.3, batch_size=256)
model.learn(total_timesteps=1000000)
model.save('policy')