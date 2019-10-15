'''
Python Jupyter - Private Variables vs Public Variables. There is no way to
                 declare private variables in Python. However, by adding _ to
                 a variable name, it declares to other programmers that 
                 variable is a private variable.
'''
#%%
class Animal:
  def __init__(self, type, age):
    self._type = type # Underscore on the attributes, but it's not guaranteed.
    self._age = age

  def run(self):
    print('run')

  def speak(self):
    print(f'Hello I\'m a {self._type}, and I\'m {self._age} years old')