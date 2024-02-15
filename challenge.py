import cv2
import numpy as np

img = cv2.imread('assets/red.png', 1)
# Resized image to work with easier (Commented out)
#img = cv2.resize(img, (0, 0), fx = 0.4, fy = 0.4)
img2 = img
# Finds dimensions of image
height = img.shape[0]
width = img.shape[1]
# Splits image vertically into 2 halves, 1 half for each line
half1 = img[0:height, 0:width//2]
half2 = img[0:height, width//2:width]

def convThresh(img):
    # Range of red for threshold
    lower_red = np.array([0, 150, 160])
    upper_red = np.array([5, 240, 255])
    # Convert from BGR to HSV image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Returns threshold image of cones
    img_thresh = cv2.inRange(imgHSV, lower_red, upper_red)  
    return img_thresh

# Converts each half into threshold images of cones
h1thresh = convThresh(half1)
h2thresh = convThresh(half2)

# Find contour list 
contours1, _ = cv2.findContours(h1thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(h2thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def createContour(contours):
    coords = [[]]
    for cnt in contours:
        # Creates contour approximations
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        # Draws contours on the image (Commented out)
        #cv2.drawContours(half2, [approx], 0, (0, 0, 0), 5)
        n = approx.ravel() 
        i = 0
        # Adds coordinates of contours into an array
        for j in n : 
            if(i % 2 == 0): 
                x = n[i] 
                y = n[i + 1] 
                coords += [[x, y]]
                i = i + 1
    return coords

coord1 = createContour(contours1)
coord2 = createContour(contours2)
# Draws lines based on highest cone and lowest cone in each half
liner = cv2.line(half1, (coord1[1]), (coord1[len(coord1) - 1]), (0, 255, 0), 8)
liner2 = cv2.line(half2, (coord2[1]), (coord2[len(coord2) - 1]), (0, 255, 0), 8)
# Concatenates both halves to form final image
final = np.concatenate((half1, half2), axis = 1)
# Saves image as a file
cv2.imwrite("answer.png", final)

'''
cv2.imshow("Image", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
