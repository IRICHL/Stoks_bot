import requests
import json

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

#Парсим топ падений
losers = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/top-losers?limit=25&offset={i}&spbeOnly=0"

    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        losers[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"losers{cout}.json", "w", encoding="utf-8") as file:
        json.dump(losers, file, indent=4, ensure_ascii=False)
    cout+=1
    losers.clear()

#Парсим топ взлетов
top = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/top-gainers?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        top[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"top{cout}.json", "w", encoding="utf-8") as file:
        json.dump(top, file, indent=4, ensure_ascii=False)
    cout += 1
    top.clear()

#парсим Лучшие акции США
Best_Stoks = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/best?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        Best_Stoks[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"best{cout}.json", "w", encoding="utf-8") as file:
        json.dump(Best_Stoks, file, indent=4, ensure_ascii=False)
    cout += 1
    Best_Stoks.clear()

#Парсим Недооцененные акции
underestimated = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/most-underestimated?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        underestimated[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"underestimated{cout}.json", "w", encoding="utf-8") as file:
        json.dump(underestimated, file, indent=4, ensure_ascii=False)
    cout += 1
    underestimated.clear()

#Парсим Переоцененные акции
overestimated = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/most-overestimated?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        overestimated[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"overestimated{cout}.json", "w", encoding="utf-8") as file:
        json.dump(overestimated, file, indent=4, ensure_ascii=False)
    cout += 1
    overestimated.clear()

#Парсим акции с лучшими дивидентами
top_dividends = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/top-dividends?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        top_dividends[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"top_dividends{cout}.json", "w", encoding="utf-8") as file:
        json.dump(top_dividends, file, indent=4, ensure_ascii=False)
    cout += 1
    top_dividends.clear()

#Самые дешевые
most_cheap = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/most-cheap?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        most_cheap[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"most_cheap{cout}.json", "w", encoding="utf-8") as file:
        json.dump(most_cheap, file, indent=4, ensure_ascii=False)
    cout += 1
    most_cheap.clear()

#Самые дорогие
most_expensive = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/most-expensive?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        most_expensive[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"most_expensive{cout}.json", "w", encoding="utf-8") as file:
        json.dump(most_expensive, file, indent=4, ensure_ascii=False)
    cout += 1
    most_expensive

#С большой капитализацией
big_capitalization = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/big-capitalization?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        big_capitalization[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"big_capitalization{cout}.json", "w", encoding="utf-8") as file:
        json.dump(big_capitalization, file, indent=4, ensure_ascii=False)
    cout += 1
    big_capitalization.clear()

#С малой капитализацие
small_capitalization = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/small-capitalization?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        small_capitalization[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"small_capitalization{cout}.json", "w", encoding="utf-8") as file:
        json.dump(small_capitalization, file, indent=4, ensure_ascii=False)
    cout += 1
    small_capitalization.clear()

#Самые активные
most_traded = {}
cout = 0
for i in range(0, 76, 25):
    url = f"https://beststocks.ru/api/stocks/collections/most-traded?limit=25&offset={i}&spbeOnly=0"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    data_response = json_data["data"]

    for j in range(0, len(data_response)):
        most_traded[data_response[j]['ticker']] = data_response[j]['ticker']

    with open(f"most_traded{cout}.json", "w", encoding="utf-8") as file:
        json.dump(most_traded, file, indent=4, ensure_ascii=False)
    cout += 1
    most_traded.clear()