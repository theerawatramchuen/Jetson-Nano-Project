#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:47:22 2019

@author: theerawatra
"""

import cv2, os, numpy as np
cap = cv2.VideoCapture(0)
path = './image/'
h = s = p = e = 0
while True:
    _, frame = cap.read()
    key = cv2.waitKey(1) & 0xFF
    if key == ord('h'): h += 1; cv2.imwrite(path + 'hammer_' + str(h) + '.png', frame)
    if key == ord('s'): s += 1; cv2.imwrite(path + 'scissors_' + str(h) + '.png', frame)
    if key == ord('p'): p += 1; cv2.imwrite(path + 'paper_' + str(h) + '.png', frame)
    if key == ord('e'): e += 1; cv2.imwrite(path + 'else_' + str(h) + '.png', frame)
    y = []; D = []
    for fname in os.listdir(path):
        if '.png' in fname:
            x = cv2.imread(path + fname)
            y.append(fname.split('_')[0])
            D.append(np.sum((x-frame)**2))
    if len(D) > 0:
        ans = y[D.index(min(D))]
        if ans != 'else' : cv2.putText(frame, ans, (10,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
    cv2.imshow('frame', frame)
