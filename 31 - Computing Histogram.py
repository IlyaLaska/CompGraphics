from PIL import Image
from pylab import *

img = Image.open('images/profile.jpg').convert('L')

imgArray = array(img)

figure()
hist(imgArray.flatten(), 128)
show()
# img.show()
