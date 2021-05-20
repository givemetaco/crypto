import data_button as db
import tkinter as tk
from tkinter import Label, Pack, StringVar, ttk
from tkinter.constants import ANCHOR, LEFT, N

from matplotlib.pyplot import hexbin

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import Coin as c
import GraphPlot as gp

bitcoin = c.Coin('BTC-USD')


root = tk.Tk()
root.resizable(False, False)  # 창 크기조절 비활성화
root.title("crypto")



s = ttk.Style()
s.configure('button.TFrame', background='red')

# 버튼이 들어갈 프레임

button_frame = ttk.Frame(root)
button_frame.configure(relief='raised', style='button.TFrame')
button_frame.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

# 버튼프레임 안의 세가지 버튼

button_1 = tk.Button(button_frame, text="Button_1",height=1)
button_1.grid(row=0, column=0)

button_2 = tk.Button(button_frame, text="Button_2",height=1)
button_2.grid(row=0, column=1)

button_3 = tk.Button(button_frame, text="Button_3",height=1)
button_3.grid(row=0, column=2)

# 그래프가 들어갈 프레임

#s.configure('graph.TFrame', background='blue')
graph_frame = tk.Frame(root,width=900,height=600,bg='blue')
#graph_frame.configure(width=900, height=600, style='graph.TFrame')
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

# 데이터 버튼 삽입
#아래 두줄은 절차지향 방식으로 작성한 코드
#bit_button=tk.Button(data_frame,text=bitcoin.name,bd=10)
#bit_button.place(x=0,y=50,width=300,height=50)
#아래는 객체지향 방식으로 작성한 코드
btc_button=db.data_button(data_frame,bitcoin)
btc_button.place_button(0,50)

# bitcoin_text=StringVar()
# bitcoin_text.set('Bitcoin(BTC): '+ str(bitcoin.get_current_data()))
# bitcoin_label=ttk.Label(data_frame,textvariable=bitcoin_text)
# bitcoin_label.grid(row=1,column=0)

# 로그가 들어갈 프레임

#아래 두줄은 ttk로 프레임을 만들기 위해서 사용하는 코드
#s.configure('log.TFrame', background="yellow")
#log_frame.configure(width=900, height=200, style='log.TFrame')
#아래는 tk로 프레임을 만들기 위한 코드
log_frame = tk.Frame(root,width=900,height=200,bg='yellow')
log_frame.grid(row=2, column=0)

# 판매,구매 버튼이 들어갈 프레임
interact_frame = tk.Frame(root,width=300,height=200,bg='pink')
interact_frame.grid(row=2, column=1)


root.mainloop()
