import os
import uuid
import shutil
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🎯 توکن ربات از BotFather
TOKEN = "7671390733:AAF00FEhDUISyxjLLKxp-MBVz57EPGP_VP0"

# 📁 مسیر ذخیره فایل‌ها
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 🔽 تابع دانلود آهنگ
def download_with_spotdl(spotify_link: str, folder: str) -> str:
    command = [
        "spotdl",
        spotify_link,
        "--output", os.path.join(folder, "{title} - {artist}.{output-ext}"),
        "--format", "mp3"
    ]
    subprocess.run(command, shell=False, check=True)
    mp3_files = [f for f in os.listdir(folder) if f.endswith(".mp3")]
    if mp3_files:
        return os.path.join(folder, mp3_files[0])
    else:
        raise FileNotFoundError("فایل mp3 پیدا نشد!")

# 🟢 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎶 سلام! لینک اسپاتیفای بفرست تا آهنگ رو برات بفرستم.")

# 📩 پیام‌های متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "open.spotify.com" in text:
        await update.message.reply_text("🔍 در حال پردازش لینک... لطفاً چند لحظه صبر کن.")

        # ساخت پوشه موقت
        uid = str(uuid.uuid4())
        temp_folder = os.path.join(DOWNLOAD_DIR, uid)
        os.makedirs(temp_folder, exist_ok=True)

        try:
            # دانلود
            file_path = download_with_spotdl(text, temp_folder)
            await update.message.reply_audio(audio=open(file_path, 'rb'))

        except Exception as e:
            await update.message.reply_text(f"❌ خطا در دانلود: {e}")

        finally:
            shutil.rmtree(temp_folder, ignore_errors=True)

    else:
        await update.message.reply_text("❗️ لطفاً لینک معتبر اسپاتیفای ارسال کن.")

# ▶️ اجرای ربات
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 ربات اجرا شد!")
    app.run_polling()

if __name__ == "__main__":
    main()
