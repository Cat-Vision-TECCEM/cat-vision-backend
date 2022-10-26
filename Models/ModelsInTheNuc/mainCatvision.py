from threading import Thread
from CatVisionDetectron import *
from ModeloJoe.modeloJoe import *
import uuid
import cv2
import requests
import json
import time

url = "http://IP:PORT/nuc/sendData"

if __name__ == "__main__":
    #time.sleep(1800)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) 

    while(True):
        ret,frame = cap.read() 
        cv2.imshow("Result", frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            imageName = 'images/'+str(uuid.uuid4())+'.jpg'
            cv2.imwrite(imageName,frame)
            cv2.destroyAllWindows()
            break

    cap.release()

    predictionDetectron2(imageName)
    jason = prediction()
    yayhijomuerde = bytes(json.dumps(jason), "utf-8")
    print(jason)
    print(yayhijomuerde)

    res = requests.post(url, yayhijomuerde)
    print(res.text)
