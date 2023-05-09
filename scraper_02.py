from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FastShopScraper:
    def __init__(self, marca) -> None:
        self.marca = marca
        self.url = f"https://www.kabum.com.br/espaco-gamer/cadeiras-gamer/{self.marca}"
        self.map = {
            "title": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[#AAA#]/main/div[#AAA#]/a/div/div[2]/div[1]/h2/span'
                # 
                # /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[1]/div/a/div[3]/h3
            },
        }


        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_site(self):
        # phone = "061003/samsung_galaxy"
        self.driver.get(self.url)
        sleep(5)
        print("========== YEAR: ==========")
        # self.get_numbers(phone)
        print(self.driver.find_element(By.XPATH, self.map['title']['xpath']).text)
        counter
        while True:
            try:
                title = self.driver.find_element(By.XPATH, self.map['title']['xpath'].replace('#counter#', str(counter))).text
                print(title, end=": ")
                counter += 1
            except Exception as e:
                print("ERRO: ", e)
                break


web_scraper = FastShopScraper()
web_scraper.open_site()


# https://www.kabum.com.br/espaco-gamer/cadeiras-gamer/corsair
# https://www.kabum.com.br/espaco-gamer/cadeiras-gamer/dt3-sports
# https://www.kabum.com.br/espaco-gamer/cadeiras-gamer/husky-gaming
# https://www.kabum.com.br/espaco-gamer/cadeiras-gamer/thunderx3
# https://www.kabum.com.br/espaco-gamer/cadeiras-gamer/xt-racer