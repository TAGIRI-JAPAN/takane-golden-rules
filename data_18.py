from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
NHG  = r("日本語","に ほん ご")
SHIN = r("新聞","しん ぶん")
YOMU = r("読","よ")+"む"
KAKU = r("書","か")+"く"
TABR = r("食","た")+"べる"
ANI  = r("兄","あに")
OSHI = r("教","おし")+"える"
RYO  = r("料理","りょう り")
NIH  = r("日本","に ほん")
UTAU = r("歌","うた")+"う"
UTA  = r("歌","うた")
KARE = r("彼","かれ")
DEN  = r("電話","でん わ")
SUK  = r("少","すこ")+"し"
ZEN  = r("全部","ぜん ぶ")
HITO = r("一","ひと")+"つ"

_N1 = "NOTE:① どうし：じしょけい＋「ことが できます」　　　② めいし：そのまま「が できます」"
_N3 = (f"NOTE:じしょけい：{r('読','よ')}みます→{YOMU}　/　{r('書','か')}きます→{KAKU}　/　"
       f"{r('食','た')}べます→{TABR}　/　します→する　/　{r('来','き')}ます→{r('来','く')}る")

# ---------------------------------------------------------------- 18-1 基本
P14 = dict(
  no="18", tag=None,
  title_jp="〜（する ことが）できます",
  title_ro='〜 (suru koto ga) dekimasu &nbsp;|&nbsp; I can 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 පුළුවන්</span>',
  basic=(f"{W}は はしで ごはんを {TABR}ことが できます。","Watashi wa hashi de gohan wo taberu koto ga dekimasu.",
         "I can eat with chopsticks.","මට චොප්ස්ටික්ස් වලින් කන්න පුළුවන්."),
  use=(f'できる ことや{r("能力","のう りょく")}を{r("言","い")}います。{r("形","かたち")}が 2つ あります。'
       f'「する」が つく めいしは「〜が できます」、ほかの どうしは じしょけい＋「ことが できます」です。',
       'It says what you are able to do. There are two forms: <b>〜 ga dekimasu</b> for nouns that '
       'take <b>suru</b>, and dictionary form + <b>koto ga dekimasu</b> for other verbs.',
       'කරන්න පුළුවන් දේ කියන එක — <b>dekimasu</b> = පුළුවන්, <b>dekimasen</b> = බැහැ. '
       'ආකාර දෙකයි: <b>suru</b> නාම පදවලට <b>〜 ga dekimasu</b>; අනිත් ක්‍රියා පදවලට '
       'ශබ්දකෝෂ ආකාරය ＋ <b>koto ga dekimasu</b>.'),
  pattern=[_N1,
           [(r("読","よ")+"みます","yomimasu"),"TO",(f"{YOMU} ことが できます","yomu koto ga dekimasu",True)],
           [(RYO,"ryouri"),"TO",(f"{RYO}が できます","ryouri ga dekimasu",True)],
           _N3],
  examples=[
    (f"{NHG}の {SHIN}を {YOMU}ことが できます。","Nihongo no shinbun wo yomu koto ga dekimasu.","I can read a Japanese newspaper.","මට ජපන් පුවත්පතක් කියවන්න පුළුවන්."),
    (f"{NHG}で メールを {KAKU}ことが できます。","Nihongo de meeru wo kaku koto ga dekimasu.","I can write an email in Japanese.","මට ජපන් භාෂාවෙන් ඊමේල් එකක් ලියන්න පුළුවන්."),
    (f"はしで ごはんを {TABR}ことが できます。","Hashi de gohan wo taberu koto ga dekimasu.","I can eat with chopsticks.","මට චොප්ස්ටික්ස් වලින් කන්න පුළුවන්."),
    (f"{ANI}は {NHG}を {OSHI}ことが できます。","Ani wa nihongo wo oshieru koto ga dekimasu.","My older brother can teach Japanese.","මගේ අයියාට ජපන් භාෂාව උගන්නන්න පුළුවන්."),
    (f"{NIH}の {UTA}を {UTAU}ことが できます。","Nihon no uta wo utau koto ga dekimasu.","I can sing a Japanese song.","මට ජපන් සිංදුවක් කියන්න පුළුවන්."),
    (f"{W}は {RYO}が できます。","Watashi wa ryouri ga dekimasu.","I can cook.","මට උයන්න පුළුවන්."),
    (f"{W}は アルバイトが できます。","Watashi wa arubaito ga dekimasu.","I can work part-time.","මට අර්ධකාලීන රැකියාව කරන්න පුළුවන්."),
  ],
  foot="〜（する ことが）できます",
)

