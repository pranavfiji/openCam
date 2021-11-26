import cv2
import numpy as np 
import time 

fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter("invicloak.avi",fourcc,20.0,(640,480))


cam=cv2.VideoCapture(0)

time.sleep(2)
bg=0

for  i in range(60):
    ret,bg = cam.read()

frame=0
while(cam.isOpened()):
    ret,img,=cam.read()

    img=cv2.imread("hi.jfij")
     

    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))

    hsv=cv2,cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    u_black=np.array([104,153,70])
    l_black=np.array([30,30,0])
    mask_1 = cv2.inRange(hsv, u_black, l_black)
    res=cv2.bitwise_and(frame,frame,mask=mask_1)

    f=frame-res
    f=np.where(f==0,image,f)
    finalOutput=cv2.addWeighted(res)
    if not ret:
        break

    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()


