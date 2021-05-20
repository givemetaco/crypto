from data_button import data_button
import tkinter as tk
from tkinter import Label, Pack, StringVar, ttk
from tkinter.constants import ANCHOR, LEFT, N

from matplotlib.pyplot import hexbin

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import CrawlData as cd

import GraphPlot as gp

bitcoin = cd.Coin('BTC-USD')


root = tk.Tk()
root.configure(width=1200, height=800)  # 메인 프레임 크기 1200x800
root.resizable(False, False)  # 창 크기조절 비활성화
root.title("crypto")



s = ttk.Style()
s.configure('button.TFrame', background='red')

# 버튼이 들어갈 프레임

button_frame = ttk.Frame(root)
button_frame.configure(relief='raised', style='button.TFrame')
button_frame.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

# 버튼프레임 안의 세가지 버튼

button_1 = ttk.Button(button_frame, text="Button_1")
button_1.grid(row=0, column=0)

button_2 = ttk.Button(button_frame, text="Button_2")
button_2.grid(row=0, column=1)

button_3 = ttk.Button(button_frame, text="Button_3")
button_3.grid(row=0, column=2)

# 그래프가 들어갈 프레임

s.configure('graph.TFrame', background='blue')
graph_frame = ttk.Frame(root)
graph_frame.configure(width=900, height=600, style='graph.TFrame')
graph_frame.grid(row=1, column=0)


chart_type = FigureCanvasTkAgg(gp.fig, graph_frame)
chart_type.get_tk_widget().place(x=0,y=0,width=900,height=600)



# 10가지 코인의 가격 정보가 들어갈 프레임

s.configure('data.TFrame', background="green")
data_frame = ttk.Frame(root)
data_frame.configure(width=300, height=600, style='data.TFrame')
data_frame.grid(row=1, column=1)

s.configure("Bold.TLabel", size=40, weight="bold")
index_label = ttk.Label(data_frame, text=' Name    Price    Change')
index_label.configure(background='yellow', font=("Courier", 13))

# 절대 위치를 설정하여 label 표시, data_frame내의 (0,0)위치
index_label.place(x=0, y=0, width=300, height=50)

# bitcoin_text=StringVar()
# bitcoin_text.set('Bitcoin(BTC): '+ str(bitcoin.get_current_data()))
# bitcoin_label=ttk.Label(data_frame,textvariable=bitcoin_text)
# bitcoin_label.grid(row=1,column=0)

# 로그가 들어갈 프레임

s.configure('log.TFrame', background="yellow")
log_frame = ttk.Frame(root)
log_frame.configure(width=900, height=200, style='log.TFrame')
log_frame.grid(row=2, column=0)

# 판매,구매 버튼이 들어갈 프레임

s.configure('interact.TFrame', background="pink")
interact_frame = ttk.Frame(root)
interact_frame.configure(width=300, height=200, style='interact.TFrame')
interact_frame.grid(row=2, column=1)


root.mainloop()
