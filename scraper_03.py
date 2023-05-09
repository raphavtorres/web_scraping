from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FastShopScraper:
    def __init__(self) -> None:
        self.url = "https://www.polishop.com.br/smartphone?_q=smartphone&map=ft&page=#PAGE#"
        self.map = {
            "title": {
                'xpath': "/html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/section/div[2]/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div[#counter#]/div[2]/section/a/article/div/p/strong"
                # /html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/section/div[2]/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div[2]/div[1]/section/a/article/div/p/strong
            },
            "price": {
                'xpath': "/html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/section/div[2]/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div[2]/div[#counter#]/section/a/article/div/div[3]/p[1]/strong"
            }
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_site(self):
        self.driver.get(self.url.replace('#PAGE#', '1'))
        sleep(5)
        print("========== YEAR: ==========")
        counter = 1
        while True:
            try:
                title = self.driver.find_element(By.XPATH, self.map['title']['xpath'].replace('#counter#', f"{counter}")).text
                print(title, end=": ")
                price = self.driver.find_element(By.XPATH, self.map['price']['xpath'].replace('#counter#', f"{counter}")).text
                print(price, end=" ")
                counter += 1
            except Exception as e:
                continue


web_scraper = FastShopScraper()
web_scraper.open_site()
