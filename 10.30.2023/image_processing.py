from PIL import Image

image = Image.open('photo.jpg')
image = image.rotate(45, fillcolor='Red')
image.save('out.jpg')