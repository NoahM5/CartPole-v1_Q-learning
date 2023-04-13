import gym
import numpy as np

env = gym.make('CartPole-v1')
env.reset()

n_states = (6, 12)
n_actions = env.action_space.n
q_table = np.zeros(n_states + (n_actions,))


alpha = 0.9
gamma = 0.99
epsilon = 0.1

count = 0

n_episodes = 300000
max_steps_per_episode = 500
average_reward_window = 100
target_average_reward = 475


episode_rewards = []

def discretize(observation):
    """Convert a continuous observation to a discrete state."""
    cart_pos, cart_vel, pole_ang, pole_vel = observation
    cart_pos_bins = np.linspace(-2.4, 2.4, 7)
    cart_vel_bins = np.linspace(-3.0, 3.0, 7)
    pole_ang_bins = np.linspace(-0.2, 0.2, 7)
    pole_vel_bins = np.linspace(-3.0, 3.0, 7)
    cart_pos_idx = np.digitize(cart_pos, cart_pos_bins)
    cart_vel_idx = np.digitize(cart_vel, cart_vel_bins)
    pole_ang_idx = np.digitize(pole_ang, pole_ang_bins)
    pole_vel_idx = np.digitize(pole_vel, pole_vel_bins)
    return (cart_pos_idx, cart_vel_idx)


def choose_action(state, epsilon):
    """Choose an action using an epsilon-greedy policy."""
    if np.random.uniform(0, 1) < epsilon:

        return env.action_space.sample()
    else:

        return np.argmax(q_table[state[0], state[1]])


for episode in range(n_episodes):
    observation = env.reset()
    state = discretize(observation)
    done = False
    episode_reward = 0

    for step in range(max_steps_per_episode):
        action = choose_action(state, epsilon)

        new_observation, reward, done, info = env.step(action)
        new_state = discretize(new_observation)

        old_q_value = q_table[state][action]
        new_q_value = (1 - alpha) * old_q_value + alpha * (reward + gamma * np.max(q_table[new_state]))
        q_table[state][action] = new_q_value

        state = new_state
        episode_reward += reward

        env.render()

        if done:
            break

    episode_rewards.append(episode_reward)

    if episode % average_reward_window == 0:
        avg_reward = np.mean(episode_rewards[-average_reward_window:])
        print(f'Experiment {count}, Episode {episode}/{n_episodes}, Average reward: {avg_reward:.2f}')

    if np.mean(episode_rewards[-average_reward_window:]) >= target_average_reward:
        print(f'Target average reward of {target_average_reward} reached after {episode} episodes')
        break

    epsilon = max(0.01, epsilon * 0.99)

env.close()
