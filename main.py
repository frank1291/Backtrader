import backtrader as bt

class TestStrategy(bt.Strategy):


    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.strftime("%d %H:%M"), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])

if __name__ == '__main__':

    cerebro = bt.Cerebro()

    cerebro.addstrategy(TestStrategy)



    #  https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_minute.csv

    data = bt.feeds.GenericCSVData(
        dataname='Binance_BTCUSDT_minute.csv',
        timeframe=bt.TimeFrame.Minutes,
        nullvalue=0.0,

        datetime=1,
        high=4,
        low=5,
        open=3,
        close=6,
        volume=7,
        openinterest=-1,

        dtformat= '%Y-%m-%d %H:%M:%S'
    )

    cerebro.adddata(data)

    cerebro.run()

