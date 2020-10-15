from PIL import Image

img = Image.new('RGB', (256, 144))

print(im.load()[4,4])

img.save('image.png')
