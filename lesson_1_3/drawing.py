# import the necessary packages
import numpy as np
import cv2

# time delay in ms
delay = 500

# initialize our canvas as a 300x300 array
# with 3 channels (R, G, & G), with a black
# background
canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.waitKey(delay)

# draw a green line from the top-left corner of our
# canvas to the bottom-right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(delay)

# draw a 3-pixel thick red line from the top-right
# corner to the bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(delay)

# draw a green 50x50 pixel square,
# starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(delay)

# draw another rectangle, this time we'll
# make it red and 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(delay)

# draw a solid blue rectangle
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(delay)

# reset the canvas and draw a while circles
# at the center of the canvas with radii that
# increase from 0 px to 150 px
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)
white = (255, 255, 255)
cv2.imshow("Canvas", canvas)
cv2.waitKey(delay)

for r in xrange(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(delay)

# let's now draw 25 random circles
for i in xrange(0, 25):
    # randomly generate a radius size between 5 and 200,
    # pick a random color, and then pick a random point
    # on the canvas where the circle will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    # draw our random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(delay)

# load a canvas with an image
image = cv2.imread("florida_trip.jpg")
cv2.imshow("Image", image)
cv2.waitKey(delay)

# draw a circle around the face, two circles covering the eyes
# and a rectangle surrounding the mouth
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

# show our work of art
cv2.imshow("Image", image)
cv2.waitKey(0)
