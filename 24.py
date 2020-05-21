from PIL import Image
from pylab import *

im = array(Image.open('images/profile.jpg'))
imshow(im)

#Selecting 4 points
pt = ginput(4)

print('Selected', pt)

show()
