class strategy_01:
    def __init__(self):
        self.target = 1
        # self.x = _param1
        # self.y = 2*_param1/(2*_param1 + 3)
        # self.stopLoss = self.target*(self.x + 1)*(1 - self.y)
        # self.boughtIndex = 1
        # self.ds = []

    def get_Option(self, currentDate, currentWallet):
        ###todayPrice = ds[currentDate]
        # print('param transit success')
        # print('current date:' + currentDate)
        action = 'buy'
        volume = 100
        return action, volume

    def set_Buyline(self):
        return

    def set_Stoploss(self):
        return

st = strategy_01