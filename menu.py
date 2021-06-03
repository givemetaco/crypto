import tkinter as tk
from tkinter import Canvas, Label, Menu, Pack, StringVar, Toplevel, ttk
from tkinter.constants import COMMAND

# 메뉴바 , 메뉴와 서브메뉴를 포함하고 있는 클라스

class Menu_class:
    def __init__(self, root,graph) -> None:
        self.root = root
        self.graph=graph
        self.menubar = Menu(root)  # 메뉴바 생성
        self.period_menu = Menu(self.menubar, tearoff=0)  # period 메뉴 만들기
        self.period_menu.add_command(label="Daily",command=self.set_period_D)
        self.period_menu.add_command(label="Weekly",command=self.set_period_W)
        self.period_menu.add_command(label="Monthly",command=self.set_period_Y)
        # 레이블 설정 + 메뉴바에 period메뉴 추가
        self.menubar.add_cascade(label='Period', menu=self.period_menu)

        # 그래프 형태를 결정하는 style 메뉴 만들기
        self.style_menu = Menu(self.menubar, tearoff=0)
        self.style_menu.add_cascade(label="Line Graph")
        self.style_menu.add_cascade(label="CandleStick Chart")
        self.menubar.add_cascade(label='Style', menu=self.style_menu)


    def set_period_D(self):
        self.graph.current_period='d'
        self.graph.update_period()
    
    def set_period_W(self):
        self.graph.current_period='w'
        self.graph.update_period()
    
    def set_period_Y(self):
        self.graph.current_period='y'
        self.graph.update_period()
