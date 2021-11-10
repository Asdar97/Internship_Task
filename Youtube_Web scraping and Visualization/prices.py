import Sells2
import pandas as pd
import pandas_datareader as dr
from datetime import datetime,date,timedelta
startTime = datetime.now()

Sells2.getSells()
df = pd.read_csv('Trading.csv', index_col = 0)

infoDict = {}
numperiods = 180

def getinfo(ticker,n = 180):
    try:
        tickerdf = dr.data.get_data_yahoo(ticker, start = date.today()- timedelta(300) , end = date.today())
        currentprice = tickerdf.iloc[-1]["Close"]
        MA = pd.Series(tickerdf["Close"].rolling(n,min_periods=0).mean(),name = 'MA')
        currentma = MA[-1]
        return (currentprice,currentma)
    except:
        return ('na','na')

def getPrice(row):
    ticker= row['Symbol']
    if ticker not in infoDict.keys():
        tickerinfo = getinfo(ticker,numperiods)
        infoDict[ticker] = {}
        infoDict[ticker]["price"] = tickerinfo[0]
        infoDict[ticker]["ma"] = tickerinfo[1]
        return infoDict[ticker]["price"]
    else:
        return infoDict[ticker]["price"]

def getMovingAverage(row):
    ticker = row['Symbol']
    return infoDict[ticker]["ma"]


df['currentprice'] = df.apply (lambda row: getPrice(row),axis = 1)
df['movingaverage'] = df.apply (lambda row:getMovingAverage(row),axis = 1)
df.to_csv('TradingPrices.csv')
print(f'Prices Gathered - Execution Time: {datetime.now() - startTime}')