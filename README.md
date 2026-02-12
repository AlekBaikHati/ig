# Vidzilla 🤖

**Simple bot for downloading videos from social media**

## What can the bot do?

- Downloads videos from 8 popular platforms
- Sends videos in two formats (video + file)
- No download limits
- No payments or subscriptions required
- Simple and clean interface

## Supported platforms:
YouTube • Instagram • TikTok • Facebook • Twitter • Pinterest • Reddit • Vimeo

---

## How to use?

1. **Find a video link** on any supported platform
2. **Send the link to the bot** in Telegram
3. **Get your video** in two formats:
   - 🎥 Video (for watching)
   - 📁 File (for downloading)

That's it! 😊

## Bot commands:
/start - Start using the bot

## For developers

If you want to run the bot yourself:

1. **Install Python 3.8+**
2. **Clone the repository:**
   ```bash
   git clone https://github.com/zerox9dev/Vidzilla.git
   cd Vidzilla
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file** with settings
5. **(Optional) Configure backup channel**

   In your `.env` file set:

   ```env
   DATABASE_CHANNEL_ID=-1001234567890
   ```

   - Use the ID of a channel where the bot is **admin**
   - Every successfully downloaded video will be **also sent to this channel** as backup

6. **Run the bot locally:**
   ```bash
   python bot.py
   ```

## Deploy to Koyeb (FREE plan)

1. Push this project to your own Git repository (GitHub, GitLab, dll.).
2. Di dashboard Koyeb, buat **New Web Service** dan pilih repository tersebut.
3. Pada bagian **Build & Run**:
   - `Build command` biarkan default (otomatis pakai `pip install -r requirements.txt` jika menggunakan Python buildpack), atau atur manual sesuai kebutuhan.
   - `Run command` gunakan:

     ```bash
     python bot.py
     ```

4. Di bagian **Environment variables**, isi:
   - `BOT_TOKEN` — token bot Telegram
   - `WEBHOOK_PATH` — misalnya `/webhook`
   - `WEBHOOK_URL` — URL aplikasi Koyeb, contoh `https://nama-app-anda.koyeb.app`
   - `MONGODB_URI`, `MONGODB_DB_NAME`, `MONGODB_USERS_COLLECTION`
   - `ADMIN_IDS`
   - (Opsional) `DATABASE_CHANNEL_ID` untuk backup channel

   Koyeb otomatis mengatur variabel `PORT`; bot sudah membaca `PORT` dari environment, jadi **tidak perlu diubah**.

5. Setelah deploy sukses, bot akan:
   - Menjalankan server `aiohttp` di `0.0.0.0:$PORT`
   - Meng-set webhook ke `WEBHOOK_URL + WEBHOOK_PATH`
   - Menjawab request GET ke `/` (root) sehingga bisa dipakai untuk ping.

## Menjaga bot tetap hidup dengan UptimeRobot

1. Buka `https://uptimerobot.com` dan buat akun gratis.
2. Buat **HTTP(s) monitor** baru:
   - `URL to monitor`: `https://nama-app-anda.koyeb.app/`
   - `Monitoring interval`: 5 menit (standar gratis).
3. Simpan monitor. UptimeRobot akan rutin memanggil endpoint `/` yang sudah disiapkan di bot, sehingga aplikasi di Koyeb tidak cepat sleep.

## License

MIT License - see [LICENSE](LICENSE) file
