#LINES,SHAPES,POLYGONS,TEXT//ALIASING//FIGURE AND TEXT

import cv2
from cv2 import LINE_8
import numpy as np

# #Creating a canvas 500x500(Three channels-BGR)
# canvas=np.zeros((500,500,3))

# #Drawing a LINE
# #Line types and the algorithms used--- Line 4 and Line 8 - Bresenham algorithm, Line AA - Gaussian filtering
# #Line 4 and Line 8 are aliased while line AA is anti aliased
# cv2.line(canvas,(0,0),(100,100),(0,255,0),2,cv2.LINE_4)
# cv2.line(canvas,(0,20),(120,120),(0,255,0),2,cv2.LINE_AA)

# #Drawing a RECTANGLE
# cv2.rectangle(canvas,(0,0),(200,300),(0,0,255),-1)
# #Drawing a CIRCLE
# cv2.circle(canvas,(250,250),20,(255,0,0),3)
# #Drawing a ARROWED LINE
# cv2.arrowedLine(canvas,(400,400),(400,500),(255,255,0),tipLength=0.3)

# #Drawing a POLYGON
# pts=np.array([[250,5],[220,80],[280,80],[100,100],[250,250]],np.int32)
# #Here Boolean True and False indicate if polygon is closed or open
# cv2.polylines(canvas,[pts],True,(0,255,0),3)
#------------------------------------------------------------------------------------

canvas=np.zeros((800,500))

#List of all fonts
fonts = [cv2.FONT_HERSHEY_COMPLEX,
            cv2.FONT_HERSHEY_DUPLEX,
            cv2.FONT_HERSHEY_PLAIN,
            cv2.FONT_HERSHEY_SIMPLEX,
            cv2.FONT_HERSHEY_TRIPLEX,
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX]

position=(10,30)
for i in range(0,8):
    cv2.putText(canvas,"THIS IS OPENCV !",position,fonts[i],1.1,(255,255,255),2,cv2.LINE_AA)
    position=(position[0],position[1]+40)
    cv2.putText(canvas,"THIS IS OPENCV !".lower(),position,fonts[i],1.1,(255,255,255),2,cv2.LINE_AA)
    position=(position[0],position[1]+40)






#Showing the canvas
cv2.imshow('Window name',canvas)
cv2.waitKey(10000)