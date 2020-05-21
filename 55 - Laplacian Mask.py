import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/profile.jpg', 0)
out = cv2.Laplacian(img, -1)

plt.imshow(out)
plt.show()
