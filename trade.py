import tkinter as tk


# class TradeButton:
#     def __init__(self, parent, entry, x=0, y=0, text=''):
#         self.button = tk.Button(parent, fg='white', bg='#404040', text=text, bd=3)
#         self.button.place(x=x, y=y, height=30, width=150)
class BuyButton:
    def __init__(self, parent, account, c2c, coin_entry, text_widget):
        button = buy_button = tk.Button(parent, text='BUY', fg='white', bg='#404040', bd=3, command=self.button_click)
        button.place(x=0, y=80, height=30, width=150)
        self.account = account
        self.c2c = c2c
        self.coin_entry = coin_entry
        self.text_widget = text_widget

    def button_click(self):
        buy_amount_coin = float(self.coin_entry.get_input())
        price_of_purchase = buy_amount_coin * self.c2c.tradelabel.current_coin.get_current_data()
        if self.account.account['KRW'] >= price_of_purchase:
            self.account.account['KRW'] = self.account.account['KRW'] - price_of_purchase
            self.account.account[self.c2c.tradelabel.current_coin.tickers] = \
                self.account.account[self.c2c.tradelabel.current_coin.tickers] + buy_amount_coin
            self.text_widget.text_widget.delete("1.0", tk.END)
            self.text_widget.text_widget.insert(tk.END,
                                                str(buy_amount_coin) + ' ' + self.c2c.tradelabel.current_coin.tickers +
                                                " Successfully purchased.\n" + str(self.account.account[
                                                                                       'KRW']) + ' ₩ Left\n Your ' + self.c2c.tradelabel.current_coin.tickers + ':' +
                                                str(self.account.account[self.c2c.tradelabel.current_coin.tickers]))
        else:
            self.text_widget.text_widget.delete("1.0", tk.END)
            self.text_widget.text_widget.insert(tk.END, 'You do not have enough money\n')
            self.text_widget.text_widget.insert(tk.END, 'You have ' + str(self.account.account['KRW']) + ' ₩')


class SellButton:
    def __init__(self, parent, account, c2c, coin_entry, text_widget):
        button = tk.Button(parent,
                           text='SELL', fg='white', bg='#404040', bd=3, command=self.button_click)
        button.place(x=150, y=80, height=30, width=150)
        self.account = account
        self.c2c = c2c
        self.coin_entry = coin_entry
        self.text_widget = text_widget

    def button_click(self):
        sell_amount_coin = float(self.coin_entry.get_input())
        price_of_sell = sell_amount_coin * self.c2c.tradelabel.current_coin.get_current_data()
        if self.account.account[self.c2c.tradelabel.current_coin.tickers] >= sell_amount_coin:
            self.account.account['KRW'] = self.account.account['KRW'] + price_of_sell
            self.account.account[self.c2c.tradelabel.current_coin.tickers] = \
                self.account.account[self.c2c.tradelabel.current_coin.tickers] - sell_amount_coin
            self.text_widget.text_widget.delete("1.0", tk.END)
            self.text_widget.text_widget.insert(tk.END,
                                                str(sell_amount_coin) + ' ' + self.c2c.tradelabel.current_coin.tickers +
                                                " Successfully sold.\n" + str(self.account.account[
                                                                                  'KRW']) + ' ₩ Left\n Your ' + self.c2c.tradelabel.current_coin.tickers + ':' +
                                                str(self.account.account[self.c2c.tradelabel.current_coin.tickers]))
        else:
            self.text_widget.text_widget.delete("1.0", tk.END)
            self.text_widget.text_widget.insert(tk.END, 'You do not have enough coin\n')
            self.text_widget.text_widget.insert(tk.END, 'You have ' + str(self.account.account[
                                                                              self.c2c.tradelabel.current_coin.tickers]) + self.c2c.tradelabel.current_coin.tickers)


class TradeEntry:
    def __init__(self, parent, x=0, y=0):
        self.buy_entry = tk.Entry(parent, font='Helvetica 16', width=12, justify='right')
        self.buy_entry.place(x=x, y=y, height=45, width=240)

    def get_input(self):
        return self.buy_entry.get()


class TradeLabel:
    def __init__(self, parent, coin, x=0, y=0):
        self.current_coin = coin
        self.buy_label = tk.Label(parent, text=self.current_coin, bg='#11004A', fg='white')
        self.buy_label.place(x=x, y=y, height=45, width=60)

    def change_coin(self, coin):
        self.current_coin = coin
        self.buy_label.configure(text=self.current_coin.tickers)


class Coin2CashLabel:
    def __init__(self, parent, tradelabel):
        self.label = tk.Label(parent, text=0, bg='#11004A',
                              fg='white', font='Helvetica 16')
        self.label.place(x=0, y=155, height=45, width=240)
        self.tradelabel = tradelabel

    def refresh(self, num):
        self.label.configure(text=str(int(num) * self.tradelabel.current_coin.get_current_data()) + ' ₩')


class RefreshButton:
    def __init__(self, parent, entry, label, c2c):
        self.refresh_button = tk.Button(parent, bg='#11004A', fg='white', text='Refresh', command=self.refresh)
        self.refresh_button.place(x=240, y=155, width=60, height=45)
        self.entry = entry
        self.label = label
        self.c2c = c2c

    def refresh(self):
        n = self.entry.get_input()
        self.c2c.refresh(n)


class TextWidget:
    def __init__(self, parent, account):
        self.account = account
        self.text_widget = tk.Text(parent, font='Helvetica 10')
        self.text_widget.place(x=0, y=0, width=300, height=80)
        self.text_widget.insert(tk.END, account.account)
