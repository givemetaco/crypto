import tkinter as tk
from tkinter import Frame, StringVar, ttk

from matplotlib.pyplot import plot
import log_label
import GraphPlot as gp
import trade


class data_button:
    def __init__(self, parent, coin, label, graph: gp.graph, coin_label: trade.TradeLabel, text_widget,
                 my_account) -> None:
        self.parent = parent
        self.label = label
        self.text_widget = text_widget
        self.my_account = my_account
        self.coin = coin
        self.graph = graph
        self.width = 300
        self.height = 60
        self.coin_label = coin_label
        self.text = tk.StringVar(parent)
        self.text.set(self.coin.tickers + '\t' +
                      str(self.coin.get_current_data()) + '\t' + 'test')

    def place_button(self, x=0, y=0):
        self.button = tk.Button(self.parent, textvariable=self.text, bd=5,
                                font='Helvetica 13', command=lambda: [self.plot_log(), self.change_coin(),self.show_account()])

        self.button.place(x=x, y=y, width=self.width, height=self.height)

    def updater(self):
        self.button.after(5000, self.updater)
        self.text.set(self.coin.tickers + '\t' +
                      str(self.coin.get_current_data()) + '\t' + 'test')

    def plot_log(self):
        self.label.set_coin(self.coin)
        self.label.updater()

    def change_coin(self):
        self.coin_label.change_coin(self.coin)
        if self.graph.current_type == 'line':
            self.graph.coin = self.coin
            self.graph.line_chart()
        else:
            self.graph.coin = self.coin
            self.graph.candle_chart()

    def show_account(self):
        self.text_widget.text_widget.delete("1.0", tk.END)
        self.text_widget.text_widget.insert(tk.END, self.my_account.account)
