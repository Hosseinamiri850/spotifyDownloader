# 📥 Spotify Downloader Bot

## Description
A simple Telegram bot that downloads Spotify tracks/playlists using `spotdl` and sends them as MP3 files.

⚠️ Disclaimer: This project is for educational purposes only. Users are responsible for complying with copyright laws.

## 🚀 Features

- Download Spotify song or playlist links
- Convert tracks to MP3 using spotdl
- Send downloaded audio files via Telegram bot
- Temporary storage cleanup after sending files

## 📦 Requirements

```txt
python-telegram-bot==20.8
spotdl==4.2.4
ffmpeg-python
```

Also make sure **ffmpeg** is installed and available in system PATH.

## 🛠 Installation

Clone repository:

```bash
git clone https://github.com/Hosseinamiri850/spotifyDownloader.git
cd spotifyDownloader
```

Create virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
# Windows
# venv\Scripts\activate

pip install -r requirements.txt
```

## ⚙️ Configuration

Open `spotifyDownloader.py` and replace the bot token:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

## ▶️ Run Bot

```bash
python spotifyDownloader.py
```

Then send `/start` and a Spotify link to bot.

## 📁 Project Structure

```
.
├── .gitignore
├── requirements.txt
├── render.yaml
└── spotifyDownloader.py
```

## ⚠️ Notes

- Ensure `ffmpeg` and `spotdl` are installed.
- Downloading copyrighted content without permission may be illegal.
- This project is for educational purposes.

---

⭐ If you like this project, consider giving a star!
