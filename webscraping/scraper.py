from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FastShopScraper:
    def __init__(self) -> None:
        self.url = "https://www.polishop.com.br/smartphone?_q=smartphone&map=ft&page=#PAGE#"
        self.map = {
            "title": {
                'xpath': "/html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/section/div[2]/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div[2]/div[#COUNTER#]/section/a/article/div/p/strong"
            },
            "price": {
                'xpath': "/html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/section/div[2]/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div[2]/div[#COUNTER#]/section/a/article/div/div[3]/p[1]/strong"
            }
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_element(self, lista):
        counter_elem = 1
        while True:
            try:
                title = self.driver.find_element(By.XPATH, self.map['title']['xpath'].replace('#COUNTER#', str(counter_elem))).text
                print(title, end=": ")
                price = self.driver.find_element(By.XPATH, self.map['price']['xpath'].replace('#COUNTER#', str(counter_elem))).text
                print(price, end=" ")
                counter_elem += 1
                print()
                dict = {}
                dict['prod'] = title
                dict['price'] = price
                lista.append(dict)
            except Exception as e:
                # print("ERRO ELEMENTO", e)
                break
        return lista

    def open_site(self, phone=""):
        lista_e = []
        lista = []
        counter = 1
        print("========== POLISHOP:", phone, "==========")
        while counter <= 5:
        # while True:
            try:
                self.driver.get(self.url.replace('#PAGE#', str(counter)))
                sleep(5)
                lista.append(self.get_element(lista_e))
                counter += 1
            except Exception as e:
                # print("ERRO SITE", e)
                break

        lista_new = []
        for dicionario in lista:
            if dicionario['prod'].startswith('SMARTPHONE'):
                lista_new.append(dicionario)


        for element in lista_new:
            print("Celular: ", element['prod'], "Valor:", element['price'], end='\n\n')
        


web_scraper = FastShopScraper()
web_scraper.open_site()
