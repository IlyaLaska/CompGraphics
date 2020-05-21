import numpy as np 
import scipy.misc, math
from PIL import Image

img = Image.open('images/lena512.bmp')
img1 = np.asarray(img)#scipy.misc.fromimage(img)
fl = img1.flatten()

hist, bins = np.histogram(img1, 256, [0,255])
cdf = hist.cumsum()
cdfNoZeroes = np.ma.masked_equal(cdf, 0)

numeratorCdfNoZeroes = (cdfNoZeroes - cdfNoZeroes.min())*255
denominatorCdfNoZeroes = (cdfNoZeroes.max() - cdfNoZeroes.min())
cdfNoZeroes = numeratorCdfNoZeroes / denominatorCdfNoZeroes

cdf = np.ma.filled(cdfNoZeroes, 0).astype('uint8')

im2 = cdf[fl]
im3 = np.reshape(im2, img1.shape)
im4 = Image.fromarray(im3)
im4.show()
