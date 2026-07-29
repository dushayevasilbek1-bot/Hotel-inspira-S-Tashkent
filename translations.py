# -*- coding: utf-8 -*-
"""
Barcha bot matnlari shu yerda saqlanadi: o'zbek (kirill), rus, ingliz.
Yangi savol/til qo'shish kerak bo'lsa, faqat shu faylni tahrirlash kifoya.
"""

# Xonani onlayn band qilish uchun sayt manzili
BOOKING_URL = "https://inspira-s.com/"

TEXTS = {
    "uz": {
        "flag": "🇺🇿",
        "name": "O'zbekcha",
        "welcome": (
            "Ассалому алайкум! 👋\n\n"
            "*Inspira-S Tashkent* (4★) меҳмонхонасининг расмий чат-ботига хуш келибсиз!\n\n"
            "Мен сизга қуйидагилар бўйича ёрдам бераман:\n"
            "• Хоналар ва уларнинг тоифалари\n"
            "• Кириш / чиқиш вақтлари\n"
            "• Нонушта, СПА ва бошқа хизматлар\n"
            "• Манзил ва трансфер\n"
            "• Администратор билан боғланиш\n\n"
            "Қуйидаги тугмалардан бирини танланг 👇"
        ),
        "choose_language": "🌐 Илтимос, тилни танланг:",
        "language_changed": "✅ Тил ўзгартирилди!",
        "menu": {
            "booking": "🏨 Хоналар тоифалари",
            "book_now": "🛏 Хонани брон қилиш",
            "checkinout": "⏰ Кириш / Чиқиш",
            "breakfast": "🍽 Нонушта ва ресторан",
            "spa": "🏊 СПА ва фитнес",
            "services": "🛎 Қўшимча хизматлар",
            "location": "📍 Манзил ва трансфер",
            "travel_agency": "✈️ Travel Agency",
            "contact": "📞 Администратор билан боғланиш",
            "language": "🌐 Тилни ўзгартириш",
            "back": "🔙 Орқага",
        },
        "answers": {
            "checkinout": (
                "⏰ *Кириш / Чиқиш вақтлари*\n\n"
                "❓ *Кириш ва чиқиш вақти қандай?*\n"
                "Меҳмонхонага жойлашиш (Check-in) вақти — 14:00 дан, хонани топшириш "
                "(Check-out) вақти — 12:00 гача.\n\n"
                "❓ *Эрта жойлашиш ёки кеч чиқиш мумкинми?*\n"
                "Ҳа, бўш хоналар мавжуд бўлса, эрта жойлашиш ёки кеч чиқиш мумкин. "
                "Қўшимча тўлов 50% (14:00 гача ёки 12:00дан кейин) ёки 100% (эрта тонгда "
                "кафолатланган жойлашиш учун) ташкил этади. Аниқ маълумот учун қабул бўлими "
                "билан боғланинг."
            ),
            "booking": (
                "🏨 *Хоналар тоифалари*\n\n"
                "Inspira-S меҳмонхонасида турли эҳтиёж ва бюджетга мос шинам хоналар мавжуд. "
                "Барча хоналар кондиционер, Smart TV, сейф, мини-бар ва иш столи билан "
                "таъминланган.\n\n"
                "Ҳар бир тоифанинг расми ва тавсифини кўриш учун қуйидаги рўйхатдан бирини "
                "танланг 👇"
            ),
            "book_now": (
                "🛏 *Хонани онлайн брон қилиш*\n\n"
                "Энг қулай нарх ва бўш хоналарни кўриш учун расмий сайтимизга ўтинг:"
            ),
            "breakfast": (
                "🍽 *Нонушта ва ресторан*\n\n"
                "Ҳа! Яшаш нархига швед столи форматидаги нонушта киритилган. Нонушта "
                "ресторанда соат 07:00 дан 10:30 гача тортиқ этилади."
            ),
            "spa": (
                "🏊 *СПА ва фитнес*\n\n"
                "Ҳа, меҳмонларимиз учун ёпиқ бассейн, сауна, ҳаммом ва фитнес-зал хизмат "
                "кўрсатади. Иш вақти: ҳар куни соат 08:00 дан 22:00 гача."
            ),
            "services": (
                "🛎 *Қўшимча хизматлар*\n\n"
                "📶 *Wi-Fi ва автотураргоҳ:*\n"
                "Ҳа, меҳмонхонамизнинг барча ҳудудида юқори тезликдаги бепул Wi-Fi ва бепул "
                "қўриқланадиган автотураргоҳ мавжуд.\n\n"
                "📋 *Хорижий фуқароларни рўйхатга олиш:*\n"
                "Ҳа, биз хорижий фуқаролар учун меҳмонхонада яшаш даври учун расмий "
                "вақтинчалик рўйхатдан ўтиш хизматини бепул тақдим этамиз."
            ),
            "location": (
                "📍 *Манзил ва трансфер*\n\n"
                "Inspira-S меҳмонхонаси Тошкент марказида жойлашган. Халқаро аэропортгача "
                "бўлган масофа тахминан 7 км (автомобилда 15-20 дақиқа). Шунингдек, биз сиз "
                "учун индивидуал трансфер хизматини ташкил қилишимиз мумкин."
            ),
            "travel_agency": (
                "✈️ *Ҳамкоримиз — Travel Agency (hhh.travel)*\n\n"
                "Экскурсия, трансфер, чипта ёки виза бўйича ёрдамга муҳтож бўлсангиз, "
                "ишончли ҳамкоримиз хизматларидан фойдаланишингиз мумкин:\n\n"
                "🏨 Меҳмонхоналарни брон қилиш\n"
                "🗺 Экскурсиялар\n"
                "🚐 Трансфер хизматлари\n"
                "🙋 Индивидуал ёрдам\n"
                "✈️ Авиа / темир йўл чипталари\n"
                "🛂 Виза бўйича кўмак\n\n"
                "📍 Ўзбекистон бўйлаб хизмат кўрсатамиз\n\n"
                "📞 +998 90 033 88 80\n"
                "✉️ hhh.travel1@gmail.com\n"
                "🌐 www.hhhtravel.uz"
            ),
            "contact": (
                "📞 *Администратор билан боғланиш*\n\n"
                "Хонадаги ички телефон орқали «0» тугмасини босиб ёки бевосита қуйидаги "
                "рақамга қўнғироқ қилиб қабул бўлими билан боғланишингиз мумкин:\n\n"
                "☎️ +998 (71) XXX-XX-XX"
            ),
        },
        "book_now_button": "🌐 Сайтга ўтиш",
        "rooms": {
            "title": "🖼 Илтимос, хона тоифасини танланг:",
            "back_to_rooms": "🔙 Хоналар рўйхатига",
            "twin_room": {
                "name": "Twin Room",
                "desc": "Иккита алоҳида каравотли қулай хона — дугона ёки ҳамкасблар билан сафар учун идеал.",
            },
            "double_room": {
                "name": "Double Room",
                "desc": "Бир катта кровать билан жиҳозланган, икки киши учун қулай хона.",
            },
            "deluxe_room": {
                "name": "Deluxe Room",
                "desc": "Кенгроқ майдон ва замонавий дизайндаги юқори даражадаги қулайликка эга хона.",
            },
            "junior_suite": {
                "name": "Junior Suite",
                "desc": "Ётоқ ва дам олиш зонаси бирлаштирилган, кенгроқ ва шинам хона.",
            },
            "corner_suite": {
                "name": "Corner Suite",
                "desc": "Бурчакда жойлашган, панорама ойналари билан кенг ёритилган хона.",
            },
            "suite_apartment": {
                "name": "Suite Apartment",
                "desc": "Алоҳида ётоқхона ва меҳмонхонага эга, энг юқори тоифадаги апартамент туридаги хона.",
            },
        },
        "photo_not_found": "🙏 Кечирасиз, бу хонанинг расми ҳозирча юкланмаган. Тез орада қўшамиз.",
        "amenities": {
            "title": "🖼 Илтимос, хизмат турини танланг:",
            "back_to_list": "🔙 Хизматлар рўйхатига",
            "spa_zone": {
                "name": "СПА зона",
                "desc": "Тинчланиш ва дам олиш учун махсус СПА зонаси — гидромассаж ванналари ва ором берувчи атмосфера билан.",
            },
            "pool": {
                "name": "Ёпиқ бассейн",
                "desc": "Йил бўйи очиқ бўлган иссиқ ёпиқ бассейн — сузиш ва дам олиш учун қулай.",
            },
            "hammam": {
                "name": "Турк ҳаммоми",
                "desc": "Анъанавий турк ҳаммоми — тошли исситгич ва миллий безак билан.",
            },
            "sauna": {
                "name": "Фин саунаси",
                "desc": "Иссиқ ёғочли фин саунаси — мушакларни бўшаштириш ва организмни тозалаш учун.",
            },
            "gym": {
                "name": "Фитнес зал",
                "desc": "Замонавий тренажёрлар билан жиҳозланган кенг фитнес зал.",
            },
        },
    },
    "ru": {
        "flag": "🇷🇺",
        "name": "Русский",
        "welcome": (
            "Здравствуйте! 👋\n\n"
            "Добро пожаловать в официальный чат-бот отеля *Inspira-S Tashkent* (4★)!\n\n"
            "Я помогу вам узнать:\n"
            "• Категории номеров\n"
            "• Время заезда / выезда\n"
            "• О завтраке, СПА и других услугах\n"
            "• Расположение и трансфер\n"
            "• Как связаться с администратором\n\n"
            "Выберите один из пунктов меню ниже 👇"
        ),
        "choose_language": "🌐 Пожалуйста, выберите язык:",
        "language_changed": "✅ Язык изменён!",
        "menu": {
            "booking": "🏨 Категории номеров",
            "book_now": "🛏 Забронировать номер",
            "checkinout": "⏰ Заезд / Выезд",
            "breakfast": "🍽 Завтрак и ресторан",
            "spa": "🏊 СПА и фитнес",
            "services": "🛎 Дополнительные услуги",
            "location": "📍 Локация и трансфер",
            "travel_agency": "✈️ Travel Agency",
            "contact": "📞 Связь с администратором",
            "language": "🌐 Изменить язык",
            "back": "🔙 Назад",
        },
        "answers": {
            "checkinout": (
                "⏰ *Время заезда и выезда*\n\n"
                "❓ *Во сколько заезд и выезд в отеле?*\n"
                "Стандартное время заезда (Check-in) — с 14:00. Время выезда (Check-out) — "
                "до 12:00.\n\n"
                "❓ *Возможен ли ранний заезд или поздний выезд?*\n"
                "Да, ранний заезд или поздний выезд возможен при наличии свободных номеров. "
                "Доплата составляет 50% от стоимости суток (до 14:00 или после 12:00) или "
                "100% при гарантированном раннем заезде ранним утром. Пожалуйста, свяжитесь "
                "с рецепцией для уточнения деталей."
            ),
            "booking": (
                "🏨 *Категории номеров*\n\n"
                "В отеле Inspira-S представлены комфортабельные номера на любой вкус и "
                "бюджет. Все номера оснащены кондиционером, Smart TV, сейфом, мини-баром и "
                "рабочим столом.\n\n"
                "Чтобы увидеть фото и описание каждой категории, выберите из списка ниже 👇"
            ),
            "book_now": (
                "🛏 *Онлайн-бронирование номера*\n\n"
                "Чтобы увидеть лучшие цены и свободные номера, перейдите на наш "
                "официальный сайт:"
            ),
            "breakfast": (
                "🍽 *Завтрак и ресторан*\n\n"
                "Да! В стоимость проживания включен богатый завтрак по системе «шведский "
                "стол» (Buffet Breakfast), который подается в нашем ресторане с 07:00 до "
                "10:30."
            ),
            "spa": (
                "🏊 *СПА и фитнес*\n\n"
                "Да, к услугам гостей наш оздоровительный комплекс: крытый бассейн, сауна, "
                "хаммам и фитнес-зал. Часы работы: ежедневно с 08:00 до 22:00."
            ),
            "services": (
                "🛎 *Дополнительные услуги*\n\n"
                "📶 *Wi-Fi и парковка:*\n"
                "Да, для всех проживающих гостей предоставляется бесплатный "
                "высокоскоростной Wi-Fi на всей территории отеля, а также бесплатная "
                "охраняемая парковка.\n\n"
                "📋 *Регистрация иностранных граждан:*\n"
                "Да, мы предоставляем официальную временную регистрацию для иностранных "
                "граждан на весь период проживания в нашем отеле бесплатно."
            ),
            "location": (
                "📍 *Локация и трансфер*\n\n"
                "Отель Inspira-S расположен в центре Ташкента. Расстояние до Международного "
                "аэропорта Ташкента — около 7 км (15–20 минут на авто). Мы также можем "
                "организовать для вас индивидуальный трансфер."
            ),
            "travel_agency": (
                "✈️ *Наш партнёр — Travel Agency (hhh.travel)*\n\n"
                "Если вам нужна помощь с экскурсиями, трансфером, билетами или визой, вы "
                "можете обратиться к нашему надёжному партнёру:\n\n"
                "🏨 Бронирование проживания\n"
                "🗺 Экскурсии\n"
                "🚐 Трансферы\n"
                "🙋 Индивидуальная поддержка\n"
                "✈️ Авиа/ж-д билеты\n"
                "🛂 Визовая поддержка\n\n"
                "📍 По всему Узбекистану\n\n"
                "📞 +998 90 033 88 80\n"
                "✉️ hhh.travel1@gmail.com\n"
                "🌐 www.hhhtravel.uz"
            ),
            "contact": (
                "📞 *Связь с администратором*\n\n"
                "Вы можете позвонить на рецепцию из номера по внутреннему номеру «0» или "
                "напрямую по телефону:\n\n"
                "☎️ +998 (71) XXX-XX-XX"
            ),
        },
        "book_now_button": "🌐 Перейти на сайт",
        "rooms": {
            "title": "🖼 Пожалуйста, выберите категорию номера:",
            "back_to_rooms": "🔙 К списку номеров",
            "twin_room": {
                "name": "Twin Room",
                "desc": "Номер с двумя отдельными кроватями — идеален для друзей или коллег.",
            },
            "double_room": {
                "name": "Double Room",
                "desc": "Уютный номер с одной большой кроватью для двоих.",
            },
            "deluxe_room": {
                "name": "Deluxe Room",
                "desc": "Просторный номер повышенной комфортности с современным дизайном.",
            },
            "junior_suite": {
                "name": "Junior Suite",
                "desc": "Просторный номер с объединённой зоной сна и отдыха.",
            },
            "corner_suite": {
                "name": "Corner Suite",
                "desc": "Угловой номер с панорамными окнами и большим количеством естественного света.",
            },
            "suite_apartment": {
                "name": "Suite Apartment",
                "desc": "Номер апартаментного типа высшей категории с отдельной спальней и гостиной.",
            },
        },
        "photo_not_found": "🙏 Извините, фото этого номера пока не загружено. Скоро добавим.",
        "amenities": {
            "title": "🖼 Пожалуйста, выберите услугу:",
            "back_to_list": "🔙 К списку услуг",
            "spa_zone": {
                "name": "СПА-зона",
                "desc": "Специальная зона для релаксации — с гидромассажными ваннами и расслабляющей атмосферой.",
            },
            "pool": {
                "name": "Крытый бассейн",
                "desc": "Тёплый крытый бассейн, доступный круглый год — идеально для плавания и отдыха.",
            },
            "hammam": {
                "name": "Турецкий хаммам",
                "desc": "Традиционный турецкий хаммам с каменным подогревом и национальным орнаментом.",
            },
            "sauna": {
                "name": "Финская сауна",
                "desc": "Тёплая деревянная финская сауна — для расслабления мышц и очищения организма.",
            },
            "gym": {
                "name": "Фитнес-зал",
                "desc": "Просторный фитнес-зал с современными тренажёрами.",
            },
        },
    },
    "en": {
        "flag": "🇬🇧",
        "name": "English",
        "welcome": (
            "Hello! 👋\n\n"
            "Welcome to the official chat-bot of *Inspira-S Tashkent* Hotel (4★)!\n\n"
            "I can help you with:\n"
            "• Room categories\n"
            "• Check-in / Check-out times\n"
            "• Breakfast, SPA and other services\n"
            "• Location and transfer\n"
            "• Contacting our front desk\n\n"
            "Please choose an option below 👇"
        ),
        "choose_language": "🌐 Please choose a language:",
        "language_changed": "✅ Language changed!",
        "menu": {
            "booking": "🏨 Room categories",
            "book_now": "🛏 Book a room",
            "checkinout": "⏰ Check-in / Check-out",
            "breakfast": "🍽 Breakfast & Restaurant",
            "spa": "🏊 SPA & Fitness",
            "services": "🛎 Additional services",
            "location": "📍 Location & Transfer",
            "travel_agency": "✈️ Travel Agency",
            "contact": "📞 Contact front desk",
            "language": "🌐 Change language",
            "back": "🔙 Back",
        },
        "answers": {
            "checkinout": (
                "⏰ *Check-in / Check-out times*\n\n"
                "❓ *What time is check-in and check-out?*\n"
                "Standard check-in time is from 14:00. Check-out time is until 12:00.\n\n"
                "❓ *Is early check-in or late check-out possible?*\n"
                "Yes, early check-in or late check-out is possible subject to room "
                "availability. An extra charge of 50% of the nightly rate applies (before "
                "14:00 or after 12:00), or 100% for a guaranteed early-morning check-in. "
                "Please contact the front desk for details."
            ),
            "booking": (
                "🏨 *Room categories*\n\n"
                "Inspira-S offers comfortable rooms to suit every need and budget. All "
                "rooms are equipped with air conditioning, a Smart TV, a safe, a mini-bar "
                "and a work desk.\n\n"
                "To see a photo and description of each category, choose one from the list "
                "below 👇"
            ),
            "book_now": (
                "🛏 *Book a room online*\n\n"
                "To see the best rates and room availability, please visit our official "
                "website:"
            ),
            "breakfast": (
                "🍽 *Breakfast & Restaurant*\n\n"
                "Yes! Breakfast is included in the room rate — a rich buffet breakfast "
                "served in our restaurant daily from 07:00 to 10:30."
            ),
            "spa": (
                "🏊 *SPA & Fitness*\n\n"
                "Yes, guests can enjoy our wellness complex: indoor pool, sauna, hammam and "
                "fitness center. Opening hours: daily from 08:00 to 22:00."
            ),
            "services": (
                "🛎 *Additional services*\n\n"
                "📶 *Wi-Fi & Parking:*\n"
                "Yes, free high-speed Wi-Fi is available throughout the hotel for all "
                "guests, along with free guarded parking.\n\n"
                "📋 *Foreign guest registration:*\n"
                "Yes, we provide official temporary registration for foreign citizens for "
                "the entire duration of their stay, free of charge."
            ),
            "location": (
                "📍 *Location & Transfer*\n\n"
                "Inspira-S Hotel is located in the center of Tashkent. The distance to "
                "Tashkent International Airport is about 7 km (15–20 minutes by car). We "
                "can also arrange an individual transfer for you."
            ),
            "travel_agency": (
                "✈️ *Our partner — Travel Agency (hhh.travel)*\n\n"
                "If you need help with excursions, transfers, tickets or a visa, you can "
                "reach out to our trusted partner:\n\n"
                "🏨 Booking accommodations\n"
                "🗺 Excursions\n"
                "🚐 Transport\n"
                "🙋 Individual support\n"
                "✈️ Avia / Railway tickets\n"
                "🛂 Visa support\n\n"
                "📍 Across all of Uzbekistan\n\n"
                "📞 +998 90 033 88 80\n"
                "✉️ hhh.travel1@gmail.com\n"
                "🌐 www.hhhtravel.uz"
            ),
            "contact": (
                "📞 *Contact front desk*\n\n"
                "You can call the front desk from your room by dialing “0”, or directly "
                "at:\n\n"
                "☎️ +998 (71) XXX-XX-XX"
            ),
        },
        "book_now_button": "🌐 Visit website",
        "rooms": {
            "title": "🖼 Please choose a room category:",
            "back_to_rooms": "🔙 Back to room list",
            "twin_room": {
                "name": "Twin Room",
                "desc": "A room with two separate beds — perfect for friends or colleagues traveling together.",
            },
            "double_room": {
                "name": "Double Room",
                "desc": "A cozy room with one large bed for two guests.",
            },
            "deluxe_room": {
                "name": "Deluxe Room",
                "desc": "A more spacious room with an enhanced comfort level and modern design.",
            },
            "junior_suite": {
                "name": "Junior Suite",
                "desc": "A spacious room combining a sleeping area and a lounge area.",
            },
            "corner_suite": {
                "name": "Corner Suite",
                "desc": "A corner room with panoramic windows and plenty of natural light.",
            },
            "suite_apartment": {
                "name": "Suite Apartment",
                "desc": "Our top-category apartment-style room with a separate bedroom and living room.",
            },
        },
        "photo_not_found": "🙏 Sorry, the photo for this room hasn't been uploaded yet. We'll add it soon.",
        "amenities": {
            "title": "🖼 Please choose a facility:",
            "back_to_list": "🔙 Back to facilities list",
            "spa_zone": {
                "name": "SPA zone",
                "desc": "A dedicated relaxation zone with hydro-massage baths and a soothing atmosphere.",
            },
            "pool": {
                "name": "Indoor pool",
                "desc": "A warm indoor pool available year-round — perfect for swimming and relaxing.",
            },
            "hammam": {
                "name": "Turkish hammam",
                "desc": "A traditional Turkish hammam with heated stone platforms and national ornamentation.",
            },
            "sauna": {
                "name": "Finnish sauna",
                "desc": "A warm wooden Finnish sauna — great for muscle relaxation and detox.",
            },
            "gym": {
                "name": "Fitness center",
                "desc": "A spacious fitness center equipped with modern gym machines.",
            },
        },
    },
}

# Til tanlash tugmalari uchun tartib
LANGUAGE_ORDER = ["uz", "ru", "en"]

# Xona tasniflari tartibi (rasm galereyasi uchun)
ROOM_ORDER = [
    "twin_room",
    "double_room",
    "deluxe_room",
    "junior_suite",
    "corner_suite",
    "suite_apartment",
]

# Xizmatlar (SPA/fitness) tartibi (rasm galereyasi uchun)
AMENITY_ORDER = ["spa_zone", "pool", "hammam", "sauna", "gym"]
