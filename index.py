import cv2

# read image
image = cv2.imread('output.jpg')

# show image
cv2.imshow("Image Show", image)

# wait while push anykey(without this, finish program soon)
cv2.waitKey(0)

# finish all window
cv2.destroyAllWindows()

# save any place
cv2.imwrite('sample.jpg', image)
