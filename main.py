from aiogram import Bot, Dispatcher, types, executor
import logging
import os

# قراءة التوكن ومعرف الأدمن من المتغيرات البيئية
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# رسالة الترحيب
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    text = (
        "👋 هلا فيك في البوت الرسمي لـ Odayhottt\n\n"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة\n\n"
        "💳 خيارات الدفع:\n"
        "- بطاقات نون مسبقة الدفع\n"
        "- كريبتو: USDT (TRC20)\n\n"
        "📲 للدفع بالكريبتو:\n"
        "🔗 https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "⏳ أو اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع الأخرى 👇"
    )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("اشترك الآن")
    await message.answer(text, reply_markup=markup)

# تفاصيل الباقة
@dp.message_handler(lambda message: message.text == "اشترك الآن")
async def show_package(message: types.Message):
    text = (
        "📦 الاشتراك الشهري الآن بـ ٥٠٠ ريال فقط\n\n"
        "وش تحصل بعد الاشتراك؟\n"
        "– أكثر من 50 فيلم كامل ✅\n"
        "– جريء ومن إنتاجي الخاص 🎬\n"
        "– كواليس وفعاليات من قلب التصوير 📹\n"
        "– جودة أعلى… وتجربة مصممة لك أنت فقط ✨\n\n"
        "🧾 خيارات الدفع:\n"
        "- بطاقات نون:\n"
        "  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/\n"
        "  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/\n"
        "- كريبتو (USDT):\n"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "✅ بعد الدفع، اضغط الزر تحت وأرسل الإثبات."
    )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("أرسلت الدفع ✅")
    await message.answer(text, reply_markup=markup)

# إثبات الدفع
@dp.message_handler(lambda message: message.text == "أرسلت الدفع ✅")
async def ask_for_proof(message: types.Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.\n"
                         "⏳ بعد المراجعة اليدوية، يتم التفعيل.")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_payment_proof(message: types.Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع جديد\n"
        f"👤 من: @{user.username if user.username else 'بدون يوزر'}\n"
        f"🆔 ID: {user.id}\n"
        f"⏱ الوقت: {message.date}\n\n"
        f"رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريباً.")

# عرض الحسابات
@dp.message_handler(commands=["accounts"])
async def send_accounts(message: types.Message):
    await message.answer("📱 كل حساباتي بمكان واحد:\n🌐 https://linktr.ee/odayhottt")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
