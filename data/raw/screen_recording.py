import cv2
import pyautogui
import numpy as np

#Specify resolution
resolution = (1928,1080)

#Specify Video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
# fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v') # note the lower case

#Specify name of the output file
filename = "Recording.avi"
#Specify frames rate. We can choose any value and experiment with it
fps = 20.0
#Creating a Videowriter object
out = cv2.VideoWriter(filename,codec,fps,resolution)
#Create an Empty window
cv2.namedWindow("Live",cv2.WINDOW_NORMAL)
#Resize this window
cv2.resizeWindow("Live",640,480)

while True:
    #Take Screenshot using PyAutoGUI
    img = pyautogui.screenshot()
    #Convert the screenshot to a numpy array
    frame = np.array(img)
    #Convert it from BGR to RGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #Write it to the output file
    out.write(frame)
    #Optional : Display the recording screen
    cv2.imshow('Live',frame)
    #Stop recording when we press 'q'quit
    if cv2.waitKey(1) == ord('q'):
        break

#Release the Video writer
out.release()
#Destroy all windows
cv2.destroyAllWindows()