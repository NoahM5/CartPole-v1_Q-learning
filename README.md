# CartPole-v1 Q-learning Agent

Description

This repository contains a Q-learning algorithm designed to solve the CartPole-v1 environment from OpenAI Gym. https://www.gymlibrary.dev/environments/classic_control/cart_pole/
The objective is to balance a pole on a cart by controlling its movement to the left or right.

Key Components

Environment: CartPole-v1 from OpenAI Gym, which involves balancing a pole on a cart. The episode ends if the pole falls or the cart exits the screen.
Libraries: Uses gym for the environment and numpy for calculations.
Q-Learning: Implements Q-learning with parameters like learning rate (alpha), discount factor (gamma), and exploration rate (epsilon).
Q-Table: A matrix that stores the Q-values for each state-action pair, predicting the expected future rewards.
Functions:
discretize(observation): Converts continuous observations into discrete states.
choose_action(state, epsilon): Determines actions using an epsilon-greedy policy.
Execution: The main loop manages the environment interactions over episodes and steps, updating the Q-values and rendering the environment to visualize the agent's behavior.
Learning Process

The Q-learning formula updates Q-values to optimize decision-making over time.
Tracking and printing average rewards help monitor learning progress, adjusting as needed to achieve desired performance levels.
