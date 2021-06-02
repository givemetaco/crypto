import matplotlib
from matplotlib import markers
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import Coin as c
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc
import matplotlib.animation as animation
import time


# bitcoin = c.Coin('BTC')

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
# fig, axes = plt.subplots(figsize=(9, 4))
# axes.plot(bitcoin.get_day_data().index, bitcoin.get_day_data()['Close'])
# axes.set(xlabel="Date", ylabel="Price($)", title="BitCoin")


class graph:
    def __init__(self, coin, parent, navigation_frame) -> None:
        self.coin = coin
        self.current_period='d'
        self.parent = parent
        self.navigation_frame = navigation_frame
        self.fig, self.axes = plt.subplots(figsize=(9, 4))
        self.axes.plot(self.coin.get_day_data().index,
                       coin.get_day_data()['Close'], color="blue")
        self.axes.set(xlabel="Date", ylabel="Price($)", title=coin.tickers)
        # self.fig.tight_layout()
        plt.subplots_adjust(left=0.088, right=0.97, top=0.94, bottom=0.083)
        self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.navigation_frame)
        self.toolbar.update()

    def start_ani(self):
        ani = animation.FuncAnimation(
            self.fig, self.change_period, interval=10000)

    def update_period(self):  # 매게변수로 d,w,y 중 하나를 받는다.
        self.axes.clear()
        if self.current_period == 'd':
            self.axes.plot(self.coin.get_day_data().index,
                           self.coin.get_day_data()['Close'], color="blue")
        elif self.current_period == 'w':
            self.axes.plot(self.coin.get_weekly_data().index,
                           self.coin.get_weekly_data()['Close'], color="blue")
        elif self.current_period == 'y':
            self.axes.plot(self.coin.get_monthly_data().index,
                           self.coin.get_monthly_data()['Close'], color="blue")
        
        self.axes.set(xlabel="Date", ylabel="Price($)",
                      title=self.coin.tickers)
        
        self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)