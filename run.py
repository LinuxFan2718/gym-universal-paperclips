import gym

env = gym.make('gym_universal_paperclips:universal-paperclips-v0')
while True:
  action = env.action_space.sample()
  print(action)
  ob, reward, done, _ = env.step(action)
  print(reward)