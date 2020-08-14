import os
import sys
from datetime import datetime
src_folder , dst_folder = sys.argv[1] , sys.argv[2]
w = list(os.walk(src_folder))
picturesPrefix= [".jpg", ".jpeg", ".png"]
videosPrefix = [".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov"]
def isVideo(name):
    for pre in videosPrefix:
        if name.lower().endswith(pre):
            return True
    return False
def isPicture(name):
    for pre in picturesPrefix:
        if name.lower().endswith(pre):
            return True
    return False
def copy(src ,dstfolder , filename):
    if not os.path.exists(dstfolder):
        os.makedirs(dstfolder)
    with open(src,"rb") as org,open(os.path.join(dstfolder ,filename),'wb') as cop:
        cop.write(org.read())
for files in w:
    for file in files[2]:
        file_address = files[0] + "/" + file
        year = str(datetime.fromtimestamp(os.path.getmtime(file_address)).year)
        if isVideo(file):
            copy(file_address ,os.path.join(dst_folder , year , "videos") ,file)
        if isPicture(file):
            copy(file_address , os.path.join(dst_folder , year , "photos") ,file)