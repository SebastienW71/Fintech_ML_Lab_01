import yfinance as yf
import numpy as np
import pandas as pd
import datetime
from dataSource import data_source
from trade_Robot import trade_Robot
from wallet import wallet
from backtest import backtest
from strategy_01 import strategy_01

st = strategy_01()
m = backtest("TSLA", 1000000, st, '2021-03-01', datetime.date.today())
m.execute()