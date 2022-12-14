from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print("bot online")
    sqlite_db.sql_start()

from handlers import client, admin, other

client.registers_handlers_client(dp)
admin.register_handlers_admin(dp)
other.registers_handlers_other(dp) #имрортировать снизу

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

