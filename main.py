
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.markdown import hlink

import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text="🔐 فعل اشتراكي")]
    ])
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
        "📲 للدفع بالكريبتو:
"
        "🔗 https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "⏳ أو اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع الأخرى 👇",
        reply_markup=kb
    )

@dp.message(F.text == "🔐 فعل اشتراكي")
async def show_plan(message: Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text="✅ أرسلت الإثبات")]
    ])
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

@dp.message(F.text == "✅ أرسلت الإثبات")
async def request_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.
⏳ بعد المراجعة اليدوية، يتم التفعيل.")

@dp.message(F.photo)
async def receive_proof(message: Message):
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

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
