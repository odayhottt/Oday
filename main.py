from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import F
from aiogram.utils.markdown import hbold
from aiogram.dispatcher.dispatcher import Dispatcher as Dispatcher3
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher3(storage=MemoryStorage())
router = Router()
dp.include_router(router)

# /start
@router.message(F.text == "/start")
async def start_handler(message: types.Message):
    text = (
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}\n\n"
        "📦 الاشتراك الشهري حالياً بـ ٥٠٠ ريال فقط\n\n"
        "وش يعطيك الاشتراك؟\n"
        "– أكثر من 50 فيلم كامل ✅\n"
        "– جريء ومن إنتاجي الخاص 🎬\n"
        "– كواليس وفعاليات من قلب التصوير 📹\n"
        "– جودة أعلى… وتجربة مصممة لك أنت فقط ✨"
    )
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 طرق الدفع"))
    keyboard.add(KeyboardButton("📬 تواصل معي"))
    await message.answer(text, reply_markup=keyboard)

# طرق الدفع
@router.message(F.text == "💰 طرق الدفع")
async def payment_info(message: types.Message):
    text = (
        "💳 طرق الدفع المتاحة:\n\n"
        "– بطاقات نون مسبقة الدفع:\n"
        "  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/\n"
        "  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/\n\n"
        "– أو كريبتو USDT (TRC20):\n"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "🎯 بعد ما تدفع، تواصل معي مباشر لتفعيل اشتراكك."
    )
    await message.answer(text)

# تواصل معي
@router.message(F.text == "📬 تواصل معي")
async def contact_handler(message: types.Message):
    await message.answer("📬 للتواصل معي مباشر:\n"
                         "اضغط هنا 👉 @odayh1\n"
                         "وراح أرد عليك بنفسي 💬")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())