from PIL import Image

width = 256
height = 144

img = Image.new('RGB', (width, height))

px = img.load()

for i in range(width):
    for j in range(height):
        px[i,j] = (0, 0, 0) if (height/2-j)**2+(i-width/2)**2>4096 or (height/2-j)**2+(i-width/2)**2<3136 else (255, 255, 255)

img.save('image.png')
