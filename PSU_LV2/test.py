import numpy as np

x = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8],
              [9, 10, 11, 12]
              ])

#print(x)
#print()

''''
print(x.shape)
print(type(x))
'''
#za jed dim   print(x[0:2])
#za dva dim   print(x[2, 0])

#1 2 5 6    print(x[0:2, 0:2])

#prvi redak print(x[0, :])
'''''
c = np.zeros((4,2))
d = np.ones((3,2))
e = np.full((1,2),5)
f = np.eye(5)

print(c)
print()
print(d)
print()
print(e)
print()
print(f)
print()
'''''

'''''
'''''

'''''
c = x.transpose()
print(c)
'''''


'''''
a = np.array([3,1,5])
b = np.array([2,4,8])

print(np.concatenate((a,b)))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print()
print(a.min())
print(a.argmin())
print(a.max())
print(a.argmax())
print(a.sum())
print(a.mean())
print()
print(np.mean(a))
print(np.max(a))
print(np.sum(a))
print()
a.sort()
print(a)
'''''

np.random.seed() #postavi seed generatora brojeva
rNumbers = np.random.rand(10) #generiraj 10 slučajnih brojeva
print(rNumbers)
print(rNumbers.mean())