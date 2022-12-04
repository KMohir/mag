from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.default.markups import cart
from loader import db

product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx='', price=0):

    global product_cb

    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(InlineKeyboardButton(f"Добавить в корзину - {price}som", callback_data=product_cb.new(id=idx, action='add')))
    markup.add(InlineKeyboardButton(text='🛒 Корзина', callback_data=cart))
    markup.add(InlineKeyboardButton(text='Назад', callback_data='home'))

    return markup