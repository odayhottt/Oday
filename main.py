from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram import Router
from aiogram import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
router = Router()
dp = Dispatcher()
dp.include_router(router)

# رسالة الترحيب
@router.message(CommandStart())
async def send_welcome(message: Message):
    markup = ReplyKeyboardMarkup(
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
        reply_markup=markup
    )

# تفاصيل الاشتراك
@router.message(F.text == "🔐 فعل اشتراكي")
async def show_package(message: Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="✅ أرسلت الإثبات")]],
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
        reply_markup=markup
    )

# استقبال إثبات الدفع
@router.message(F.text == "✅ أرسلت الإثبات")
async def ask_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.
"
                         "⏳ بعد المراجعة اليدوية، يتم التفعيل.")

@router.message(F.photo)
async def handle_proof(message: Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع جديد
"
        f"👤 من: @{user.username if user.username else 'بدون يوزر'}
"
        f"🆔 ID: {user.id}

"
        f"رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.answer("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريباً.")

# تشغيل البوت
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
