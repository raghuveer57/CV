import numpy as np

mylist  = [1,2,3]

print(type(mylist))

nparr = np.array(mylist)

print(nparr)

print(type(nparr))

print(np.arange(0,10,2))

print(np.zeros(shape=(5,5)))

np.random.seed(102)
arr = np.random.randint(0,100,10)
print(arr)

arr2 = arr.reshape(2,5)
print(arr2)