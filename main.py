import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Missing BOT_TOKEN in environment variables")

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="💳 طرق الاشتراك")],
        [KeyboardButton(text="🎁 بطاقات نون")]
    ], resize_keyboard=True)
    await message.answer(
        f"👋 أنا {hbold('Prince Oday 🔥')}"
        "هنا كل محتواي الجريء والمميز تحصل عليه بعد الاشتراك
"
        "كل شي مصمم خصيصًا لك 👑",
        reply_markup=kb
    )

@dp.message(F.text == "💳 طرق الاشتراك")
async def subscription_methods(message: Message):
    await message.answer(
        "💳 خيارات الاشتراك:
"
        "- بطاقات نون مسبقة الدفع
"
        "- كريبتو (USDT - TRC20)

"
        "بعد الدفع، أرسل لنا الإثبات ليتم التفعيل يدويًا ✅"
    )

@dp.message(F.text == "🎁 بطاقات نون")
async def noon_cards(message: Message):
    await message.answer(
        "🎁 تقدر تشتري بطاقات نون من هنا:
"
        "🔗 https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/
"
        "🔗 https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())