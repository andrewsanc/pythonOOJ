'''
Python Jupyter - Inheritance. Inheritance allows new objects to take on new properties
                 of an existing object. 
'''
#%%
class User:
  def signIn(self):
    return 'Logged In'

class Wizard(User): # Wizard class inherits from User class
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'{self.name} attacks with their {self.power} ability.')

class Archer(User): # Archer class inherits from User class
  def __init__(self, name, numArrows):
    self.name = name
    self.numArrows = numArrows

  def attack(self):
    self.numArrows -= 1
    print(f'{self.name} attacks with their arrow. {self.numArrows} remain.')

wizard1 = Wizard('Merlin', 'fireball')
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

#%%
isinstance(archer1, Archer)
isinstance(wizard1, Archer)
#%%
