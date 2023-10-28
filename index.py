import cv2

# read image
image = cv2.imread('output.jpg')

# resize image
image_resized = cv2.resize(image, (500, 300))

# put text on image
font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(image_resized,'Hello World!', (50,50), font,1, (0, 255, 0), 1)

# put line to image(line-weight=-1, fill in image)
cv2.rectangle(image_resized, (50,50), (200,100), (20, 20, 20), -1)

# rotate 90 dgr
# rotated_image =cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) 

# change color to gray
# gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

# show image
# cv2.imshow("Image Show", image)
cv2.imshow("Image Show", image_resized)
# cv2.imshow("Image Show",rotated_image)
# cv2.imshow("Image Show",gray_image)

# wait while push anykey(without this, finish program soon)
cv2.waitKey(0)

# finish all window
cv2.destroyAllWindows()

# save any place
# cv2.imwrite('images/nice_img.jpg', image_resized)
