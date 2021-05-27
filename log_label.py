import tkinter as tk
from tkinter import ttk


class LLabel:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.width = 900
        self.height = 160
        self.text=tk.StringVar(parent)
        # self.text.set(self.coin.get_transaction()[0]['transaction_date']+ '\t\t' +self.coin.get_transaction()[0]['price']+'\t\t'+self.coin.get_transaction()[0]['units_traded']+'\n'+\
        #     self.coin.get_transaction()[1]['transaction_date']+ '\t\t' +self.coin.get_transaction()[1]['price']+'\t\t'+self.coin.get_transaction()[1]['units_traded']+'\n'+\
        #     self.coin.get_transaction()[2]['transaction_date']+ '\t\t' +self.coin.get_transaction()[2]['price']+'\t\t'+self.coin.get_transaction()[2]['units_traded']+'\n'+\
        #     self.coin.get_transaction()[3]['transaction_date']+ '\t\t' +self.coin.get_transaction()[3]['price']+'\t\t'+self.coin.get_transaction()[3]['units_traded']+'\n'+\
        #     self.coin.get_transaction()[4]['transaction_date']+ '\t\t' +self.coin.get_transaction()[4]['price']+'\t\t'+self.coin.get_transaction()[4]['units_traded']+'\n'+\
        #     self.coin.get_transaction()[5]['transaction_date']+ '\t\t' +self.coin.get_transaction()[5]['price']+'\t\t'+self.coin.get_transaction()[5]['units_traded']       
        # )

    def place_label(self, x, y):
        self.label = tk.Label(self.parent,textvariable=self.text,font='Helvetica 13')
        self.label.place(x=x, y=y, width=self.width, height=self.height)

    def set_coin(self,coin):
        self.coin=coin

    def updater(self):
        self.label.after(3000,self.updater)
        data=self.coin.get_transaction()
        self.text.set(data[0]['transaction_date']+ '\t\t' +data[0]['price']+'\t\t'+data[0]['units_traded']+'\n'+\
            data[2]['transaction_date']+ '\t\t' +data[1]['price']+'\t\t'+data[2]['units_traded']+'\n'+\
            data[3]['transaction_date']+ '\t\t' +data[2]['price']+'\t\t'+data[3]['units_traded']+'\n'+\
            data[4]['transaction_date']+ '\t\t' +data[3]['price']+'\t\t'+data[4]['units_traded']+'\n'+\
            data[5]['transaction_date']+ '\t\t' +data[4]['price']+'\t\t'+data[5]['units_traded'] 
            )
