#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 18-10-26 上午11:00 
# @Author : Xier
# @File : img2avi.py 


import cv2
import os
import numpy as np
from PIL import Image, ImageDraw,ImageFont

fps = 5
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video_writer = cv2.VideoWriter(filename='./result.avi', fourcc=fourcc, fps=fps, frameSize=(480,360))

for i in range(370):
    p = str(i).zfill(4)
    # print(str(p)+'.png'+'233333')
    if os.path.exists('/home/chenxier/mosse-object-tracking/datasets/surfer/'+p+'.jpg'):
    # #判断图片是否存在
        img = cv2.imread(filename='/home/chenxier/mosse-object-tracking/datasets/surfer/'+p+'.jpg')
        cv2.waitKey(100)
        video_writer.write(img)
        print(str(p) + '.jpg' + ' done!')
video_writer.release()
