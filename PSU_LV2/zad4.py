import numpy as np
import matplotlib.pyplot as plt

size = 50
rows = 4
cols = 5

arr_zeros = np.zeros((size, size))
#arr_ones = np.ones((size, size))
arr_ones = np.full((size, size), 255)

my_array1 = np.vstack((arr_zeros, arr_ones))#crno bijelo
my_array1d = np.vstack((my_array1, my_array1))#crno bijelo crno bijelo

my_array2 = np.vstack((arr_ones, arr_zeros))#bijelo crno
my_array2d = np.vstack((my_array2, my_array2))#bijelo crno bijelo crno bijelo

my_array3 = np.hstack((my_array1d, my_array2d))
my_array3 = np.hstack((my_array3, my_array3))
my_array3 = np.hstack((my_array3, my_array1d))

plt.axis([0, cols*size, rows*size, 0])
plt.imshow(my_array3, cmap = "gray", vmin = 0, vmax = 255)
plt.show()
