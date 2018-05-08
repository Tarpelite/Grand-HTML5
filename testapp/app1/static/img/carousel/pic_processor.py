from PIL import Image
im = Image.open('example2.jpg')
im2 = Image.open('logo.jpg')
print(im.size)
print(im2.size)
im2_resize = im2.resize((300, 150))
im2_resize.save('beihanglogo.jpg')
