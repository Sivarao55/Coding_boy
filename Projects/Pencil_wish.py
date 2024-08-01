import cv2

filename = 'Sivarao.jpg'#put image path

img = cv2.imread(filename)
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow('original Image',img)
cv2.imshow('Now Image',gray_image)
cv2.waitKey(0)
