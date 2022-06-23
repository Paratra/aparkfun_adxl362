import ADXL362
import time
from pdb import set_trace as st
# from datetime import datetime
import pandas as pd

accel = ADXL362.ADXL362(device=0, ce_pin=0)
accel.begin_measure()
x_list = []
y_list = []
z_list = []

t_start = time.time()

while True:
    if time.time() - t_start >10:
        break

    x_list.append(accel.read_x())
    y_list.append(accel.read_y())
    z_list.append(accel.read_z())

    # print('-----------------------')
    # print (accel.read_x())
    # print (accel.read_y())
    # print (accel.read_z())
    # print (accel.read_temp())
    # print (accel.read_xyz())
    time.sleep(0.1)
data_pd = pd.DataFrame(np.array([x_list, y_list, z_list]).T, columns=['x','y','z'])
data_pd.to_csv('./data_test.csv')
print('Save Done!')
# st()
