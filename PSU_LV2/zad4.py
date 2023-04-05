import numpy as np
import matplotlib.pyplot as plt

size = 50
rows = 20
cols = 10

def kockice(size, rows, cols):
    arr_zeros = np.zeros((size, size))#crno
    #arr_ones = np.ones((size, size))
    arr_ones = np.full((size, size), 255)#bijelo

    my_array1 = np.vstack((arr_zeros, arr_ones)*int(rows/2) + (arr_zeros,)*int(rows%2))#crno bijelo crno...

    my_array2 = np.vstack((arr_ones, arr_zeros)*int(rows/2) + (arr_ones,)*int(rows%2))#bijelo crno bijelo...
    
    my_array3 = my_array1

    for i in range(cols):
        if i%2==0:
            my_array3 = np.hstack((my_array3, my_array2))
        if i%2==1:
            my_array3 = np.hstack((my_array3, my_array1))

    return my_array3
    

plt.axis([0, cols*size, rows*size, 0])
plt.imshow(kockice(size, rows, cols), cmap = "gray", vmin = 0, vmax = 255)
plt.show()
