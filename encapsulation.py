'''
Python Jupyter - Encapsulation. Refers to encapsulating class variables 
                 and providing methods that is able to mutate those variables.
'''
#%%
class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')

  def speak(self):
    print(f'my name is {self.name}, and I am {self.age} years old')

person1 = Animal('human', 20)
print(person1.name, person1.age)

#%%
