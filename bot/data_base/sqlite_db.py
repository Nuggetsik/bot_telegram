import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('../admin_backend/tga/db.sqlite3')
    cur = base.cursor()
    if base:
        print("Date base connect OK!")
    base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM ugc_profile').fetchall():
        await bot.send_photo(message.from_user.id, ret[-1],f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[3]}') #ret[-1] - Изображение
    
