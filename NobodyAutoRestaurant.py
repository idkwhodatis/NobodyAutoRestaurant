import time
import keyboard
import numpy
import pyautogui
import cv2

def autoRun():
    target=cv2.imread("target.png",cv2.IMREAD_GRAYSCALE)
    tw,th=target.shape[::-1]
    while True:
        img=pyautogui.screenshot()
        img=numpy.array(img)
        img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        result=cv2.matchTemplate(img,target,cv2.TM_CCOEFF_NORMED)
        location=numpy.where(result>=0.95)
        for pos in zip(*location[::-1]):
            pyautogui.moveTo(pos[0],pos[1],duration=0.1)
            pyautogui.click()
        time.sleep(0.25)

autoRun()