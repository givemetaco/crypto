import tkinter as tk
from tkinter import Canvas, Label, Menu, Pack, StringVar, Toplevel, ttk
from tkinter.constants import COMMAND
import json


# 메뉴바 , 메뉴와 서브메뉴를 포함하고 있는 클라스
class Menu_class:
    def __init__(self, root, graph, account,text_widget) -> None:
        self.root = root
        self.text_widget=text_widget
        self.graph = graph
        self.account = account
        self.menubar = Menu(root)  # 메뉴바 생성
        self.period_menu = Menu(self.menubar, tearoff=0)  # period 메뉴 만들기

        # 메뉴버튼을 누르면 실행될 command를 추가해주는 코드
        self.period_menu.add_cascade(label="Daily", command=self.set_period_D)
        self.period_menu.add_cascade(label="Weekly", command=self.set_period_W)
        self.period_menu.add_cascade(label="Monthly", command=self.set_period_Y)

        # 레이블 설정 + 메뉴바에 period메뉴 추가
        self.menubar.add_cascade(label='Period', menu=self.period_menu)

        # 그래프 형태를 결정하는 style 메뉴 만들기
        self.style_menu = Menu(self.menubar, tearoff=0)
        self.style_menu.add_cascade(label="Line Graph", command=self.change_to_line)
        self.style_menu.add_cascade(label="CandleStick Chart", command=self.change_to_candle)
        self.menubar.add_cascade(label='Style', menu=self.style_menu)

        # 저장 메뉴 만들기
        self.save_menu = Menu(self.menubar, tearoff=0)
        self.save_menu.add_cascade(label="Save", command=self.save)
        self.menubar.add_cascade(label='Save', menu=self.save_menu)

    def set_period_D(self):
        self.graph.current_period = 'd'
        self.graph.update_period()

    def set_period_W(self):
        self.graph.current_period = 'w'
        self.graph.update_period()

    def set_period_Y(self):
        self.graph.current_period = 'y'
        self.graph.update_period()

    def change_to_candle(self):
        self.graph.candle_chart()

    def change_to_line(self):
        self.graph.line_chart()

    def save(self):
        json_object = json.dumps(self.account.account, indent=4)
        try:
            with open('data.json', 'w') as f:
                f.write(json_object)
                print("Save Success!")
        except:
            print("Save Error!")

        self.text_widget.text_widget.delete("1.0",tk.END)
        self.text_widget.text_widget.insert(tk.END,"Saved!")
