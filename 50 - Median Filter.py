#Mean and Median for Noise reduction

from PIL import Image
import scipy.ndimage as sc
import scipy.misc as sm

# import numpy as np

a = Image.open('images/lena_noisy.png')

b = sc.filters.median_filter(a, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

b = Image.fromarray(b)

b.show()
