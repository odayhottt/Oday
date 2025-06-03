from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

from aiogram.client.default import DefaultBotProperties

from aiogram.client.default import DefaultBotProperties

from aiogram.client.default import DefaultBotProperties

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 طرق الدفع")],
            [KeyboardButton(text="📬 تواصل معي")]
        ],
        resize_keyboard=True
    )

    text = (
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}\n"
        f"📦 {hbold('تفاصيل الاشتراك:')}\n"
        "الاشتراك الشهري حاليًا ٥٠٠ ريال فقط.\n\n"
        "وش تحصل بعد الاشتراك؟\n"
        "✅ أكثر من 50 فيلم كامل – جريء ومن إنتاجي الخاص\n"
        "🎥 كواليس وفعاليات من قلب التصوير\n"
        "📸 جودة أعلى… وتجربة مصممة لك أنت فقط ✨\n\n"
        "👇 اختر أحد الخيارات تحت عشان تكمل:"
    )

    await message.answer(text, reply_markup=keyboard)

@dp.message(F.text == "💰 طرق الدفع")
async def payment_handler(message: types.Message):
    text = (
        "💳 طرق الدفع المتاحة:\n"
        "1- بطاقات نون (تقدر تشتريها من المواقع التالية):\n"
        "• https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/\n"
        "• https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/\n\n"
        "2- كريبتو (USDT - TRC20):\n"
        "• https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207"
    )
    await message.answer(text)

@dp.message(F.text == "📬 تواصل معي")
async def contact_handler(message: types.Message):
    user_tag = "@odayh1"  # غير المعرف إذا احتجت
    await message.answer(f"راسلني خاص على التليجرام: 👉 {user_tag}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
