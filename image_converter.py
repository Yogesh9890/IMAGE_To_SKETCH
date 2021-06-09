import numpy as np 
import cv2
import imageio
import scipy.ndimage

img = input("Enter Name Of Image: ")

def grayscale(asd):
    return np.dot(asd[...,:3],[0.299,0.587,0.114])

def dodge(front, back):
    result = front*255/(255-back+1)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')      #uint for 8 bit integer

a = imageio.imread(img)
b = grayscale(a)
i = 255 - b

f = scipy.ndimage.filters.gaussian_filter(i, sigma=45)
r = dodge(f, b)

cv2.imwrite(img + '(1)', r)
