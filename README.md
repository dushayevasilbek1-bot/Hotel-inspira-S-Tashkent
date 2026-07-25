[README.md](https://github.com/user-attachments/files/30371958/README.md)
# Inspira-S Tashkent — Telegram FAQ Bot

3 tilli (🇺🇿 O'zbek, 🇷🇺 Rus, 🇬🇧 Ingliz) mehmonxona chat-boti. Foydalanuvchi istalgan vaqtda
tilni o'zgartira oladi. GitHub + Render.com orqali **butunlay bepul** deploy qilinadi.

## 📁 Fayllar tuzilmasi

```
hotel-bot/
├── bot.py              # botning asosiy kodi
├── translations.py     # barcha matnlar (uz/ru/en) — shu yerdan tahrirlanadi
├── requirements.txt    # kerakli kutubxonalar
├── Procfile             # Render/Heroku uchun ishga tushirish buyrug'i
├── runtime.txt          # Python versiyasi
├── render.yaml          # Render uchun avtomatik sozlama (ixtiyoriy)
├── .gitignore
└── images/
    ├── README.md
    ├── standard.jpg     # (o'zingiz qo'shasiz)
    ├── twin.jpg         # (o'zingiz qo'shasiz)
    ├── superior.jpg     # (o'zingiz qo'shasiz)
    └── suite.jpg        # (o'zingiz qo'shasiz)
```

---

## 1-qadam: Telegram botini yaratish (BotFather)

1. Telegram'da **@BotFather** ni oching.
2. `/newbot` buyrug'ini yuboring.
3. Bot uchun nom bering (masalan: `Inspira-S Tashkent Hotel Bot`).
4. Username bering — oxiri `bot` bilan tugashi kerak (masalan: `inspira_s_hotel_bot`).
5. BotFather sizga **TOKEN** beradi — bu shunga o'xshaydi:
   `123456789:AAExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   **Bu tokenni hech kimga bermang va saqlab qo'ying — keyingi qadamlarda kerak bo'ladi.**

---

## 2-qadam: Loyihani GitHub'ga yuklash

1. [github.com](https://github.com) da bepul akkaunt oching (agar yo'q bo'lsa).
2. Yangi **repository** yarating (masalan: `inspira-s-hotel-bot`), **Public** yoki **Private** — farqi yo'q.
3. Ushbu papkadagi barcha fayllarni (`bot.py`, `translations.py`, `requirements.txt`,
   `Procfile`, `runtime.txt`, `render.yaml`, `.gitignore`, `images/` papkasi) shu repository'ga yuklang.

   Buni ikki xil usulda qilishingiz mumkin:

   **A) GitHub veb-sayti orqali (kompyuterda git bo'lmasa ham bo'ladi):**
   - Repository sahifasida **"Add file" → "Upload files"** tugmasini bosing.
   - Barcha fayllarni sudrab tashlang (drag-and-drop), so'ng **"Commit changes"** tugmasini bosing.
   - `images` papkasini alohida yaratish uchun: "Add file" → "Create new file" → nomini
     `images/standard.jpg`... deb yozsangiz, GitHub avtomatik `images` papkasini yaratadi
     (lekin rasm faylini shu usulda emas, "Upload files" orqali yuklash tavsiya etiladi).

   **B) Git orqali (agar kompyuteringizda git o'rnatilgan bo'lsa):**
   ```bash
   cd hotel-bot
   git init
   git add .
   git commit -m "Inspira-S hotel bot"
   git branch -M main
   git remote add origin https://github.com/USERNAME/inspira-s-hotel-bot.git
   git push -u origin main
   ```

---

## 3-qadam: Render.com'da bepul deploy qilish

1. [render.com](https://render.com) saytiga kiring, GitHub akkauntingiz bilan ro'yxatdan o'ting.
2. Dashboard'da **"New +" → "Web Service"** ni tanlang.
3. GitHub repository'ingizni ulang (`inspira-s-hotel-bot`).
4. Sozlamalarni quyidagicha kiriting:
   - **Name:** istalgan nom (masalan: `inspira-s-hotel-bot`)
   - **Region:** eng yaqinini tanlang
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - **Instance Type:** **Free** ✅
5. **"Advanced" → "Add Environment Variable"** bo'limida:
   - **Key:** `BOT_TOKEN`
   - **Value:** BotFather'dan olgan tokeningiz
6. **"Create Web Service"** tugmasini bosing. Render avtomatik ravishda loyihani yig'ib,
   ishga tushiradi (bir necha daqiqa vaqt oladi).
7. Loglarda `Bot polling boshlandi...` degan yozuvni ko'rsangiz — bot ishga tushdi! ✅

> Eslatma: agar `render.yaml` faylidan foydalanmoqchi bo'lsangiz, Render dashboard'da
> **"New +" → "Blueprint"** ni tanlab, repository'ni ko'rsatsangiz ham bo'ladi — sozlamalar
> avtomatik olinadi, faqat `BOT_TOKEN` qiymatini qo'lda kiritishingiz kerak bo'ladi.

---

## 4-qadam: Botni Telegram'da sinab ko'rish

Telegram'da botingizni toping (username orqali) va `/start` bosing. Til tanlash tugmalari
chiqadi, keyin asosiy menyu ko'rinadi.

---

## ⚠️ Bepul tarif haqida muhim eslatma

Render'ning **Free** tarifidagi Web Service'lar **15 daqiqa faoliyatsizlikdan keyin "uxlab
qoladi"** va keyingi so'rovda ~30-60 soniya ichida qayta uyg'onadi. Oddiy FAQ bot uchun bu
odatda muammo emas (foydalanuvchi xabar yozganda bot bir necha soniyada javob beradi), lekin
agar botni doimiy "uyg'oq" holatda ushlab turmoqchi bo'lsangiz:

- Bepul **[UptimeRobot](https://uptimerobot.com)** xizmatidan foydalaning: u har 5 daqiqada
  bot manzilingizga (masalan `https://inspira-s-hotel-bot.onrender.com`) so'rov yuborib,
  uni uyg'oq saqlab turadi. Bot ichidagi Flask server (`bot.py` da) aynan shu maqsad uchun
  qo'shilgan — u `/` manzilida "Inspira-S Tashkent hotel bot is running ✅" deb javob beradi.

Bu — Telegram botlarni Render'ning bepul tarifida ishlatishning standart va keng tarqalgan usuli.

---

## 🖼 Xona rasmlarini qo'shish

`images/` papkasiga quyidagi nomlar bilan JPG rasm qo'shing:

- `standard.jpg`
- `twin.jpg`
- `superior.jpg`
- `suite.jpg`

Rasm qo'shgach GitHub'ga push qiling (yoki "Upload files" orqali yuklang) — Render avtomatik
qayta deploy qiladi (agar avtomatik bo'lmasa, Render dashboard'da **"Manual Deploy" → "Deploy
latest commit"** tugmasini bosing). Rasm mavjud bo'lmagan xona uchun bot faqat matn (nom +
tavsif) yuboradi, xatolik chiqmaydi.

---

## ✏️ Matnlarni tahrirlash

Barcha savol-javoblar, tugma nomlari va tillar `translations.py` faylida joylashgan.
Narxlarni, telefon raqamini (`+998 (71) XXX-XX-XX`), yoki matnlarni o'zgartirish uchun shu
faylni tahrirlab, GitHub'ga qayta yuklash yetarli.

## ➕ Yangi savol/kategoriya qo'shish

1. `translations.py` da har uchala til (`uz`, `ru`, `en`) ichidagi `menu` va `answers`
   lug'atlariga yangi kalit va matn qo'shing.
2. `bot.py` dagi `main_menu_keyboard()` funksiyasida yangi tugmani joylashtiring va
   `handle_text()` ichidagi `key_map` ga qo'shing.
