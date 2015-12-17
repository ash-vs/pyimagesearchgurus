# import packages
import argparse
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, grab its dimensions, and show it
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# access the NumPy array representing the image
(b, g, r) = image[0, 0]
print "Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

# change the value of the previously retrieved pixel to be red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print "Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

# get the value for the quiz
(b, g, r) = image[225, 111]
print "Pixel at x = 111 and y = 225 - Red: {r}, Green {g}, Blue: {b}".format(r=r, g=g, b=b)

# compute the center of the image
(cX, cY) = (w / 2, h / 2)

# grab the top left corner of the image
top_left = image[0:cY, 0:cX]
top_right = image[0:cY, cX:w]
bottom_right = image[cY:h, cX:w]
bottom_left = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", top_left)
cv2.imshow("Top-Right Corner", top_right)
cv2.imshow("Bottom-Right Corner", bottom_right)
cv2.imshow("Bottom-Left Corner", bottom_left)

# make the top-left corner of the original image green
image[0:cY, 0:cX] = (0, 255, 0)

# show the updated original image
cv2.imshow("Updated", image)

cv2.waitKey(0)
