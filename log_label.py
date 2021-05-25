import tkinter as tk
from tkinter import ttk


class LLabel:
    def __init__(self, parent, coin) -> None:
        self.parent = parent
        self.coin = coin
        self.width = 900
        self.height = 160
        self.text=tk.StringVar(parent)
        self.text.set(self.coin.get_transaction()[0]['transaction_date']+ '\t\t' +self.coin.get_transaction()[0]['price']+'\t\t'+self.coin.get_transaction()[0]['units_traded']+'\n'+\
            self.coin.get_transaction()[1]['transaction_date']+ '\t\t' +self.coin.get_transaction()[1]['price']+'\t\t'+self.coin.get_transaction()[1]['units_traded']+'\n'+\
            self.coin.get_transaction()[2]['transaction_date']+ '\t\t' +self.coin.get_transaction()[2]['price']+'\t\t'+self.coin.get_transaction()[2]['units_traded']+'\n'+\
            self.coin.get_transaction()[3]['transaction_date']+ '\t\t' +self.coin.get_transaction()[3]['price']+'\t\t'+self.coin.get_transaction()[3]['units_traded']+'\n'+\
            self.coin.get_transaction()[4]['transaction_date']+ '\t\t' +self.coin.get_transaction()[4]['price']+'\t\t'+self.coin.get_transaction()[4]['units_traded']+'\n'+\
            self.coin.get_transaction()[5]['transaction_date']+ '\t\t' +self.coin.get_transaction()[5]['price']+'\t\t'+self.coin.get_transaction()[5]['units_traded']       
        )

    def place_label(self, x, y):
        self.label = tk.Label(self.parent,textvariable=self.text,font='Helvetica 13')
        self.label.place(x=x, y=y, width=self.width, height=self.height)
    
    def updater(self):
        self.label.after(3000,self.updater)
        self.text.set(self.coin.get_transaction()[0]['transaction_date']+ '\t\t' +self.coin.get_transaction()[0]['price']+'\t\t'+self.coin.get_transaction()[0]['units_traded']+'\n'+\
            self.coin.get_transaction()[1]['transaction_date']+ '\t\t' +self.coin.get_transaction()[1]['price']+'\t\t'+self.coin.get_transaction()[1]['units_traded']+'\n'+\
            self.coin.get_transaction()[2]['transaction_date']+ '\t\t' +self.coin.get_transaction()[2]['price']+'\t\t'+self.coin.get_transaction()[2]['units_traded']+'\n'+\
            self.coin.get_transaction()[3]['transaction_date']+ '\t\t' +self.coin.get_transaction()[3]['price']+'\t\t'+self.coin.get_transaction()[3]['units_traded']+'\n'+\
            self.coin.get_transaction()[4]['transaction_date']+ '\t\t' +self.coin.get_transaction()[4]['price']+'\t\t'+self.coin.get_transaction()[4]['units_traded']+'\n'+\
            self.coin.get_transaction()[5]['transaction_date']+ '\t\t' +self.coin.get_transaction()[5]['price']+'\t\t'+self.coin.get_transaction()[5]['units_traded']       
        )
