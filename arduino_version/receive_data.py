import time
import serial
from pdb import set_trace as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft

def velo_calc(x,delta_t):
  v0 = 0
  vel_list = []
  for ind, each_x in enumerate(x):
      v = v0+each_x*delta_t
      vel_list.append(v)
      v0 = v

  return np.array(vel_list)


def get_fft(data_arr, delta_T):
  N = len(data_arr)
  T = delta_T
  xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
  yf = fft.fft(data_arr)

  return xf, yf, N


def main():

  ser = serial.Serial( 
    port='/dev/tty.usbmodem145101',#
    baudrate=9600,# 
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
  )
  every_time = time.strftime('%Y-%m-%d %H:%M:%S')# 
  data = ''

  data_list = []
  x_offset = -0.02
  y_offset = -0.05
  z_offset = 0.18


  ## local G
  G = 979627 / 1000 / 100

  # time.sleep(1)

  t_threshold = 20

  t_start = time.time()
  print('Start')
  while True:
    # print(int(t_start - time.time()))
    if time.time() - t_start  > t_threshold:
      break

    
    
    
    data = ser.readline()
    data_str = data.decode()
    if len(data)<16 or 'Starting' in data_str:
      continue
    
    # print(data)
    data_devide_list = data_str.replace('\r\n','').split(',')

    x_acc = (float(data_devide_list[0]) - x_offset) * G
    y_acc = (float(data_devide_list[1]) - y_offset) * G
    z_acc = -(float(data_devide_list[2]) - z_offset) * G

    data_list.append([x_acc, y_acc, z_acc])

  print('Done')


  # data_pd = pd.DataFrame(data_list, columns=['x','y','z'])
  # data_pd.plot(kind='line',y=['x'])
  # data_pd.plot(kind='line',y=['y'])
  # data_pd.plot(kind='line',y=['z'])

  data_arr = np.array(data_list)
  Fz = np.round(t_threshold/ len(data_arr[:,0]),3)


  # velo_x_arr = velo_calc(data_arr[:,0],delta_t=0.01)
  # velo_y_arr = velo_calc(data_arr[:,1],delta_t=0.01)
  # velo_z_arr = velo_calc(data_arr[:,2],delta_t=0.01)

  # data_arr[:,0] = velo_x_arr
  # data_arr[:,1] = velo_y_arr
  # data_arr[:,2] = velo_z_arr



  x_xf, x_yf, x_N = get_fft(data_arr[:,0], delta_T=Fz)
  y_xf, y_yf, y_N = get_fft(data_arr[:,1], delta_T=Fz)
  z_xf, z_yf, z_N = get_fft(data_arr[:,2], delta_T=Fz)






  ####### plotting
  position = 'Free-Run'

  plt.figure('X-Axis',figsize=(12,6))

  plt.subplot(2,1,1)
  plt.title(f'{position}-X-Axis')

  plt.plot(data_arr[:,0])
  plt.xlabel(f'Time({Fz}s)')
  plt.ylabel('Acceleration(m/s^2)')

  
  plt.subplot(2,1,2)
  plt.plot(x_xf, 2.0/x_N * np.abs(x_yf[0:x_N//2]))
  plt.xlabel('Frequency(Hz)')
  plt.xticks(np.arange(0, 25, step=1))
  plt.grid()

  plt.savefig(f'./{position}_x.png')

  plt.figure('Y-Axis',figsize=(12,6))

  plt.subplot(2,1,1)
  plt.title(f'{position}-Y-Axis')

  plt.plot(data_arr[:,1])
  plt.xlabel(f'Time({Fz}s)')
  plt.ylabel('Acceleration(m/s^2)')

  
  plt.subplot(2,1,2)
  plt.plot(y_xf, 2.0/y_N * np.abs(y_yf[0:y_N//2]))
  plt.xlabel('Frequency(Hz)')
  plt.xticks(np.arange(0, 25, step=1))
  plt.grid()

  plt.savefig(f'./{position}_y.png')


  plt.figure('Z-Axis',figsize=(12,6))
  plt.subplot(2,1,1)
  plt.title(f'{position}-Z-Axis')

  plt.plot(data_arr[:,2])
  plt.xlabel(f'Time({Fz}s)')
  plt.ylabel('Acceleration(m/s^2)')

  
  plt.subplot(2,1,2)
  plt.plot(z_xf, 2.0/z_N * np.abs(z_yf[0:z_N//2]))
  plt.xlabel('Frequency(Hz)')
  plt.xticks(np.arange(0, 25, step=1))
  plt.grid()

  plt.savefig(f'./{position}_z.png')



  plt.show()



if __name__ == '__main__':
  main()