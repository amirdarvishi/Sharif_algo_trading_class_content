import pandas as pd 
# import yfinance as yf
# import matplotlib.pyplot as plt
import investpy


# https://python.plainenglish.io/how-to-download-trading-data-from-binance-with-python-21634af30195
# library introduced by Mr Montakhab for recieving data of market
# read data of crypto and fill in Pandas dataframe
df = investpy.get_crypto_historical_data(crypto='bitcoin' , from_date='01/01/2010' ,to_date='01/01/2022')
print(df)


# read from csv
df = pd.read_csv('BTCUSDT.csv')
df = pd.read_excel('BTCUSDT.xlsx')
print(df)
print(df.head(15))
print(df.tail(15))

print(df['low'].head(5))

print(df.columns)

# read each column
df2 = df[['time', 'high']]
print(df2)

# read each row
print(df.iloc[2:12])

for index, rows in df.iterrows():
    print(rows['high'])

# # download data from yahoo introducd by mr Montakhab
df = yf.download('BTC-USD',  start='2021-05-01', actions='inline',auto_adjust=True)
df['Close'].plot(label='BTC')
plt.show()


# filtering rows
print(df.loc[df['high'] > 45000])

# specific location or cell 
print(df.iloc[3,3])


# # sort data
df1 = df.sort_values(['high'], ascending= 1)
df1.reset_index(drop=True, inplace = True)
print(df1.head(5))

# statistics of dataframe
print(df.describe())

df['average_price'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
df['mean_price'] = df.iloc[:, 4:8].mean(axis=1)
df = df.drop(columns=['average_price'])
print(df.head(5))


cols = list(df.columns)
df = df[cols[0:2] + [cols[-1]] + cols[5:7]]
print(df.head(5))

# export 
df.to_csv('modified_btc.csv')

# filtering with and 
print(df.loc[(df['high'] > 45000 ) & ((df['high'] - df['low']) > 1000)])

print( df.loc[~df['exchange'].str.contains('oke')])

# change data in dataframe
df.loc[df['time'] == '2022-08-15T09:05:00', 'exchange'] = 'kucoin'
print( df.loc[df['exchange'].str.contains('kuc')])

# group by
print(df.groupby(['exchange']).max().sort_values('exchange'))