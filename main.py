import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
import os

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# /start
@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="🔐 فعل اشتراكي"))

    await message.answer(
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Odayhottt')}

"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة

"
        "💳 خيارات الدفع:
"
        "- بطاقات نون مسبقة الدفع
"
        "- كريبتو: USDT (TRC20)

"
        "🔗 للدفع بالكريبتو:
"
        "https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "⏳ اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع 👇",
        reply_markup=kb
    )

# تفاصيل الباقة
@dp.message(F.text == "🔐 فعل اشتراكي")
async def show_package(message: Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="✅ أرسلت الإثبات"))

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
        reply_markup=kb
    )

# إثبات الدفع
@dp.message(F.text == "✅ أرسلت الإثبات")
async def ask_for_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.
"
                         "⏳ بعد المراجعة اليدوية، يتم التفعيل.")

@dp.message(F.photo)
async def handle_photo(message: Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع جديد
"
        f"👤 من: @{user.username or 'بدون يوزر'}
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
@dp.message(F.text == "/accounts")
async def accounts(message: Message):
    await message.answer("📱 كل حساباتي بمكان واحد:
🌐 https://linktr.ee/odayhottt")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
