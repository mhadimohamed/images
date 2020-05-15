
"""
this code is how convert your images to csv 
data fil using python PIL
(Python Imaging Library)
"""
from PIL import Image
import numpy as np
import os
import csv
import sys
"""create foldar and put your
images in the folder"""

filelist=[]
def createfilelist(myDir,format='.png'):
    print(myDir)
    for root,dirs,files in os.walk(myDir,topdown=False):
        for name in files:
            if name.endswith(format):
                fullName=os.path.join(root,name)
                filelist.append(fullName)
    return filelist

"""load the original images"""

the_filelist=createfilelist("‪Users\ACER\Pictures")
for file in filelist:
    print(i)
img_file = Image.open(file)
    
"""get the original parametres of images"""

heigth = img_file.size
width = img_file
format = img_file.format
mode = img_file.mode

"""convert the original images to nympy array"""

x = np.asarray(img_file.getdata(),dtype=np.int)
x = x.flatten()
print(x)
with open("img_csv_data.csv","a",newline="")as f:
    writer = csv.writer(f)
writer.writerow(x)


    
                            