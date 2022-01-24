#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File mp4_to_gif.py
# Date 2019-07-03 10:43
# Author Medue

import time
import datetime
import os
import hashlib
from cv2 import VideoCapture
from moviepy.editor import *

dir_paths = '/Users/akio/Downloads/ofs0qJ7z/'

files = os.listdir(dir_paths)


def get_file_size(file_path):
    f_size = os.path.getsize(file_path)
    f_size = f_size/float(1024)
    return round(f_size, 2)


for file in files:
    file_ext = str(os.path.splitext(file)[-1]).lower()
    if file_ext != '.mp4':
        continue
    file_name = dir_paths+file
    file_size = int(get_file_size(file_name))
    clip = VideoFileClip(file_name)
    v_len = clip.duration
    if v_len > 10:
        v_len = 6

    if v_len < 3:
        zoom = 0
    elif 3 <= v_len <= 5:
        zoom = 1
    elif 5 < v_len < 7:
        zoom = 2.4
    else:
        zoom = 2.7
    # zoom = 2
    cap = VideoCapture(file_name)
    # 获取视频信息
    if zoom > 0:
        content = clip.subclip(0, v_len).resize((int(cap.get(3)/zoom), int(cap.get(4)/zoom)))  # 修改分辨率
    else:
        content = clip.subclip(0, v_len)  # 不修改分辨率
    # 导出GIF
    md5 = hashlib.md5()
    md5.update(file_name.encode(encoding='utf-8'))
    gif_name = md5.hexdigest()+'.gif'

    fuzz = 1

    if file_size > 1600:
        fuzz = 0.5

    content.write_gif(filename=dir_paths+gif_name, fuzz=fuzz, fps=12)

    del(
        clip,
        cap,
        md5
    )
pass
