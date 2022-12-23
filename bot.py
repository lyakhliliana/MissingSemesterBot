import asyncio
import logging
import random
import traceback
import telebot

from telebot.async_telebot import AsyncTeleBot

logger = telebot.logger
telebot.logger.setLevel(logging.ERROR)


class ExceptionHandler(telebot.ExceptionHandler):
    def handle(self, exception: Exception):
        logger.error(exception)
        print(traceback.format_exc())


TOKEN = '5959148099:AAFifwjPIR29d8HsWzQLNQHEeTjEJqlwvcM'
bot = AsyncTeleBot(TOKEN, exception_handler=ExceptionHandler())

replies = ['Yes', 'No', 'Ho-ho', 'Brr...']
gifs = ['data/5ae19b85197371.5d75094a2ecee.gif', 'data/8c9e158c184a944.gif',
        'data/cat-computer-veryfas.gif', 'data/peach-cat-cute.gif']
audio = ['data/cat-meow_g1oerneo.mp3', 'data/zvuk-koshki.mp3']
photo = ['data/maxresdefault.jpg', 'data/9f1fc8c29f87a1f237a2f2bf2300f1c1.jpg']


@bot.message_handler(commands=["start"])
async def start(message: telebot.types.Message):
    text = """
Привет!    
Это Бен!
Он *ВАНГА* - ОН ВАШ *ДЕТЕКТОР* ЛЖИ
Задайте любой вопрос:), он вам ответит
Формат вопроса: Я сдам коллок?
Плюс ко всему есть команды...
"""
    await bot.reply_to(message, text=text, parse_mode='Markdown')


@bot.message_handler(func=lambda x: str(x.text).endswith('?'))
async def reply_ben(message: telebot.types.Message):
    await bot.reply_to(message, text=replies[random.randrange(0, 4)],
                       parse_mode='Markdown')


@bot.message_handler(commands=["send_gif"])
async def gif_send(message: telebot.types.Message):
    await bot.send_animation(message.chat.id,
                             open(gifs[random.randrange(0, 4)], 'rb'))


@bot.message_handler(commands=["send_audio"])
async def send_audio(message: telebot.types.Message):
    await bot.send_audio(message.chat.id,
                         open(audio[random.randrange(0, 2)], 'rb'))


@bot.message_handler(commands=["send_photo"])
async def send_photo(message: telebot.types.Message):
    await bot.send_photo(message.chat.id,
                         open(photo[random.randrange(0, 2)], 'rb'))


async def main():
    await bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    asyncio.run(main())
