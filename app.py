# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from texting import text
import time
img1 = cv.imread('towlogo400p.png',cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('towtruck720p.jpg',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# outputs the image
#plt.imshow(img3)
#plt.show()
# prints length of matches and if length is long enough prints "Logo Detected" to console along with texting user
print(len(matches))
if len(matches) > 100:
  print("Logo Detected!")
  text.textme()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
