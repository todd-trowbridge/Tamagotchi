class Pet:
  def __init__(self, name, fullness=50, happiness=30, hunger=5, mopiness=5):
    self.name = name
    self.fullness = fullness
    self.happiness = happiness
    self.hunger = hunger
    self.mopiness = mopiness
    self.toys = []

  def eat_food(self):
    self.fullness += 10

  def get_love(self):
    self.happiness += 10

  def be_alive(self):
    self.fullness -= self.hunger
    self.happiness -= self.mopiness
    for toy in self.toys:
      self.happiness += toy.use()

  def get_status(self):
    return f"""
    Pet: {self.name}
    Happiness: {self.happiness}
    Fullness: {self.fullness}"""
  
  def is_alive(self):
    return self.fullness > 0 and self.happiness > 0

  def __str__(self):
    return f'''
    name: {self.name}
    happiness: {self.happiness}
    fullness: {self.fullness}
    '''
  
  def give_toy(self, toy):
    self.toys.append(toy)