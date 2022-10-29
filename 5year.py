import pytse_client as tse
import pandas as pd

# for in all symbols
# for every symbol filter date > 2017-09-01
# append to new df close of firt day and last day
main = pd.DataFrame(columns=['symbol','first','last'])
for symbol in tse.all_symbols():
    try:
        ticker = tse.Ticker(symbol+'-ت').history
        df = ticker.loc[ticker['date'] > '2017-09-01']
        # main = main.append({'symbol':symbol, 'first': df.iloc[0,4],'last': df.iloc[-1,4]},ignore_index=True)
        main = main.concat([pd.DataFrame({'symbol':symbol, 'first': df.iloc[0,4],'last': df.iloc[-1,4]}),main],ignore_index=True)
    except:
        continue

# multiply = lastclose/first close
main['multiply'] = main['last']/main['first']
main = main.sort_values('multiply',ascending=False)
print(main)
main.to_csv('5year.csv',encoding='UTF-8')

