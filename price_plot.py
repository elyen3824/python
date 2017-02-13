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

def plot_dataFrame(df, title, xlabel, ylabel, font_size):
    plt= df.plot(title= title, fontsize= font_size)
    plt.set_xlabel(xlabel)
    plt.set_ylabel(ylabel)
    return plt
    
def save_plot(plot, file_format):
    #legend = plot.legend(loc=0, shadow=True)
    fig= plot.get_figure()
    fig.savefig("fig.svg", format=file_format)
    return plot

def add_data_plot(plot, label, data):
    data.plot(label= label, ax= plot)
    return plot
    
def plot_histogram(df, bins, label):
    #df.hist(bins=bins, label=label)
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(df, bins, normed=1)
    return  ax

def add_vertical_line(plot, data, color, line_style, line_width):
    plot.axvline(data, color=color, linestyle= line_style, linewidth= line_width)

def normalize_data(df):
    return df / df.ix[0,:]
    
def multi_ticks_dataFrame(ticksList, startDate, endDate, column):
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
    return df

def get_mean(df):
    return df.mean()
    
def get_standard_deviation(df):
    return df.std()

def get_median(df):
    return df.median()
    
def get_rolling_mean(df, days):
    return df.rolling(window=days).mean()

def get_rolling_std(df, days):
    return df.rolling(window=days).std()

def get_rolling_median(df, days):
    return df.rolling(window=days).median()
    
def get_bollinger_band(rm, std):
    upper_band= rm+2*std 
    lower_band= rm-2*std
    return upper_band, lower_band

def compute_daily_return(df):
    daily_returns= df.copy()
    daily_returns[1:]=(df[1:]/df[:-1].values)-1
    daily_returns.ix[0,:]=0
    return daily_returns
    
def compute_cumulative_return(df, start, end):
    return (df[start]/df[end].values)-1
    
def test_run():
    df= multi_ticks_dataFrame(['AAPL','MSFT','GOOG'], datetime.strptime("01/01/2016", "%d/%m/%Y"), datetime.strptime("28/01/2017", "%d/%m/%Y"), "Close")
    fill_missing_datas(df)
    df= compute_daily_return(df)
    print(df)
    #df= normalize_data(df)
    #print(df)
    print("mean: "+str(get_mean(df)))
    print("standard deviation: "+str(get_standard_deviation(df)))
    print("median: "+str(get_median(df)))
    plot= plot_histogram(df['AAPL'], 20, "AAPL")
    plot= plot_histogram(df['MSFT'], 20, "MSF T")
    mean= get_mean(df['AAPL'])
    std= get_standard_deviation(df['AAPL'])
    add_vertical_line(plot, mean, 'w', 'dashed', 2)
    add_vertical_line(plot, -std, 'r', 'dashed', 2)
    add_vertical_line(plot, std, 'r', 'dashed', 2)
    #plot= add_data_plot(plot,"Rolling Mean", get_rolling_mean(df['AAPL'],20))
    #upper, lower=get_bollinger_band(get_rolling_mean(df['AAPL'],20), get_rolling_std(df['AAPL'],20))
    #plot= add_data_plot(plot,"Upper Band", upper)
    #plot= add_data_plot(plot,"Lower Band", lower)
    save_plot(plot, "svg")
    
test_run()