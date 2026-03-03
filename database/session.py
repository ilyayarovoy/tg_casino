from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)