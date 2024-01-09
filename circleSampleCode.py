from djitellopy import Tello
import time
import math
import cv2

tello = Tello()
tello.connect()

print(tello.get_battery())
tello.takeoff()

while True:
    # duration is calculated by the time it takes for the drone to complete a circle.
    # which is related to the rotation degree(yaw velocity).
    # duration = 360 / rotation degree.
    # Rotation degree is related to yaw velocity and is recorded in the resource.md file.
    duration = 14.5
    command = input("Enter command: ")
    if command == "u":
        tello.move_up(40)
    elif command == "c":
        # The drone will fly in a circle with its camera facing the direction of flight.
        # lr = 0, fb = 25, ud = 0, yaw = 40
        # fb will determine the radius of the circle.
        # fb = (2 * pi * r) / duration
        tello.send_rc_control(0, 25, 0, 40)
        # time.sleep(duration) is used here to make sure the drone will complete the full circle(360 degree).
        time.sleep(duration)
        # tello.send_rc_control(0, 0, 0, 0) is used here to make sure the drone will stop after completing the circle.
        tello.send_rc_control(0, 0, 0, 0)
    elif command == "i":
        # The drone will fly in a circle with its camera facing towards the center of the circle (point of interest)
        # lr = -35, fb = 0, ud = 0, yaw = 40
        # lr will determine the radius of the circle.
        # lr = (2 * pi * r) / duration
        tello.send_rc_control(-35, 0, 0, 40)
        # time.sleep(duration) is used here to make sure the drone will complete the full circle(360 degree).
        time.sleep(duration)
        # tello.send_rc_control(0, 0, 0, 0) is used here to make sure the drone will stop after completing the circle.
        tello.send_rc_control(0, 0, 0, 0)
    else:
        tello.send_rc_control(0, 0, 0, 0)
        tello.land()
        tello.end()
        