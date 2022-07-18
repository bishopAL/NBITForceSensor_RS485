from PortHandle import PortHandle
import time
import pandas as pd
import datetime

recordData = pd.DataFrame(columns=['T', 'F_x', 'F_y', 'F_z', 'T_x', 'T_y', 'T_z'])
ph = PortHandle('/dev/ttyUSB0', 115200)
ph.setZero()
time.sleep(0.05)
startTime = time.time()
presentTime = 0
iteration = 0
while(presentTime<=60):
    ph.getForce()
    presentTime = time.time() - startTime
    recordData.loc[iteration] = [presentTime] + ph.force
    iteration += 1
    print(presentTime, ph.force)

current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
recordData.to_csv('current_date'+'.csv', index=None)