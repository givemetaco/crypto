from matplotlib.figure import Figure
from log_label import LLabel
import data_button as db
import tkinter as tk
from tkinter import Canvas, Label, Menu, Pack, StringVar, Toplevel, ttk
import menu

import Coin as c
import GraphPlot as gp

bitcoin = c.Coin('BTC')
ethereum = c.Coin('ETH')
ethereumC = c.Coin('ETC')
dogecoin = c.Coin('DOGE')
cardano = c.Coin('ADA')
eos = c.Coin('EOS')
ripple = c.Coin('XRP')
chainlink = c.Coin('LINK')
litecoin = c.Coin('LTC')
bitcoinCash = c.Coin('BCH')

root = tk.Tk()
root.resizable(False, False)  # 창 크기조절 비활성화
root.title("crypto")

root.option_add('*tearOff', False)  # Menu버튼을 만들기 위해서 넣어줘야 하는 코드

s = ttk.Style()
s.configure('button.TFrame', background='red')

# 그래프가 들어갈 프레임

graph_frame = tk.Frame(root, width=900, height=600)
graph_frame.grid(row=1, column=0)

graph_graph_frame = tk.Frame(graph_frame, width=900, height=570, bg='red')
graph_graph_frame.grid(row=0, column=0)

navigation_frame = tk.Frame(graph_frame, width=900, height=30)
navigation_frame.grid(row=1, column=0)

graph = gp.graph(bitcoin, graph_graph_frame, navigation_frame)

# 메뉴가 들어갈 프레임

menu_frame = ttk.Frame(root)
menu_frame.configure(relief='raised', style='button.TFrame')
menu_frame.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

# 메뉴 객체 생성
menu = menu.Menu_class(menu_frame, graph)

# 로그가 들어갈 프레임

log_frame = tk.Frame(root, width=900, height=200, bg='yellow')
log_frame.grid(row=2, column=0)

index_label = tk.Label(
    log_frame, text='TIME\t\tPRICE(KRW)\t\tVOLUME(BTC)', bd=5, font='TIMES 17')
index_label.place(x=0, y=0, width=900, height=40)

log_label = LLabel(log_frame)
log_label.place_label(0, 40)

# 10가지 코인의 가격 정보가 들어갈 프레임

s.configure('data.TFrame', background="green")
data_frame = ttk.Frame(root)
data_frame.configure(width=300, height=600, style='data.TFrame')
data_frame.grid(row=1, column=1)

s.configure("Bold.TLabel", size=40, weight="bold")
index_label = ttk.Label(
    data_frame, text='   Name    Price    Change', font='TIMES 15')
index_label.configure(background='yellow', font=("Courier", 13))

# 절대 위치를 설정하여 label 표시, data_frame내의 (0,0)위치
index_label.place(x=0, y=0, width=300, height=50)

# 데이터 버튼 삽입
btc_button = db.data_button(data_frame, bitcoin, log_label, graph)
btc_button.place_button(0, 50)
btc_button.updater()

eth_button = db.data_button(data_frame, ethereum, log_label, graph)
eth_button.place_button(0, 105)
eth_button.updater()

etc_button = db.data_button(data_frame, ethereumC, log_label, graph)
etc_button.place_button(0, 160)
etc_button.updater()

doge_button = db.data_button(data_frame, dogecoin, log_label, graph)
doge_button.place_button(0, 215)
doge_button.updater()

ada_button = db.data_button(data_frame, cardano, log_label, graph)
ada_button.place_button(0, 270)
ada_button.updater()

eos_button = db.data_button(data_frame, eos, log_label, graph)
eos_button.place_button(0, 325)
eos_button.updater()

ripple_button = db.data_button(data_frame, ripple, log_label, graph)
ripple_button.place_button(0, 380)
ripple_button.updater()

chainlink_button = db.data_button(data_frame, chainlink, log_label, graph)
chainlink_button.place_button(0, 435)
chainlink_button.updater()

litecoin_button = db.data_button(data_frame, litecoin, log_label, graph)
litecoin_button.place_button(0, 490)
litecoin_button.updater()

bch_button = db.data_button(data_frame, bitcoinCash, log_label, graph)
bch_button.place_button(0, 545)
bch_button.updater()

# 판매,구매 버튼이 들어갈 프레임
interact_frame = tk.Frame(root, width=300, height=200, bg='pink')
interact_frame.grid(row=2, column=1)

root.config(menu=menu.menubar)
root.mainloop()
