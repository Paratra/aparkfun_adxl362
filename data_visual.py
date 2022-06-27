import pandas as pd
import numpy as np
from pdb import set_trace as st
import matplotlib.pyplot as plt

def main():
    ## load data
    data_pd = pd.read_csv('data_test.csv')

    ## visulize
    # plt.figure()
    data_pd.plot(kind='line',y=['x'])
    data_pd.plot(kind='line',y=['y'])
    data_pd.plot(kind='line',y=['z'])
    data_pd.plot(kind='line',y=['x_velo'])
    data_pd.plot(kind='line',y=['y_velo'])
    data_pd.plot(kind='line',y=['z_velo'])
    # data_pd.plot(kind='line',y='y',color='green')
    # data_pd.plot(kind='line',y='z',color='blue')

    plt.show()


if __name__ == "__main__":
    main()