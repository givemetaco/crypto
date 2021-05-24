import tkinter as tk
from tkinter import Frame, StringVar, ttk

class data_button:
    def __init__(self,parent,coin) -> None:
        self.parent=parent
        self.coin=coin
        self.width=300
        self.height=60

    
    def place_button(self,x=0,y=0):
        self.button=tk.Button(self.parent,text=self.coin.name,bd=5)
        self.button.place(x=x,y=y,width=self.width,height=self.height)
    
    # def update(self,parent)->None:
    #     self.button['text']= 

