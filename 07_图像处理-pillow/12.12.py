from PIL import Image
import glob,os
size = (128,128)
for infile in glob.glob("D:/python/ch12/*.jpg"):
    f, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size,Image.ANTIALIAS)
img.save(f+".thumbnail","JPEG")
