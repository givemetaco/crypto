def run_program(my_account):
    from matplotlib.figure import Figure
    from log_label import LLabel
    import data_button as db
    import tkinter as tk
    from tkinter import Canvas, Label, Menu, Pack, StringVar, Toplevel, ttk
    import menu

    import Coin as c
    import GraphPlot as gp

    import trade

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

    # 로그가 들어갈 프레임

    log_frame = tk.Frame(root, width=900, height=200, bg='yellow')
    log_frame.grid(row=2, column=0)

    index_label = tk.Label(
        log_frame, text='\tTIME\t\tPRICE(KRW)\t\tVOLUME(BTC)', bd=5, font='TIMES 17', bg='#4A4A4A', fg='white')
    index_label.place(x=0, y=0, width=900, height=40)

    log_label = LLabel(log_frame)
    log_label.place_label(0, 40)

    # 판매,구매 버튼이 들어갈 프레임
    interact_frame = tk.Frame(root, width=300, height=200, bg='pink')
    interact_frame.grid(row=2, column=1)
    coin_entry = trade.TradeEntry(interact_frame, x=0, y=110)
    coin_label = trade.TradeLabel(interact_frame, bitcoin, x=240, y=110)
    coin_to_cash_label = trade.Coin2CashLabel(interact_frame, coin_label)
    # cash_label = trade.TradeLabel(interact_frame, x=240, y=155, text='KRW')
    refresh_button = trade.RefreshButton(interact_frame, coin_entry, coin_label, coin_to_cash_label)
    text_widget = trade.TextWidget(interact_frame, my_account)
    buy_button = trade.BuyButton(interact_frame, my_account, coin_to_cash_label, coin_entry, text_widget)
    sell_button = trade.SellButton(interact_frame, my_account, coin_to_cash_label, coin_entry, text_widget)

    # 10가지 코인의 가격 정보가 들어갈 프레임
    s.configure('data.TFrame', background="green")
    data_frame = ttk.Frame(root)
    data_frame.configure(width=300, height=600, style='data.TFrame')
    data_frame.grid(row=1, column=1)

    s.configure("Bold.TLabel", size=40, weight="bold")
    index_label = tk.Label(
        data_frame, text='Name\tPrice\tChange', font='TIMES 15', bg='#4A4A4A', fg='white')

    # 절대 위치를 설정하여 label 표시, data_frame내의 (0,0)위치
    index_label.place(x=0, y=0, width=300, height=50)

    # 데이터 버튼 삽입
    btc_button = db.data_button(data_frame, bitcoin, log_label, graph, coin_label, text_widget,my_account)
    btc_button.place_button(0, 50)
    btc_button.updater()

    eth_button = db.data_button(data_frame, ethereum, log_label, graph, coin_label, text_widget,my_account)
    eth_button.place_button(0, 105)
    eth_button.updater()

    etc_button = db.data_button(data_frame, ethereumC, log_label, graph, coin_label, text_widget,my_account)
    etc_button.place_button(0, 160)
    etc_button.updater()

    doge_button = db.data_button(data_frame, dogecoin, log_label, graph, coin_label, text_widget,my_account)
    doge_button.place_button(0, 215)
    doge_button.updater()

    ada_button = db.data_button(data_frame, cardano, log_label, graph, coin_label, text_widget,my_account)
    ada_button.place_button(0, 270)
    ada_button.updater()

    eos_button = db.data_button(data_frame, eos, log_label, graph, coin_label, text_widget,my_account)
    eos_button.place_button(0, 325)
    eos_button.updater()

    ripple_button = db.data_button(data_frame, ripple, log_label, graph, coin_label, text_widget,my_account)
    ripple_button.place_button(0, 380)
    ripple_button.updater()

    chainlink_button = db.data_button(data_frame, chainlink, log_label, graph, coin_label, text_widget,my_account)
    chainlink_button.place_button(0, 435)
    chainlink_button.updater()

    litecoin_button = db.data_button(data_frame, litecoin, log_label, graph, coin_label, text_widget,my_account)
    litecoin_button.place_button(0, 490)
    litecoin_button.updater()

    bch_button = db.data_button(data_frame, bitcoinCash, log_label, graph, coin_label, text_widget,my_account)
    bch_button.place_button(0, 545)
    bch_button.updater()

    # 메뉴가 들어갈 프레임

    menu_frame = ttk.Frame(root)
    menu_frame.configure(relief='raised', style='button.TFrame')
    menu_frame.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

    # 메뉴 객체 생성
    menu = menu.Menu_class(menu_frame, graph, my_account, text_widget)

    root.config(menu=menu.menubar)
    root.mainloop()
