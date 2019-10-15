'''
Python Jupyter - Polymorphism. Poly - means many. Morphism - means forms. Refers to the
                 way in which object classes can share the same name but the methods can
                 act differently depending on which object class calls it.
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

wiz1 = Wizard('Merlin', 'frostbolt')
arch1 = Archer('Hunter', 30)

def playerAttack(char):
  char.attack() # Both classes have an attack method, but calls each one specifc to their class

playerAttack(wiz1)
playerAttack(arch1)

#%%
class User:
  def signIn(self):
    return 'Logged In'

  def attack(self):
    return 'do nothing'

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

wiz1 = Wizard('Merlin', 'frostbolt')
arch1 = Archer('Hunter', 30)

def playerAttack(char):
  char.attack() # Both classes have an attack method, but calls each one specifc to their class

playerAttack(wiz1)
playerAttack(arch1)

for char in [wiz1, arch1]:
  char.attack() # When called, the User attack method gets overrided by other classes Attack method