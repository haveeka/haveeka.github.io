import os
from PIL import Image
from resizeimage import resizeimage

base_folder = input("Enter the folder path: ")

for r,d,f in os.walk(base_folder):
    for file in f:
        if '.jpg' or '.jpeg' or '.png' in file:
            print("Resizing "+file)
            with Image.open(file) as image:
                cover = resizeimage.resize_cover(image, [270, 280])
                rename = "icon_"+file
                cover.save(rename, image.format)