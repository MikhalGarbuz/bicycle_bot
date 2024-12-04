from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config import connstr

engine = create_async_engine(connstr, echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger)
    tg_user_name: Mapped[str] = mapped_column(String(100))
    user_chat_id: Mapped[int] = mapped_column()


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    name: Mapped[str] = mapped_column(String(25))

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(String(200))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
