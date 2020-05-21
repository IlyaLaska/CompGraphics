# from PIL import Image
import cv2
# from skimage import img_as_ubyte
# import skimage as s
# import scipy.ndimage as sc
# import scipy.misc as sm
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/profile.jpg', 0)
# img = s.img_as_int(moon)

sobelX = cv2.Sobel(img, -1, 1, 0, ksize=5)
sobelY = cv2.Sobel(img, -1, 0, 1, ksize=5)



plt.imshow(sobelX, cmap='gray')
plt.show()
plt.imshow(sobelY, cmap='gray')
plt.show()
