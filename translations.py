# -*- coding: utf-8 -*-
"""
Barcha bot matnlari shu yerda saqlanadi: o'zbek (kirill), rus, ingliz.
Yangi savol/til qo'shish kerak bo'lsa, faqat shu faylni tahrirlash kifoya.
"""

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
            "checkinout": "⏰ Кириш / Чиқиш",
            "breakfast": "🍽 Нонушта ва ресторан",
            "spa": "🏊 СПА ва фитнес",
            "services": "🛎 Қўшимча хизматлар",
            "location": "📍 Манзил ва трансфер",
            "rooms_photo": "🖼 Хоналар расмлари",
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
                "Inspira-S меҳмонхонасида Standard (бир/икки кишилик), Twin, Superior ва "
                "Suite (Люкс) тоифасидаги шинам хоналар мавжуд. Барча хоналар кондиционер, "
                "Smart TV, сейф, мини-бар ва иш столи билан таъминланган.\n\n"
                "Хоналарнинг расмларини кўриш учун «🖼 Хоналар расмлари» тугмасини босинг."
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
            "contact": (
                "📞 *Администратор билан боғланиш*\n\n"
                "Хонадаги ички телефон орқали «0» тугмасини босиб ёки бевосита қуйидаги "
                "рақамга қўнғироқ қилиб қабул бўлими билан боғланишингиз мумкин:\n\n"
                "☎️ +998 (71) XXX-XX-XX"
            ),
        },
        "rooms": {
            "title": "🖼 Илтимос, хона тоифасини танланг:",
            "back_to_rooms": "🔙 Хоналар рўйхатига",
            "standard": {
                "name": "Standard",
                "desc": "Қулай бир ёки икки кишилик хона. Кондиционер, Smart TV, сейф ва иш столи мавжуд.",
            },
            "twin": {
                "name": "Twin",
                "desc": "Иккита алоҳида каравотли хона — дугона ёки ҳамкасблар билан дам олиш учун қулай.",
            },
            "superior": {
                "name": "Superior",
                "desc": "Кенгроқ майдонли, замонавий дизайндаги қулай хона.",
            },
            "suite": {
                "name": "Suite (Люкс)",
                "desc": "Меҳмонхонанинг энг юқори тоифадаги хонаси — алоҳида ётоқхона ва меҳмон хонаси билан.",
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
            "checkinout": "⏰ Заезд / Выезд",
            "breakfast": "🍽 Завтрак и ресторан",
            "spa": "🏊 СПА и фитнес",
            "services": "🛎 Дополнительные услуги",
            "location": "📍 Локация и трансфер",
            "rooms_photo": "🖼 Фото номеров",
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
                "В отеле Inspira-S представлены комфортабельные номера различных категорий: "
                "Standard (Одноместный/Двухместный), Twin, Superior и Suite (Люкс). Все "
                "номера оснащены кондиционером, Smart TV, сейфом, мини-баром и рабочим "
                "столом.\n\n"
                "Чтобы посмотреть фото номеров, нажмите «🖼 Фото номеров»."
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
            "contact": (
                "📞 *Связь с администратором*\n\n"
                "Вы можете позвонить на рецепцию из номера по внутреннему номеру «0» или "
                "напрямую по телефону:\n\n"
                "☎️ +998 (71) XXX-XX-XX"
            ),
        },
        "rooms": {
            "title": "🖼 Пожалуйста, выберите категорию номера:",
            "back_to_rooms": "🔙 К списку номеров",
            "standard": {
                "name": "Standard",
                "desc": "Уютный одно- или двухместный номер. Кондиционер, Smart TV, сейф и рабочий стол.",
            },
            "twin": {
                "name": "Twin",
                "desc": "Номер с двумя отдельными кроватями — удобен для друзей или коллег.",
            },
            "superior": {
                "name": "Superior",
                "desc": "Просторный номер с современным дизайном.",
            },
            "suite": {
                "name": "Suite (Люкс)",
                "desc": "Номер высшей категории — с отдельной спальней и гостиной зоной.",
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
            "checkinout": "⏰ Check-in / Check-out",
            "breakfast": "🍽 Breakfast & Restaurant",
            "spa": "🏊 SPA & Fitness",
            "services": "🛎 Additional services",
            "location": "📍 Location & Transfer",
            "rooms_photo": "🖼 Room photos",
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
                "Inspira-S offers comfortable rooms in several categories: Standard "
                "(single/double), Twin, Superior, and Suite. All rooms are equipped with "
                "air conditioning, a Smart TV, a safe, a mini-bar and a work desk.\n\n"
                "Tap “🖼 Room photos” to see pictures of each room type."
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
            "contact": (
                "📞 *Contact front desk*\n\n"
                "You can call the front desk from your room by dialing “0”, or directly "
                "at:\n\n"
                "☎️ +998 (71) XXX-XX-XX"
            ),
        },
        "rooms": {
            "title": "🖼 Please choose a room category:",
            "back_to_rooms": "🔙 Back to room list",
            "standard": {
                "name": "Standard",
                "desc": "A cozy single or double room with air conditioning, Smart TV, safe and a work desk.",
            },
            "twin": {
                "name": "Twin",
                "desc": "A room with two separate beds — great for friends or colleagues traveling together.",
            },
            "superior": {
                "name": "Superior",
                "desc": "A more spacious room with a modern design.",
            },
            "suite": {
                "name": "Suite",
                "desc": "Our top-category room with a separate bedroom and living area.",
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
ROOM_ORDER = ["standard", "twin", "superior", "suite"]

# Xizmatlar (SPA/fitness) tartibi (rasm galereyasi uchun)
AMENITY_ORDER = ["spa_zone", "pool", "hammam", "sauna", "gym"]

