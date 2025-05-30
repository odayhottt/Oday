
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.utils.markdown import hbold
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram import Router
import asyncio
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")  # يجب وضعه كـ string في Render

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()
dp.include_router(router)

logging.basicConfig(level=logging.INFO)

# زر الاشتراك
subscribe_button = ReplyKeyboardMarkup(
    keyboard=[[{"text": "🔐 فعل اشتراكي"}]],
    resize_keyboard=True
)

# رسالة البداية
@router.message(F.text == "/start")
async def start_handler(message: Message):
    text = (
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
        "⏳ أو اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع 👇"
    )
    await message.answer(text, reply_markup=subscribe_button)

# تفاصيل الباقة
@router.message(F.text == "🔐 فعل اشتراكي")
async def subscribe_handler(message: Message):
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
        "✅ بعد الدفع، أرسل صورة إثبات الدفع هنا في الخاص."
    )
    await message.answer(text)

# استلام إثبات الدفع (صور)
@router.message(F.photo)
async def payment_proof_handler(message: Message):
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
    await bot.send_photo(chat_id=int(ADMIN_ID), photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريباً.")

# روابط حساباتي
@router.message(F.text == "/accounts")
async def accounts_handler(message: Message):
    await message.answer("📱 كل حساباتي بمكان واحد:
🌐 https://linktr.ee/odayhottt")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
