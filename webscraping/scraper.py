from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FastShopScraper:
    def __init__(self, subject_index) -> None:
        self.subject_index = subject_index
        SUBJECT = ["de-entretenimento", "biografias", "de-ficcao", "de-mitologia-e-folclore", "de-arte-e-fotografia"]

        self.url = f"https://www.kabum.com.br/livros/livros-{SUBJECT[self.subject_index]}"
        self.map = {
            "title": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[#counter#]/a/div/button/div/h2/span'
            },
            "price": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[#counter#]/a/div/div/span[2]'
            }
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)


    def open_site(self):
        self.driver.get(self.url)
        sleep(5)
        print("========== BOOKS: ==========")
        counter = 1
        while True:
            try:
                title = self.driver.find_element(By.XPATH, self.map['title']['xpath'].replace('#counter#', str(counter))).text
                print(title, end=": ")
                price = self.driver.find_element(By.XPATH, self.map['price']['xpath'].replace('#counter#', str(counter))).text
                print(price)
                counter += 1
            except Exception as e:
                # print("ERRO: ", e)
                break


web_scraper = FastShopScraper(4)  # maximum 4
web_scraper.open_site()


# https://www.kabum.com.br/livros/livros-de-entretenimento
# https://www.kabum.com.br/livros/livros-biografias
# https://www.kabum.com.br/livros/livros-de-ficcao
# https://www.kabum.com.br/livros/livros-de-mitologia-e-folclore
# https://www.kabum.com.br/livros/livros-de-arte-e-fotografia