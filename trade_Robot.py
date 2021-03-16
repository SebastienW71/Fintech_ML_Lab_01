import yfinance as yf
import numpy as np
import pandas as pd
import datetime


class trade_Robot:

    '''
    trade_robot: 从wallet获得最新的持仓情况（现有现金，现有股票持仓），
                 从backtest kernel获得当前股价，
                 从策略集合获得当前的操作
     Only to execute buy or sell action, return remain capital, current holding position
     currentPosition 现有的持仓股数
     买卖操作返回的是（持有现金，持仓数目，股票现价，操作名称）
     目前只支持一个股票
    '''


    def __init__(self, _ticker):
        self.ticker = _ticker

    def get_Currentwallet(self, _currentPrice, _currentCapital, _currentPosition):
        # for single stock
        self.currentCapital = _currentCapital
        self.currentPosition = _currentPosition
        self.currentPrice = _currentPrice

    def buy(self, volume):
        if volume % 100 != 0:
            print('volume must be the multiple of 100')
            return 'Trade failed'
        if self.capital_Check('buy', volume):
            self.currentCapital = self.currentCapital - volume * self.currentPrice
            self.currentPosition = self.currentPosition + volume
            return self.currentCapital, self.currentPosition, self.currentPrice, self.ticker, 'buy'
        else:
            print('Trade failed')
            return self.no_Action()

    def sell(self, volume):
        if volume % 100 != 0:
            print('volume must be the multiple of 100')
            errorMes = 'Trade failed'
            return errorMes
        if self.capital_Check('sell', volume):
            self.currentCapital = self.currentCapital + volume * self.currentPrice
            self.currentPosition = self.currentPosition - volume
            return self.currentCapital, self.currentPosition, self.currentPrice, self.ticker, 'sell'
        else:
            print('Trade failed')
            return self.no_Action()

    def no_Action(self):
        return self.currentCapital, self.currentPosition, self.currentPrice, self.ticker, 'no Action'

    def capital_Check(self, action, volume):
        if action == 'buy':
            if self.currentCapital >= volume * self.currentPrice:
                return True
            else:
                print('Insufficient current capital')
                return False
        if action == 'sell':
            if self.currentPosition >= volume:
                return True
            else:
                print('Insufficient holding position')
                return False
