import cv2
import numpy as np

img = cv2.imread('assets/red.png', 1)
#img = cv2.resize(img, (0, 0), fx = 0.4, fy = 0.4)
img2 = img
height = img.shape[0]
width = img.shape[1]
half1 = img[0:height, 0:width//2]
half2 = img[0:height, width//2:width]

def convThresh(img):
    lower_red = np.array([0, 150, 160])
    upper_red = np.array([5, 240, 255])
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_thresh = cv2.inRange(imgHSV, lower_red, upper_red)  
    return img_thresh

h1thresh = convThresh(half1)
h2thresh = convThresh(half2)

contours1, _ = cv2.findContours(h1thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(h2thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def createContour(contours):
    coords = [[]]
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        #cv2.drawContours(half2, [approx], 0, (0, 0, 0), 5)
        n = approx.ravel() 
        i = 0
        for j in n : 
            if(i % 2 == 0): 
                x = n[i] 
                y = n[i + 1] 
                coords += [[x, y]]
                i = i + 1
    return coords

coord1 = createContour(contours1)
coord2 = createContour(contours2)
liner = cv2.line(half1, (coord1[1]), (coord1[len(coord1) - 1]), (0, 255, 0), 8)
liner2 = cv2.line(half2, (coord2[1]), (coord2[len(coord2) - 1]), (0, 255, 0), 8)
final = np.concatenate((half1, half2), axis = 1)

cv2.imwrite("answer.png", final)
cv2.waitKey(0)
cv2.destroyAllWindows()

