import os

from audio import download_audio
from pytube import YouTube
from aiogram import types, Dispatcher, Bot, executor

TOKEN_API = 'Your token'

async def on_startup(_):
    print('Bot is working')
bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f'Hey, {message.from_user.first_name}!\nI can convert a YouTube link '
                                                         f'to mp3 format, just send me link' + '🐝')

@dp.message_handler()
async def convert_link(message : types.Message):
    if message.text.startswith('https://www.youtube.com/'):
        url = message.text
        yt = YouTube(url)

        await bot.send_message(chat_id=message.chat.id,text=f"*download started *: {yt.title}\n"
                                                            f"*from channel *: [{yt.author}]({yt.channel_url})", parse_mode='Markdown')

        title = download_audio(url)
        audio = open(f"audio/{title}", 'rb')
        await bot.send_audio(chat_id=message.chat.id, audio=audio)
        await bot.send_message(chat_id=message.chat.id, text="enjoy!" + '❤️')
        os.remove(f'audio/{title}')
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)