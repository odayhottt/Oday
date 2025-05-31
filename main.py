from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.client.default import DefaultBotProperties
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 طرق الدفع")],
            [KeyboardButton(text="📬 تواصل معي")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        f"👋 هلا فيك في البوت الرسمي لـ {hbold('Prince Oday 🔥')}"
        " الاشتراك الشهري حالياً ٥٠٠ ريال فقط"
        "وش تحصل بعد الاشتراك؟"

        
"– أكثر من 50 فيلم كامل ✅"
        
"– جريء ومن إنتاجي الخاص 🎬"
        
"– كواليس وفعاليات من قلب التصوير 📹"
        
"– جودة أعلى… وتجربة مصممة لك أنت فقط ✨"

        "اختر أحد الخيارات تحت 👇",
        reply_markup=keyboard
    )

@dp.message(F.text == "💰 طرق الدفع")
async def payment_options(message: Message):
    await message.answer(
        "💳 طرق الدفع المتاحة:"
     
   "- 1- بطاقات نون (تقدر تشتريها من هالمواقع):"
        
"  • https://ar-saudi.likecard.com/online-shopping/noon/noon-ksa/"
        
"  • https://yougotagift.com/shop/ar-sa/brands/noon-gift-card-sa/"
        

"- 2- كريبتو (USDT - شبكة TRC20):"
        "  • https://nowpayments.io/payment/?iid=5028834055&paymentId=6382218207"
    )

@dp.message(F.text == "📬 تواصل معي")
async def contact_me(message: Message):
    await message.answer("📲 تقدر تتواصل معي مباشرة على تيليجرام:@odayh1")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())