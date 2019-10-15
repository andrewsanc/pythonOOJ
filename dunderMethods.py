'''
Python Jupyter - Dunder methods are commenoly used for operator overloading.
'''
#%%
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age

  def __str__(self):
    return f'{self.color}'

actionFigure = Toy('red', 0)
print(actionFigure.__str__())
print(str(actionFigure))

#%%
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age

  def __str__(self):
    return f'{self.color}'

  def __len__(self): # Overloading the len function for Toy class to return a specific int
    return 1203

actionFigure = Toy('red', 0)
print(len(actionFigure))

#%%
