import cv2
import numpy as np
import time
import HandTrackingModule as ht
import pyautogui   # Install using "pip install pyautogui"

### Variables Declaration
pTime = 0               # Used to calculate frame rate
width = 640             # Width of Camera
height = 600            # Height of Camera
frameR = 100            # Frame Rate
smoothening = 15         # Smoothening Factor
prev_x, prev_y = 0, 0   # Previous coordinates
curr_x, curr_y = 0, 0   # Current coordinates
clicking = False
cap = cv2.VideoCapture(0)   # Getting video feed from the webcam
cap.set(3, width)           # Adjusting size
cap.set(4, height)

detector = ht.handDetector(maxHands=1)                 
screen_width, screen_height = pyautogui.size()      
while True:
    success, img = cap.read()
    img = detector.findHands(img)                       
    lmlist, bbox = detector.findPosition(img)           

    if len(lmlist) != 0:
        x1, y1 = lmlist[4][1:]
        x2, y2 = lmlist[8][1:]
        x3 = np.interp(x1, (frameR, width - frameR), (0, screen_width))
        y3 = np.interp(y1, (frameR, height - frameR), (0, screen_height))

        curr_x = prev_x + (x3 - prev_x) / smoothening
        curr_y = prev_y + (y3 - prev_y) / smoothening
        fingers = detector.fingersUp()    
        cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)   
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:     
            pyautogui.moveTo(screen_width - (2 * curr_x), curr_y)    
            cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
            prev_x, prev_y = curr_x, curr_y
        if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:     
            pyautogui.click(button='right')
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:     
            pyautogui.click(button='left')
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            time.sleep(0.05)
            pyautogui.scroll(1)
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            time.sleep(0.05)
            pyautogui.scroll(-1)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
