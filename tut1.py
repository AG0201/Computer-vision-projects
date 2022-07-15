#Image,Video Read/Write
import cv2
#Channel order is BGR in Color mode
img = cv2.imread('doraemon.jpg',cv2.IMREAD_COLOR)
#function to display
#cv2.imshow('Window name',img)
#cv2.waitKey()
#------------------

#VIDEO CAPTURE
# cap=cv2.VideoCapture(0)             #read video from webcam
# opened=cap.isOpened()               #check if camera is open

# height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)       #properties
# width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# frame_rate=cap.get(cv2.CAP_PROP_FPS)
# aperture=cap.get(cv2.CAP_PROP_APERTURE)
# focus=cap.get(cv2.CAP_PROP_FOCUS)

# print(f"Height = {height}, Width = {width}, Frame rate = {frame_rate}, Aperture = {aperture}, Focus = {focus}")

# if(opened):                                 #if camera is open
#     while(cap.isOpened()):                  #Till camera is open
#         ret, frame=cap.read()               #Store camera feed in frame, ret gives boolean for feed(true means it is receiving feed)
#         if(ret==True):                      
#             cv2.imshow('Window name',frame)         #showing feed
#             if(cv2.waitKey(2)==27):                 #check for any key press every 2 msec, ASCII value for esc key is 27
#                 break
# cap.release()
# cv2.destroyAllWindows()
#----------------------------------------------------------------------------

#VIDEO WRITER

cap=cv2.VideoCapture(0)
opened=cap.isOpened()

#fourcc
fourcc=cv2.VideoWriter_fourcc(*'MJPG')

height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)       #properties
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_rate=cap.get(cv2.CAP_PROP_FPS)

#Video writer
out=cv2.VideoWriter('Video.mp4',fourcc,frame_rate,(int(width),int(height)))

if(opened):
    while(cap.isOpened):
        ret, frame=cap.read()
        if(ret==True):
            cv2.imshow('Window',frame)
            out.write(frame)
            if(cv2.waitKey(2)==27):
                break
out.release()
cap.release()
cv2.destroyAllWindows()



