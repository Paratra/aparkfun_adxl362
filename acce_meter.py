import ADXL362_ming
import time
from pdb import set_trace as st
# from datetime import datetime
import pandas as pd
import numpy as np


COLLECT_TIME = 15


accel = ADXL362_ming.ADXL362(device=0, ce_pin=0)
accel.begin_measure()
x_list = []
y_list = []
z_list = []

t_start = time.time()

while True:
    # if (time.time() - t_start) % 1 == 0:
    #     print(f'Collecting Time: {(time.time() - t_start)}')
    
    if time.time() - t_start > COLLECT_TIME:
        break

    x_list.append(accel.read_x()/1000)
    y_list.append(accel.read_y()/1000)
    z_list.append(accel.read_z()/1000)

    # print('-----------------------')
    # print (accel.read_x())
    # print (accel.read_y())
    # print (accel.read_z())
    # print (accel.read_temp())
    # print (accel.read_xyz())
    time.sleep(0.1)

x_arr = np.array(x_list) - np.mean(x_list)
y_arr = np.array(y_list) - np.mean(y_list)
z_arr = np.array(z_list) - np.mean(z_list)

# data_pd = pd.DataFrame(np.array([x_arr, y_arr, z_arr]).T, columns=['x','y','z'])
data_pd = pd.DataFrame(np.array([x_arr]).T, columns=['x'])

data_pd.to_csv('./data_test.csv')
print('Save Done!')
# st()
