import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties

# بياناتك
BOT_TOKEN = "ضع_توكن_البوت_هنا"
ADMIN_ID = 123456789  # ضع رقم معرفك هنا بدون @

# إعداد البوت
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# رسالة البداية
@dp.message(F.text == "/start")
async def start_handler(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🔐 فعل اشتراكي")
    await message.answer(
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}\n\n"
        "🔥 هنا تقدر تشترك بسهولة بخيارات دفع مرنة\n\n"
        "💳 الدفع المتاح:\n"
        "- بطاقات نون مسبقة الدفع\n"
        "- كريبتو: USDT (TRC20)\n\n"
        "🧾 للدفع بالكريبتو:\n"
        "<a href='https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207'>اضغط هنا للدفع</a>\n\n"
        "👇 اضغط الزر تحت تشوف تفاصيل الباقة وطريقة التفعيل",
        reply_markup=markup
    )

# تفاصيل الباقة
@dp.message(F.text == "🔐 فعل اشتراكي")
async def subscribe_handler(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ أرسلت الإثبات")
    await message.answer(
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط\n\n"
        "وش تحصل بعد الاشتراك؟\n"
        "– أكثر من 50 فيلم كامل ✅\n"
        "– جريء ومن إنتاجي الخاص 🎬\n"
        "– كواليس وفعاليات من قلب التصوير 📹\n"
        "– جودة أعلى… وتجربة مصممة لك أنت فقط ✨\n\n"
        "💳 خيارات الدفع:\n"
        "- بطاقات نون:\n"
        "  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/\n"
        "  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/\n"
        "- كريبتو (USDT):\n"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "📩 بعد الدفع، اضغط (✅ أرسلت الإثبات) وأرسل السكرين.",
        reply_markup=markup
    )

# استلام الإثبات
@dp.message(F.text == "✅ أرسلت الإثبات")
async def wait_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.\n"
                         "📬 التفعيل يتم يدويًا بعد المراجعة.")

@dp.message(F.photo)
async def handle_proof(message: Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع جديد\n"
        f"👤 من: @{user.username or 'بدون يوزر'}\n"
        f"🆔 ID: {user.id}\n"
        f"⏱ الوقت: {message.date}\n"
        f"رابط: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("✅ تم استلام الإثبات، التفعيل خلال وقت قصير.")

# تشغيل البوت
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())