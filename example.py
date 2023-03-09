
from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/tty.usbserial-14420")

try:
    servo1 = LX16A(3)
    servo2 = LX16A(4)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo1.move(sin(t) * 10 + 120)
    servo2.move(cos(t) * 10 + 120)

    time.sleep(0.05)
    t += 0.1