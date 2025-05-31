import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher()

ADMIN_ID = int(os.getenv("ADMIN_ID"))

@dp.message(F.text == "/start")
async def welcome(message: Message):
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
        "⏳ اضغط الزر تحت علشان تعرف التفاصيل 👇",
        reply_markup=keyboard
    )

@dp.message(F.text == "🔐 فعل اشتراكي")
async def show_package(message: Message):
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
        "- كريبتو:
"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "✅ بعد الدفع، اضغط الزر تحت وأرسل الإثبات.",
        reply_markup=keyboard
    )

@dp.message(F.text == "📸 أرسلت الإثبات")
async def request_proof(message: Message):
    await message.answer("📤 أرسل صورة أو سكرين لإثبات الدفع.
"
                         "🔎 بنراجعها يدويًا ونفعل اشتراكك بإذن الله.")

@dp.message(F.photo)
async def forward_proof(message: Message):
    user = message.from_user
    caption = (
        f"🧾 إثبات دفع جديد
"
        f"👤 المستخدم: @{user.username or 'بدون معرف'}
"
        f"🆔 ID: {user.id}
"
        f"📎 رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونرجع لك قريبًا.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
