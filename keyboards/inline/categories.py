from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions
from aiogram.utils.callback_data import CallbackData

from keyboards.default.markups import cart
from keyboards.inline.products_from_cart import product_markup
from loader import db, bot

category_cb = CallbackData('category', 'id', 'action')
cat_cb = CallbackData('categori', 'id', 'action')
product_cb= CallbackData('product', 'id', 'action')

def categories_markup(product):
    markup = InlineKeyboardMarkup(row_width=3)
    for idx, title, tag in product:
        markup.insert(InlineKeyboardButton(title, callback_data=product_cb.new(id=idx, action='view')))

    # cart=InlineKeyboardButton(text='🛒 Корзина', callback_data='Корзинка')
    # info=InlineKeyboardButton(text = 'Информация', url = 'https://www.youtube.com', callback_data='about')
    # que=InlineKeyboardButton(text = '❓ Вопросы', callback_data='Вопросы')
    # de=InlineKeyboardButton(text = '🚚 Статус заказа', callback_data='Buyurtma holati')
    markup.add(InlineKeyboardButton(text='🛒 Корзина', callback_data='Корзинка'),InlineKeyboardButton(text = 'Информация', url = 'https://www.youtube.com', callback_data='about'))
    markup.add(InlineKeyboardButton(text = '❓ Вопросы', callback_data='Вопросы'),InlineKeyboardButton(text = '🚚 Статус заказа', callback_data='Buyurtma holati'))
    return markup
def categories_markup1():
    global cat_cb

    markup = InlineKeyboardMarkup(row_width=3)
    product=db.fetchall('''SELECT * FROM categori''')

    for idx,title in product:
        markup.insert(InlineKeyboardButton(title, callback_data=category_cb.new(id=idx, action='view')))
    # cart=InlineKeyboardButton(text='🛒 Корзина', callback_data='Корзинка')
    # info=InlineKeyboardButton(text = 'Информация', url = 'https://www.youtube.com', callback_data='about')
    # que=InlineKeyboardButton(text = '❓ Вопросы', callback_data='Вопросы')
    # de=InlineKeyboardButton(text = '🚚 Статус заказа', callback_data='Buyurtma holati')
    markup.add(InlineKeyboardButton(text='🛒 Корзина', callback_data='Корзинка'),
               InlineKeyboardButton(text='Информация', url='https://www.youtube.com', callback_data='about'))
    markup.add(InlineKeyboardButton(text='❓ Вопросы', callback_data='Вопросы'),
               InlineKeyboardButton(text='🚚 Статус заказа', callback_data='Buyurtma holati'))
    return markup

async def show_products(m, products):

    if len(products) == 0:

        await m.answer('Здесь ничего нет 😢')

    else:

        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)

        for idx, title, body, image, price, _ in products:

            markup = product_markup(idx, price)
            text = f'<b>{title}</b>\n\n{body}'

            await m.answer_photo(photo=image,
                                 caption=text,
                                 reply_markup=markup)