import gym
from gym import spaces
from selenium import webdriver

class UniversalPaperclipsEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.driver = webdriver.Firefox()
    url = "https://www.decisionproblem.com/paperclips/index2.html"
    self.driver.get(url)

    self.makePaperclipButton = self.driver.find_element_by_id('btnMakePaperclip')
    self.lowerPriceButton = self.driver.find_element_by_id('btnLowerPrice')
    self.raisePriceButton = self.driver.find_element_by_id('btnRaisePrice')
    self.expandMarketingButton = self.driver.find_element_by_id('btnExpandMarketing')
    self.buyWireButton = self.driver.find_element_by_id('btnBuyWire')
    self.allButtons = [ \
            self.makePaperclipButton, \
            self.lowerPriceButton, \
            self.raisePriceButton, \
            self.expandMarketingButton, \
            self.buyWireButton ]

    self.numPaperclipsSpan = self.driver.find_element_by_id('clips')
    self.availableFundsSpan = self.driver.find_element_by_id('funds')
    self.unsoldInventorySpan = self.driver.find_element_by_id('unsoldClips')
    self.pricePerClipSpan = self.driver.find_element_by_id('margin')
    self.publicDemandSpan = self.driver.find_element_by_id('demand')
    self.marketingLevelSpan = self.driver.find_element_by_id('marketingLvl')
    self.marketingCostSpan = self.driver.find_element_by_id('adCost')
    self.clipsPerSecondSpan = self.driver.find_element_by_id('clipmakerRate')
    self.inchesOfWireSpan = self.driver.find_element_by_id('wire')
    self.wireCostSpan = self.driver.find_element_by_id('wireCost')

    self.action_space = spaces.Discrete(5)
    self.observation_space = spaces.Box(low=0.0, high=float('inf'), shape=(10,), dtype=float)

  def step(self, action):
        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        # take a step action
        #oldPaperclipCount = self.numFromSpan(self.numPaperclipsSpan)
        print('action', action)
        self.allButtons[action].click() # assuming action is a integer from 0-4

        # set gym's special variables
        ob = self.observation()
        reward = self.numFromSpan(self.numPaperclipsSpan)
        episode_over = False # TODO find win condition

        return ob, reward, episode_over, {}

  def reset(self):
    pass
  def render(self, mode='human'):
    pass
  def close(self):
    self.driver.close()


  # helpers
  def numFromSpan(self, element):
    return float(element.text.replace(',',''))

  def enabledButtons(self):
    return [button for button in self.allButtons if button.is_enabled()]
  
  def observation(self):
    return ( \
      self.numFromSpan(self.numPaperclipsSpan), \
      self.numFromSpan(self.availableFundsSpan), \
      self.numFromSpan(self.unsoldInventorySpan), \
      self.numFromSpan(self.pricePerClipSpan), \
      self.numFromSpan(self.publicDemandSpan), \
      self.numFromSpan(self.marketingLevelSpan), \
      self.numFromSpan(self.marketingCostSpan), \
      self.numFromSpan(self.clipsPerSecondSpan), \
      self.numFromSpan(self.inchesOfWireSpan), \
      self.numFromSpan(self.wireCostSpan))