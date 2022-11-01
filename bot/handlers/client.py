from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


#старт/помощь
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/SushiSheefBot')

#режим роботы
async def sushi_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Чт: 9:00 - 19:30; Пт: 0:00 - 23:00')
    
#расположение
async def sushi_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Пушкина')


#@dp.message_handler(commands=['Меню'])
async def sushi_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def registers_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(sushi_open_command, commands=['Режим_работы'])
    dp.register_message_handler(sushi_place_command, commands=['Расположение'])
    dp.register_message_handler(sushi_menu_command, commands=['Меню'])