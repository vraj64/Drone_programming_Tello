#import dependencies:
from djitellopy import Tello
from time import sleep

#calling the Tello function:
tello = Tello()

#connecting the drone with the computer:
tello.connect()

#battery status of the drone will be printed in the terminal:
print(tello.get_battery())

# Basic tello operations:

#Takeoff the drone:
tello.takeoff()
sleep(2) # sleep commands are used to stay in that position, 
         #before executing the next command

#Basic maneuvures of the drone
tello.move_left(100)
sleep(2)

tello.rotate_counter_clockwise(90)
sleep(2)

tello.move_forward(100)
sleep(2)


# land the drone:
tello.land()