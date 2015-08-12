import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread( "png.png" )
plt.imshow( img )
plt.xticks([]), plt.yticks([])
plt.show()
