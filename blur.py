# Importing necessary Libraries
from PIL import Image, ImageFilter

# Loading the Image
before = Image.open('input.jpg')

# Operating the blur effect on the image
after = before.filter(ImageFilter.BLUR)

# Saving the image as output
after.save('output.jpg')