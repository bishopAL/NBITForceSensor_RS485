from PortHandle import PortHandle
import time

ph = PortHandle('/dev/ttyUSB0', 115200)
ph.setZero()
time.sleep(0.05)
for i in range(500):
    ph.getForce()
    print(ph.force)
    time.sleep(0.01)