'''
Python Jupyter - Abstraction. Abstracting information and retrieving only which is necessary
                 Use case, You have TV remote. The remote has exterior buttons that provide
                 functionality. However, the user doesn't know interior implementation of that
                 particular button. The implementation is abstracted out from play button.
'''
#%%
class Animal:
  def __init__(self, type, age):
    self.type = type
    self.age = age

  def run(self):
    print('run')

  def speak(self):
    print(f'Hello I\'m a {self.type}, and I\'m {self.age} years old')


human = Animal('human', 20)
human.speak() # The speak function is abstracted out


#%%
