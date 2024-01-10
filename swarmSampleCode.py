from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.187",
    "192.168.0.188"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
swarm.move_up(100)

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

# making each tello do something unique in parallel
swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))

# customMovement to draw a heart
def customMovement(i, tello):
    if i == 0:
        if tello.get_height() < 180:
            tello.move_up(180 - tello.get_height())
        tello.curve_xyz_speed(0, -53, 40, 0, -106, 0, 20)
        tello.go_xyz_speed(0, 106, -90, 20)  # 假设 move_right 是一个移动无人机向右的方法
        # for i in range(5):
        #     tello.move_up(40)
        #     tello.move_down(40)
    elif i == 1:
        if tello.get_height() < 180:
            tello.move_up(180 - tello.get_height())
        tello.curve_xyz_speed(0, 53, 40, 0, 106, 0, 20)
        tello.go_xyz_speed(0, -106, -90, 20)   # 假设 move_left 是一个移动无人机向左的方法
        # for i in range(5):
        #     tello.move_down(40)
        #     tello.move_up(40)

# function to check which tello is the No.1
def checkNum(i, tello):
    if i == 0:
        tello.move_up(40)
        tello.move_down(40)

# control the drone by keyboard
while True:
    command = input("Enter command: ")
    if command == "u":
        swarm.move_up(40)
    elif command == "c":
        swarm.parallel(checkNum)
    elif command == "l":
        swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))
    elif command == "p":
        swarm.parallel(customMovement)
    else:
        swarm.land()
        break
        
swarm.end()
