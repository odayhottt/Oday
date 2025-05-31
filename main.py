import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram import types
from aiogram import Dispatcher
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram import Router
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📦 تفاصيل الباقة")],
    [KeyboardButton(text="💳 الدفع")],
    [KeyboardButton(text="✉️ أرسلت الدفع")],
], resize_keyboard=True)

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}

"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة",
        reply_markup=keyboard
    )

@router.message(F.text == "📦 تفاصيل الباقة")
async def package_details(message: Message):
    await message.answer(
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط

"
        "وش تحصل؟
"
        "– أكثر من 50 فيلم خاص 🎥
"
        "– كواليس حصرية 🎬
"
        "– جودة أعلى وتجربة لك أنت بس ✨"
    )

@router.message(F.text == "💳 الدفع")
async def payment_options(message: Message):
    await message.answer(
        "💳 اختر طريقتك:
"
        "🔶 بطاقات نون:
"
        "• https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/
"
        "• https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/

"
        "💠 كريبتو (USDT):
"
        "• https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "✉️ بعد الدفع، اضغط «أرسلت الدفع» وأرسل سكرين.",
        disable_web_page_preview=True
    )

@router.message(F.text == "✉️ أرسلت الدفع")
async def ask_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.
⏳ بعد المراجعة اليدوية، يتم التفعيل.")

@router.message(F.photo)
async def handle_photo(message: Message):
    user = message.from_user
    caption = (
        f"🧾 إثبات دفع جديد
"
        f"• الاسم: {user.full_name}
"
        f"• المعرف: @{user.username if user.username else 'بدون معرف'}
"
        f"• ID: {user.id}
"
        f"• رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريب.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())