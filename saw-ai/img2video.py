import cv2,os
import glob
import numpy as np

def main():
    img_array = []
    for filename in glob.glob ('C:/Users/41162395/Desktop/Dataset/*.jpg'): #('C:/New folder/Images/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('saw.avi', cv2.VideoWriter_fourcc(*'DIVX'), 2, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

if __name__ == '__main__':
    main()