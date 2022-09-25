import time
import logging
from scripts.wt901c import WT901C_RS232


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

PORT = "/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0"
BAUDRATE = 9600
N_ITER = 100

wt901c = WT901C_RS232(PORT, BAUDRATE)
wt901c.open()

for _ in range(N_ITER):
    start = time.time()
    while not wt901c.update():
        pass
    end = time.time()
    print("elapsed: ", end - start)
    print(wt901c.acceration, wt901c.magnetic, wt901c.angle_rpy, wt901c.angular_velocity)
wt901c.close()