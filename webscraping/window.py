import tkinter as tk
from tkinter import ttk
import awesometkinter as atk
import matplotlib.pyplot as plt
import pandas as pd

from db_functions import select_products
from scraper import KabumScraper
from lists_subjects import SUBJECTS, url_subject

window = tk.Tk()


class Application():
    def __init__(self):
        self.window = window
        self.files = ["To Excel", "To CSV"]
        self.screen()
        self.frame()
        self.buttons()
        self.products_table()
        self.comboBox()
        self.image()
        window.mainloop()

    def screen(self):
        self.window.title("KaBuM!")
        self.img_logo = tk.PhotoImage(file="imagekabum.png")
        self.window.iconphoto(False, self.img_logo)
        self.window.geometry('900x400')
        self.window.configure(background='#001E66', border=0.8)
        self.window.resizable(False, False)
        self.defaultFont = tk.font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="sans-serif",
                                   size=11)

    def frame(self):
        self.frame_0 = tk.Frame(self.window, bg="#0060B1")
        self.frame_0.place(relx=0.03, rely=0.06, relwidth=0.94, relheight=0.12)

        self.frame_1 = tk.Frame(self.window, bg='#0060B1')
        self.frame_1.place(relx=0.03, rely=0.22, relwidth=0.94, relheight=0.7)

    def buttons(self):
        self.btn_search = atk.Button3d(
            self.frame_0, bg="#FF6500", text="SEARCH", fg="#ffffff",
            command=self.read_products)
        self.btn_search.place(relx=0.25, rely=0.08, relwidth=0.1, relheight=0.9)

        self.btn_update = atk.Button3d(
            self.frame_0, bg="#FF6500", text="UPDATE", fg="#ffffff",
            command=self.update)
        self.btn_update.place(relx=0.77, rely=0.08, relwidth=0.1, relheight=0.9)

        self.btn_graph = atk.Button3d(self.frame_0, bg="#FF6500", text="GRAPH",
                                      fg="#ffffff", command=self.graph)
        self.btn_graph.place(relx=0.88, rely=0.08, relwidth=0.1, relheight=0.9)

        self.btn_file = atk.Button3d(self.frame_0, bg="#FF6500", text="FILE",
                                      fg="#ffffff", command=self.create_file)
        self.btn_file.place(relx=0.57, rely=0.08, relwidth=0.1, relheight=0.9)

    def comboBox(self):
        self.cb_products = ttk.Combobox(self.frame_0, values=SUBJECTS,
                                        font=("sans-serif", 12))
        self.cb_products.set(SUBJECTS[0])
        self.cb_products.pack()
        self.cb_products.place(relx=0.01, rely=0.20, relwidth=0.22,
                               relheight=0.7)
        
        self.cb_file = ttk.Combobox(self.frame_0, values=self.files,
                                        font=("sans-serif", 12))
        self.cb_file.set(self.files[0])
        self.cb_file.pack()
        self.cb_file.place(relx=0.45, rely=0.20, relwidth=0.10,
                               relheight=0.7)

    def products_table(self):
        self.list_prods_tb = ttk.Treeview(
            self.frame_1,
            height=3,
            columns=(
                'col0', 'col1', 'col3'
                ),
            )
        self.list_prods_tb.heading('#0', text='')
        self.list_prods_tb.heading('#1', text='TITLE')
        self.list_prods_tb.heading('#2', text='PRICE')

        self.list_prods_tb.column('#0', width=0)
        self.list_prods_tb.column('#1', width=400)
        self.list_prods_tb.column('#2', width=80)

        self.list_prods_tb.place(
            relx=0.01, rely=0.02, relwidth=0.6, relheight=0.96
            )
        self.scrool_list = ttk.Scrollbar(self.frame_1, orient='vertical')
        self.list_prods_tb.configure(yscrollcommand=self.scrool_list.set)
        self.scrool_list.place(
            relx=0.97, rely=0.02, relwidth=0.03, relheight=0.96
            )

    def image(self):
        self.img_ninja = tk.PhotoImage(file="card_kabum.png")
        self.lb_img = tk.Label(self.frame_1, image=self.img_ninja)
        self.lb_img.place(relx=0.62, rely=0.02, relwidth=0.34, relheight=1)

    def clear(self):
        self.list_prods_tb.delete(*self.list_prods_tb.get_children())

    def read_products(self):
        self.clear()
        subject = url_subject[self.get_subject_index()]
        products = select_products(subject)
        for product in products:
            self.list_prods_tb.insert("", "end", values=product)

    def get_subject(self):
        return self.cb_products.get()

    def get_subject_index(self):
        subject = self.get_subject()
        index_subject = SUBJECTS.index(subject)
        return index_subject

    def update(self):
        product_index = self.get_subject_index()
        web_scraper = KabumScraper(product_index)
        web_scraper.open_site()

    def graph(self):
        plt.rcParams['ytick.labelsize'] = 8
        fig, ax = plt.subplots()

        titles, prices = self.get_titles_and_prices()
        bar_colors = 'tab:blue'

        ax.barh(titles, prices, align='center', color=bar_colors)
        ax.invert_yaxis()
        ax.set_title(f'Graphic - {self.get_subject()}')
        ax.set_xlabel('Amount of occurrences')

        plt.show()

    def get_dict_titles_prices(self):
        dict_list = []
        subject = url_subject[self.get_subject_index()]
        products = select_products(subject)

        for product in products:
            dict = {}
            dict['title'] = product[0]
            dict['price'] = float(product[1].replace(",", "."))
            dict_list.append(dict)

        return dict_list

    def get_titles_and_prices(self):
        dict_list = self.get_dict_titles_prices()
        title_list = [""]
        price_list = [0.0]

        def order(dict):
            return dict['price']

        dict_list_sort = sorted(dict_list, key=order)
        for dict in dict_list_sort:
            title_list.append(dict['title'])
            price_list.append(dict['price'])
        return title_list, price_list

    def create_file(self):
        dict = self.get_dict_titles_prices()
        data = pd.DataFrame(data=dict)

        if self.cb_file.get() == "To Excel":
            data.to_excel("web_scraping_excel.xlsx", index=False)
        else:
            data.to_csv("web_scraping_csv.xlsx", index=False)
