import tkinter as tk
from tkinter import Label, Pack, ttk
from tkinter.constants import ANCHOR, LEFT

from matplotlib.pyplot import hexbin


root = tk.Tk()
root.configure(width=1200, height=800)
root.resizable(False, False)
root.title("crypto")

s = ttk.Style()
s.configure('button.TFrame', background='red')

# 버튼이 들어갈 프레임

button_frame = ttk.Frame(root)
button_frame.configure(relief='raised', style='button.TFrame')
button_frame.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)


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

# 10가지 코인의 가격 정보가 들어갈 프레임

s.configure('data.TFrame', background="green")
data_frame = ttk.Frame(root)
data_frame.configure(width=300, height=600, style='data.TFrame')
data_frame.grid(row=1, column=1)

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
