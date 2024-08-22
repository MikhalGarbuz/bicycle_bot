from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import bot.keyboards as kb
import bot.database.requests as rq

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply("Вітаємо у нашому магазині", reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer("Виберіть категорію товару", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer("Ви вибрали товар по категорії")
    await callback.message.edit_text('Виберіть товар з категорії', reply_markup=await kb.items(callback.data.split("_")[1]))

@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split("_")[1])
    await callback.answer("Ви вибрали товар")
    await callback.message.edit_text(f'{item_data.name}\n Ціна: {item_data.price}грн', reply_markup=await kb.items(callback.data.split("_")[1]))


@router.callback_query(F.data =='to_main')
async def category(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Головна", reply_markup=kb.main)