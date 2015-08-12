import cv2
import numpy

cap = cv2.VideoCapture(0)
#cv2.namedWindow( "vidcap.py", cv2.WINDOW_AUTOSIZE )
#textOrg = point((img.cols - textSize.width)/2, (img.rows + textSize.height)/2)
text = "opencv"
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 1
retval, baseline = cv2.getTextSize(text, fontFace, fontScale, thickness)
x = 0
y = retval[1]
print retval
print baseline

while 1:
    ret, frame = cap.read()
    if frame != None:
        height = frame.shape[0]
        width = frame.shape[1]
    cv2.putText( frame, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, thickness, (0,0,0) )
    cv2.imshow( "vidcap.py", frame )
    key = cv2.waitKey(1)
    if( key == 32 or key == 27 ):
        break
    elif key == 65361:
        x -= 10
        print "left"
    elif key == 65362:
        y -= 10
        print "up"
    elif key == 65363:
        print "right"
        x += 10
    elif key == 65364:
        y += 10
        print "down"
    elif key == -1:
        pass
    else:
        print key
    print "xy", x, y
    print "baseline", baseline
print "width", width
print "height", height
