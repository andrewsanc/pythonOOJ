'''
Python Jupyter - Multiple Inheritance.
'''
#%%
class User():
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

  def checkArrows(self):
    return f'{self.numArrows} remain.'

  def run(self):
    print('Ran really fast')

class HybridBorg(Wizard, Archer): # Inherits from Archer and Wizard class
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)

hb1 = HybridBorg('Borgie', 'fireball', 100)
print(hb1.checkArrows())
print(hb1.attack())
#%%
