import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

import os

# المتغيرات من البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# إعداد البوت
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# رسالة الترحيب
@dp.message(CommandStart())
async def send_welcome(message: Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="🔐 فعل اشتراكي"))
    await message.answer(
        "👋 هلا فيك في البوت الرسمي لـ " + hbold("Odayhottt") + "

"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة

"
        "💳 خيارات الدفع:
"
        "- بطاقات نون
"
        "- كريبتو: USDT (TRC20)

"
        "📲 للدفع بالكريبتو:
"
        "🔗 https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "أو اضغط الزر تحت 👇",
        reply_markup=kb,
    )

# تفاصيل الاشتراك
@dp.message(F.text == "🔐 فعل اشتراكي")
async def show_subscription(message: Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="✅ أرسلت الدفع"))
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
        "– جودة أعلى وتجربة مصممة لك أنت فقط ✨

"
        "🧾 الدفع:
"
        "- بطاقات نون:
"
        "  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/
"
        "  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/
"
        "- كريبتو (USDT TRC20):
"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "✅ بعد الدفع، اضغط الزر تحت وأرسل الإثبات.",
        reply_markup=kb,
    )

# إثبات الدفع
@dp.message(F.text == "✅ أرسلت الدفع")
async def request_payment_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.
"
                         "⏳ بعد المراجعة اليدوية، يتم التفعيل.")

# استلام إثبات الدفع
@dp.message(F.photo)
async def handle_photo(message: Message):
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

# روابط الحسابات
@dp.message(F.text.lower().in_(["حساباتي", "accounts"]))
async def send_accounts(message: Message):
    await message.answer("📱 كل حساباتي بمكان واحد:
🌐 https://linktr.ee/odayhottt")

# بدء البوت
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())