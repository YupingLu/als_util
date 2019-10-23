#!/usr/bin/env python
# coding: utf-8
'''
scripts to viz input variables
Copyright (c) Yuping Lu <yupinglu89@gmail.com>, 2019
Last Update: 10/23/2019
'''

# load libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# user data
df = pd.read_pickle("EPU_2019.10.18_00.00.raw.pickle.gz")
# ap data
#df = pd.read_pickle("EPU_2019.09.22to23_MLData.pickle.gz")
Time = np.array([x for x in range(len(df))])/36000
xlim_max = int(np.ceil(Time[-1]))

# Beam Current (DCCT)
plt.figure(figsize=(13,4))
plt.title("DCCT")
plt.plot(Time,df.DCCT,'b-')
plt.xticks(np.arange(0,xlim_max+1))
plt.xlim(0, xlim_max+0.5)
plt.grid(True)
plt.xlabel("Time [H]")
plt.show()

# Dispersion Wave Parameter
plt.figure(figsize=(13,4))
plt.title("DWParam1")
plt.plot(Time,df.DWParam1,'b-')
plt.xticks(np.arange(0,xlim_max+1))
plt.xlim(0, xlim_max+0.5)
plt.grid(True)
plt.xlabel("Time [H]")
plt.show()

# Beam Size
plt.figure(figsize=(13,4))
plt.title("Red:XRMSAve, Blue:YRMSAve")
plt.plot(Time, df.XRMSAve, 'r-', linewidth=0.5)
plt.plot(Time, df.YRMSAve, 'b-', linewidth=0.5)
plt.xticks(np.arange(0,xlim_max+1))
plt.xlim(0, xlim_max+0.5)
plt.grid(True)
plt.xlabel("Time [H]")
plt.show()

# Beam Size between 40 and 53
plt.figure(figsize=(13,4))
plt.title("Red:XRMSAve, Blue:YRMSAve")
plt.plot(Time, df.XRMSAve, 'r-', linewidth=0.5)
plt.plot(Time, df.YRMSAve, 'b-', linewidth=0.5)
plt.xticks(np.arange(0,xlim_max+1))
plt.xlim(0, xlim_max+0.5)
plt.ylim(40,53)
plt.grid(True)
plt.xlabel("Time [H]")
plt.show()

# ID Scan - Vertical Gap
plt.figure(figsize=(13,4))
plt.title("ID Scan")

for col in ['SR04U.1.V','SR04U.2.V','SR07U.1.V',
            'SR07U.2.V','SR11U.1.V','SR11U.2.V',
            'SR08U','SR09U','SR10U','SR12U']:
    plt.plot(Time, df[col])

plt.xticks(np.arange(0,xlim_max+1))
plt.xlim(0, xlim_max+0.5)
plt.grid(True)
plt.xlabel("Time [H]")
plt.show()

# ID Scan - Horizontal Shift
plt.figure(figsize=(13,4))
plt.title("ID Scan")

for col in ['SR04U.1.A','SR04U.1.B','SR04U.2.A',
            'SR04U.2.B','SR07U.1.A','SR07U.1.B',
            'SR07U.2.A','SR07U.2.B','SR11U.1.A',
            'SR11U.1.B','SR11U.2.A','SR11U.2.B']:
    plt.plot(Time, df[col])
    
plt.xticks(np.arange(0,xlim_max+1))
plt.xlim(0, xlim_max+0.5)
plt.grid(True)
plt.xlabel("Time [H]")
plt.show()