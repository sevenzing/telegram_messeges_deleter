from aiogram import types
from misc import dp, database
from constants import stickers, BOT_ADMIN

@dp.message_handler(user_id=BOT_ADMIN, text_contains='#say')
async def admin(message: types.Message):
    pass

@dp.message_handler(content_types=['sticker'])
async def check_sticker_to_delete(message: types.Message):
    chat_id = message.chat.id
    message_id = message.message_id
    sticker_id = message.sticker.file_unique_id
    data = database.hgetall(chat_id)
    if not data:
        print(f'No data. update  with message_id={message_id}')
        database.hmset(chat_id, {'stick_id':sticker_id, 'message_id': message_id})
        return
    old_sticker_id = data[b'stick_id'].decode()
    old_message_id = int(data[b'message_id'].decode())
    deleted = False
    print(sticker_id, data, sticker_id, message_id)
    
    if sticker_id not in stickers:
        print('sticker not in stickers')
        await message.delete()
        deleted = True
    
    # only if we have actual information
    elif message_id == old_message_id + 1:
        print(stickers[old_sticker_id], stickers[sticker_id])
        
        if stickers[old_sticker_id][1] != stickers[sticker_id][0]:
            print('sticker isn\'t correct')
            await message.delete()
            deleted = True
    else:
        print('We have not actual inf')
    
    print(f'update  with message_id={message_id}. is sticker updated {not deleted}')
    database.hmset(chat_id, {'stick_id':sticker_id if not deleted else old_sticker_id, 'message_id': message_id})


@dp.message_handler(content_types=types.ContentType.ANY)
async def delete(message: types.Message):
    await message.delete()


