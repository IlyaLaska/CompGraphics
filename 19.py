from PIL import Image

img = Image.open('./images/profile.jpg')

imgGrey = Image.open('./images/profile.jpg').convert('L')

imgGrey.show()
