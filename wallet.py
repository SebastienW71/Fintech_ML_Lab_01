import yfinance as yf
import numpy as np
import pandas as pd
import datetime

class wallet:
    '''
    store the data of current bought tickers,
    current capital, current hoding position, current share value, historical data
    for now, the wallet only allow single ticker
    '''

    def __init__(self, _ticker, _initialCapital, _startdate):
        self.initialCapital = _initialCapital
        self.startdate = datetime.datetime.strptime(_startdate, '%Y-%m-%d')
        self.startIndex = 0
        self.currentIndex = self.startIndex
        self.ticker = _ticker
        self.shares_Data = pd.DataFrame([],
                                        columns=['date',
                                                 'ticker',
                                                 'remainCapital',
                                                 'currentPosition',
                                                 'currentShareprice',
                                                 'currentSharesValue',
                                                 'currentTotalCapital'
                                                 ])

    def initialization(self):
        # set yesterday of the startday as the initial date
        self.shares_Data = pd.DataFrame({
            'date': [(self.startdate - datetime.timedelta(days=1))],  # format: datetime
            'ticker': [self.ticker],
            'remainCapital': [self.initialCapital],
            'currentPosition': [0],
            'currentShareprice': [0],
            'currentSharesValue': [0],
            'currentTotalCapital': [self.initialCapital]
        })
        self.currentIndex = self.startIndex
        return

    def update_Wallet(self, currentDate, updatedCapital, updatedPosition, currentPrice):
        self.currentIndex += 1
        currentDate = datetime.datetime.strptime(currentDate, '%Y-%m-%d')
        self.shares_Data.loc[self.currentIndex] = [
            currentDate,
            self.ticker,
            updatedCapital,
            updatedPosition,
            currentPrice,
            updatedPosition * currentPrice,
            updatedCapital + updatedPosition * currentPrice
        ]
        return

    def current_stat(self):
        # get current wallet stat
        data = self.shares_Data.loc[self.currentIndex][:]
        data = pd.DataFrame(data)
        data = data.transpose()
        return data

    def historical_stat(self):
        data = self.shares_Data
        return data

