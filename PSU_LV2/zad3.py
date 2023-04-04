import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import RegularGridInterpolator

#og size: 960x640
#funkcija sa neta za promjenu rezolucije slike
def regrid(data, out_x, out_y):
    m = max(data.shape[0], data.shape[1])
    y = np.linspace(0, 1.0/m, data.shape[0])
    x = np.linspace(0, 1.0/m, data.shape[1])
    interpolating_function = RegularGridInterpolator((y, x), data)

    yv, xv = np.meshgrid(np.linspace(0, 1.0/m, out_y), np.linspace(0, 1.0/m, out_x))

    return interpolating_function((xv, yv))
 

img = plt.imread("tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)

#brightness?

img2 = np.rot90(img,3) #zakrenuta slika

img3 = np.fliplr(img) #zrcaljena slika

img4 = regrid(img, 100, 500) #promijenjena rezolucija slike

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()