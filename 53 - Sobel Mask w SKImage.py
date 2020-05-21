from PIL import Image
from skimage import filters
from scipy import ndimage

a = Image.open('images/moon.jpg')

b = filters.sobel(a)

b = Image.fromarray(b)

b.show()
