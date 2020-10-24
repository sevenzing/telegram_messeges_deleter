from aiogram import types
from misc import dp
from constants import stickers

@dp.message_handler(content_types=['sticker'])
async def check_sticker_to_delete(message: types.Message):
    _id = message.sticker.file_unique_id
    print(_id, stickers)
    if _id not in stickers:
        await message.delete()
    
@dp.message_handler(content_types=types.ContentType.ANY)
async def delete(message: types.Message):
    await message.delete()


