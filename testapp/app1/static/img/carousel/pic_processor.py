from PIL import Image
im = Image.open('default2.jpg')
im2 = Image.open('top1.jpg')
print(im.size)
print(im2.size)
im2_resize = im2.resize(im.size)
im2_resize.save('top2.jpg')
