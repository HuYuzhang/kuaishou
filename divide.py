import os
# import cv2
import json
from subprocess import *

def comp(a, b):
    return int(a[:-4]) < int(b[:-4])
def n2i(a):
    return int(a[:-4])
def f2i(a):
    return int(a.name[:-4])
train_path = "origin"

videos = os.scandir(train_path)
videos = [video for video in videos if not video.name.startswith('.') and video.is_dir()]

for video in videos:
    files = os.scandir(video.path + '/a')
    files = [f for f in files if not f.name.startswith(',') and f.is_file()]
    files.sort(key=f2i)
    file_names = [f.name for f in files]
    file_paths = [f.path for f in files]

    for i in range(405):
        cur_path = video.path + '/a/%02d'%(i / 15 + 1)
        if i % 15 == 0:
            c = Popen(['mkdir', cur_path])
            c.wait()
        c = Popen(['mv', file_paths[i], cur_path + '/%03d'%((i % 15) + 1)])
        c.wait()
    print(video.path)
    break