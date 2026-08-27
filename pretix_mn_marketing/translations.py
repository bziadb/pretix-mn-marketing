"""Landing-page copy for every language pretix officially ships.

Each entry has the same set of keys. Missing / partial entries fall back to
English at render time (see views.LandingPageView.get_context_data).
"""

TRANSLATIONS = {
    # ---------- English (source) ----------
    'en': {
        'hello': 'Hello!',
        'welcome': 'Welcome to <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'This is where we run our ticketing and event platform. '
                      'If you want to buy a ticket, please follow the direct link '
                      'to your event.',
        'p_contact': 'For questions about digital content, sponsoring or custom '
                     'event solutions, please contact MN Marketing Network directly.',
        'enjoy': 'Enjoy!',
        'login': 'Login',
        'contact': 'Contact',
        'poweredby': 'powered by',
    },

    # ---------- German ----------
    'de': {
        'hello': 'Hallo!',
        'welcome': 'Willkommen bei <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Hier läuft unsere Ticketing- und Event-Plattform. Wenn du '
                      'ein Ticket kaufen möchtest, folge einfach dem direkten Link '
                      'zu deiner Veranstaltung.',
        'p_contact': 'Für Anfragen zu digitalen Inhalten, Sponsoring oder '
                     'individuellen Event-Lösungen erreichst du uns direkt bei '
                     'MN Marketing Network.',
        'enjoy': 'Viel Spaß!',
        'login': 'Login',
        'contact': 'Kontakt',
        'poweredby': 'betrieben mit',
    },
    'de-informal': {
        'hello': 'Hallo!',
        'welcome': 'Willkommen bei <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Hier läuft unsere Ticketing- und Event-Plattform. Wenn du '
                      'ein Ticket kaufen möchtest, folg einfach dem direkten Link '
                      'zu deiner Veranstaltung.',
        'p_contact': 'Fragen zu digitalen Inhalten, Sponsoring oder eigenen '
                     'Event-Lösungen? Schreib uns direkt bei MN Marketing Network.',
        'enjoy': 'Viel Spaß!',
        'login': 'Login',
        'contact': 'Kontakt',
        'poweredby': 'betrieben mit',
    },

    # ---------- Arabic (RTL) ----------
    'ar': {
        'hello': 'مرحبًا!',
        'welcome': 'أهلاً بكم في <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'هذه هي منصتنا للتذاكر والفعاليات. إذا كنت ترغب في شراء تذكرة، '
                      'يرجى اتباع الرابط المباشر للفعالية الخاصة بك.',
        'p_contact': 'للأسئلة حول المحتوى الرقمي أو الرعاية أو حلول الفعاليات المخصصة، '
                     'يرجى التواصل مع MN Marketing Network مباشرة.',
        'enjoy': 'استمتع!',
        'login': 'تسجيل الدخول',
        'contact': 'اتصل بنا',
        'poweredby': 'مدعوم من',
    },

    # ---------- Basque ----------
    'eu': {
        'hello': 'Kaixo!',
        'welcome': 'Ongi etorri <strong>MN Marketing Network e.U.</strong> plataformara',
        'p_platform': 'Hemen dabil gure sarrera- eta ekitaldi-plataforma. Sarrera bat '
                      'erosi nahi baduzu, jarraitu zure ekitaldirako esteka zuzenari.',
        'p_contact': 'Eduki digitalei, babesleei edo ekitaldi pertsonalizatuei buruzko '
                     'galderetarako, jar zaitez zuzenean harremanetan MN Marketing '
                     'Network-ekin.',
        'enjoy': 'Ondo pasa!',
        'login': 'Saioa hasi',
        'contact': 'Kontaktua',
        'poweredby': 'bidez',
    },

    # ---------- Catalan ----------
    'ca': {
        'hello': 'Hola!',
        'welcome': 'Benvingut/da a <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Aquí funciona la nostra plataforma de venda d’entrades i esdeveniments. '
                      'Si vols comprar una entrada, segueix l’enllaç directe al teu esdeveniment.',
        'p_contact': 'Per a preguntes sobre continguts digitals, patrocini o solucions '
                     'personalitzades d’esdeveniments, contacta directament amb MN Marketing Network.',
        'enjoy': 'Que gaudeixis!',
        'login': 'Entra',
        'contact': 'Contacte',
        'poweredby': 'amb la tecnologia de',
    },

    # ---------- Chinese (Simplified) ----------
    'zh-hans': {
        'hello': '你好！',
        'welcome': '欢迎来到 <strong>MN Marketing Network e.U.</strong>',
        'p_platform': '这里是我们的票务和活动平台。如需购票，请直接点击您活动的专属链接。',
        'p_contact': '如有关于数字内容、赞助或定制活动方案的问题，请直接联系 MN Marketing Network。',
        'enjoy': '祝您愉快！',
        'login': '登录',
        'contact': '联系我们',
        'poweredby': '技术支持',
    },

    # ---------- Chinese (Traditional) ----------
    'zh-hant': {
        'hello': '您好！',
        'welcome': '歡迎來到 <strong>MN Marketing Network e.U.</strong>',
        'p_platform': '這裡是我們的票務與活動平台。如需購票,請直接點擊您活動的專屬連結。',
        'p_contact': '如有關於數位內容、贊助或客製化活動方案的問題,請直接聯絡 MN Marketing Network。',
        'enjoy': '祝您愉快!',
        'login': '登入',
        'contact': '聯絡我們',
        'poweredby': '技術支援',
    },

    # ---------- Czech ----------
    'cs': {
        'hello': 'Ahoj!',
        'welcome': 'Vítejte v <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Zde běží naše platforma pro prodej vstupenek a pořádání akcí. '
                      'Chcete-li si koupit vstupenku, přejděte prosím na přímý odkaz '
                      'své akce.',
        'p_contact': 'Máte-li dotazy ohledně digitálního obsahu, sponzorství nebo '
                     'individuálních řešení akcí, kontaktujte prosím přímo '
                     'MN Marketing Network.',
        'enjoy': 'Užijte si!',
        'login': 'Přihlásit',
        'contact': 'Kontakt',
        'poweredby': 'poháněno',
    },

    # ---------- Croatian ----------
    'hr': {
        'hello': 'Bok!',
        'welcome': 'Dobrodošli u <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Ovdje se nalazi naša platforma za prodaju ulaznica i događaje. '
                      'Ako želite kupiti ulaznicu, slijedite izravan link do vašeg događaja.',
        'p_contact': 'Za pitanja o digitalnim sadržajima, sponzorstvima ili '
                     'prilagođenim rješenjima za događaje obratite se izravno '
                     'MN Marketing Networku.',
        'enjoy': 'Uživajte!',
        'login': 'Prijava',
        'contact': 'Kontakt',
        'poweredby': 'pokreće',
    },

    # ---------- Danish ----------
    'da': {
        'hello': 'Hej!',
        'welcome': 'Velkommen til <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Her kører vores billet- og eventplatform. Hvis du vil købe en '
                      'billet, så følg venligst det direkte link til dit arrangement.',
        'p_contact': 'For spørgsmål om digitalt indhold, sponsorater eller '
                     'skræddersyede løsninger, kontakt MN Marketing Network direkte.',
        'enjoy': 'God fornøjelse!',
        'login': 'Log ind',
        'contact': 'Kontakt',
        'poweredby': 'drevet af',
    },

    # ---------- Dutch ----------
    'nl': {
        'hello': 'Hallo!',
        'welcome': 'Welkom bij <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Hier draait ons ticketing- en evenementenplatform. Wil je een '
                      'ticket kopen, volg dan de directe link naar je evenement.',
        'p_contact': 'Voor vragen over digitale content, sponsoring of maatwerk-'
                     'evenementen kunt u rechtstreeks contact opnemen met '
                     'MN Marketing Network.',
        'enjoy': 'Veel plezier!',
        'login': 'Inloggen',
        'contact': 'Contact',
        'poweredby': 'mogelijk gemaakt door',
    },
    'nl-informal': {
        'hello': 'Hoi!',
        'welcome': 'Welkom bij <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Hier draait ons ticketing- en evenementenplatform. Wil je een '
                      'ticket kopen, volg dan de directe link naar je evenement.',
        'p_contact': 'Vragen over digitale content, sponsoring of eigen event-'
                     'oplossingen? Neem direct contact op met MN Marketing Network.',
        'enjoy': 'Veel plezier!',
        'login': 'Inloggen',
        'contact': 'Contact',
        'poweredby': 'mogelijk gemaakt door',
    },

    # ---------- French ----------
    'fr': {
        'hello': 'Bonjour !',
        'welcome': 'Bienvenue chez <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Voici notre plateforme de billetterie et d’événements. Pour '
                      'acheter un billet, veuillez suivre le lien direct vers votre '
                      'événement.',
        'p_contact': 'Pour toute question sur les contenus numériques, le parrainage '
                     'ou des solutions événementielles sur mesure, contactez '
                     'directement MN Marketing Network.',
        'enjoy': 'Profitez bien !',
        'login': 'Connexion',
        'contact': 'Contact',
        'poweredby': 'propulsé par',
    },

    # ---------- Finnish ----------
    'fi': {
        'hello': 'Hei!',
        'welcome': 'Tervetuloa <strong>MN Marketing Network e.U.</strong>:hun',
        'p_platform': 'Tämä on lippukauppa- ja tapahtuma-alustamme. Jos haluat ostaa '
                      'lipun, seuraa suoraa linkkiä tapahtumaasi.',
        'p_contact': 'Kysymyksiä digitaalisesta sisällöstä, sponsoroinnista tai '
                     'räätälöidyistä tapahtumaratkaisuista? Ota yhteyttä suoraan '
                     'MN Marketing Networkiin.',
        'enjoy': 'Nauti!',
        'login': 'Kirjaudu',
        'contact': 'Yhteystiedot',
        'poweredby': 'käyttövoimana',
    },

    # ---------- Galician ----------
    'gl': {
        'hello': 'Ola!',
        'welcome': 'Benvido/a a <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Aquí funciona a nosa plataforma de venda de entradas e eventos. '
                      'Se queres mercar unha entrada, segue a ligazón directa ao teu evento.',
        'p_contact': 'Para preguntas sobre contido dixital, patrocinio ou solucións '
                     'personalizadas de eventos, contacta directamente con '
                     'MN Marketing Network.',
        'enjoy': 'Que o desfrutes!',
        'login': 'Iniciar sesión',
        'contact': 'Contacto',
        'poweredby': 'con tecnoloxía de',
    },

    # ---------- Greek ----------
    'el': {
        'hello': 'Γεια σας!',
        'welcome': 'Καλώς ήρθατε στην <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Εδώ λειτουργεί η πλατφόρμα μας για εισιτήρια και εκδηλώσεις. '
                      'Αν θέλετε να αγοράσετε εισιτήριο, ακολουθήστε τον απευθείας '
                      'σύνδεσμο για την εκδήλωσή σας.',
        'p_contact': 'Για ερωτήσεις σχετικά με ψηφιακό περιεχόμενο, χορηγίες ή '
                     'εξατομικευμένες λύσεις εκδηλώσεων, επικοινωνήστε απευθείας '
                     'με την MN Marketing Network.',
        'enjoy': 'Καλή διασκέδαση!',
        'login': 'Σύνδεση',
        'contact': 'Επικοινωνία',
        'poweredby': 'με τη δύναμη του',
    },

    # ---------- Hebrew (RTL) ----------
    'he': {
        'hello': 'שלום!',
        'welcome': 'ברוכים הבאים ל־<strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'כאן פועלת פלטפורמת הכרטיסים והאירועים שלנו. אם ברצונך לרכוש '
                      'כרטיס, יש לעקוב אחר הקישור הישיר לאירוע שלך.',
        'p_contact': 'לשאלות בנוגע לתוכן דיגיטלי, חסויות או פתרונות אירועים בהתאמה '
                     'אישית, ניתן ליצור קשר ישירות עם MN Marketing Network.',
        'enjoy': 'תיהנו!',
        'login': 'התחברות',
        'contact': 'צור קשר',
        'poweredby': 'מופעל על ידי',
    },

    # ---------- Indonesian ----------
    'id': {
        'hello': 'Halo!',
        'welcome': 'Selamat datang di <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Di sini kami menjalankan platform tiket dan acara kami. '
                      'Jika Anda ingin membeli tiket, silakan ikuti tautan langsung '
                      'ke acara Anda.',
        'p_contact': 'Untuk pertanyaan tentang konten digital, sponsor, atau solusi '
                     'acara khusus, silakan hubungi MN Marketing Network secara langsung.',
        'enjoy': 'Selamat menikmati!',
        'login': 'Masuk',
        'contact': 'Kontak',
        'poweredby': 'didukung oleh',
    },

    # ---------- Italian ----------
    'it': {
        'hello': 'Ciao!',
        'welcome': 'Benvenuto/a in <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Qui funziona la nostra piattaforma di biglietteria ed eventi. '
                      'Se desideri acquistare un biglietto, segui il link diretto '
                      'al tuo evento.',
        'p_contact': 'Per domande su contenuti digitali, sponsorizzazioni o soluzioni '
                     'evento personalizzate, contatta direttamente MN Marketing Network.',
        'enjoy': 'Buon divertimento!',
        'login': 'Accedi',
        'contact': 'Contatto',
        'poweredby': 'con tecnologia',
    },

    # ---------- Japanese ----------
    'ja': {
        'hello': 'こんにちは！',
        'welcome': '<strong>MN Marketing Network e.U.</strong> へようこそ',
        'p_platform': 'ここでは、当社のチケット販売・イベントプラットフォームを運営しています。'
                      'チケットをご購入の際は、イベントへの直接リンクからお進みください。',
        'p_contact': 'デジタルコンテンツ、スポンサーシップ、カスタムイベントに関するお問い合わせは、'
                     'MN Marketing Network まで直接ご連絡ください。',
        'enjoy': 'お楽しみください！',
        'login': 'ログイン',
        'contact': 'お問い合わせ',
        'poweredby': 'Powered by',
    },

    # ---------- Latvian ----------
    'lv': {
        'hello': 'Sveiki!',
        'welcome': 'Laipni lūdzam <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Šeit darbojas mūsu biļešu un pasākumu platforma. Ja vēlaties '
                      'iegādāties biļeti, lūdzu, sekojiet tiešajai saitei uz jūsu '
                      'pasākumu.',
        'p_contact': 'Jautājumiem par digitālo saturu, sponsorēšanu vai '
                     'individuāliem pasākumu risinājumiem sazinieties tieši ar '
                     'MN Marketing Network.',
        'enjoy': 'Baudiet!',
        'login': 'Pieteikties',
        'contact': 'Kontakti',
        'poweredby': 'darbina',
    },

    # ---------- Norwegian Bokmål ----------
    'nb-no': {
        'hello': 'Hei!',
        'welcome': 'Velkommen til <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Her kjører vi vår billett- og arrangementsplattform. Ønsker '
                      'du å kjøpe billett, følg gjerne den direkte lenken til '
                      'arrangementet ditt.',
        'p_contact': 'For spørsmål om digitalt innhold, sponsing eller '
                     'skreddersydde arrangementsløsninger, kontakt MN Marketing '
                     'Network direkte.',
        'enjoy': 'God fornøyelse!',
        'login': 'Logg inn',
        'contact': 'Kontakt',
        'poweredby': 'drevet av',
    },

    # ---------- Polish ----------
    'pl': {
        'hello': 'Cześć!',
        'welcome': 'Witamy w <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Tutaj działa nasza platforma do sprzedaży biletów i obsługi '
                      'wydarzeń. Aby kupić bilet, kliknij bezpośredni link do swojego '
                      'wydarzenia.',
        'p_contact': 'W sprawie pytań dotyczących treści cyfrowych, sponsoringu lub '
                     'niestandardowych rozwiązań eventowych prosimy o bezpośredni '
                     'kontakt z MN Marketing Network.',
        'enjoy': 'Miłej zabawy!',
        'login': 'Zaloguj się',
        'contact': 'Kontakt',
        'poweredby': 'napędzane przez',
    },

    # ---------- Portuguese (Portugal) ----------
    'pt-pt': {
        'hello': 'Olá!',
        'welcome': 'Bem-vindo/a à <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'É aqui que corre a nossa plataforma de venda de bilhetes e '
                      'eventos. Para comprar um bilhete, siga o link direto para o '
                      'seu evento.',
        'p_contact': 'Para questões sobre conteúdo digital, patrocínio ou soluções '
                     'personalizadas de eventos, contacte diretamente a '
                     'MN Marketing Network.',
        'enjoy': 'Divirta-se!',
        'login': 'Entrar',
        'contact': 'Contacto',
        'poweredby': 'com tecnologia de',
    },

    # ---------- Portuguese (Brazil) ----------
    'pt-br': {
        'hello': 'Olá!',
        'welcome': 'Bem-vindo(a) à <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'É aqui que roda nossa plataforma de ingressos e eventos. Para '
                      'comprar um ingresso, siga o link direto para o seu evento.',
        'p_contact': 'Para dúvidas sobre conteúdo digital, patrocínio ou soluções '
                     'personalizadas de eventos, entre em contato diretamente com '
                     'a MN Marketing Network.',
        'enjoy': 'Aproveite!',
        'login': 'Entrar',
        'contact': 'Contato',
        'poweredby': 'desenvolvido com',
    },

    # ---------- Romanian ----------
    'ro': {
        'hello': 'Salut!',
        'welcome': 'Bine ai venit la <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Aici rulează platforma noastră de bilete și evenimente. '
                      'Dacă vrei să cumperi un bilet, urmează linkul direct '
                      'către evenimentul tău.',
        'p_contact': 'Pentru întrebări despre conținut digital, sponsorizări '
                     'sau soluții personalizate pentru evenimente, contactează '
                     'direct MN Marketing Network.',
        'enjoy': 'Distracție plăcută!',
        'login': 'Autentificare',
        'contact': 'Contact',
        'poweredby': 'susținut de',
    },

    # ---------- Russian ----------
    'ru': {
        'hello': 'Привет!',
        'welcome': 'Добро пожаловать в <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Здесь работает наша платформа продажи билетов и организации '
                      'мероприятий. Чтобы купить билет, перейдите по прямой ссылке '
                      'на ваше мероприятие.',
        'p_contact': 'По вопросам цифрового контента, спонсорства или '
                     'индивидуальных решений для мероприятий обращайтесь напрямую '
                     'в MN Marketing Network.',
        'enjoy': 'Наслаждайтесь!',
        'login': 'Войти',
        'contact': 'Контакты',
        'poweredby': 'работает на',
    },

    # ---------- Slovak ----------
    'sk': {
        'hello': 'Ahoj!',
        'welcome': 'Vitajte v <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Tu beží naša platforma pre predaj vstupeniek a organizáciu '
                      'podujatí. Ak si chcete kúpiť vstupenku, prejdite na priamy '
                      'odkaz na vaše podujatie.',
        'p_contact': 'Ak máte otázky týkajúce sa digitálneho obsahu, sponzoringu '
                     'alebo prispôsobených riešení pre podujatia, kontaktujte '
                     'MN Marketing Network priamo.',
        'enjoy': 'Užite si to!',
        'login': 'Prihlásiť sa',
        'contact': 'Kontakt',
        'poweredby': 'poháňané',
    },

    # ---------- Slovenian ----------
    'sl': {
        'hello': 'Zdravo!',
        'welcome': 'Dobrodošli v <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Tu deluje naša platforma za prodajo vstopnic in dogodkov. '
                      'Če želite kupiti vstopnico, sledite neposredni povezavi '
                      'do svojega dogodka.',
        'p_contact': 'Za vprašanja o digitalni vsebini, sponzoriranju ali '
                     'prilagojenih rešitvah za dogodke se obrnite neposredno na '
                     'MN Marketing Network.',
        'enjoy': 'Uživajte!',
        'login': 'Prijava',
        'contact': 'Stik',
        'poweredby': 'poganja',
    },

    # ---------- Spanish ----------
    'es': {
        'hello': '¡Hola!',
        'welcome': 'Bienvenido/a a <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Aquí funciona nuestra plataforma de venta de entradas y eventos. '
                      'Si quieres comprar una entrada, sigue el enlace directo a tu evento.',
        'p_contact': 'Para consultas sobre contenido digital, patrocinio o soluciones '
                     'personalizadas para eventos, contacta directamente con '
                     'MN Marketing Network.',
        'enjoy': '¡Que lo disfrutes!',
        'login': 'Acceder',
        'contact': 'Contacto',
        'poweredby': 'con tecnología de',
    },
    'es-419': {
        'hello': '¡Hola!',
        'welcome': 'Bienvenido/a a <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Aquí funciona nuestra plataforma de venta de entradas y eventos. '
                      'Si quieres comprar una entrada, sigue el enlace directo a tu evento.',
        'p_contact': 'Para consultas sobre contenido digital, patrocinios o soluciones '
                     'personalizadas para eventos, contacta directamente con '
                     'MN Marketing Network.',
        'enjoy': '¡Que lo disfrutes!',
        'login': 'Ingresar',
        'contact': 'Contacto',
        'poweredby': 'con tecnología de',
    },

    # ---------- Swedish ----------
    'sv': {
        'hello': 'Hej!',
        'welcome': 'Välkommen till <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Här kör vi vår biljett- och eventplattform. Om du vill köpa '
                      'en biljett, följ den direkta länken till ditt evenemang.',
        'p_contact': 'För frågor om digitalt innehåll, sponsring eller '
                     'skräddarsydda evenemangslösningar, kontakta MN Marketing '
                     'Network direkt.',
        'enjoy': 'Ha så kul!',
        'login': 'Logga in',
        'contact': 'Kontakt',
        'poweredby': 'drivs av',
    },

    # ---------- Turkish ----------
    'tr': {
        'hello': 'Merhaba!',
        'welcome': '<strong>MN Marketing Network e.U.</strong>’ye hoş geldiniz',
        'p_platform': 'Bilet ve etkinlik platformumuz burada çalışıyor. Bilet almak '
                      'istiyorsanız lütfen etkinliğinize ait doğrudan bağlantıyı '
                      'takip edin.',
        'p_contact': 'Dijital içerik, sponsorluk veya özel etkinlik çözümleri '
                     'hakkında sorularınız için doğrudan MN Marketing Network ile '
                     'iletişime geçin.',
        'enjoy': 'İyi eğlenceler!',
        'login': 'Giriş yap',
        'contact': 'İletişim',
        'poweredby': 'destekleyen',
    },

    # ---------- Ukrainian ----------
    'uk': {
        'hello': 'Привіт!',
        'welcome': 'Ласкаво просимо до <strong>MN Marketing Network e.U.</strong>',
        'p_platform': 'Тут працює наша платформа продажу квитків і організації подій. '
                      'Щоб придбати квиток, перейдіть за прямим посиланням на ваш захід.',
        'p_contact': 'Щодо цифрового контенту, спонсорства або індивідуальних '
                     'рішень для заходів звертайтеся безпосередньо до MN Marketing '
                     'Network.',
        'enjoy': 'Насолоджуйтесь!',
        'login': 'Увійти',
        'contact': 'Контакти',
        'poweredby': 'працює на',
    },
}

