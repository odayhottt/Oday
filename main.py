
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Text
from aiogram import F
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram import Router
from aiogram import Dispatcher
from aiogram import types
from aiogram import Bot
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Text
from aiogram import Dispatcher, Router
from aiogram.types import Message
from aiogram import BaseMiddleware
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}

"
        "📦 الاشتراك الشهري حالياً بـ ٥٠٠ ريال فقط

"
        "وش تحصل بعد الاشتراك؟
"
        "– أكثر من 50 فيلم كامل ✅
"
        "– جريء ومن إنتاجي الخاص 🎬
"
        "– كواليس وفعاليات من قلب التصوير 📹
"
        "– جودة أعلى… وتجربة مصممة لك أنت فقط ✨

"
        "💳 طرق الاشتراك:
"
        "• بطاقات نون:
"
        "  - https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/
"
        "  - https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/
"
        "• كريبتو (USDT - TRC20):
"
        "  - https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207
"
    )
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📬 تواصل معي")],
        ],
        resize_keyboard=True
    )
    await message.answer(text, reply_markup=keyboard)

@router.message(Text("📬 تواصل معي"))
async def contact_handler(message: Message):
    await message.answer("📩 تقدر تتواصل معي مباشر هنا: @odayh1")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
