import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

class PaymentState(StatesGroup):
    waiting_for_proof = State()

@dp.message(F.text, commands="start")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.clear()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[types.KeyboardButton(text="🔐 فعل اشتراكي")]])
    text = (
        "👋 هلا فيك في البوت الرسمي لـ Odayhottt\n\n"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة\n\n"
        "💳 خيارات الدفع:\n"
        "- بطاقات نون مسبقة الدفع\n"
        "- كريبتو: USDT (TRC20)\n\n"
        "📲 للدفع بالكريبتو:\n"
        "🔗 https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "📦 اضغط الزر تحت تشوف تفاصيل الاشتراك 👇"
    )
    await message.answer(text, reply_markup=markup)

@dp.message(F.text == "🔐 فعل اشتراكي")
async def show_package(message: types.Message, state: FSMContext):
    await state.set_state(PaymentState.waiting_for_proof)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 اشتري بطاقة نون", url="https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/")],
        [InlineKeyboardButton(text="🎁 متجر نون الآخر", url="https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/")],
        [InlineKeyboardButton(text="🔗 ادفع كريبتو (USDT)", url="https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207")],
        [InlineKeyboardButton(text="✉️ أرسل الإثبات في الخاص", url="https://t.me/odayh1")]
    ])
    await message.answer(
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط\n\n"
        "وش تحصل بعد الاشتراك؟\n"
        "– أكثر من 50 فيلم كامل ✅\n"
        "– جريء ومن إنتاجي الخاص 🎬\n"
        "– كواليس وفعاليات من قلب التصوير 📹\n"
        "– جودة أعلى… وتجربة مصممة لك أنت فقط ✨\n\n"
        "✅ بعد الدفع، أرسل الإثبات على الخاص.",
        reply_markup=markup
    )

@dp.message(F.photo)
async def handle_proof(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != PaymentState.waiting_for_proof.state:
        await message.reply("❗ اضغط أولًا على '🔐 فعل اشتراكي' علشان نكمل.")
        return

    caption = (
        f"🔔 إثبات دفع جديد\n"
        f"👤 من: @{message.from_user.username or 'بدون يوزر'}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"رابط مباشر: tg://user?id={message.from_user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريباً.")
    await state.clear()

@dp.message(F.text, commands="accounts")
async def send_accounts(message: types.Message):
    await message.answer("📱 كل حساباتي بمكان واحد:\n🌐 https://linktr.ee/odayhottt")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
