from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Акции")
        ],
        [
            KeyboardButton(text="Лучшие эксперты")
        ],
        [
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

markup_stoks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лучшие акции США")
        ],
        [
            KeyboardButton(text="Лидеры роста"),
            KeyboardButton(text="Лидеры падения")
        ],
        [
            KeyboardButton(text="Недооцененные"),
            KeyboardButton(text="Переоцененные")
        ],
        [
            KeyboardButton(text="Самые дешёвые"),
            KeyboardButton(text="Самые дорогие")
        ],
        [
            KeyboardButton(text="С большой капитализацией"),
            KeyboardButton(text="С малой капитализацией")
        ],
        [
            KeyboardButton(text="Лучшие дивиденды"),
            KeyboardButton(text="Самые активные")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]

    ],
    resize_keyboard=True
)

best = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лучшие акции США 1-25")
        ],
        [
            KeyboardButton(text="Лучшие акции США 26-50")
        ],
        [
            KeyboardButton(text="Лучшие акции США 51-75")
        ],
        [
            KeyboardButton(text="Лучшие акции США 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

big_capitalization = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="С большой капитализацией 1-25")
        ],
        [
            KeyboardButton(text="С большой капитализацией 26-50")
        ],
        [
            KeyboardButton(text="С большой капитализацией 51-75")
        ],
        [
            KeyboardButton(text="С большой капитализацией 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

small_capitalization = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="С малой капитализацией 1-25")
        ],
        [
            KeyboardButton(text="С малой капитализацией 26-50")
        ],
        [
            KeyboardButton(text="С малой капитализацией 51-75")
        ],
        [
            KeyboardButton(text="С малой капитализацией 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

losers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лидеры падения 1-25")
        ],
        [
            KeyboardButton(text="Лидеры падения 26-50")
        ],
        [
            KeyboardButton(text="Лидеры падения 51-75")
        ],
        [
            KeyboardButton(text="Лидеры падения 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

most_cheap = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Самые дешёвые 1-25")
        ],
        [
            KeyboardButton(text="Самые дешёвые 26-50")
        ],
        [
            KeyboardButton(text="Самые дешёвые 51-75")
        ],
        [
            KeyboardButton(text="Самые дешёвые 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

most_expensive = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Самые дорогие 1-25")
        ],
        [
            KeyboardButton(text="Самые дорогие 26-50")
        ],
        [
            KeyboardButton(text="Самые дорогие 51-75")
        ],
        [
            KeyboardButton(text="Самые дорогие 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

most_traded = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Самые активные 1-25")
        ],
        [
            KeyboardButton(text="Самые активные 26-50")
        ],
        [
            KeyboardButton(text="Самые активные 51-75")
        ],
        [
            KeyboardButton(text="Самые активные 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

overestimated = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Переоцененные 1-25")
        ],
        [
            KeyboardButton(text="Переоцененные 26-50")
        ],
        [
            KeyboardButton(text="Переоцененные 51-75")
        ],
        [
            KeyboardButton(text="Переоцененные 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

top = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лидеры роста 1-25")
        ],
        [
            KeyboardButton(text="Лидеры роста 26-50")
        ],
        [
            KeyboardButton(text="Лидеры роста 51-75")
        ],
        [
            KeyboardButton(text="Лидеры роста 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

top_dividends = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лучшие дивиденды 1-25")
        ],
        [
            KeyboardButton(text="Лучшие дивиденды 26-50")
        ],
        [
            KeyboardButton(text="Лучшие дивиденды 51-75")
        ],
        [
            KeyboardButton(text="Лучшие дивиденды 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

underestimated = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Недооцененные 1-25")
        ],
        [
            KeyboardButton(text="Недооцененные 26-50")
        ],
        [
            KeyboardButton(text="Недооцененные 51-75")
        ],
        [
            KeyboardButton(text="Недооцененные 76-100")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]
    ],
    resize_keyboard=True
)

best_experts = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="25 лучших аналитиков")
        ],
        [
            KeyboardButton(text="25 лучших финансовых блогеров")
        ],
        [
            KeyboardButton(text="25 лучших инсайдеров")
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Закрыть меню")
        ]

    ],
    resize_keyboard=True
)