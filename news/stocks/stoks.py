import requests
from bs4 import BeautifulSoup
import json
import time
from random import randint
from threading import Thread

headers = {
    "accept": "* / *",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

info_all_stoks0 = {}
info_all_stoks1 = {}
info_all_stoks2 = {}
info_all_stoks3 = {}
info_all_stoks4 = {}
info_all_stoks5 = {}


def parse_stok0():
    with open("all_stoks0.json") as file:
        all_stoks = json.load(file)
    for article_name, article_href in all_stoks.items():
        url = article_href
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        try:
            ticker_stok = soup.find(class_="stock-view-company__wrap")
        except:
            ticker_stok = "Нет тикера"
        name_stok = soup.find(class_="stock-view-company__company text-ellipsis")
        price_stok = soup.find(class_="stock-view-info__price-current nobr h4")
        change_price_stok = soup.find(class_="stock-view-info__price-change")
        date_price_stok = soup.find(class_="stock-view-info__desc text-t-md text-grey hidden-by-lg")
        articles_stoks = soup.find(class_="stock-indicators").find_all(class_="indicators-main__text")
        info_all_stoks0[ticker_stok.text.strip()] = {
            "Тикер": ticker_stok.text.strip(),
            "Название акции": name_stok.text.strip(),
            "Стоимость акции": price_stok.text.strip(),
            "Изменение стоимости": change_price_stok.text.strip(),
            "Время информации": date_price_stok.text.strip(),
            "Капитализация компании": articles_stoks[0].text.strip(),
            "P/E": articles_stoks[1].text.strip(),
            "EBITDA": articles_stoks[2].text.strip(),
            "Прибыль на акцию:": articles_stoks[3].text.strip(),
            "Дата следующей отчётности": articles_stoks[4].text.strip(),
            "Дивидендный доход": articles_stoks[5].text.strip()
        }
        slp = randint(1, 4)
        print(slp)
        print("th1")
        time.sleep(slp)
    with open("final_stoks/info_all_stoks0.json", "w", encoding="utf-8") as file:
        json.dump(info_all_stoks0, file, indent=4, ensure_ascii=False)


def parse_stok1():
    with open("all_stoks1.json") as file:
        all_stoks = json.load(file)
    for article_name, article_href in all_stoks.items():
        url = article_href
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        try:
            ticker_stok = soup.find(class_="stock-view-company__wrap")
        except:
            ticker_stok = "Нет тикера"
        name_stok = soup.find(class_="stock-view-company__company text-ellipsis")
        price_stok = soup.find(class_="stock-view-info__price-current nobr h4")
        change_price_stok = soup.find(class_="stock-view-info__price-change")
        date_price_stok = soup.find(class_="stock-view-info__desc text-t-md text-grey hidden-by-lg")
        articles_stoks = soup.find(class_="stock-indicators").find_all(class_="indicators-main__text")
        info_all_stoks1[ticker_stok.text.strip()] = {
            "Тикер": ticker_stok.text.strip(),
            "Название акции": name_stok.text.strip(),
            "Стоимость акции": price_stok.text.strip(),
            "Изменение стоимости": change_price_stok.text.strip(),
            "Время информации": date_price_stok.text.strip(),
            "Капитализация компании": articles_stoks[0].text.strip(),
            "P/E": articles_stoks[1].text.strip(),
            "EBITDA": articles_stoks[2].text.strip(),
            "Прибыль на акцию:": articles_stoks[3].text.strip(),
            "Дата следующей отчётности": articles_stoks[4].text.strip(),
            "Дивидендный доход": articles_stoks[5].text.strip()
        }
        slp = randint(1, 4)
        print(slp)
        print("th2")
        time.sleep(slp)
    with open("final_stoks/info_all_stoks1.json", "w", encoding="utf-8") as file:
        json.dump(info_all_stoks1, file, indent=4, ensure_ascii=False)


def parse_stok2():
    with open("all_stoks2.json") as file:
        all_stoks = json.load(file)
    for article_name, article_href in all_stoks.items():
        url = article_href
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        try:
            ticker_stok = soup.find(class_="stock-view-company__wrap")
        except:
            ticker_stok = "Нет тикера"
        articles_stoks = soup.find(class_="stock-indicators").find_all(class_="indicators-main__text")
        name_stok = soup.find(class_="stock-view-company__company text-ellipsis")
        price_stok = soup.find(class_="stock-view-info__price-current nobr h4")
        change_price_stok = soup.find(class_="stock-view-info__price-change")
        date_price_stok = soup.find(class_="stock-view-info__desc text-t-md text-grey hidden-by-lg")

        info_all_stoks2[ticker_stok.text.strip()] = {
            "Тикер": ticker_stok.text.strip(),
            "Название акции": name_stok.text.strip(),
            "Стоимость акции": price_stok.text.strip(),
            "Изменение стоимости": change_price_stok.text.strip(),
            "Время информации": date_price_stok.text.strip(),
            "Капитализация компании": articles_stoks[0].text.strip(),
            "P/E": articles_stoks[1].text.strip(),
            "EBITDA": articles_stoks[2].text.strip(),
            "Прибыль на акцию:": articles_stoks[3].text.strip(),
            "Дата следующей отчётности": articles_stoks[4].text.strip(),
            "Дивидендный доход": articles_stoks[5].text.strip()
        }
        slp = randint(1, 4)
        print(slp)
        print("th3")
        time.sleep(slp)
    with open("final_stoks/info_all_stoks2.json", "w", encoding="utf-8") as file:
        json.dump(info_all_stoks2, file, indent=4, ensure_ascii=False)


def parse_stok3():
    with open("all_stoks3.json") as file:
        all_stoks = json.load(file)
    for article_name, article_href in all_stoks.items():
        url = article_href
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        try:
            ticker_stok = soup.find(class_="stock-view-company__wrap")
        except:
            ticker_stok = "Нет тикера"
        name_stok = soup.find(class_="stock-view-company__company text-ellipsis")
        price_stok = soup.find(class_="stock-view-info__price-current nobr h4")
        change_price_stok = soup.find(class_="stock-view-info__price-change")
        date_price_stok = soup.find(class_="stock-view-info__desc text-t-md text-grey hidden-by-lg")
        articles_stoks = soup.find(class_="stock-indicators").find_all(class_="indicators-main__text")
        info_all_stoks3[ticker_stok.text.strip()] = {
            "Тикер": ticker_stok.text.strip(),
            "Название акции": name_stok.text.strip(),
            "Стоимость акции": price_stok.text.strip(),
            "Изменение стоимости": change_price_stok.text.strip(),
            "Время информации": date_price_stok.text.strip(),
            "Капитализация компании": articles_stoks[0].text.strip(),
            "P/E": articles_stoks[1].text.strip(),
            "EBITDA": articles_stoks[2].text.strip(),
            "Прибыль на акцию:": articles_stoks[3].text.strip(),
            "Дата следующей отчётности": articles_stoks[4].text.strip(),
            "Дивидендный доход": articles_stoks[5].text.strip()
        }
        slp = randint(1, 4)
        print(slp)
        print("th4")
        time.sleep(slp)
    with open("final_stoks/info_all_stoks3.json", "w", encoding="utf-8") as file:
        json.dump(info_all_stoks3, file, indent=4, ensure_ascii=False)


def parse_stok4():
    with open("all_stoks4.json") as file:
        all_stoks = json.load(file)
    for article_name, article_href in all_stoks.items():
        url = article_href
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        try:
            ticker_stok = soup.find(class_="stock-view-company__wrap")
        except:
            ticker_stok = "Нет тикера"
        name_stok = soup.find(class_="stock-view-company__company text-ellipsis")
        try:
            price_stok = str(soup.find(class_="stock-view-info__price-current nobr h4"))
        except:
            price_stok = str("Нет данных")
        print(price_stok.text)
        change_price_stok = soup.find(class_="stock-view-info__price-change")
        date_price_stok = soup.find(class_="stock-view-info__desc text-t-md text-grey hidden-by-lg")
        articles_stoks = soup.find(class_="stock-indicators").find_all(class_="indicators-main__text")
        info_all_stoks4[ticker_stok.text.strip()] = {
            "Тикер": ticker_stok.text.strip(),
            "Название акции": name_stok.text.strip(),
            "Стоимость акции": price_stok.text.strip(),
            "Изменение стоимости": change_price_stok.text.strip(),
            "Время информации": date_price_stok.text.strip(),
            "Капитализация компании": articles_stoks[0].text.strip(),
            "P/E": articles_stoks[1].text.strip(),
            "EBITDA": articles_stoks[2].text.strip(),
            "Прибыль на акцию:": articles_stoks[3].text.strip(),
            "Дата следующей отчётности": articles_stoks[4].text.strip(),
            "Дивидендный доход": articles_stoks[5].text.strip()
        }
        slp = randint(1, 4)
        print(slp)
        print("th5")
        time.sleep(slp)
    with open("final_stoks/info_all_stoks4.json", "w", encoding="utf-8") as file:
        json.dump(info_all_stoks4, file, indent=4, ensure_ascii=False)


def parse_stok5():
    with open("all_rustoks.json") as file:
        all_stoks = json.load(file)
    for article_name, article_href in all_stoks.items():
        url = article_href
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        ticker_stok = soup.find(class_="rustock-view-company__ticker nobr h2 nuxt-link-exact-active nuxt-link-active")
        name_stok = soup.find(class_="rustock-view-company__company")
        price_stok = soup.find(class_="rustock-view-info__price-current nobr h4")
        change_price_stok = soup.find(class_="rustock-view-info__price-change")
        date_price_stok = soup.find(class_="rustock-view-info__desc text-t-md text-grey hidden-by-lg")
        articles_stoks = soup.find(class_="stock-indicators").find_all(class_="indicators-main__text")
        info_all_stoks5[ticker_stok.text.strip()] = {
            "Тикер": ticker_stok.text.strip(),
            "Название акции": name_stok.text.strip(),
            "Стоимость акции": price_stok.text.strip(),
            "Изменение стоимости": change_price_stok.text.strip(),
            "Время информации": date_price_stok.text.strip(),
            "Капитализация компании": articles_stoks[0].text.strip(),
            "P/E": articles_stoks[1].text.strip(),
            "EBITDA": articles_stoks[2].text.strip(),
            "Прибыль на акцию:": articles_stoks[3].text.strip(),
            "Дата следующей отчётности": articles_stoks[4].text.strip(),
            "Дивидендный доход": articles_stoks[5].text.strip()
        }
        slp = randint(1, 4)
        print(slp)
        print("th6")
        time.sleep(slp)
    with open("final_stoks/info_all_stoks5.json", "w", encoding="utf-8") as file:
        json.dump(info_all_stoks5, file, indent=4, ensure_ascii=False)


t1 = Thread(target=parse_stok0)
t2 = Thread(target=parse_stok1)
t3 = Thread(target=parse_stok2)
t4 = Thread(target=parse_stok3)
t5 = Thread(target=parse_stok4)
t6 = Thread(target=parse_stok5)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
