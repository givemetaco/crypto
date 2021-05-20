import matplotlib
from matplotlib import markers
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import Coin as c
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc

bitcoin = c.Coin('BTC-USD')

"""
fig = plt.figure(figsize=(8, 5))
fig.set_facecolor('w')
gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
axes = []
axes.append(plt.subplot(gs[0]))
axes.append(plt.subplot(gs[1], sharex=axes[0]))
axes[0].get_xaxis().set_visible(False)


x = np.arange(len(bitcoin.data.index))
ohlc = bitcoin.data[['Open', 'High', 'Low', 'Close']].astype(int).values
dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))

# 봉차트
candlestick_ohlc(axes[0], dohlc, width=0.5, colorup='r', colordown='b')

# 거래량 차트
axes[1].bar(x, bitcoin.data.Volume, color='k', width=0.6, align='center')

line_axes=fig.add_axes(bitcoin.data.index,bitcoin.data['Close'])

plt.tight_layout()
"""
# line_fig,line_axes=plt.subplots()
# line_axes.plot(bitcoin.data.index,bitcoin.data['Close'])
fig, axes = plt.subplots(figsize=(9, 4))
axes.plot(bitcoin.get_day_data().index, bitcoin.get_day_data()['Close'])
axes.set(xlabel="Date", ylabel="Price($)", title="BitCoin")
axes.grid()
# axes.text(bitcoin.data.index[3],bitcoin.data['Close'][3],bitcoin.data['Close'][3])
#plt.show()

class graph:
    def __init__(self,coin) -> None:
        self.coin=coin
    
    def line_graph(self,period)->tuple:
        if period=='1d':
            self.fig, self.axes = plt.subplots(figsize=(9, 4))
            self.axes.plot(self.coin.get_day_data().index, self.coin.get_day_data()['Close'])
            self.axes.set(xlabel="Date", ylabel="Price($)", title="BitCoin")
            self.axes.grid()
            return (self.fig,self.axes)