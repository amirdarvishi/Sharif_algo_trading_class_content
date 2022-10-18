from turtle import color
import pandas as pd
import numpy as np 
import talib
import matplotlib.pyplot as plt

df = pd.read_csv('BTCUSDT.csv')
df = df.head(300)
df = df.drop(axis =1,columns=['low','high','open','exchange'])
df['sma10'] = talib.SMA(df['close'], 10)
df['sma15'] = talib.SMA(df['close'], 15)
df['signals'] = 0
df['signals'] = np.where(df['sma10'] > df['sma15'], 1, 0)
df['position'] = df['signals'].diff()

plt.plot(df['close'],label = 'close price',linewidth = 0.9)
plt.plot(df['sma10'],label = 'sma10',linewidth = 0.7,color = 'g')
plt.plot(df['sma15'],label = 'sma15',linewidth = 0.7,color = 'r')

plt.plot(df[df['position'] == 1].index,df['sma10'][df['position'] == 1],'^',markersize = 6,color='g',label='buy')
plt.plot(df[df['position'] == -1].index,df['sma10'][df['position'] == -1],'v',markersize = 6,color='r',label='sell')
plt.show()