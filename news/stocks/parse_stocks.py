import requests
from bs4 import BeautifulSoup
import json


def get_all_url():
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    # Достаем популярные зарубежные акции
    url = "https://beststocks.ru/stocks"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_stoks = soup.find(class_="stocks-list").find("ul").find_all("a")

    popular_stoks = {}
    for article in articles_stoks:
        article_name = article.text
        article_href = article.text

        popular_stoks[article_name.strip()] = article_href.strip()
    # Достаем популярные Российские акции
    url = "https://beststocks.ru/stocks/ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_stoks = soup.find(class_="stocks-list").find("ul").find_all("a")

    for article in articles_stoks:
        article_name = article.text
        article_href = article.text

        popular_stoks[article_name.strip()] = article_href.strip()
    # записываем популярные акции в файл
    with open("all_popular_stoks.json", "w") as file:
        json.dump(popular_stoks, file, indent=4, ensure_ascii=False)

    eng = {}
    all_stoks = {}
    num_tick = {}
    num = 0
    # Достаем все зарубежные акции акции
    for i in range(97, 123):
        eng[chr(i)] = 'https://beststocks.ru/stocks/letter-' + chr(i)
        url = eng[chr(i)]
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        articles_stoks = soup.find(class_="stocks-list").find("ul").find_all("a")

        for article in articles_stoks:
            article_name = article.text
            article_href = "https://beststocks.ru" + article.get("href")

            all_stoks[article_name.strip()] = article_href
            num_tick[article_name.strip()] = num
            num += 1
    # Достаем все Российские акции акции
    rus = {}
    all_rustoks = {}
    for i in range(1072, 1081):
        rus[chr(i)] = 'https://beststocks.ru/stocks/ru/letter-' + chr(i)
        url = rus[chr(i)]
        req = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(req.text, "lxml")
        articles_stoks = soup.find(class_="stocks-list").find("ul").find_all("a")

        for article in articles_stoks:
            article_name = article.text
            article_href = "https://beststocks.ru" + article.get("href")

            all_rustoks[article_name.strip()] = article_href
            num_tick[article_name.strip()] = num
            num += 1

    for i in range(1082, 1098):
        rus[chr(i)] = 'https://beststocks.ru/stocks/ru/letter-' + chr(i)
        url = rus[chr(i)]
        req = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(req.text, "lxml")
        articles_stoks = soup.find(class_="stocks-list").find("ul").find_all("a")

        for article in articles_stoks:
            article_name = article.text
            article_href = "https://beststocks.ru" + article.get("href")

            all_rustoks[article_name.strip()] = article_href
            num_tick[article_name.strip()] = num
            num += 1

    for i in range(1101, 1104):
        rus[chr(i)] = 'https://beststocks.ru/stocks/ru/letter-' + chr(i)
        url = rus[chr(i)]
        req = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(req.text, "lxml")
        articles_stoks = soup.find(class_="stocks-list").find("ul").find_all("a")

        for article in articles_stoks:
            article_name = article.text
            article_href = "https://beststocks.ru" + article.get("href")

            all_rustoks[article_name.strip()] = article_href
            num_tick[article_name.strip()] = num
            num += 1

    count = 0
    value = 0
    stoks = {}

    for article_name, article_href in all_stoks.items():
        stoks[article_name] = article_href
        num_tick[article_name] = value
        value += 1
        if value == 2500:
            stoks[article_name] = article_href
            with open(f"all_stoks{count}.json", "w") as file:
                json.dump(stoks, file, indent=4, ensure_ascii=False)
            count += 1
            stoks.clear()
            value = 0
    with open(f"num_tick.json", "w") as file:
        json.dump(num_tick, file, indent=4, ensure_ascii=False)
    with open(f"all_stoks{count}.json", "w") as file:
        json.dump(stoks, file, indent=4, ensure_ascii=False)
    with open(f"all_rustoks.json", "w") as file:
        json.dump(all_rustoks, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_all_url()