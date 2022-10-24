from CatVisionDetectron import *
from ModeloJoe.modeloJoe import *
import uuid

import cv2

cap = cv2.VideoCapture(0) 
ret,frame = cap.read() 

while(True): 
    if cv2.waitKey(1) & 0xFF == ord('y'):
        imageName = 'images/'+str(uuid.uuid4())+'.jpg'
        cv2.imwrite(imageName,frame)
        cv2.destroyAllWindows()
        break

cap.release()

predictionDetectron2(imageName)
jason = prediction()
yayhijomuerde = bytes(str(jason),"utf-8")

