# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 21:18:29 2017

@author: alex
"""
import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey
#import pyautogui

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)
print('down')
pyautogui.keyDown('w')
time.sleep(3)
print('up')
pyautogui.keyUp('w')

#def process_img(original_image):
#    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
#    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
#    return processed_img
#
#last_time = time.time()
#while(True):
#    screen = np.array(ImageGrab.grab(bbox=(0,40,1024,800)))
#    new_screen = process_img(screen)
#    
#    print("Loop took {} seconds".format(time.time()-last_time))
#    last_time = time.time()
#    cv2.imshow('win',new_screen)
#   # cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#        cv2.destroyAllWindows()
#        break

#