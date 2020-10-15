from PIL import Image

img = Image.new('RGB', (256, 144))

print(img.load()[4,4])

img.save('image.png')
