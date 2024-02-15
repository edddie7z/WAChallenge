# Wisconsin Autonomous Perception Coding Challenge - Edward Zhao

# Methodology 
For my libraries, I used OpenCV for image processing and NumPy for array use. I started by splitting the given image in half as there are two lines of cones, one on each half of the image. Each half was converted into HSV images with a given range of red to show only the cones, turning each half into a threshold image of the cones. Then, I found the contours of all the cones on each image and saved the coordinates onto an array. I drew the lines by using the coordinates for the highest cone and the lowest cone on each image. Finally, I concatenated both halves to form the final image with the drawn boundary lines on the cones. 

What I tried and why I think it did not work: 
One thing I tried was to use HoughLines to try to detect the boundary line drawn by the cones. However, I think this did not work because the cones were too far apart and HoughLines only works on detecting fully drawn lines that are already in the image. 

# Answer Image
![](https://github.com/edddie7z/WAChallenge/blob/main/answer.png)


