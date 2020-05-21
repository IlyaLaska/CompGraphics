from PIL import Image

img = Image.open('images/profile.png')

#Resize
smallImg = img.resize((2000, 2000))
# smallImg.show()

#Crop
box = (200, 200, 400, 400)
region = img.crop(box)
# region.show()

#Rotation

rotatedImg = img.rotate(80)
rotatedImg.show()
