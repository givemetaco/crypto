import tkinter as tk
from tkinter import Frame, StringVar, ttk

from matplotlib.pyplot import plot
import log_label
import GraphPlot as gp


class data_button:
    def __init__(self, parent, coin, label, graph: gp.graph) -> None:
        self.parent = parent
        self.label = label
        self.coin = coin
        self.graph = graph
        self.width = 300
        self.height = 60
        self.text = tk.StringVar(parent)
        self.text.set(self.coin.tickers + '\t' +
                      str(self.coin.get_current_data()) + '\t' + 'test')

    def place_button(self, x=0, y=0):
        self.button = tk.Button(self.parent, textvariable=self.text, bd=5,
                                font='Helvetica 13', command=lambda: [self.plot_log(),  self.change_coin()])
        self.button.place(x=x, y=y, width=self.width, height=self.height)

    def updater(self):
        self.button.after(5000, self.updater)
        self.text.set(self.coin.tickers + '\t' +
                      str(self.coin.get_current_data()) + '\t' + 'test')

    def plot_log(self):
        self.label.set_coin(self.coin)
        self.label.updater()

    def change_coin(self):
        if self.graph.current_type == 'line':
            self.graph.coin = self.coin
            self.graph.line_chart()
        else:
            self.graph.coin = self.coin
            self.graph.candle_chart()
