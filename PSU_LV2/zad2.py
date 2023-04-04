import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols = (1, 2, 3, 4, 5, 6),
                  delimiter = ",", skiprows = 1)

x = data[0:, 3]#hp
y = data[0:, 0]#mpg
z = data[0:, 5]#wt

plt.xlabel('Horse Power')
plt.ylabel('Miles per Gallon')
plt.title("Zadatak 2")
plt.scatter(x, y, c = "indigo", marker="*", s = z * 50, label = "mpg/hp")

plt.plot(kind = "scatter", label = "Weight(lbs/1000)", color = "red")
plt.legend()
plt.show()

print("Min, max i suma")
print(min(y))
print(max(y))
print(sum(y) / len(y))
print()

a=[]

for i in range(len(y)):
    if data[i, 1] == 6:
        a.append(data[i, 0])

print("Min, max i suma 6 cilindara")
print(min(a))
print(max(a))
print(sum(a) / len(a))

