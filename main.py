
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import os

# متغيرات البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(lambda message: message.text == "/start")
async def send_welcome(message: Message):
    text = (
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
        "⏳ اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع الأخرى 👇"
    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text="🔐 فعل اشتراكي")]
    ])
    await message.answer(text, reply_markup=keyboard)

@dp.message(lambda message: message.text == "🔐 فعل اشتراكي")
async def show_package(message: Message):
    text = (
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
        "✅ بعد الدفع، أرسل الإثبات الآن هنا."
    )
    await message.answer(text)

@dp.message(lambda message: message.photo)
async def handle_payment_proof(message: Message):
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

@dp.message(lambda message: message.text == "/accounts")
async def send_accounts(message: Message):
    await message.answer("📱 كل حساباتي بمكان واحد:
🌐 https://linktr.ee/odayhottt")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
