import tkinter as tk
from tkinter import ttk


class LLabel:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.width = 900
        self.height = 160
        self.text = tk.StringVar(parent)

    def place_label(self, x, y):
        self.label = tk.Label(self.parent, textvariable=self.text, font='Helvetica 15', justify='left', bg='gray')
        self.label.place(x=x, y=y, width=self.width, height=self.height)

    def set_coin(self, coin):
        self.coin = coin

    def updater(self):
        self.label.after(5000, self.updater)
        data = self.coin.get_transaction()
        self.text.set(
            data[0]['transaction_date'] + '\t' + data[0]['price'] + '\t\t' + data[0]['units_traded'] + '\n' + \
            data[2]['transaction_date'] + '\t' + data[1]['price'] + '\t\t' + data[2]['units_traded'] + '\n' + \
            data[3]['transaction_date'] + '\t' + data[2]['price'] + '\t\t' + data[3]['units_traded'] + '\n' + \
            data[4]['transaction_date'] + '\t' + data[3]['price'] + '\t\t' + data[4]['units_traded'] + '\n' + \
            data[5]['transaction_date'] + '\t' + data[4]['price'] + '\t\t' + data[5]['units_traded']
        )
