import yfinance as yf
import numpy as np
import pandas as pd
import datetime
from dataSource import data_source
from trade_Robot import trade_Robot
from wallet import wallet

class backtest:
    '''
    backtest kernel only got basic stock data (data, price) to execute trade and get simulated gain
    strategy get the date info
    trade get the action from strategy, get the current holding stat from wallet
    wallet get the update holding stat from the trade
    For now, the back test use daily close price as the final trading price
    '''

    def __init__(self, _ticker, _initialCapital, _strategy, _startDate, _endDate):
        self.ticker = _ticker
        self.ds = data_source(_ticker)
        self.strategy = _strategy
        self.initialCapital = _initialCapital
        self.startDate = _startDate
        self.startIndex = 0
        self.endIndex = 0
        self.wallet = wallet(_ticker, self.initialCapital, _startDate)
        self.wallet.initialization()  # initialize wallet at the beginning
        self.hist = self.ds.get_Dailydata(_startDate, _endDate)  # get all historical basic data
        self.trade = trade_Robot(_ticker)

    def execute(self):
        # loop: read operations from strategy, execute trade, update wallet and go to next trading day
        self.initializeKernel()
        print('Back test Start, initial wallet stat:')
        print(self.wallet.current_stat())
        print('-------------------------------------------')

        while True:
            isEnd, data = self.getABatch()
            if isEnd == True:
                print('Last Day Reached, End')
                break
            else:
                print('-----------------' + data['date'] + '-----------------')
                # transfer current wallet stat, current date to strategy,
                currWallet = self.wallet.current_stat()
                # get operation from strategy
                action, volume = self.strategy.get_Option(data['date'], currWallet)
                print('action is: ', action)
                print('volume is: ', volume)
                #print(action)
                # trade robot execute the trade action, return
                # use today's close price as the trade price
                self.trade.get_Currentwallet(data['close'],
                                             currWallet['remainCapital'][self.currentIndex],
                                             currWallet['currentPosition'][self.currentIndex])
                if action == 'buy':
                    # trade_Robot will print the error message if the trade is failed
                    newCapital, newPosition, p, t, action = self.trade.buy(volume)
                    if action == 'fail':
                        break

                elif action == 'sell':
                    newCapital, newPosition, p, t, action = self.trade.sell(volume)
                    if action == 'fail':
                        break
                else:
                    print('lazy, no action today')
                    newCapital, newPosition, p, t, action = self.trade.no_Action()
                # update wallet

                self.wallet.update_Wallet(data['date'], newCapital, newPosition, p)
                print('wallet_updated')
                print(self.wallet.current_stat())

                # update index, and go to next day

                self.seeU_Tomorrow()

        return

    def initializeKernel(self):
        # restart
        self.currentDate = self.startDate
        self.currentIndex = self.startIndex
        self.endIndex = self.startIndex + len(self.hist)  # endIndex is 1 bigger than the last index
        self.remainHistdata = self.hist
        self.wallet.initialization()
        return

    def getABatch(self):
        # same to getABatch (in old version)
        if self.currentIndex < self.endIndex:
            dataBatch = self.hist.loc[self.currentIndex][:]
            isEnd = False
            return isEnd, dataBatch
        else:
            isEnd = True
            return isEnd, []

    def seeU_Tomorrow(self):
        self.currentIndex += 1
        return

    def legal_Check(self):
        return

