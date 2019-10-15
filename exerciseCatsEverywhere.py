# Python Jupyter - Exercise: Cats Everywhere
#%%
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
#%%
cat1 = Cat('Grumpy Cat', 2)
cat2 = Cat('Keyboard Cat', 1)
cat3 = Cat('Garfield', 5)

# 2 Create a function that finds the oldest cat
#%%
def findOldest():
  cats = [cat1, cat2, cat3]
  maxAge = 0
  for cat in cats:
    if cat.age > maxAge:
      maxAge = cat.age
  return maxAge

findOldest()

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
#%%
print(f'The oldest cat is {findOldest()}')

#%%