# ---------------------------------------------------------------- 18-2 否定
P14N = dict(
  no="18", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜（する ことが）できません",
  title_ro='〜 (suru koto ga) dekimasen &nbsp;|&nbsp; I cannot 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 බැහැ</span>',
  basic=(f"{W}は はしで ごはんを {TABR}ことが できません。","Watashi wa hashi de gohan wo taberu koto ga dekimasen.",
         "I cannot eat with chopsticks.","මට චොප්ස්ටික්ස් වලින් කන්න බැහැ."),
  use=(f'「できます」を「できません」に かえるだけです。'
       f'まえの{r("部分","ぶ ぶん")}（じしょけい＋ことが）は{r("変","か")}わりません。'
       f'「まだ できません」と{r("言","い")}うと「これから できるように なる」{r("気持","き も")}ちが{r("伝","つた")}わります。',
       'Just change <b>dekimasu</b> to <b>dekimasen</b>. The part before it does not change. '
       'Saying <b>mada dekimasen</b> ("I cannot do it yet") sounds more positive.',
       '<b>dekimasu</b> එක <b>dekimasen</b> කරන්න විතරයි. ඊට කලින් කොටස වෙනස් වෙන්නේ නැහැ. '
       '<b>mada dekimasen</b> ("තාම බැහැ") කිව්වොත් ඉදිරියේදී පුළුවන් වෙයි කියන හැඟීම එනවා.'),
  pattern=[[("〜ことが","~ koto ga"),("できます","dekimasu")],
           "ARROW",
           [("〜ことが","~ koto ga"),("できません","dekimasen",True)],
           "NOTE:まだ できません = තාම බැහැ（not yet — but I will be able to）"],
  examples=[
    (f"{NHG}の {SHIN}を {YOMU}ことが できません。","Nihongo no shinbun wo yomu koto ga dekimasen.","I cannot read a Japanese newspaper.","මට ජපන් පුවත්පතක් කියවන්න බැහැ."),
    (f"{NHG}で メールを {KAKU}ことが できません。","Nihongo de meeru wo kaku koto ga dekimasen.","I cannot write an email in Japanese.","මට ජපන් භාෂාවෙන් ඊමේල් එකක් ලියන්න බැහැ."),
    (f"はしで ごはんを {TABR}ことが できません。","Hashi de gohan wo taberu koto ga dekimasen.","I cannot eat with chopsticks.","මට චොප්ස්ටික්ස් වලින් කන්න බැහැ."),
    (f"{ANI}は {NHG}を {OSHI}ことが できません。","Ani wa nihongo wo oshieru koto ga dekimasen.","My older brother cannot teach Japanese.","මගේ අයියාට ජපන් භාෂාව උගන්නන්න බැහැ."),
    (f"{NIH}の {UTA}を {UTAU}ことが できません。","Nihon no uta wo utau koto ga dekimasen.","I cannot sing a Japanese song.","මට ජපන් සිංදුවක් කියන්න බැහැ."),
    (f"{W}は {RYO}が できません。","Watashi wa ryouri ga dekimasen.","I cannot cook.","මට උයන්න බැහැ."),
    (f"{W}は まだ アルバイトが できません。","Watashi wa mada arubaito ga dekimasen.","I cannot work part-time yet.","මට තාම අර්ධකාලීන රැකියාව කරන්න බැහැ."),
  ],
  foot="〜（する ことが）できません",
)

