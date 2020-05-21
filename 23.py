from PIL import Image
from pylab import *

im = array(Image.open('images/profile.jpg'))
imshow(im)

x = [150,150, 300, 300]
y = [50, 500, 10, 600]
plot(x, y, 'r*')
plot(x[:2], y[:2], 'r')
plot(x[2:], y[2:], 'ks:')

title('Plotting')

show()
