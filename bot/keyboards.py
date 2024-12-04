from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.database.requests import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "Наші послуги")],
                                        [KeyboardButton(text = "Про нас")]] ,
                                        #[KeyboardButton(text = "Наш канал")]],
                            resize_keyboard = True,
                           input_field_placeholder="Вітаю!!! Виберіть пункт меню")

async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.row(InlineKeyboardButton(text=f"{item.name} Ціна: {item.price}", callback_data=f"item_{item.id}"))
    if category_id ==1:
        keyboard.row(InlineKeyboardButton(text="Зв'язатись для бронювання", url = "https://t.me/scuoladilobotomia"))
    else:
        keyboard.row(InlineKeyboardButton(text="Зв'язатись для купівлі", url= "https://t.me/scuoladilobotomia"))
    keyboard.row(InlineKeyboardButton(text="Назад", callback_data="categories"))
    return keyboard.as_markup()

async def back_to_main():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="back_to_main"))

    return keyboard.as_markup()

async def back_to_categories():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="categories"))

    return keyboard.as_markup()
async def item(category_id, item_id):
    keyboard = InlineKeyboardBuilder()
    if category_id == 1:
        keyboard.add(InlineKeyboardButton(text="Орендувати", callback_data=f"operationrent_{item_id}"))
    else:
        keyboard.add(InlineKeyboardButton(text="Купити", callback_data=f"operationbuy_{item_id}"))
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data=f"category_{category_id}"))
    return keyboard.as_markup()


async def categories():
    all_items = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"category_{item.id}"))
    keyboard.add(InlineKeyboardButton(text="На головну", callback_data="back_to_main"))

    return keyboard.adjust(2).as_markup()