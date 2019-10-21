#!/usr/bin/env python
# coding: utf-8
'''
script to get the baseline of YRMSAve and XRMSAve
Copyright (c) Yuping Lu <yupinglu89@gmail.com>, 2019
Last Update: 10/21/2019
'''

# load libs
import numpy as np
import pandas as pd

# function to get YMRSAve
def getYRMS(fs):
    data = []
    # load files
    for f in fs:
        tmp_df = pd.read_pickle(f)
        data.append(tmp_df)
    
    df = pd.concat(data, ignore_index=True, sort =False)

    # filter data by date
    df = df.astype({'Sec': 'int64'})
    df.rename(index=str, columns={'Min':'Minute'}, inplace=True)
    df.rename(index=str, columns={'Sec':'Second'}, inplace=True)
    df['Year'] = pd.Series(2019, index=df.index)
    df = df.set_index(pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']]))
    df = df.loc['2019-10-16 08:00:00' : '2019-10-18 08:00:00']
    
    df = df[['XRMSAve','YRMSAve']]
    
    # remove extreme values
    df = df[(df.XRMSAve < 53) & (df.XRMSAve > 40)]
    df = df[(df.YRMSAve < 53) & (df.YRMSAve > 40)]
    
    data = df.to_numpy()

    print('XRMSAve MIN: %.2f, MAX: %.2f' % (data[:,0].min(), data[:,0].max()))
    print('XRMSAve STD: %.4f' % (data[:,0].std()))
    print('YRMSAve MIN: %.2f, MAX: %.2f' % (data[:,1].min(), data[:,1].max()))
    print('YRMSAve STD: %.4f' % (data[:,1].std()))
    

# function to get YMRSAve with downsample
def getYRMS1(fs):
    data = []
    # load files
    for f in fs:
        tmp_df = pd.read_pickle(f)
        data.append(tmp_df)
    
    df = pd.concat(data, ignore_index=True, sort =False)

    # filter data by date
    df = df.astype({'Sec': 'int64'})
    df.rename(index=str, columns={'Min':'Minute'}, inplace=True)
    df.rename(index=str, columns={'Sec':'Second'}, inplace=True)
    df['Year'] = pd.Series(2019, index=df.index)
    df = df.set_index(pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']]))
    df = df.loc['2019-10-16 08:00:00' : '2019-10-18 08:00:00']
    
    df = df[['XRMSAve','YRMSAve']]
    
    # downsample
    idx = list(range(0, len(df), 10))
    df = df.iloc[idx,:]
    
    # remove extreme values
    df = df[(df.XRMSAve < 53) & (df.XRMSAve > 40)]
    df = df[(df.YRMSAve < 53) & (df.YRMSAve > 40)]
    
    data = df.to_numpy()

    print('XRMSAve MIN: %.2f, MAX: %.2f' % (data[:,0].min(), data[:,0].max()))
    print('XRMSAve STD: %.4f' % (data[:,0].std()))
    print('YRMSAve MIN: %.2f, MAX: %.2f' % (data[:,1].min(), data[:,1].max()))
    print('YRMSAve STD: %.4f' % (data[:,1].std()))


files = ["EPU_2019.10.16_00.00.raw.pickle.gz", "EPU_2019.10.17_00.00.raw.pickle.gz", \
         "EPU_2019.10.18_00.00.raw.pickle.gz"]
d1 = getYRMS(files)
d2 = getYRMS1([files)