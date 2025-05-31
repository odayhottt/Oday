
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_USERNAME = os.getenv("OWNER_USERNAME")  # مثال: odayh1

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 طرق الدفع")],
            [KeyboardButton(text="📬 تواصل معي")]
        ],
        resize_keyboard=True
    )

    welcome_text = (
        "👋 هلا فيك في البوت الرسمي لـ <b>Prince Oday 🔥</b>\n\n"
        "📦 <b>تفاصيل الاشتراك:</b>\n"
        "الاشتراك الشهري حاليًا <b>٥٠٠ ريال</b> فقط.\n\n"
        "وش تحصل بعد الاشتراك؟\n"
        "– أكثر من 50 فيلم كامل ✅ وجريء من إنتاجي الخاص 🎬\n"
        "– كواليس وفعاليات من قلب التصوير 📹\n"
        "– جودة أعلى… وتجربة مصممة لك أنت فقط ✨\n"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

@dp.message(F.text == "💰 طرق الدفع")
async def payment_options(message: Message):
    await message.answer(
        "💳 تقدر تشترك عن طريق التحويل البنكي أو بطاقات نون.\n"
        "تواصل معي مباشرة عشان أرسل لك التفاصيل الكاملة 🔒"
    )

@dp.message(F.text == "📬 تواصل معي")
async def contact(message: Message):
    await message.answer(f"راسلني خاص على التيليجرام:\n👉 @{OWNER_USERNAME}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
