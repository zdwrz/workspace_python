import PIL
import os
from PIL import Image
from io import BytesIO
from os import path


def resize_pic(width_size, targetFile, targetFolder):
    extension = path.splitext(targetFile)[1].lower()
    filename = os.path.basename(targetFile)

    if extension in ['.jpeg', '.jpg']:
        format = 'JPEG'
    if extension in ['.png']:
        format = 'PNG'
    # Resizing the image
    img = Image.open(targetFile)
    wpercent = (width_size / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    if img.size[0] > width_size:
        img = img.resize((width_size, hsize), PIL.Image.ANTIALIAS)

    compressed_folder = os.path.join(targetFolder, "compressed")
    if not os.path.exists(compressed_folder):
        os.mkdir(compressed_folder)
    img.save(os.path.join(compressed_folder ,filename), format)
    print("File is saved in : " + os.path.join(compressed_folder ,filename))

def compress(target, width_size):
    isdir = os.path.isdir(target)
    if isdir:
        print(target + " is a folder")
        for root, dirs, files in os.walk(target):
            path = root.split(os.sep)
            print((len(path) - 1) * '-', os.path.basename(root))
            for file in files:
                ext = os.path.splitext(file)[1].lower();
                if( ext in ['.jpeg','.jpg', '.png']):
                    print(len(path) * '-', root + file)
                    resize_pic(width_size, root + file, root)
        print("All Done")
    else:
        print("Compressing just one file")
        resize_pic(width_size, target, os.path.dirname(target))

compress("/Users/daweizhuang/Desktop/SIS_Test/", 1000)
# resize_pic(600, "/Users/daweizhuang/Desktop/SIS_Test/IMG_20180612_143545.jpg","/Users/daweizhuang/Desktop/SIS_Test_Compressed")
