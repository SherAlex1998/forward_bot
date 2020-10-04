from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

#from config import token, group_id

token = os.environ['TOKEN']
group_id = os.environ['GROUP_ID']


WEBHOOK_HOST = 'https://deploy-heroku-bot.tashepsilontestbot.com'  # name your app
WEBHOOK_PATH = '/webhook/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.environ.get('PORT')

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def forward_message(message: types.Message):
    if message.chat.type == "private":
        print(message.from_user.id)
        await message.forward(group_id,message)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    # insert code here to run it before shutdown
    pass

if __name__ == '__main__':
    executor.start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=WEBAPP_HOST, port=WEBAPP_PORT)