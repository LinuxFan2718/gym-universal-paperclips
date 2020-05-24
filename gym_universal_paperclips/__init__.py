from gym.envs.registration import register

register(
    id='universal-paperclips-v0',
    entry_point='gym_universal_paperclips.envs:UniversalPaperclipsEnv',
)

