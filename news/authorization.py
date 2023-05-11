from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from data.config import email,password
import requests
from random import randint
from bs4 import BeautifulSoup
import json
import pickle
import time
def auth():
    url = "https://beststocks.ru/login"
    ser = Service("C:\\Users\\Данил\\Desktop\\Python\\bot\\news\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=ser, options=options)

    try:
        driver.get(url=url)
        time.sleep(5)

        email_input = driver.find_element(By.ID, "user-email")
        email_input.clear()
        email_input.send_keys(email)
        time.sleep(randint(5,7))

        password_input = driver.find_element(By.ID, "user-password")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(randint(3,5))
        password_input.send_keys(Keys.ENTER)
        #login_button = driver.find_element(By.CLASS_NAME, "button").click()
        time.sleep(randint(5,7))

        driver.get("https://beststocks.ru/smart-score")
        st = []

                                                                               # Smart-score
        for i in range(0,11):

             time.sleep(10)
             src = driver.page_source

             soup = BeautifulSoup(src, "lxml")
             ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")
             for item in ticker_stok:
                 st.append(item.text.strip())

             next = driver.find_element(By.CLASS_NAME, "pagination__img-next").click()

        with open("smart-score.json", "w", encoding="utf-8") as file:
             json.dump(st, file, indent=4, ensure_ascii=False)
        st.clear()

                                                                              #Лучшие акции аналитиков
        driver.get("https://beststocks.ru/best")
        for i in range(0,33):

            time.sleep(10)
            src = driver.page_source

            soup = BeautifulSoup(src, "lxml")
            ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")
            for item in ticker_stok:
                st.append(item.text.strip())

            next = driver.find_element(By.CLASS_NAME, "pagination__img-next").click()

        with open("best-stoks-analisyts.json", "w", encoding="utf-8") as file:
             json.dump(st, file, indent=4, ensure_ascii=False)

                                                                             #Акции в тренде
        trending = {}
        driver.get("https://beststocks.ru/trending")
        for i in range(0,4):

            time.sleep(10)
            src = driver.page_source

            soup = BeautifulSoup(src, "lxml")
            ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")
            konsensus = soup.find(class_="table-wrap__content").find_all(class_="table-consensus")

            for j in range(0, len(ticker_stok)):
                trending[ticker_stok[j].text.strip()] = {
                    "Тикер": ticker_stok[j].text.strip(),
                    "Консенсус": konsensus[j].text.strip()
                }
            next = driver.find_element(By.CLASS_NAME, "pagination__img-next").click()

        with open("trendin.json", "w", encoding="utf-8") as file:
            json.dump(trending, file, indent=4, ensure_ascii=False)

                                                                             #Рекомендации по акциям
        driver.get("https://beststocks.ru/recommendations")
        recom = {}
        for i in range(0,6):
            time.sleep(10)
            src = driver.page_source

            soup = BeautifulSoup(src, "lxml")
            rating = soup.find(class_="table-wrap__content").find_all(class_="table-rating")
            name = soup.find(class_="table-wrap__content").find_all(class_="table-expert__name text-ellipsis")
            company = soup.find(class_="table-wrap__content").find_all(class_="table-expert__company text-ellipsis text-grey")
            success = soup.find(class_="table-wrap__content").find_all(class_="table-progress")
            rec = soup.find(class_="table-wrap__content").find_all(class_="table-expert-recommendation")
            ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")

            for j in range(0, len(rating)):
                recom[ticker_stok[j].text.strip()] = {
                    "Рейтинг": rating[j].text.strip(),
                    "Имя": name[j].text.strip(),
                    "Компания": company[j].text.strip(),
                    "Успех": success[j].text.strip(),
                    "Рекомендация": rec[j].text.strip(),
                    "Тикер": ticker_stok[j].text.strip()
                }
            next = driver.find_element(By.CLASS_NAME, "pagination__img-next").click()

        with open("recom.json", "w", encoding="utf-8") as file:
            json.dump(recom, file, indent=4, ensure_ascii=False)
                                                                               #Топ-аналитиков
        with open("analysts/top_analysts.json", encoding="utf-8") as file:
            top_analysts = json.load(file)
        prog = []
        g = 0
        for item in top_analysts:
            driver.get(top_analysts[item])
            time.sleep(10)
            src = driver.page_source

            soup = BeautifulSoup(src, "lxml")
            ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")
            rec = soup.find(class_="table-wrap__content").find_all(class_="table-expert-recommendation")
            date = soup.find(class_="table-wrap__content").find("tbody").find_all(class_="nobr")
            k=2
            for j in range(0, len(ticker_stok)):
                prog.append({
                    "Тикер": ticker_stok[j].text.strip(),
                    "Рекомендация": rec[j].text.strip(),
                    "Дата": date[j+k].text.strip()
                })
                k=k+2

            with open(f"analysts/t-analysts/top_analysts{g}.json", "w", encoding="utf-8") as file:
                json.dump(prog, file, indent=4, ensure_ascii=False)
            prog.clear()
            g += 1
                                                                               #Топ-блоггеров
        with open("analysts/top-bloggers.json", encoding="utf-8") as file:
            top_bloggers = json.load(file)
        g = 0
        for item in top_bloggers:
            driver.get(top_bloggers[item])
            time.sleep(10)
            src = driver.page_source

            soup = BeautifulSoup(src, "lxml")
            ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")
            rec = soup.find(class_="table-wrap__content").find_all(class_="table-expert-recommendation")
            date = soup.find(class_="table-wrap__content").find("tbody").find_all(class_="text-ellipsis")
            for j in range(0, len(ticker_stok)):
                prog.append({
                    "Тикер": ticker_stok[j].text.strip(),
                    "Рекомендация": rec[j].text.strip(),
                    "Дата": date[j].text.strip()
                })

            with open(f"analysts/t-bloggers/top_bloggers{g}.json", "w", encoding="utf-8") as file:
                json.dump(prog, file, indent=4, ensure_ascii=False)
            prog.clear()
            g += 1
                                                                                #Топ-инсайдеров
        with open("analysts/top-insiders.json", encoding="utf-8") as file:
            top_insiders = json.load(file)
        g = 0
        for item in top_insiders:
            driver.get(top_insiders[item])
            time.sleep(10)
            src = driver.page_source

            soup = BeautifulSoup(src, "lxml")
            ticker_stok = soup.find(class_="table-wrap__content").find_all(class_="stock__ticker nobr")
            rec = soup.find(class_="table-wrap__content").find_all(class_="table-insider-action")
            date = soup.find(class_="table-wrap__content").find("tbody").find_all(class_="nobr")
            k = -1
            kk = 0
            for j in range(0, len(ticker_stok)):
                k = k + 3
                kk = kk + 3
                prog.append({
                    "Тикер": ticker_stok[j].text.strip(),
                    "Рекомендация": rec[j].text.strip(),
                    "Сумма": date[j+k].text.strip(),
                    "Дата": date[j+kk].text.strip()
                })

            with open(f"analysts/t-insiders/top_insiders{g}.json", "w", encoding="utf-8") as file:
                json.dump(prog, file, indent=4, ensure_ascii=False)
            prog.clear()
            g+=1

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__=='__main__':
    auth()