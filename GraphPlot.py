import matplotlib
from matplotlib import markers
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc
import matplotlib.animation as animation
import time



class graph:
    def __init__(self, coin, parent, navigation_frame) -> None:
        self.coin = coin
        self.current_period = 'd'
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
        self.current_type = 'line'

    def start_ani(self):
        ani = animation.FuncAnimation(
            self.fig, self.update_period, interval=10000)

    def update_period(self):  # 매게변수로 d,w,y 중 하나를 받는다.
        self.axes.clear()
        if self.current_type == 'line':
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

        elif self.current_type == 'candle':
            self.axes.clear()
            gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
            self.axes = []
            self.axes.append(plt.subplot(gs[0]))
            self.axes.append(plt.subplot(gs[1], sharex=self.axes[0]))
            self.axes[0].get_xaxis().set_visible(False)
            if self.current_period == 'd':
                x = np.arange(len(self.coin.get_day_data().index))
                ohlc = self.coin.get_day_data()[[
                    'Open', 'High', 'Low', 'Close']].astype(int).values
                dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
                self.axes[1].bar(x, self.coin.get_day_data().Volume, color='k',
                                 width=0.6, align='center')
            elif self.current_period == 'w':
                x = np.arange(len(self.coin.get_weekly_data().index))
                ohlc = self.coin.get_weekly_data()[[
                    'Open', 'High', 'Low', 'Close']].astype(int).values
                dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
                self.axes[1].bar(x, self.coin.get_weekly_data().Volume, color='k',
                                 width=0.6, align='center')
            elif self.current_period == 'y':
                x = np.arange(len(self.coin.get_monthly_data().index))
                ohlc = self.coin.get_monthly_data()[[
                    'Open', 'High', 'Low', 'Close']].astype(int).values
                dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
                self.axes[1].bar(x, self.coin.get_monthly_data().Volume, color='k',
                                 width=0.6, align='center')

            candlestick_ohlc(self.axes[0], dohlc,
                             width=0.5, colorup='r', colordown='b')

            self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)

    def candle_chart(self):
        self.current_type = 'candle'
        self.axes.clear()
        self.fig.set_facecolor('w')
        gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        self.axes = []
        self.axes.append(plt.subplot(gs[0]))
        self.axes.append(plt.subplot(gs[1], sharex=self.axes[0]))
        self.axes[0].get_xaxis().set_visible(False)

        if self.current_period == 'd':
            x = np.arange(len(self.coin.get_day_data().index))
            ohlc = self.coin.get_day_data()[[
                'Open', 'High', 'Low', 'Close']].astype(int).values
            dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
            self.axes[1].bar(x, self.coin.get_day_data().Volume, color='k',
                             width=0.6, align='center')
        elif self.current_period == 'w':
            x = np.arange(len(self.coin.get_weekly_data().index))
            ohlc = self.coin.get_weekly_data()[[
                'Open', 'High', 'Low', 'Close']].astype(int).values
            dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
            self.axes[1].bar(x, self.coin.get_weekly_data().Volume, color='k',
                             width=0.6, align='center')
        elif self.current_period == 'y':
            x = np.arange(len(self.coin.get_monthly_data().index))
            ohlc = self.coin.get_monthly_data()[[
                'Open', 'High', 'Low', 'Close']].astype(int).values
            dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
            self.axes[1].bar(x, self.coin.get_monthly_data().Volume, color='k',
                             width=0.6, align='center')

        # 봉차트
        candlestick_ohlc(self.axes[0], dohlc,
                         width=0.5, colorup='r', colordown='b')

        # 거래량 차트
        # axes[1].bar(x, self.coin.data.Volume, color='k',
        #             width=0.6, align='center')

        # line_axes=self.fig.add_axes(self.coin.data.index,self.coin.data['Close'])
        plt.tight_layout()

        self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)

    def line_chart(self):
        self.current_type = 'line'
        self.axes.clear()
        if self.current_period == 'd':
            self.axes = self.fig.add_subplot(1, 1, 1)
            self.axes.clear()
            self.axes.plot(self.coin.get_day_data().index,
                           self.coin.get_day_data()['Close'], color="blue")
            self.axes.set(xlabel="Date", ylabel="Price($)",
                          title=self.coin.tickers)
            plt.subplots_adjust(left=0.088, right=0.97, top=0.94, bottom=0.083)
            self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)
        elif self.current_period == 'w':
            self.axes = self.fig.add_subplot(1, 1, 1)
            self.axes.clear()
            self.axes.plot(self.coin.get_weekly_data().index,
                           self.coin.get_weekly_data()['Close'], color="blue")
            self.axes.set(xlabel="Date", ylabel="Price($)",
                          title=self.coin.tickers)
            plt.subplots_adjust(left=0.088, right=0.97, top=0.94, bottom=0.083)
            self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)
        elif self.current_period == 'y':
            self.axes = self.fig.add_subplot(1, 1, 1)
            self.axes.clear()
            self.axes.plot(self.coin.get_monthly_data().index,
                           self.coin.get_monthly_data()['Close'], color="blue")
            self.axes.set(xlabel="Date", ylabel="Price($)",
                          title=self.coin.tickers)
            plt.subplots_adjust(left=0.088, right=0.97, top=0.94, bottom=0.083)
            self.canvas = FigureCanvasTkAgg(self.fig, self.parent)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=0, y=0, width=900, height=570)
