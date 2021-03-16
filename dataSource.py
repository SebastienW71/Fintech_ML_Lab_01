import yfinance as yf
import numpy as np
import pandas as pd
import datetime

## this data source is to provide basic daily data from yahoo finance

class data_source:
    def __init__(self, _ticker):
        self.ticker = yf.Ticker(_ticker)

    def get_Dailydata(self, _startdate, _enddate):
        basic_data = self.ticker.history(start=_startdate, end=_enddate)
        data = {
            'open': round(basic_data['Open'], 2),
            'high': round(basic_data['High'], 2),
            'low': round(basic_data['Low'], 2),
            'close': round(basic_data['Close'], 2),
            'volume': round(basic_data['Volume'], 2)
        }
        df = pd.DataFrame(data)
        df = df.reset_index()
        df = df.rename(columns={'Date': 'date'})
        df['date'] = df['date'].astype(str)
        # df = df.iloc[1:].reset_index(drop = True)
        return df

