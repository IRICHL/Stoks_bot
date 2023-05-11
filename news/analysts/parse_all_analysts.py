import requests
from bs4 import BeautifulSoup
import json


headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
#Парсим топ аналитиков
url = "https://beststocks.ru/top-analysts"
r = requests.get(url=url, headers=headers)


soup = BeautifulSoup(r.text, "lxml")
articles_analysts = soup.find(class_="analyst-list__list row").find_all("a", class_="expert-person__link h5")
company_analysts = soup.find(class_="analyst-list__list row").find_all(class_="expert__company text-grey text-ellipsis")
yield_analysts = soup.find(class_="analyst-list__list row").find_all(class_="expert__text text-sm text-green")
index_analysts = soup.find(class_="analyst-list__list row").find_all(class_="expert__text text-sm")

best_analysts = {}
for analysts in articles_analysts:
    analysts_name = analysts.text
    analysts_href = "https://beststocks.ru" + analysts.get("href")

    best_analysts[analysts_name.strip()] = analysts_href

with open("top_analysts.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()

for analysts in range(0, len(articles_analysts)):
    best_analysts[articles_analysts[analysts].text.strip()] = {
        "Компания": company_analysts[analysts].text.strip(),
        "Доходность": yield_analysts[analysts].text.strip(),
        "Индекс успеха": index_analysts[analysts].text.strip()
    }
with open("Itop_analysts.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()

#Парсим топ блогеров
url = "https://beststocks.ru/top-bloggers"
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
articles_analysts = soup.find(class_="blogger-list__list row").find_all("a", class_="expert-person__link h5")
company_analysts = soup.find(class_="blogger-list__list row").find_all(class_="expert__company text-grey text-ellipsis")
yield_analysts = soup.find(class_="blogger-list__list row").find_all(class_="expert__text text-sm text-green")
index_analysts = soup.find(class_="blogger-list__list row").find_all(class_="expert__text text-sm")

for analysts in articles_analysts:
    analysts_name = analysts.text
    analysts_href = "https://beststocks.ru" + analysts.get("href")

    best_analysts[analysts_name.strip()] = analysts_href

with open("top-bloggers.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()

for analysts in range(0, len(articles_analysts)):
    best_analysts[articles_analysts[analysts].text.strip()] = {
        "Компания": company_analysts[analysts].text.strip(),
        "Доходность": yield_analysts[analysts].text.strip(),
        "Индекс успеха": index_analysts[analysts].text.strip()
    }
with open("Itop-bloggers.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()

#Парсим инсайдеров
url = "https://beststocks.ru/top-insiders"
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
articles_analysts = soup.find(class_="insider-list__list row").find_all("a", class_="expert-person__link h5")
company_analysts = soup.find(class_="insider-list__list row").find_all(class_="expert__company text-grey text-ellipsis")
yield_analysts = soup.find(class_="insider-list__list row").find_all(class_="expert__text text-sm text-green")
index_analysts = soup.find(class_="insider-list__list row").find_all(class_="expert__text text-sm")

for analysts in articles_analysts:
    analysts_name = analysts.text
    analysts_href = "https://beststocks.ru" + analysts.get("href")

    best_analysts[analysts_name.strip()] = analysts_href

with open("top-insiders.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()

for analysts in range(0, len(articles_analysts)):
    best_analysts[articles_analysts[analysts].text.strip()] = {
        "Компания": company_analysts[analysts].text.strip(),
        "Доходность": yield_analysts[analysts].text.strip(),
        "Индекс успеха": index_analysts[analysts].text.strip()
    }
with open("Itop-insiders.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()

#
url = "https://beststocks.ru/top-hedge-funds"
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
articles_analysts = soup.find(class_="hedge-fund-experts-list__list row").find_all("a", class_="expert-person__link h5")

for analysts in articles_analysts:
    analysts_name = analysts.text
    analysts_href = "https://beststocks.ru" + analysts.get("href")

    best_analysts[analysts_name.strip()] = analysts_href

with open("top-hedge-funds.json", "w") as file:
    json.dump(best_analysts, file, indent=4, ensure_ascii=False)
best_analysts.clear()
