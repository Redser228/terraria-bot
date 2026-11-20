import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
# Ссылка на размещенный файл index.html (обязательно HTTPS)
GAME_URL = "https://ваш-домен.github.io/terraria_bot/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚔️ Играть в Pixel Realm",
                    web_app=WebAppInfo(url=GAME_URL)
                )
            ]
        ]
    )
    await message.answer(
        "🌲 **Добро пожаловать в Pixel Realm!**\n\n"
        "Исследуй процедурный мир, копай шахты, строй укрытия, выполняй задания Гида и сражайся с боссами.\n\n"
        "Нажми кнопку ниже, чтобы начать приключение:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())