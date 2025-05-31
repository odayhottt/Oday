import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.markdown import hbold
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.runner import run_polling

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(CommandStart())
async def welcome(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text="🔐 فعل اشتراكي")]
    ])
    await message.answer(
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}\n\n"
        "🔥 هنا تقدر تشترك بسهولة ونساعدك بخيارات دفع مرنة\n\n"
        "💳 خيارات الدفع:\n"
        "- بطاقات نون مسبقة الدفع\n"
        "- كريبتو: USDT (TRC20)\n\n"
        "📲 للدفع بالكريبتو:\n"
        "🔗 https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207\n\n"
        "⏳ أو اضغط الزر تحت تشوف تفاصيل الباقة وطريقة الدفع 👇",
        reply_markup=markup
    )

@router.message(F.text == "🔐 فعل اشتراكي")
async def show_package(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text="✅ أرسلت الإثبات")]
    ])
    await message.answer(
        "📦 الاشتراك الشهري بـ ٥٠٠ ريال فقط\n\n"
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
        "✅ بعد الدفع، اضغط الزر تحت وأرسل الإثبات.",
        reply_markup=markup
    )

@router.message(F.text == "✅ أرسلت الإثبات")
async def ask_for_proof(message: Message):
    await message.answer("📸 أرسل الآن صورة أو سكرين لإثبات الدفع.\n"
                         "⏳ بعد المراجعة اليدوية، يتم التفعيل.")

@router.message(F.photo)
async def forward_proof(message: Message):
    user = message.from_user
    caption = (
        f"🔔 إثبات دفع جديد\n"
        f"👤 من: @{user.username or 'بدون يوزر'}\n"
        f"🆔 ID: {user.id}\n"
        f"⏱ الوقت: {message.date}\n"
        f"رابط مباشر: tg://user?id={user.id}"
    )
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
    await message.reply("📩 تم استلام الإثبات، بنراجع ونتواصل معك قريباً.")

if __name__ == "__main__":
    run_polling(dp, bot=bot)