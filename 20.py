from PIL import Image
import os

filelist = ['./images/profile.jpg', './images/moon.jpg']

for fIn in filelist:
  print(os.path.splitext(fIn))
  fOut = os.path.splitext(fIn)[0] + '.png'
  try:
    Image.open(fIn).save(fOut)
  except IOError:
    print('Could not convert', fIn)