# ---------------------------------------------------------------- 18-3 疑問
P14Q = dict(
  no="18", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜（する ことが）できますか？",
  title_ro='〜 (suru koto ga) dekimasu ka &nbsp;|&nbsp; Can you 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 පුළුවන්ද?</span>',
  basic=(f"あなたは はしで ごはんを {TABR}ことが できますか。","Anata wa hashi de gohan wo taberu koto ga dekimasu ka.",
         "Can you eat with chopsticks?","ඔබට චොප්ස්ටික්ස් වලින් කන්න පුළුවන්ද?"),
  use=(f'「できます」のうしろに「か」をつけるだけです。'
       f'めんせつや アルバイトの{r("面接","めん せつ")}で「〜が できますか」は かならず{r("聞","き")}かれます。'
       f'{r("答","こた")}えを{r("用意","よう い")}して おきましょう。',
       'Just add <b>ka</b> after <b>dekimasu</b>. '
       'You will always be asked <b>〜 ga dekimasu ka</b> in a job or part-time interview, '
       'so it is worth preparing your answer.',
       '<b>dekimasu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       'රැකියා සම්මුඛ පරීක්ෂණයකදී <b>〜 ga dekimasu ka</b> අනිවාර්යයෙන් අහනවා. '
       'උත්තරය කලින් සූදානම් කරගන්න.'),
  pattern=[[("〜ことが","~ koto ga"),("できます","dekimasu")],
           "ARROW",
           [("〜ことが","~ koto ga"),("できますか？","dekimasu ka",True)]],
  examples=[
    (f"{NHG}の {SHIN}を {YOMU}ことが できますか。","Nihongo no shinbun wo yomu koto ga dekimasu ka.","Can you read a Japanese newspaper?","ඔබට ජපන් පුවත්පතක් කියවන්න පුළුවන්ද?"),
    (f"{NHG}で メールを {KAKU}ことが できますか。","Nihongo de meeru wo kaku koto ga dekimasu ka.","Can you write an email in Japanese?","ඔබට ජපන් භාෂාවෙන් ඊමේල් එකක් ලියන්න පුළුවන්ද?"),
    (f"はしで ごはんを {TABR}ことが できますか。","Hashi de gohan wo taberu koto ga dekimasu ka.","Can you eat with chopsticks?","ඔබට චොප්ස්ටික්ස් වලින් කන්න පුළුවන්ද?"),
    (f"{KARE}は {NHG}を {OSHI}ことが できますか。","Kare wa nihongo wo oshieru koto ga dekimasu ka.","Can he teach Japanese?","ඔහුට ජපන් භාෂාව උගන්නන්න පුළුවන්ද?"),
    (f"{NIH}の {UTA}を {UTAU}ことが できますか。","Nihon no uta wo utau koto ga dekimasu ka.","Can you sing a Japanese song?","ඔබට ජපන් සිංදුවක් කියන්න පුළුවන්ද?"),
    (f"{RYO}が できますか。","Ryouri ga dekimasu ka.","Can you cook?","ඔබට උයන්න පුළුවන්ද?"),
    (f"アルバイトが できますか。","Arubaito ga dekimasu ka.","Can you work part-time?","ඔබට අර්ධකාලීන රැකියාව කරන්න පුළුවන්ද?"),
  ],
  foot="〜（する ことが）できますか？",
)

# ---------------------------------------------------------------- 18-4 / 18-5 答え方
_USE = (f'「はい、できます。」「いいえ、できません。」が{r("基本","き ほん")}です。'
        f'できる ていどを つけると もっと よく{r("伝","つた")}わります'
        f'（{SUK} できます・あまり できません・{ZEN} できます）。',
        'The basic answers are <b>Hai, dekimasu</b> and <b>Iie, dekimasen</b>. '
        'Adding how well you can do it says much more: <b>sukoshi dekimasu</b> (a little), '
        '<b>amari dekimasen</b> (not really), <b>zenbu dekimasu</b> (all of it).',
        'මූලික උත්තර <b>Hai, dekimasu</b> සහ <b>Iie, dekimasen</b>. '
        'කොච්චර පුළුවන්ද කියලා දැම්මොත් වඩා හොඳයි: <b>sukoshi dekimasu</b> (ටිකක්), '
        '<b>amari dekimasen</b> (එච්චර නැහැ), <b>zenbu dekimasu</b> (ඔක්කොම).')

