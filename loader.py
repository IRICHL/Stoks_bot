from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import json
from data.config import BOT_TOKEN
from db import Database

bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('database.db')


with open("news/analysts/t-analysts/top_analysts0.json", encoding="utf-8") as file:
    top_analysts0 = json.load(file)
with open("news/analysts/t-analysts/top_analysts1.json", encoding="utf-8") as file:
    top_analysts1 = json.load(file)
with open("news/analysts/t-analysts/top_analysts2.json", encoding="utf-8") as file:
    top_analysts2 = json.load(file)
with open("news/analysts/t-analysts/top_analysts3.json", encoding="utf-8") as file:
    top_analysts3 = json.load(file)
with open("news/analysts/t-analysts/top_analysts4.json", encoding="utf-8") as file:
    top_analysts4 = json.load(file)
with open("news/analysts/t-analysts/top_analysts5.json", encoding="utf-8") as file:
    top_analysts5 = json.load(file)
with open("news/analysts/t-analysts/top_analysts6.json", encoding="utf-8") as file:
    top_analysts6 = json.load(file)
with open("news/analysts/t-analysts/top_analysts7.json", encoding="utf-8") as file:
    top_analysts7 = json.load(file)
with open("news/analysts/t-analysts/top_analysts8.json", encoding="utf-8") as file:
    top_analysts8 = json.load(file)
with open("news/analysts/t-analysts/top_analysts9.json", encoding="utf-8") as file:
    top_analysts9 = json.load(file)
with open("news/analysts/t-analysts/top_analysts10.json", encoding="utf-8") as file:
    top_analysts10 = json.load(file)
with open("news/analysts/t-analysts/top_analysts11.json", encoding="utf-8") as file:
    top_analysts11 = json.load(file)
with open("news/analysts/t-analysts/top_analysts12.json", encoding="utf-8") as file:
    top_analysts12 = json.load(file)
with open("news/analysts/t-analysts/top_analysts13.json", encoding="utf-8") as file:
    top_analysts13 = json.load(file)
with open("news/analysts/t-analysts/top_analysts14.json", encoding="utf-8") as file:
    top_analysts14 = json.load(file)
with open("news/analysts/t-analysts/top_analysts15.json", encoding="utf-8") as file:
    top_analysts15 = json.load(file)
with open("news/analysts/t-analysts/top_analysts16.json", encoding="utf-8") as file:
    top_analysts16 = json.load(file)
with open("news/analysts/t-analysts/top_analysts17.json", encoding="utf-8") as file:
    top_analysts17 = json.load(file)
with open("news/analysts/t-analysts/top_analysts18.json", encoding="utf-8") as file:
    top_analysts18 = json.load(file)
with open("news/analysts/t-analysts/top_analysts19.json", encoding="utf-8") as file:
    top_analysts19 = json.load(file)
with open("news/analysts/t-analysts/top_analysts20.json", encoding="utf-8") as file:
    top_analysts20 = json.load(file)
with open("news/analysts/t-analysts/top_analysts21.json", encoding="utf-8") as file:
    top_analysts21 = json.load(file)
with open("news/analysts/t-analysts/top_analysts22.json", encoding="utf-8") as file:
    top_analysts22 = json.load(file)
with open("news/analysts/t-analysts/top_analysts23.json", encoding="utf-8") as file:
    top_analysts23 = json.load(file)
with open("news/analysts/t-analysts/top_analysts24.json", encoding="utf-8") as file:
    top_analysts24 = json.load(file)

with open("news/analysts/t-bloggers/top_bloggers0.json", encoding="utf-8") as file:
    top_bloggers0 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers1.json", encoding="utf-8") as file:
    top_bloggers1 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers2.json", encoding="utf-8") as file:
    top_bloggers2 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers3.json", encoding="utf-8") as file:
    top_bloggers3 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers4.json", encoding="utf-8") as file:
    top_bloggers4 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers5.json", encoding="utf-8") as file:
    top_bloggers5 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers6.json", encoding="utf-8") as file:
    top_bloggers6 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers7.json", encoding="utf-8") as file:
    top_bloggers7 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers8.json", encoding="utf-8") as file:
    top_bloggers8 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers9.json", encoding="utf-8") as file:
    top_bloggers9 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers10.json", encoding="utf-8") as file:
    top_bloggers10 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers11.json", encoding="utf-8") as file:
    top_bloggers11 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers12.json", encoding="utf-8") as file:
    top_bloggers12 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers13.json", encoding="utf-8") as file:
    top_bloggers13 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers14.json", encoding="utf-8") as file:
    top_bloggers14 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers15.json", encoding="utf-8") as file:
    top_bloggers15 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers16.json", encoding="utf-8") as file:
    top_bloggers16 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers17.json", encoding="utf-8") as file:
    top_bloggers17 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers18.json", encoding="utf-8") as file:
    top_bloggers18 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers19.json", encoding="utf-8") as file:
    top_bloggers19 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers20.json", encoding="utf-8") as file:
    top_bloggers20 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers21.json", encoding="utf-8") as file:
    top_bloggers21 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers22.json", encoding="utf-8") as file:
    top_bloggers22 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers23.json", encoding="utf-8") as file:
    top_bloggers23 = json.load(file)
