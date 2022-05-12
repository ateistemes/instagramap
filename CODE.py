import os
from PIL import Image, ImageFont, ImageDraw

size = (1080, 1080)
directory = os.getcwd()
cnt = 0
for im in os.listdir((directory + "/imagesbefore")):
    if im.endswith('.png'):
        image = Image.open(directory + '/imagesbefore/'  + im)
        cropped = image.resize(size)
        grey_image = cropped.convert('L')
        width, height = grey_image.size
        draw = ImageDraw.Draw(grey_image)
        text = "Timur Tynychbekov"
        font = ImageFont.truetype("Ubuntu-M.ttf", 40, )
        text_w, text_h = draw.textsize(text, font)

        x = width - text_w - 10
        y = height - text_h - 15

        draw.text((x, y), text, font=font, fill= 128)
        grey_image.save((directory + "/imagesafter/" + str(cnt) ), 'png')
        cnt += 1

