import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd 
import time as datetime
from datetime import datetime

base_url= "http://www.google.com/finance/historical"
dateFormat= "%m-%d-%y"

def get_data(symbol, startdate, enddate, column):
    df= pd.read_csv(get_url(symbol, startdate, enddate), parse_dates=True, index_col="Date", usecols=["Date", column], na_values=["nan"])
    print(df)
    return df

def get_url(symbol, startdate, enddate):
    dstart= startdate.strftime(dateFormat)
    estart= enddate.strftime(dateFormat)
    url= base_url+"?q="+symbol+"&startdate="+dstart+"&enddate="+estart+"&output=csv"
    print(url)
    return url

def plotDataFrame(df):
    pl= df.plot()
    fig= pl.get_figure()
    fig.savefig("fig.svg", format="svg")

def normalize_data(df):
    return df / df.ix[0,:]
    
def multiTicksDataFrame(ticksList, startDate, endDate, column):
    dates= pd.date_range(startDate, endDate)
    df= pd.DataFrame(index=dates)
    for tick in ticksList:
        tempDf= get_data(tick, startDate, endDate, column).rename(columns={column:tick})
        tempDf= tempDf.dropna(subset=[tick])
        df= df.join(tempDf, rsuffix="_"+tick)
    df.dropna(axis=0, how='any', thresh=None, subset=ticksList, inplace=True)
    return df

def fill_missing_datas(df):
    df.fillna(method='ffill', inplace='TRUE')
    df.fillna(method='ffill', inplace='TRUE')

def mean(df):
    return df.mean()
    
def standardDeviation(df):
    return df.std()

def median(df):
    return df.median()
    
def rolling_mean(df, days):
    return df.rolling(window=days).mean()

def rolling_std(df, days):
    return df.rolling(window=days).std()

def rolling_median(df, days):
    return df.rolling(window=days).median()

###
def test_run():
    df= multiTicksDataFrame(['AAPL','MSFT','GOOG'], datetime.strptime("01/01/2017", "%d/%m/%Y"), datetime.strptime("24/01/2017", "%d/%m/%Y"), "Close")
    df= normalize_data(df)
    fill_missing_datas(df)
    print("mean: "+str(mean(df)))
    print("standard deviation: "+str(standardDeviation(df)))
    print("median: "+str(median(df)))
    plotDataFrame(df)
    
test_run()