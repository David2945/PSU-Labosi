import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols = (1, 2, 3, 4, 5, 6),
                  delimiter = ",", skiprows = 1)

x = data[0:, 3]#hp
y = data[0:, 0]#mpg
z = data[0:, 5]#wt

'''''
print(x)
print()
print(y)

'''''

#print(z)

plt.xlabel('Horse Power')
plt.ylabel('Miles per Gallon')
plt.title("Zadatak 2")
plt.scatter(x, y, c="green", marker="s", s = 10)

plt.plot(kind='scatter', label = "Weight(lbs/1000)", color='red')
plt.legend(bbox_to_anchor = (0.75, 1.15), ncol = 2)
plt.show()

#mpg o hp
#wt bojano po velicini

