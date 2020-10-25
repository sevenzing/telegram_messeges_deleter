from aiogram import executor
from misc import dp
import logging
import adminer

if __name__ == '__main__':
        
    executor.start_polling(dp, skip_updates=False)
