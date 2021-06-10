from matplotlib.figure import Figure
from log_label import LLabel
import data_button as db
import tkinter as tk
from tkinter import Canvas, Label, Menu, Pack, StringVar, Toplevel, ttk
from tkinter.constants import ANCHOR, LEFT, N
import menu
import window
import account as act
# import matplotlib
# from matplotlib.pyplot import hexbin

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

# from matplotlib.figure import Figure

import Coin as c
import GraphPlot as gp

from PIL import Image, ImageTk


def click_button_3():
    import json

    account = {
        'BTC': 0,
        'ETH': 0,
        'DOGE': 0,
        'ADA': 0,
        'XRP': 0,
        'ETC': 0,
        'EOS': 0,
        'LINK': 0,
        'LTC': 0,
        'BCH': 0,
        'KRW': 100_000_000
    }

    json_object = json.dumps(account, indent=4)

    with open('data.json', 'w') as make_file:
        make_file.write(json_object)

    my_account = act.Account()
    window.run_program(my_account)


def click_button_4():
    import json
    from collections import OrderedDict

    try:
        with open('data.json', 'r') as f:
            my_account = act.Account
            my_account.account = json.load(f)
            print("파일이 존재합니다.")
            print(my_account.account)

    except:
        print("찾는 파일이 없습니다.")

        account = {
            'BTC': 0,
            'ETH': 0,
            'DOGE': 0,
            'ADA': 0,
            'XRP': 0,
            'ETC': 0,
            'EOS': 0,
            'LINK': 0,
            'LTC': 0,
            'BCH': 0
        }

        json_object = json.dumps(account, indent=4)

        with open('data.json', 'w') as make_file:
            make_file.write(json_object)

    window.run_program(my_account)


root = tk.Tk()

label = tk.Label(root)
root.title("BITCOIN")
root.geometry("640x480")

button_3 = tk.Button(root, text="새로하기", command=click_button_3)
button_4 = tk.Button(root, text="이어하기", command=click_button_4)

button_3.pack()
button_4.pack()

img = Image.open(r"image.jpg")
label.img = ImageTk.PhotoImage(img)
label['image'] = label.img
label.pack(side=LEFT)

root.mainloop()
