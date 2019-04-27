import os
# import cv2
import json
from subprocess import *

def comp(a, b):
    return int(a[:-4]) < int(b[:-4])
def n2i(a):
    return int(a[:-4])
train_path = "origin"

videos = os.scandir(train_path)
videos = [video for video in videos if not video.name.startswith('.') and video.is_dir()]

for video in videos:
    files = os.scandir(video.path)
    files = [f for f in files if not f.name.startswith(',') and f.is_file()]

    # I'm sad to say that we have to add this 'mid_path' to the path
    # Because the Dataset class force me to do like that :(
    # Then in this mid_path, I will make 9 folders, which name from 01 to 09 to cater the Dataset class
    # Because we need 9 * 15 * 3 images, which equals to 405.
    # However, in some videos, the frame's number is less than it.
    # In this situation, I...emmm decide to copy some image to make sure that the total number is 405
    # That might sounds absurd, but what can I do 555? For I have no access to Youtube
    mid_path = video.path + '/a'
    if not os.path.exists(mid_path):
        c = Popen(['mkdir', mid_path])
        c.wait()

    file_names = [f.name for f in files]
    file_names.sort(key=n2i)
    file_ids = [int(name[:-4]) for name in file_names]
    file_ids.sort()
    

    # %%% STEP 1: Copy frame to 405 frames %%%
    # Now we have less than 405 images
    # (In fact, I see all the videos and sadly, no video has more than 405 frames)
    length = len(file_ids)
    if (length < 405):
        for _id in range(length, 405):
            # print(video.path + '/' + file_names[_id - length], mid_path + '/' + str(id) + '.png')
            c = Popen(['cp', video.path + '/' + file_names[(_id - length) % length], mid_path + '/' + str(_id + 1) + '.png'])
            c.wait()

    # %%% STEP 2: Move original frame to a folder and rename %%%
    for i in file_ids:
        c = Popen(['mv', video.path + '/' + str(i) + '.png', mid_path + '/' + '%03d'%(i + 1) + '.png'])
        c.wait()
    print(mid_path + "OK")