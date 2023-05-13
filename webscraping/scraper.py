from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from db_functions import insert_db, create_table
from lists_subjects import SUBJECTS, url_subject


class KabumScraper:
    def __init__(self, subject_index) -> None:
        self.subject_index = subject_index
        self.url_subject = url_subject[self.subject_index]
        self.subject = SUBJECTS[self.subject_index]

        self.url = f"https://www.kabum.com.br/livros/livros-{self.url_subject}"
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
        subject = self.subject
        # subject = self.subject.lower().replace(" ", "_")
        self.driver.get(self.url)

        create_table(subject)
        table = f"products{subject}"

        sleep(5)
        print("========== BOOKS: ==========")
        counter = 1
        while True:
            try:
                title = self.driver.find_element(
                    By.XPATH, self.map['title']['xpath'].replace('#counter#', str(counter))).text
                print(title, end=": ")
                price = self.driver.find_element(
                    By.XPATH, self.map['price']['xpath'].replace('#counter#', str(counter))).text
                print(price)
                counter += 1
            except Exception:
                # print("ERRO: ", e)
                break
            insert_db(
                table=table,
                title=title,
                price=price)


# web_scraper = KabumScraper(4)  # maximum 4
# web_scraper.open_site()


# https://www.kabum.com.br/livros/livros-de-entretenimento
# https://www.kabum.com.br/livros/livros-biografias
# https://www.kabum.com.br/livros/livros-de-ficcao
# https://www.kabum.com.br/livros/livros-de-mitologia-e-folclore
# https://www.kabum.com.br/livros/livros-de-arte-e-fotografia
