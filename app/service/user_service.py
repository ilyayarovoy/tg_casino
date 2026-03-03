import asyncio

from app.repositories.user_repo import UserRepository

class UserService:

    @staticmethod
    async def register_new_user(telegram_id, firstname, lastname, balance):
        user = await UserRepository.get_user_by_id(telegram_id)

        if not user:
            await UserRepository.add_user_to_database(telegram_id, firstname, lastname, balance)

    @staticmethod
    async def get_balance(telegram_id):
        user = await UserRepository.get_user_by_id(telegram_id)
        balance = user.balance
        return balance

    @staticmethod
    async def deposit(telegram_id, amount):
        user = await UserRepository.get_user_by_id(telegram_id=telegram_id)
        current_balance = user.balance
        new_balance = current_balance + amount
        await UserRepository.update_balance(telegram_id=telegram_id, new_balance=new_balance)


    @staticmethod
    async def withdraw(telegram_id, amount):
        user = await UserRepository.get_user_by_id(telegram_id=telegram_id)
        current_balance = user.balance
        if amount > current_balance:
            raise ValueError("Недостаточно средств")
        new_balance = current_balance - amount
        await UserRepository.update_balance(telegram_id=telegram_id, new_balance=new_balance)

    @staticmethod
    async def increase_balance_by_2(telegram_id, balance):
        new_balance = balance * 2
        await UserRepository.update_balance(telegram_id=telegram_id, new_balance=new_balance)

    @staticmethod
    async def reduce_balance_by_2(telegram_id, balance):
        new_balance = balance / 2
        await UserRepository.update_balance(telegram_id=telegram_id, new_balance=new_balance)





