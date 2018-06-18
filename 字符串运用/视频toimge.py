#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/6/13"



import numpy as np
import cv2
import os

#视频来源路径
input_path = './视频路径'
#图片保存路径
output_path = './Images'
image_id = 0

def movie2image(movie_full_name, output_path):
    global image_id
    image_id += 1
    movie_path, movie_name = os.path.split(movie_full_name)
    file_title = os.path.splitext(movie_name)[0]
    output_path = '%s/%d.%s' % (output_path, image_id, file_title)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    frame_id = 0
    cap = cv2.VideoCapture(movie_full_name)
    while True:
        ret, im = cap.read()
        if im is None:
            break
        frame_id += 1
        image_name = '%s/%s%03d.png' % (output_path, file_title, frame_id)
        im_np = cv2.imencode('.png', im)[1]
        im_np.tofile(image_name)


def is_movie(ext):
    return ext.lower() in set(['.mp4', '.mpeg', '.mpg', '.avi', 'rm', 'rmvb'])


def movie2image_all(input_path, output_path):
    for name in os.listdir(input_path):
        full_name = '%s/%s' % (input_path, name)
        if os.path.isdir(full_name):
            movie2image_all(full_name, output_path)
        else:
            ext = os.path.splitext(name)[1]
            if ext and is_movie(ext):
                print(full_name)
                movie2image(full_name, output_path)


if not os.path.exists(output_path):
    os.makedirs(output_path)
movie2image_all(input_path, output_path)
print('OK....')