with open("news/analysts/t-bloggers/top_bloggers24.json", encoding="utf-8") as file:
    top_bloggers24 = json.load(file)

with open("news/analysts/t-insiders/top_insiders0.json", encoding="utf-8") as file:
    top_insiders0 = json.load(file)
with open("news/analysts/t-insiders/top_insiders1.json", encoding="utf-8") as file:
    top_insiders1 = json.load(file)
with open("news/analysts/t-insiders/top_insiders2.json", encoding="utf-8") as file:
    top_insiders2 = json.load(file)
with open("news/analysts/t-insiders/top_insiders3.json", encoding="utf-8") as file:
    top_insiders3 = json.load(file)
with open("news/analysts/t-insiders/top_insiders4.json", encoding="utf-8") as file:
    top_insiders4 = json.load(file)
with open("news/analysts/t-insiders/top_insiders5.json", encoding="utf-8") as file:
    top_insiders5 = json.load(file)
with open("news/analysts/t-insiders/top_insiders6.json", encoding="utf-8") as file:
    top_insiders6 = json.load(file)
with open("news/analysts/t-insiders/top_insiders7.json", encoding="utf-8") as file:
    top_insiders7 = json.load(file)
with open("news/analysts/t-insiders/top_insiders8.json", encoding="utf-8") as file:
    top_insiders8 = json.load(file)
with open("news/analysts/t-insiders/top_insiders9.json", encoding="utf-8") as file:
    top_insiders9 = json.load(file)
with open("news/analysts/t-insiders/top_insiders10.json", encoding="utf-8") as file:
    top_insiders10 = json.load(file)
with open("news/analysts/t-insiders/top_insiders11.json", encoding="utf-8") as file:
    top_insiders11 = json.load(file)
with open("news/analysts/t-insiders/top_insiders12.json", encoding="utf-8") as file:
    top_insiders12 = json.load(file)
with open("news/analysts/t-insiders/top_insiders13.json", encoding="utf-8") as file:
    top_insiders13 = json.load(file)
with open("news/analysts/t-insiders/top_insiders14.json", encoding="utf-8") as file:
    top_insiders14 = json.load(file)
with open("news/analysts/t-insiders/top_insiders15.json", encoding="utf-8") as file:
    top_insiders15 = json.load(file)
with open("news/analysts/t-insiders/top_insiders16.json", encoding="utf-8") as file:
    top_insiders16 = json.load(file)
with open("news/analysts/t-insiders/top_insiders17.json", encoding="utf-8") as file:
    top_insiders17 = json.load(file)
with open("news/analysts/t-insiders/top_insiders18.json", encoding="utf-8") as file:
    top_insiders18 = json.load(file)
with open("news/analysts/t-insiders/top_insiders19.json", encoding="utf-8") as file:
    top_insiders19 = json.load(file)
with open("news/analysts/t-insiders/top_insiders20.json", encoding="utf-8") as file:
    top_insiders20 = json.load(file)
with open("news/analysts/t-insiders/top_insiders21.json", encoding="utf-8") as file:
    top_insiders21 = json.load(file)
with open("news/analysts/t-insiders/top_insiders22.json", encoding="utf-8") as file:
    top_insiders22 = json.load(file)
with open("news/analysts/t-insiders/top_insiders23.json", encoding="utf-8") as file:
    top_insiders23 = json.load(file)
with open("news/analysts/t-insiders/top_insiders24.json", encoding="utf-8") as file:
    top_insiders24 = json.load(file)


with open("news/analysts/Itop-bloggers.json") as file:
    top_bloggers = json.load(file)
with open("news/analysts/Itop_analysts.json") as file:
    top_analysts = json.load(file)
with open("news/analysts/Itop-insiders.json") as file:
    top_insiders = json.load(file)

with open("news/stocks/best0.json") as file:
    best0 = json.load(file)
with open("news/stocks/best1.json") as file:
    best1 = json.load(file)
with open("news/stocks/best2.json") as file:
    best2 = json.load(file)
with open("news/stocks/best3.json") as file:
    best3 = json.load(file)

with open("news/stocks/big_capitalization0.json") as file:
    big_capitalization0 = json.load(file)
