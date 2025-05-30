
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# تعريف حالات المستخدم
class UserStates(StatesGroup):
    waiting_for_payment = State()

# رسالة الترحيب
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📦 تفاصيل الباقة", "💳 الدفع", "📩 أرسلت الدفع")
    await message.answer("👋 هلا فيك، وش حاب تسوي؟", reply_markup=markup)

# تفاصيل الباقة
@dp.message_handler(lambda message: message.text == "📦 تفاصيل الباقة")
async def package_details(message: types.Message):
    text = (
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط\n\n"
        "وش تحصل؟\n"
        "– أكثر من 50 فيلم خاص 🎬\n"
        "– كواليس حصرية 📹\n"
        "– جودة أعلى وتجربة لك أنت بس ✨"
    )
    await message.answer(text)

# خيارات الدفع
@dp.message_handler(lambda message: message.text == "💳 الدفع")
async def payment_options(message: types.Message, state: FSMContext):
    await UserStates.waiting_for_payment.set()
    await message.answer(
        "💳 اختر طريقتك:\n"
        "🔸 بطاقات نون:\n"
        "  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/\n"
        "  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/\n\n"
        "🔹 كريبتو (USDT):\n"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "📩 بعد الدفع، اضغط «أرسلت الدفع» وأرسل سكرين."
    )

# إثبات الدفع
@dp.message_handler(lambda message: message.text == "📩 أرسلت الدفع")
async def ask_proof(message: types.Message, state: FSMContext):
    current = await state.get_state()
    if current != UserStates.waiting_for_payment.state:
        await message.answer("💡 اضغط أول على «💳 الدفع» واختار طريقتك، بعدين أرسل الإثبات.")
        return
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.")
    await state.finish()

@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.DOCUMENT])
async def handle_payment_proof(message: types.Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع\n"
        f"👤 @{user.username if user.username else 'بدون يوزر'}\n"
        f"🆔 {user.id}\n"
        f"📆 {message.date}\n\n"
        f"رابط: tg://user?id={user.id}"
    )
    admin_id = int(os.getenv("ADMIN_ID"))
    if message.photo:
        await bot.send_photo(chat_id=admin_id, photo=message.photo[-1].file_id, caption=caption)
    elif message.document:
        await bot.send_document(chat_id=admin_id, document=message.document.file_id, caption=caption)

    await message.reply("📩 استلمنا الإثبات، بنراجعه ونرجع لك قريب.")

# عرض الحسابات
@dp.message_handler(commands=["accounts"])
async def send_accounts(message: types.Message):
    await message.answer("📱 كل حساباتي هنا:\nhttps://linktr.ee/odayhottt")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
