from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    text = (
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}

"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة

"
        "💳 الدفع:
"
        "– بطاقات نون مسبقة الدفع
"
        "– كريبتو: USDT (TRC20)

"
        "📦 اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع 👇"
    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text="📦 تفاصيل الباقة")],
        [types.KeyboardButton(text="💳 الدفع")],
        [types.KeyboardButton(text="✉️ أرسلت الدفع")]
    ])
    await message.answer(text, reply_markup=keyboard)

@dp.message(F.text == "📦 تفاصيل الباقة")
async def package_details(message: Message):
    text = (
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط

"
        "وش تحصل؟
"
        "– أكثر من 50 فيلم خاص 🎬
"
        "– كواليس حصرية 📸
"
        "– جودة أعلى وتجربة لك أنت بس ✨"
    )
    await message.answer(text)

@dp.message(F.text == "💳 الدفع")
async def payment_options(message: Message):
    text = (
        "💳 اختر طريقتك:
"
        "🔶 بطاقات نون:
"
        "• https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/
"
        "• https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/

"
        "🔷 كريبتو (USDT):
"
        "• https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207

"
        "✉️ بعد الدفع، اضغط «أرسلت الدفع» وأرسل سكرين."
    )
    await message.answer(text)

@dp.message(F.text == "✉️ أرسلت الدفع")
async def request_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.
بعد المراجعة اليدوية، يتم التفعيل ⏳.")

@dp.message(F.photo)
async def handle_proof(message: Message):
    user = message.from_user
    caption = (
        "🔔 إثبات دفع جديد
"
        f"👤 من: @{user.username or 'بدون يوزر'}
"
        f"🆔 ID: {user.id}
"
        f"رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات. بنراجع ونرد عليك قريب.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
