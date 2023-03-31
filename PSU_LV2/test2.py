import numpy as np
import matplotlib.pyplot as plt

'''''
x = np.linspace(0, 6, num=30) #generira 30 brojeva od 0 do 6 sa nekim razmakom
y= np.sin(x) 
plt.plot(x, y, 'b', linewidth=1, marker=".", markersize=5)
plt.axis([0,6,-2,2])
plt.xlabel('x')
plt.ylabel('vrijednosti funkcije')
plt.title('sinus funkcija')
plt.show()
'''''

img = plt.imread("tiger.png")
'''''
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")
plt.show()
'''''

print(type(img))
print(img.shape)

img_grayscale = img[:, :, 0]
# prvi red print(img[:, 0, 0])
# prvi piksel print(img[0, 0, 0])

img_grayscale[0, 0] = 1
print(img[0, 0, 0])
print(img_grayscale[0, 0])