with open("news/stocks/big_capitalization1.json") as file:
    big_capitalization1 = json.load(file)
with open("news/stocks/big_capitalization2.json") as file:
    big_capitalization2 = json.load(file)
with open("news/stocks/big_capitalization3.json") as file:
    big_capitalization3 = json.load(file)

with open("news/stocks/losers0.json") as file:
    losers0 = json.load(file)
with open("news/stocks/losers1.json") as file:
    losers1 = json.load(file)
with open("news/stocks/losers2.json") as file:
    losers2 = json.load(file)
with open("news/stocks/losers3.json") as file:
    losers3 = json.load(file)

with open("news/stocks/most_cheap0.json") as file:
    most_cheap0 = json.load(file)
with open("news/stocks/most_cheap1.json") as file:
    most_cheap1 = json.load(file)
with open("news/stocks/most_cheap2.json") as file:
    most_cheap2 = json.load(file)
with open("news/stocks/most_cheap3.json") as file:
    most_cheap3 = json.load(file)

with open("news/stocks/most_expensive0.json") as file:
    most_expensive0 = json.load(file)
with open("news/stocks/most_expensive1.json") as file:
    most_expensive1 = json.load(file)
with open("news/stocks/most_expensive2.json") as file:
    most_expensive2 = json.load(file)
with open("news/stocks/most_expensive3.json") as file:
    most_expensive3 = json.load(file)

with open("news/stocks/most_traded0.json") as file:
    most_traded0 = json.load(file)
with open("news/stocks/most_traded1.json") as file:
    most_traded1 = json.load(file)
with open("news/stocks/most_traded2.json") as file:
    most_traded2 = json.load(file)
with open("news/stocks/most_traded3.json") as file:
    most_traded3 = json.load(file)

with open("news/stocks/overestimated0.json") as file:
    overestimated0 = json.load(file)
with open("news/stocks/overestimated1.json") as file:
    overestimated1 = json.load(file)
with open("news/stocks/overestimated2.json") as file:
    overestimated2 = json.load(file)
with open("news/stocks/overestimated3.json") as file:
    overestimated3 = json.load(file)

with open("news/stocks/small_capitalization0.json") as file:
    small_capitalization0 = json.load(file)
with open("news/stocks/small_capitalization1.json") as file:
    small_capitalization1 = json.load(file)
with open("news/stocks/small_capitalization2.json") as file:
    small_capitalization2 = json.load(file)
with open("news/stocks/small_capitalization3.json") as file:
    small_capitalization3 = json.load(file)

with open("news/stocks/top0.json") as file:
    top0 = json.load(file)
with open("news/stocks/top1.json") as file:
    top1 = json.load(file)
with open("news/stocks/top2.json") as file:
    top2 = json.load(file)
with open("news/stocks/top3.json") as file:
    top3 = json.load(file)

with open("news/stocks/top_dividends0.json") as file:
    top_dividends0 = json.load(file)
with open("news/stocks/top_dividends1.json") as file:
    top_dividends1 = json.load(file)
with open("news/stocks/top_dividends2.json") as file:
    top_dividends2 = json.load(file)
with open("news/stocks/top_dividends3.json") as file:
    top_dividends3 = json.load(file)

with open("news/stocks/underestimated0.json") as file:
    underestimated0 = json.load(file)
with open("news/stocks/underestimated1.json") as file:
    underestimated1 = json.load(file)
with open("news/stocks/underestimated2.json") as file:
    underestimated2 = json.load(file)
with open("news/stocks/underestimated3.json") as file:
    underestimated3 = json.load(file)

with open("news/stocks/final_stoks/info_all_stoks0.json", encoding="utf-8") as file:
    info_all_stoks0 = json.load(file)
with open("news/stocks/final_stoks/info_all_stoks1.json", encoding="utf-8") as file:
    info_all_stoks1 = json.load(file)
with open("news/stocks/final_stoks/info_all_stoks2.json", encoding="utf-8") as file:
    info_all_stoks2 = json.load(file)
with open("news/stocks/final_stoks/info_all_stoks3.json", encoding="utf-8") as file:
    info_all_stoks3 = json.load(file)
with open("news/stocks/final_stoks/info_all_stoks4.json", encoding="utf-8") as file:
    info_all_stoks4 = json.load(file)
with open("news/stocks/final_stoks/info_all_stoks5.json", encoding="utf-8") as file:
    info_all_stoks5 = json.load(file)

info_all_stoks = {**info_all_stoks0, **info_all_stoks1, **info_all_stoks2, **info_all_stoks3, **info_all_stoks4,
                  **info_all_stoks5}

if __name__ == "__main__":
    from app import on_startup
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
