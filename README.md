# 🎮 Telegram Bot — Игры и Профиль

Это Telegram-бот, который позволяет пользователям управлять своим **балансом** и играть в мини-игры прямо в чате.

В боте есть:  
- **Профиль** — просмотр баланса, пополнение и вывод средств  
- **Игры** — три мини-игры:  
  1. 50/50  
  2. Кости  
  3. Русская рулетка  

---

## 🛠 Технологии

- Python 3.10+  
- [aiogram 3](https://docs.aiogram.dev/en/latest/) — библиотека для Telegram-бота  
- SQLAlchemy (асинхронная работа с базой данных)  
- Асинхронная база данных (SQLite)  

---

## ⚙️ Установка


1. Клонируем репозиторий:


git clone <your-repo-url>
cd <project-folder>

2. Создаем и активируем виртуальное окружение:
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate

3. Устанавливаем зависимости:
pip install -r requirements.txt

4. Создаем .env файл и добавляем токен бота и базу данных:
BOT_TOKEN=ваш_токен_бота
DATABASE_URL=sqlite+aiosqlite:///./bot.db

project/
│
├─ app/
│   ├─ routers/
│   │   ├─ start.py                # Стартовые команды / меню
│   │   ├─ profile.py              # Профиль пользователя
│   │   └─ games/                  # Игры
│   │       ├─ fifty_fifty_play.py
│   │       ├─ dice_play.py
│   │       └─ russian_roullete_play.py
│   │
│   ├─ service/
│   │   └─ user_service.py         # Логика управления пользователем и балансом
│   │
│   ├─ repositories/
│   │   └─ user_repo.py            # Работа с базой данных
│   │
│   ├─ keyboards/                  # Инлайн-кнопки для игр и меню
│   │   ├─ menu_keyboard.py
│   │   └─ games/
│   │       ├─ fifty_fifty.py
│   │       ├─ dice_keyboard.py
│   │       └─ russian_roulette_keyboard.py
│   │
│   └─ states/                     # FSM для депозита/вывода и игр
│       ├─ deposit_state.py
│       └─ withdraw_state.py
│
├─ database/
│   ├─ models/
│   │   └─ users.py
│   └─ session.py
│
├─ main.py                         # Точка входа
└─ requirements.txt
