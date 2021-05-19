import tkinter as tk
from tkinter import ttk

class data_button:
    def __init__(self,parent,coin) -> None:
        self.parent=parent
        self.coin=coin
        self.data_btn=ttk.Button(self.parent,text=self.coin+'data')

