from bot.database.models import async_session
from bot.database.models import User, Category, Item
from sqlalchemy import select

async def set_user(tg_id, tg_user_name, user_chat_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            new_user = User(tg_id=tg_id, tg_user_name=tg_user_name, user_chat_id = user_chat_id)
            session.add(new_user)
            #session.add(User(tg_user_name = tg_user_name))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


async def get_category_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category==category_id))


async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))

