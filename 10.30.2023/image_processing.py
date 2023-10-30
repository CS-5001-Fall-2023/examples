from PIL import Image

im = Image.open('photo.jpg')
im = im.rotate(45)
im.save('out.jpg')


