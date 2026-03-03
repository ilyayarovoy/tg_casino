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


