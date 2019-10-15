'''
Python Jupyter - Exercise: Extending list
'''
#%%
class SuperList():
  def __init__(self):
    self.list = []

  def __len__(self):
    return len(self.list)

  def append(self, item):
    self.list.append(item)
    return self.list

superList1 = SuperList();
len(superList1)
superList1.append('weee')
print(issubclass(SuperList, list))
#%%
