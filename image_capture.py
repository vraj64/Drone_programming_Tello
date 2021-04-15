#import dependencies:
from djitellopy import Tello
import cv2
from time import sleep

#calling the Tello function:
tello = Tello()

#connecting the drone with the computer:
tello.connect()

#battery status of the drone will be printed in the terminal:
print(tello.get_battery())

#To start the stream from the drone camera:
me.streamon()

# To display the the camera frame in the system: 
while True:
  img = me.get_frame_read().frame
  img = cv2.resize(img, (360, 240))
  cv2.imshow('Drone-frame', img)
  cv2.waitKey(1)
