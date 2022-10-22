import pandas as pd
import talib
import matplotlib.pyplot as plt

# read btc price in 5 min timeframe 
df= pd.read_csv('BTCUSDT.csv')
# slice first n item of prices becuse file is so big and we need some of that for our tests
df = df.head(45)

# calculate sma
sma20 = talib.SMA(df['close'].values, 20)
# calculate macd 
macd,macdsignal,df['macdhist'] = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
# filter all things with macdhistorical bigger than 2
df_signal = df.loc[df['macdhist'] > 2]
# plot
plt.plot(df['time'], df['close'], label = 'price',color = 'red')
plt.plot(df['time'],sma20,label = 'sma', color = 'blue',linewidth = 0.5)
plt.scatter(df_signal['time'],df_signal['close'],label = 'signal', s=12)
plt.title('BTC chart and signal')

plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation = 45, ha='right')

plt.show()
