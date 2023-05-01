import sys
import os
from PIL import Image, ImageOps



if len(sys.argv) == 1:
    print('\n    Please specify file path\n')
else:
    file_path = sys.argv[1]
    file_name = os.path.splitext(file_path)[0]
    file_extension = os.path.splitext(file_path)[1]
    new_file_path = file_name + '_transparent.png'

    # get original image
    try:
        original_image = Image.open(file_path).convert('RGBA')
    except FileNotFoundError as e:
        print('\n    ' + file_path + ' not found, try again\n')
        exit()

    # create same size image filled with white
    white_bg = original_image.copy() # to have the same file settings
    white_bg.paste('white', [0,0,white_bg.size[0],white_bg.size[1]])

    # create image with original image on top of white background
        # might look a little different from the original, but it is correct
        # will look exactly the same as in an image editing software
        # not sure why but w/ white bg and w/o bg on somewhere white looks a bit different
    image_with_bg = Image.alpha_composite(white_bg, original_image)

    # get brightness from the image
    brightness = ImageOps.invert(image_with_bg.convert('RGB')).convert('L')

    # create new image, filled with black, of same size
    black = Image.new('L', original_image.size, color='black')

    # set transparency as the brightness
    black.putalpha(brightness)

    # save new file (will overwrite the existing file)
    black.save(new_file_path)
