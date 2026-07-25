# -*- coding: utf-8 -*-
"""
Inspira-S Tashkent Hotel — Telegram FAQ bot
3 tilli (UZ / RU / EN), til almashtirish funksiyasi bor.
Render.com'ning bepul (Web Service) tarifida ishlash uchun ichida
kichik Flask serveri ham ishlaydi (Render "Web Service" portni talab qiladi).
"""

import os
import io
import logging
import threading

from PIL import Image
from flask import Flask
from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputMediaPhoto,
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from translations import TEXTS, LANGUAGE_ORDER, ROOM_ORDER, AMENITY_ORDER

# Har bir xizmat turiga tegishli rasm fayllari (images/ papkasida).
# Bir nechta rasm bo'lsa, hammasi albom (media group) qilib yuboriladi.
AMENITY_IMAGES = {
    "spa_zone": ["spa_zone.jpg"],
    "pool": ["pool_1.jpg", "pool_2.jpg"],
    "hammam": ["hammam_1.jpg", "hammam_2.jpg"],
    "sauna": ["sauna.jpg"],
    "gym": ["gym_1.jpg", "gym_2.jpg"],
}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
DEFAULT_LANG = "uz"
IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# Foydalanuvchi tilini xotirada saqlaymiz: {chat_id: "uz"/"ru"/"en"}
user_lang = {}

# Telegram fotosurat sifatida yuboriladigan rasmlar uchun talablar:
# - eni + bo'yi yig'indisi 10000 pikseldan oshmasligi kerak
# - tomonlar nisbati 20:1 dan oshmasligi kerak
# Shu sababli har bir rasmni yuborishdan oldin xavfsiz o'lchamga moslaymiz.
MAX_PHOTO_DIMENSION = 1600  # eng katta tomon shu qiymatdan oshmasin
JPEG_QUALITY = 85

# Qayta ishlangan rasmlarni xotirada keshlab qo'yamiz, shunda har safar
# qayta hisoblashning hojati bo'lmaydi: {file_path: (mtime, jpeg_bytes)}
_photo_cache = {}


def get_safe_photo_bytes(path: str) -> bytes:
    """Berilgan rasm faylini Telegram talablariga mos (o'lchami xavfsiz,
    JPEG formatida) xom bayt (bytes) ko'rinishida qaytaradi. Natija xotirada
    keshlanadi, fayl o'zgarmagan ekan qayta ishlanmaydi."""
    mtime = os.path.getmtime(path)
    cached = _photo_cache.get(path)

    if cached and cached[0] == mtime:
        return cached[1]

    with Image.open(path) as img:
        img = img.convert("RGB")
        width, height = img.size
        largest_side = max(width, height)
        if largest_side > MAX_PHOTO_DIMENSION:
            scale = MAX_PHOTO_DIMENSION / largest_side
            new_size = (max(1, int(width * scale)), max(1, int(height * scale)))
            img = img.resize(new_size, Image.LANCZOS)

        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=JPEG_QUALITY, optimize=True)
        data = buffer.getvalue()

    _photo_cache[path] = (mtime, data)
    return data


def get_safe_photo(path: str) -> io.BytesIO:
    """Bitta rasm yuborish uchun (reply_photo) — har safar yangi BytesIO
    obyekti qaytaradi (fayl kabi, bir marta o'qiladi)."""
    data = get_safe_photo_bytes(path)
    buf = io.BytesIO(data)
    buf.name = os.path.basename(path)  # Telegram uchun fayl nomi/format maslahati
    return buf


def get_lang(chat_id: int) -> str:
    return user_lang.get(chat_id, DEFAULT_LANG)


def t(chat_id: int):
    """Shu foydalanuvchi tilidagi matnlar lug'atini qaytaradi."""
    return TEXTS[get_lang(chat_id)]