_PAT = [[("はい、","Hai,"),"BLANK",("できます","dekimasu",True)],
        [("いいえ、","Iie,"),"BLANK",("できません","dekimasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{NHG}の {SHIN}を {YOMU}ことが できますか。","Nihongo no shinbun wo yomu koto ga dekimasu ka.","Can you read a Japanese newspaper?","ඔබට ජපන් පුවත්පතක් කියවන්න පුළුවන්ද?"),
         ("いいえ、できません。","Iie, dekimasen.","No, I can't.","නැහැ, බැහැ.")),
  ("QA", (f"{NHG}で メールを {KAKU}ことが できますか。","Nihongo de meeru wo kaku koto ga dekimasu ka.","Can you write an email in Japanese?","ඔබට ජපන් භාෂාවෙන් ඊමේල් එකක් ලියන්න පුළුවන්ද?"),
         ("はい、できます。","Hai, dekimasu.","Yes, I can.","ඔව්, පුළුවන්.")),
  ("QA", (f"はしで ごはんを {TABR}ことが できますか。","Hashi de gohan wo taberu koto ga dekimasu ka.","Can you eat with chopsticks?","ඔබට චොප්ස්ටික්ස් වලින් කන්න පුළුවන්ද?"),
         ("はい、できます。","Hai, dekimasu.","Yes, I can.","ඔව්, පුළුවන්.")),
  ("QA", (f"{KARE}は {NHG}を {OSHI}ことが できますか。","Kare wa nihongo wo oshieru koto ga dekimasu ka.","Can he teach Japanese?","ඔහුට ජපන් භාෂාව උගන්නන්න පුළුවන්ද?"),
         ("いいえ、できません。","Iie, dekimasen.","No, he can't.","නැහැ, බැහැ.")),
  ("QA", (f"{RYO}が できますか。","Ryouri ga dekimasu ka.","Can you cook?","ඔබට උයන්න පුළුවන්ද?"),
         (f"はい、{SUK} できます。","Hai, sukoshi dekimasu.","Yes, a little.","ඔව්, ටිකක් පුළුවන්.")),
  ("QA", (f"アルバイトが できますか。","Arubaito ga dekimasu ka.","Can you work part-time?","ඔබට අර්ධකාලීන රැකියාව කරන්න පුළුවන්ද?"),
         ("いいえ、まだ できません。","Iie, mada dekimasen.","No, not yet.","නැහැ, තාම බැහැ.")),
  ("QA", (f"{NIH}の {UTA}を {UTAU}ことが できますか。","Nihon no uta wo utau koto ga dekimasu ka.","Can you sing a Japanese song?","ඔබට ජපන් සිංදුවක් කියන්න පුළුවන්ද?"),
         (f"はい、{HITO}だけ できます。","Hai, hitotsu dake dekimasu.","Yes, just one.","ඔව්, එකක් විතරයි.")),
  ("QA", (f"{NHG}で {DEN}が できますか。","Nihongo de denwa ga dekimasu ka.","Can you make a phone call in Japanese?","ඔබට ජපන් භාෂාවෙන් දුරකථන ඇමතුමක් ගන්න පුළුවන්ද?"),
         ("ちょっと むずかしいです。","Chotto muzukashii desu.","That's a bit difficult for me.","ඒක ටිකක් අමාරුයි.")),
  ("QA", (f"ひらがなを {KAKU}ことが できますか。","Hiragana wo kaku koto ga dekimasu ka.","Can you write hiragana?","ඔබට හිරගනා ලියන්න පුළුවන්ද?"),
         (f"はい、{ZEN} できます。","Hai, zenbu dekimasu.","Yes, all of it.","ඔව්, ඔක්කොම පුළුවන්.")),
]

P14A = dict(
  no="18", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、できます。　／　いいえ、できません。","Hai, dekimasu. / Iie, dekimasen.",
         "Yes, I can. / No, I can't.","ඔව්, පුළුවන්. / නැහැ, බැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P14A2 = dict(
  no="18", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P14A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{SUK} できます。","Sukoshi dekimasu.","I can do it a little.","ටිකක් පුළුවන්."),
    ("あまり できません。","Amari dekimasen.","Not really.","එච්චර පුළුවන්කමක් නැහැ."),
    ("まだ できません。","Mada dekimasen.","Not yet.","තාම බැහැ."),
    (f"がんばります。","Ganbarimasu.","I'll do my best.","මම උත්සාහ කරන්නම්."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P14,"p18_1_dekimasu"), (P14N,"p18_2_negative"), (P14Q,"p18_3_question"),
                    (P14A,"p18_4_answer"), (P14A2,"p18_5_answer2")]:
        render(p, stem)
