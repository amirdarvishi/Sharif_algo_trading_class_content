import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# read from csv
df = pd.read_csv('BTCUSDT.csv')
print('reading csv complted')
df1= df.head(20)


  
plt.figure()
  
# "up" dataframe will store the df1 
# when the closing stock price is greater
# than or equal to the opening stock prices
up = df1[df1.close >= df1.open]
  
# "down" dataframe will store the df1
# when the closing stock price is
# lesser than the opening stock prices
down = df1[df1.close < df1.open]
  
# When the stock prices have decreased, then it
# will be represented by blue color candlestick
col1 = 'green'
  
# When the stock prices have increased, then it 
# will be represented by green color candlestick
col2 = 'red'
  
# Setting width of candlestick elements
width = .3
width2 = .03
  
# Plotting up prices of the stock
plt.bar(up.time, up.close-up.open, width, bottom=up.open, color=col1)
plt.bar(up.time, up.high-up.close, width2, bottom=up.close, color=col1)
plt.bar(up.time, up.low-up.open, width2, bottom=up.open, color=col1)
  
# Plotting down prices of the stock
plt.bar(down.time, down.close-down.open, width, bottom=down.open, color=col2)
plt.bar(down.time, down.high-down.open, width2, bottom=down.open, color=col2)
plt.bar(down.time, down.low-down.close, width2, bottom=down.close, color=col2)
  
# rotating the x-axis tick labels at 30degree 
# towards right
plt.xticks(rotation=45, ha='right')
  
# displaying candlestick chart of stock data 
# of a week
plt.show()