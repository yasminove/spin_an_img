from PIL import Image

img = Image.open('baby.jpeg')

spin_img = img.transpose(Image.ROTATE_90)

spin_img.show()