# Languages that render right-to-left (used to add dir="rtl" on the <html> tag).
RTL_LANGS = {'ar', 'he'}

# Contact URL per language. Any language not listed falls back to the English URL.
_CONTACT_DEFAULT_EN = 'https://www.m-n.marketing/en/request-information'
CONTACT_URLS = {
    'en':          'https://www.m-n.marketing/en/request-information',
    'de':          'https://www.m-n.marketing/de/informationen-anfordern',
    'de-informal': 'https://www.m-n.marketing/de/informationen-anfordern',
}


def get_contact_url(language_code: str) -> str:
    if not language_code:
        return _CONTACT_DEFAULT_EN
    code = language_code.lower()
    if code in CONTACT_URLS:
        return CONTACT_URLS[code]
    base = code.split('-')[0]
    if base in CONTACT_URLS:
        return CONTACT_URLS[base]
    return _CONTACT_DEFAULT_EN


def get_translation(language_code: str) -> dict:
    """Look up translation for the requested language, falling back to English."""
    if not language_code:
        return TRANSLATIONS['en']
    code = language_code.lower()
    if code in TRANSLATIONS:
        return TRANSLATIONS[code]
    # Fall back to the base language (e.g. "de-at" -> "de", "en-gb" -> "en").
    base = code.split('-')[0]
    if base in TRANSLATIONS:
        return TRANSLATIONS[base]
    return TRANSLATIONS['en']