def main_menu_keyboard(chat_id: int) -> ReplyKeyboardMarkup:
    menu = t(chat_id)["menu"]
    buttons = [
        [menu["booking"], menu["rooms_photo"]],
        [menu["checkinout"], menu["breakfast"]],
        [menu["spa"], menu["services"]],
        [menu["location"], menu["contact"]],
        [menu["language"]],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def language_inline_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for code in LANGUAGE_ORDER:
        label = f"{TEXTS[code]['flag']} {TEXTS[code]['name']}"
        buttons.append([InlineKeyboardButton(label, callback_data=f"lang:{code}")])
    return InlineKeyboardMarkup(buttons)


def rooms_inline_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    rooms = t(chat_id)["rooms"]
    buttons = []
    for key in ROOM_ORDER:
        buttons.append(
            [InlineKeyboardButton(rooms[key]["name"], callback_data=f"room:{key}")]
        )
    return InlineKeyboardMarkup(buttons)


def amenities_inline_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    amenities = t(chat_id)["amenities"]
    buttons = []
    for key in AMENITY_ORDER:
        buttons.append(
            [InlineKeyboardButton(amenities[key]["name"], callback_data=f"amenity:{key}")]
        )
    return InlineKeyboardMarkup(buttons)


# ---------- Buyruqlar (Commands) ----------

async def send_welcome(message, chat_id: int):
    """Xush kelibsiz xabarini yuboradi. Agar mehmonxona bino rasmi (images/exterior.jpg)
    mavjud bo'lsa, uni rasm ostidagi izoh (caption) sifatida yuboradi, aks holda oddiy
    matn ko'rinishida yuboradi."""
    texts = t(chat_id)
    exterior_path = os.path.join(IMAGES_DIR, "exterior.jpg")

    try:
        if os.path.exists(exterior_path):
            await message.reply_photo(
                photo=get_safe_photo(exterior_path),
                caption=texts["welcome"],
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=main_menu_keyboard(chat_id),
            )
        else:
            await message.reply_text(
                texts["welcome"],
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=main_menu_keyboard(chat_id),
            )
    except Exception:
        logger.exception("Xush kelibsiz rasmini yuborishda xato: %s", exterior_path)
        await message.reply_text(
            texts["welcome"],
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=main_menu_keyboard(chat_id),
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in user_lang:
        # Til hali tanlanmagan bo'lsa — avval tilni so'raymiz
        await update.message.reply_text(
            TEXTS[DEFAULT_LANG]["choose_language"],
            reply_markup=language_inline_keyboard(),
        )
    else:
        await send_welcome(update.message, chat_id)


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(
        t(chat_id)["choose_language"],
        reply_markup=language_inline_keyboard(),
    )


# ---------- Asosiy menyu tugmalari (matnli xabarlar) ----------

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text
    texts = t(chat_id)
    menu = texts["menu"]

    # Matnni menyu kaliti bilan solishtiramiz
    if text == menu["language"]:
        await update.message.reply_text(
            texts["choose_language"], reply_markup=language_inline_keyboard()
        )
        return

    if text == menu["rooms_photo"]:
        await update.message.reply_text(
            texts["rooms"]["title"], reply_markup=rooms_inline_keyboard(chat_id)
        )
        return

    if text == menu["spa"]:
        # Avval qisqa matnli javob, so'ng rasmli xizmatlar galereyasi
        await update.message.reply_text(
            texts["answers"]["spa"], parse_mode=ParseMode.MARKDOWN
        )
        await update.message.reply_text(
            texts["amenities"]["title"], reply_markup=amenities_inline_keyboard(chat_id)
        )
        return

    key_map = {
        menu["booking"]: "booking",
        menu["checkinout"]: "checkinout",
        menu["breakfast"]: "breakfast",
        menu["services"]: "services",
        menu["location"]: "location",
        menu["contact"]: "contact",
    }

    if text in key_map:
        answer_key = key_map[text]
        await update.message.reply_text(
            texts["answers"][answer_key],
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=main_menu_keyboard(chat_id),
        )
        return

    # Tanilmagan matn kelsa — asosiy menyuni qayta ko'rsatamiz
    if chat_id not in user_lang:
        await update.message.reply_text(
            TEXTS[DEFAULT_LANG]["choose_language"],
            reply_markup=language_inline_keyboard(),
        )
    else:
        await send_welcome(update.message, chat_id)


# ---------- Inline tugmalar (CallbackQuery) ----------

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    await query.answer()

    data = query.data

    if data.startswith("lang:"):
        lang_code = data.split(":", 1)[1]
        user_lang[chat_id] = lang_code
        texts = TEXTS[lang_code]
        await query.message.reply_text(texts["language_changed"])
        await send_welcome(query.message, chat_id)
        return

    if data.startswith("room:"):
        room_key = data.split(":", 1)[1]
        texts = t(chat_id)
        room = texts["rooms"][room_key]
        caption = f"*{room['name']}*\n\n{room['desc']}"
        image_path = os.path.join(IMAGES_DIR, f"{room_key}.jpg")

        try:
            if os.path.exists(image_path):
                await query.message.reply_photo(
                    photo=get_safe_photo(image_path),
                    caption=caption,
                    parse_mode=ParseMode.MARKDOWN,
                )
            else:
                await query.message.reply_text(
                    f"{caption}\n\n{texts['photo_not_found']}",
                    parse_mode=ParseMode.MARKDOWN,
                )
        except Exception:
            logger.exception(
                "Xona rasmini yuborishda xato: room_key=%s, fayl=%s",
                room_key,
                image_path,
            )
            await query.message.reply_text(
                f"{caption}\n\n⚠️ Rasmni yuborishda texnik xatolik yuz berdi. "
                f"Iltimos keyinroq urinib ko'ring yoki administratorga xabar bering.",
                parse_mode=ParseMode.MARKDOWN,
            )

        await query.message.reply_text(
            texts["rooms"]["title"], reply_markup=rooms_inline_keyboard(chat_id)
        )
        return

    if data.startswith("amenity:"):
        amenity_key = data.split(":", 1)[1]
        texts = t(chat_id)
        amenity = texts["amenities"][amenity_key]
        caption = f"*{amenity['name']}*\n\n{amenity['desc']}"
        filenames = AMENITY_IMAGES.get(amenity_key, [])
        existing_paths = [
            os.path.join(IMAGES_DIR, fn)
            for fn in filenames
            if os.path.exists(os.path.join(IMAGES_DIR, fn))
        ]

        try:
            if not existing_paths:
                await query.message.reply_text(
                    f"{caption}\n\n{texts['photo_not_found']}",
                    parse_mode=ParseMode.MARKDOWN,
                )
            elif len(existing_paths) == 1:
                await query.message.reply_photo(
                    photo=get_safe_photo(existing_paths[0]),
                    caption=caption,
                    parse_mode=ParseMode.MARKDOWN,
                )
            else:
                media_group = []
                for index, path in enumerate(existing_paths):
                    if index == 0:
                        media_group.append(
                            InputMediaPhoto(
                                media=get_safe_photo(path),
                                caption=caption,
                                parse_mode=ParseMode.MARKDOWN,
                            )
                        )
                    else:
                        media_group.append(InputMediaPhoto(media=get_safe_photo(path)))
                await query.message.reply_media_group(media=media_group)
        except Exception:
            # Rasm yuborishda kutilmagan xato bo'lsa (masalan fayl hajmi katta,
            # buzilgan fayl va h.k.) — bot "jim" qolmasin, aniq xabar va log beramiz.
            logger.exception(
                "Amenity rasm(lar)ini yuborishda xato: amenity_key=%s, fayllar=%s",
                amenity_key,
                existing_paths,
            )
            await query.message.reply_text(
                f"{caption}\n\n⚠️ Rasmni yuborishda texnik xatolik yuz berdi. "
                f"Iltimos keyinroq urinib ko'ring yoki administratorga xabar bering.",
                parse_mode=ParseMode.MARKDOWN,
            )

        await query.message.reply_text(
            texts["amenities"]["title"], reply_markup=amenities_inline_keyboard(chat_id)
        )
        return


# ---------- Render uchun kichik Flask server (bot uxlab qolmasligi/portni ushlab turish uchun) ----------

flask_app = Flask(__name__)


@flask_app.route("/")
def health_check():
    return "Inspira-S Tashkent hotel bot is running ✅"


def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)


def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN topilmadi! Render'ning Environment bo'limida BOT_TOKEN "
            "nomli environment variable qo'shing."
        )

    # Flask serverni alohida threadda ishga tushiramiz (Render portni talab qiladi)
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .read_timeout(30)
        .write_timeout(30)
        .connect_timeout(30)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("language", language_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(CallbackQueryHandler(handle_callback))

    logger.info("Bot polling boshlandi...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
