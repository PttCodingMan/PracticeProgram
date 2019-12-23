from PIL import Image


# Starbucks_Coffee.png

TargetImage = '星巴克.jpg'

im = Image.open(TargetImage)
im = im.convert('RGB')
width, height = im.size

# print(width, height)

pix = im.load()

print(im.size)
print(pix[0, 0])

img = Image.new('RGB', (width * 2, height * 2))
img.save(TargetImage.replace('.', '_result.'))
