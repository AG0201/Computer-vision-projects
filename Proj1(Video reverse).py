#Import library
import cv2

#Video capture instance
cap=cv2.VideoCapture('template.mp4')

#Storing properties of video
frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)        #Total no. of frames in video
fps=cap.get(cv2.CAP_PROP_FPS)                   #fps of video
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)       #height
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)         #width

#Initialize the output writer for video
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('Reverse.mp4',fourcc,fps,(int(width*0.5),int(height*0.5)))

print(f"No. of frames = {frames}")
print(f"fps = {fps}")

#Getting index of last frame of video file
frame_index=frames-1

#Checking if video instance is ready
if(cap.isOpened()):
    #Reading till end of video
    while(frame_index!=0):
        #We set current frame position to last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)        #POS frames stands for position of frame
        ret, frame=cap.read()

        #Resize the frame
        frame=cv2.resize(frame,(int(width*0.5),int(height*0.5)))

        #Optional: To show the reverse video
        #cv2.imshow('Window',frame)

        #Writing the reversed video
        out.write(frame)
        #Decrementing frame index at each step
        frame_index-=1

        #Printing the progress
        if(frame_index%100==0):
            print(frame_index)
        
        # if(cv2.waitKey(2)==ord('q')):
        #     break

out.release()
cap.relaese()
cv2.destroyAllWindows()



