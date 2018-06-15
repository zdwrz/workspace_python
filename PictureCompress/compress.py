import PIL
import os
from PIL import Image
from io import BytesIO
from os import path
import zipfile

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
    return os.path.join(compressed_folder ,filename)

def compress(target, width_size, createzip=True):
    isdir = os.path.isdir(target)
    if isdir:
        print(target + " is a folder")
        for root, dirs, files in os.walk(target):
            path = root.split(os.sep)
            # print((len(path) - 1) * '-', os.path.basename(root))
            for file in files:
                ext = os.path.splitext(file)[1].lower();
                if( ext in ['.jpeg','.jpg', '.png']):
                    full_path = os.path.join(root, file)
                    print(len(path) * '-', full_path, "is compressing...to...")
                    try:
                        print(len(path) * '--', resize_pic(width_size, full_path, root))
                    except:
                        print("Cannot compress file: " + full_path)
        if createzip:
            zipPath(os.path.join(target,"compressed"), target)
        print("All Done")
    else:
        print("Compressing just one file")
        resize_pic(width_size, target, os.path.dirname(target))

def zipPath(target, destination):
    zf = zipfile.ZipFile(os.path.join(destination,"compressed_files.zip"), mode="w", compression= zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(target):
        for file in files:
            zf.write(os.path.join(root, file), file)
    print("Created zip file: " + zf.filename)

# zipPath("/Users/daweizhuang/Desktop/SIS_Test/compressed/")
compress("/Users/daweizhuang/Desktop/SIS_Test/", 1000)
# resize_pic(600, "/Users/daweizhuang/Desktop/SIS_Test/IMG_20180612_143545.jpg","/Users/daweizhuang/Desktop/SIS_Test_Compressed")
