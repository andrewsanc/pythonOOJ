'''
Python Jupyter - Super
'''
#%%
class User:
  def __init__(self, email):
    self.email = email

  def signIn(self):
    return 'Logged In'

class Wizard(User): # Wizard class inherits from User class
  def __init__(self, name, power, email):
    super().__init__(email) # Super will inherit constructor attributes from parent class
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

wiz1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wiz1.email)

#%%
