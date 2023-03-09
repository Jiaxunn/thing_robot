from pylx16a.lx16a import *
import time

num_of_motors=8
motor_list=[]
standing_pose=[99.6, 87.12, 11.76, 18.48, 99.36, 79.2, 0, 18.0]

#test
move_1=[96.08, 77.76, 23.04, 50.64, 115.44, 93.84, 39.12, 56.16]
move_2=[96.08, 77.76, 26.16, 9.12, 115.44, 93.84, 39.12, 56.16]
move_3=[96.08, 77.76, 26.16, 9.12, 87.6, 81.6, 39.12, 56.16]
move_4=[96.08, 77.76, 26.16, 9.12, 87.6, 81.6, 47.04, 10.8]
move_5=[96.08, 77.76, 41.52, 28.56, 115.44, 93.84, 39.12, 56.16]

LX16A.initialize("/dev/tty.usbserial-1440")

#creat list of servo objects
for i in range(num_of_motors):
    servo=LX16A(i+1)
    servo.set_angle_limits(0, 180)
    motor_list.append(servo)
motor_list[-1].set_angle_offset(-20)

def get_jointangle(motor_idx):
    packet=[motor_list[motor_idx]._id, 3 , 28]
    while True:
        LX16A._send_packet(packet)
        received = LX16A._controller.read(2 + 6)
        time.sleep(0.005)
        received = list(received[5:-1])
        if len(received)== 2:
            angle = received[0] + received[1] * 256
            break
    return LX16A._from_servo_range(angle - 65536 if angle > 32767 else angle)
def get_voltage(motor_idx):
    packet = [motor_list[motor_idx]._id, 3, 27]

    while True:
        LX16A._send_packet(packet)
        received = LX16A._controller.read(2 + 6)
        time.sleep(0.005)
        received = list(received[5:-1])
        if len(received)== 2:
            vol = received[0] + received[1] * 256
            break
    return vol

def get_pysical_angle():
    angle_list=[]
    for i in range(num_of_motors):
        angle=get_jointangle(i)
        angle_list.append(angle)
    return angle_list

def get_vol_list():
    vol_list=[]
    for i in range(num_of_motors):
        angle=get_voltage(i)
        vol_list.append(angle)
    return vol_list

def move_joints(angle_list,t):
    for i in range(num_of_motors):
        motor_list[i].move(angle_list[i],t)


print("joints angle=",get_pysical_angle())
input("enter to continue ...")
while True:
    move_joints(move_1,350)
    time.sleep(0.5)
    # input("press enter")
    move_joints(move_2,350)
    time.sleep(0.5)
    # input("press enter")
    move_joints(move_3,350)
    time.sleep(0.5)
    # input("press enter")
    move_joints(move_4,350)
    time.sleep(0.5)




