import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import RegularGridInterpolator

#default size: 960x640
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
#print(img.shape)
#print(img.dtype)

#b)
img1 = np.rot90(img, 3) #zarotirana slika

#c)
img2 = np.fliplr(img) #zrcaljena slika

#d)
img3 = regrid(img, 96, 64) #rezolucija smanjena 10 puta - default rezolucija je 960x640

#e)
left1, right1 = np.hsplit(img, [480])
prva_cetvrtina, druga_cetvrtina = np.hsplit(left1, [240])

arr_zeros = np.zeros((640, 240))#cetvrtina - crnilo
arr_zeros2 = np.hstack((arr_zeros, arr_zeros))#polovina - crnilo

img4 = np.hstack((arr_zeros, druga_cetvrtina))
img4 = np.hstack((img4, arr_zeros2))


plt.figure()
#plt.imshow(img4, cmap="gray")

#a)
#plt.imshow(img, cmap="gray", vmin = -1, vmax = 1) #povećan brightness - vmin mijenjamo u neg smjeru, vmax ostaje 1
plt.imshow(img, cmap="gray", vmin = 0, vmax = 10) #smanjen brightness - vmax mijennjamo u pozitivnom smjeru, vmin ostaje 0

plt.show()
