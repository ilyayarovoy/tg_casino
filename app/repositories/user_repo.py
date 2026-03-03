from database.session import async_session
from sqlalchemy import select
from database.models.users import User

class UserRepository:

    @staticmethod
    async def get_user_by_id(telegram_id):
        async with async_session() as session:
            stmt = select(User).where(User.telegram_id == telegram_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    @staticmethod
    async def add_user_to_database(telegram_id: int, firstname: str, lastname: str, balance: float):
        async with async_session() as session:
            new_user = User(telegram_id=telegram_id, firstname=firstname, lastname=lastname, balance=balance)
            session.add(new_user)
            await session.commit()

    @staticmethod
    async def update_balance(telegram_id, new_balance):
        async with async_session() as session:
            stmt = select(User).where(User.telegram_id == telegram_id)
            result = await session.execute(stmt)
            user = result.scalar_one_or_none()

            if user:
                user.balance = new_balance
                await session.commit()
                return True
            else: return False




