#!/usr/bin/env python3

from PIL import Image
from os import listdir, path
import os

# gather list of image files:
files = [f for f in listdir("supplier-data/images") if f.endswith(".tiff")]

# reprocess images:
for file in files:
    src_img = Image.open(os.path.join("supplier-data/images", file))
    new_img = src_img.resize((600,400))
    #convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")
    #Extracting extension from filename in Python
    file, ext = path.splitext(file)
    file += ".jpeg"
    new_img.save("supplier-data/images" + file,"JPEG")
    print(new_img)
    new_img.show()




