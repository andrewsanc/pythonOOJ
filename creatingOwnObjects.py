#%%
class PlayerCharacter:
  def __init__(self, name):
    self.name = name

  def run(self):
    print('run')

# Instantiate from class
player1 = PlayerCharacter('andrew')
print(player1.name)
player1.run()

#%%
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')

player2 = PlayerCharacter('Luci', 3)
player1 = PlayerCharacter('Alcazar', 8)
print(player1.name, player1.age)
print(player2.name, player2.age)
print(player2.run())

#%%
