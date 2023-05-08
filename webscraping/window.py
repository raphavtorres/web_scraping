import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
    
# from scraper import WebScraper

window = tk.Tk()


class Application():
    def __init__(self) -> None:
        # self.MEGA_YEARS = MEGA_YEARS
        self.window = window
        self.screen()
        self.frame()
        self.buttons()
        self.inputs()
        self.labels()
        self.list_megas()
        self.comboBox()
        window.mainloop()

    def screen(self):
        self.window.title("Fast-Shop")
        self.window.geometry('1000x600')
        self.window.configure(background='#27a15b', border=0.8)
        self.window.resizable(False, False)


windowapp = Application()