import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='try_ikey')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)

    text_and_data = (
        ('Kendrick', 'https://en.wikipedia.org/wiki/Kendrick_Lamar'),
        ('Linkin Park', 'https://ru.wikipedia.org/wiki/Linkin_Park'),
    )
    # in real life for the callback_data the callback data factory should be used
    # here the raw string is used for the simplicity
    row_btns = (types.InlineKeyboardButton(text, url=data) for text, data in text_and_data)

    keyboard_markup.row(*row_btns)

    await message.reply("Who do you want to know about more?", reply_markup=keyboard_markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)