import cv2

img = cv2.imread( "png.png" )
cv2.imshow( "name", img )
cv2.waitKey(0)
cv2.destroyAllWindows()
