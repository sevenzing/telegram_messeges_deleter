from aiogram import Bot, Dispatcher, types
from redis import Redis
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import constants

bot = Bot(token=constants.BOT_TOKEN)
database = Redis(**constants.redis)
storage = RedisStorage2(**constants.redis)
dp = Dispatcher(bot)
