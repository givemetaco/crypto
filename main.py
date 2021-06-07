from matplotlib.figure import Figure
from log_label import LLabel
import data_button as db
import tkinter as tk
from tkinter import Canvas, Label, Menu, Pack, StringVar, Toplevel, ttk
from tkinter.constants import ANCHOR, LEFT, N
import menu
import window
import account
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
    from collections import OrderedDict

    file_data = OrderedDict()

    file_data["BTC"] = 0
    file_data["ETH"] = 0
    file_data["DOGE"] = 0
    file_data["ADA"] = 0
    file_data["XRP"] = 0
    file_data["ETC"] = 0
    file_data["EOS"] = 0
    file_data["LINK"] = 0
    file_data["LTC"] = 0
    file_data["BCH"] = 0
    file_data["KRW"] = 100_000_000

    print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

    with open('data.json', 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent = "\t")
    
    my_account=account.Account
    window.run_program()

def click_button_4():

    import json
    from collections import OrderedDict

    file_data = OrderedDict()

    try:
        with open('data.json', 'r') as f:
            my_account=account.Account
            my_account.account = json.load(f)
            print("파일이 존재합니다.")
            print(my_account.account)

    except:
        print("찾는 파일이 없습니다.")

        file_data["BTC"] = 0
        file_data["ETH"] = 0
        file_data["DOGE"] = 0
        file_data["ADA"] = 0
        file_data["XRP"] = 0
        file_data["ETC"] = 0
        file_data["EOS"] = 0
        file_data["LINK"] = 0
        file_data["LTC"] = 0
        file_data["BCH"] = 0
        file_data["KRW"] = 100_000_000

        print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

        with open('data.json', 'w', encoding="utf-8") as make_file:
            json.dump(file_data, make_file, ensure_ascii=False, indent = "\t")

    window.run_program()

root = tk.Tk()

label = tk.Label(root)
root.title("BITCOIN")
root.geometry("640x480")

button_3 = tk.Button(root, text="새로하기", command = click_button_3)
button_4 = tk.Button(root, text="이어하기", command = click_button_4)

button_3.pack()
button_4.pack()

img = Image.open(r"image.jpg")
label.img = ImageTk.PhotoImage(img)
label['image'] = label.img
label.pack(side=LEFT)

root.mainloop()