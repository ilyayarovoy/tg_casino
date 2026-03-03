import asyncio
from database.session import engine
from database.base import Base

# Импорт таблиц БД!
from database.models import users

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_db())