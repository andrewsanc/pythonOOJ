# Python Jupyter - Class Methods and Static Methods
#%%
class MathMethods:
  def __init__(self, operation):
    self.operation = operation
    self.value = value

  @classmethod # Special case methods
  def addingThings(cls, num1, num2):
    return num1 + num2

print(MathMethods.addingThings(2,3)) # Can access class methods without instantiating 

#%%
class MathMethods:
  def __init__(self, operation, value):
    self.operation = operation
    self.value = value

  @classmethod # Special case methods
  def addingThings(cls, num1, num2):
    return cls('Sum', num1 + num2) # Can create new instances of classes from class methods

newOperation = MathMethods.addingThings(5,6)
print(newOperation.operation, newOperation.value)

#%%
class MathMethods:
  def __init__(self, operation, value):
    self.operation = operation
    self.value = value

  @staticmethod
  def valueOperation(num1, num2):
    return num1 + num2

newOperation = MathMethods('adding new value', 12)
print(newOperation.valueOperation(2,123))

#%%
