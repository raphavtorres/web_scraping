import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
    
from scraper import WebScraper

window = tk.Tk()

SUBJECT = ["Entretenimento", "Biografias", "Ficção", "Mitologia e Folclore", "Arte e Fotografia"]
class Application():
   
    def __init__(self) -> None:
        self.window = window
        self.screen()
        self.frame()
        self.buttons()
        # self.inputs()
        # self.labels()
        self.products_table()
        self.comboBox()
        window.mainloop()

    def screen(self):
        self.window.title("Fast-Shop")
        self.window.geometry('900x400')
        self.window.configure(background='#27a15b', border=0.8)
        self.window.resizable(False, False)

    def frame(self):
        self.frame_0 = tk.Frame(self.window, bg="#5effa4")
        self.frame_0.place(relx=0.03, rely=0.06, relwidth=0.94, relheight=0.12)

        self.frame_1 = tk.Frame(self.window, bg='#5effa4')
        self.frame_1.place(relx=0.03, rely=0.22, relwidth=0.94, relheight=0.7)

    def buttons(self):
        self.btn_search = tk.Button(self.frame_0, bg="#7a2c64", border=0, text="Search", font=("sans-serif", 12), fg="#ffffff")
        self.btn_search.place(relx=0.77, rely=0.20, relwidth=0.1, relheight=0.7)

        self.btn_update = tk.Button(self.frame_0, bg="#7a2c64", border=0, text="Update", font=("sans-serif", 12), fg="#ffffff")
        self.btn_update.place(relx=0.6, rely=0.20, relwidth=0.1, relheight=0.7)

        self.btn_update = tk.Button(self.frame_0, bg="#7a2c64", border=0, text="Update", font=("sans-serif", 12), fg="#ffffff")
        self.btn_update.place(relx=0.3, rely=0.20, relwidth=0.1, relheight=0.7)

    def comboBox(self):
            self.cb_years = ttk.Combobox(self.frame_0, values=SUBJECT, font=("sans-serif", 12))
            self.cb_years.set(SUBJECT[0])
            self.cb_years.pack()
            self.cb_years.place(relx=0.01, rely=0.20, relwidth=0.22, relheight=0.7)

    def products_table(self):
        self.list_megas_tb = ttk.Treeview(
            self.frame_1,
            height=3,
            columns=(
                'col0', 'col1', 'col3'
                )
            )
        self.list_megas_tb.heading('#0', text='')
        self.list_megas_tb.heading('#1', text='TITLE')
        self.list_megas_tb.heading('#2', text='PRICE')

        self.list_megas_tb.column('#0', width=0)
        self.list_megas_tb.column('#1', width=250)
        self.list_megas_tb.column('#2', width=200)

        self.list_megas_tb.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
        self.scrool_list = tk.Scrollbar(self.frame_1, orient='vertical')
        self.list_megas_tb.configure(yscrollcommand=self.scrool_list.set)
        self.scrool_list.place(relx=0.97, rely=0.02, relwidth=0.03, relheight=0.96)

    def clear(self):
        self.list_megas_tb.delete(*self.list_megas_tb.get_children())

    def update(self):
        year = self.get_year()
        web_scraper_update = WebScraper()
        web_scraper_update.open_site(year)

    # def graph(self):
    #     fig, ax = plt.subplots()
    #     numbers = [str(num) for num in range(1, 61)]
    #     counts = self.get_numbers()
    #     bar_colors = 'tab:blue'

    #     ax.bar(numbers, counts, color=bar_colors)

    #     ax.set_title(f'Graphic representation - {self.get_year()}')
    #     ax.set_ylabel('Amount of occurrences')

    #     plt.show()

windowapp = Application()
