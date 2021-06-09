class Pet:
  def __init__(self, name, fullness=50, happiness=30, hunger=5, mopiness=5):
    self.name = name
    self.fullness = fullness
    self.happiness = happiness
    self.hunger = hunger
    self.mopiness = mopiness

  def eat_food(self):
    self.fullness += 10

  def get_love(self):
    self.happiness += 10

  def be_alive(self):
    self.fullness -= self.hunger
    self.happiness -= self.mopiness

  def get_status(self):
    return f"""
  Pet: {self.name}
  Happiness: {self.happiness}
  Fullness: {self.fullness}"""