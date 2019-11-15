from PIL import Image, ImageFilter

before = Image.open('destination.jpg')
after = before.filter(ImageFilter.BLUR)
after.save('output.jpg')