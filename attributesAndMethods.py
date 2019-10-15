# Python Jupyter - Attributes and Methods
#%%
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')

help(PlayerCharacter) # Prints the blueprint of the class

#%%
class PlayerCharacter:
  # Class Object Attribute
  membership = True # Static variable that doesn't change across instances
  def __init__(self, name, age):
    if PlayerCharacter.membership:
      self.name = name
      self.age = age

  def shout(self):
    print(f'my name is {self.name}')
    return 'done'

p1 = PlayerCharacter('Cindy', 44)
p2 = PlayerCharacter('Tom', 21)
p2.attack = 50

print(p1.shout())
print(p2.shout())

#%%
class PlayerCharacter:
  # Class Object Attribute
  membership = True # Static variable that doesn't change across instances
  def __init__(self, name, age):
    if PlayerCharacter.membership:
      self.name = name
      self.age = age

  def shout(self):
    print(f'my name is {self.name}!!!!')
    return 'done'

  def hello(self):
    print(f'hellloooo!!')
    return 'done'

p1 = PlayerCharacter('Cindy', 44)
p2 = PlayerCharacter('Tom', 21)
p2.attack = 50

print(p1.shout())
print(p2.hello())


#%%
