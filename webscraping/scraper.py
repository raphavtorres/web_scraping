from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FastShopScraper:
    def __init__(self) -> None:
        self.url = "https://www.fastshop.com.br/web/c/4611686018425#PHONE#"
        self.map = {
            "title": {
                'xpath': "/html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[#counter#]/div/a/div[3]/h3"
            },
            "price": {
                'xpath': "/html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[#counter#]/div/a/div[3]/div[2]/app-price-v2/div/div[2]/span[1]"
            }
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_site(self, phone=""):
        self.driver.get(self.url.replace('#phone#', phone))
        sleep(5)
        print("========== YEAR:", phone, "==========")
        # self.get_numbers(phone)


# ((IPHONE))
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[1]/div/a/div[3]/h3   
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[1]/div/a/div[3]/div[2]/p ((no price))

# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[2]/div/a/div[3]/h3
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[2]/div/a/div[3]/div[2]/p ((no price))

# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[3]/div/a/div[3]/h3
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[3]/div/a/div[3]/div[2]/app-price-v2/div/div[2]/span[1]  ((with price))

# ---------------------
# ((MOTOROLA))
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[1]/div/a/div[3]/h3
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[1]/div/a/div[3]/div[2]/app-price-v2/div/div[2%]/span[1]
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[1%]/div/a/div[3]/div[2]/app-price-v2/div/div[3%]/div

# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[2%]/div/a/div[3]/h3
# /html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[2%]/div/a/div[3]/div[2]/app-price-v2/div/div[1]/span[1]


# ---------------------

# https://www.fastshop.com.br/web/c/4611686018425  -  061003/samsung_galaxy
# https://www.fastshop.com.br/web/c/4611686018425  -  486503/iphone_
# https://www.fastshop.com.br/web/c/4611686018425  -  153535/motorola_moto
# https://www.fastshop.com.br/web/c/4611686018425  -  049504/zenfone_asus
# https://www.fastshop.com.br/web/c/4611686018425  -  159013/lg_smartphone
# https://www.fastshop.com.br/web/c/4611686018425  -  429004/xiaomi
# https://www.fastshop.com.br/web/c/4611686018425  -  494009/grupo_infinix
# https://www.fastshop.com.br/web/c/4611686018425  -  494008/grupo_positivo
