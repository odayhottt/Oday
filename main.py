from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.utils.chat_action import ChatActionMiddleware
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher
from aiogram import Bot
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)
dp.message.middleware(ChatActionMiddleware())


@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🔐 فعل اشتراكي")]],
        resize_keyboard=True
    )
    await message.answer(
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}

"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة

"
        "💳 خيارات الدفع:
"
        "- بطاقات نون مسبقة الدفع
"
        "- كريبتو: USDT (TRC20)

"
        "📲 للدفع بالكريبتو:
"
        "🔗 https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "⏳ أو اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع الأخرى 👇",
        reply_markup=keyboard
    )


@router.message(F.text == "🔐 فعل اشتراكي")
async def show_package_details(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📸 أرسلت الإثبات")]],
        resize_keyboard=True
    )
    await message.answer(
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط

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
        "🧾 خيارات الدفع:
"
        "- بطاقات نون:
"
        "  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/
"
        "  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/
"
        "- كريبتو (USDT):
"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "✅ بعد الدفع، اضغط الزر تحت وأرسل الإثبات.",
        reply_markup=keyboard
    )


@router.message(F.text == "📸 أرسلت الإثبات")
async def ask_for_proof(message: types.Message):
    await message.answer(
        "📸 أرسل صورة أو سكرين لإثبات الدفع هنا.
"
        "🔔 بعد المراجعة اليدوية، يتم التفعيل عبر الخاص."
    )


@router.message(F.photo)
async def handle_payment_proof(message: types.Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع جديد
"
        f"👤 من: @{user.username if user.username else 'بدون يوزر'}
"
        f"🆔 ID: {user.id}
"
        f"⏱ الوقت: {message.date}

"
        f"رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريباً.")


@router.message(F.text == "/accounts")
async def send_accounts(message: types.Message):
    await message.answer("📱 كل حساباتي بمكان واحد:
🌐 https://linktr.ee/odayhottt")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
