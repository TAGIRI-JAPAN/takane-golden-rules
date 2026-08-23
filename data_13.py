from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
WTC  = r("私","わたし")+"たち"
KIN  = r("昨日","きのう")
KES  = r("今朝","け さ")
SSH  = r("先週","せん しゅう")
SGE  = r("先月","せん げつ")
KYN  = r("去年","きょ ねん")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
TABM = r("食","た")+"べました"
TABN = r("食","た")+"べませんでした"
TABK = r("食","た")+"べましたか"
TOS  = r("図書館","と しょ かん")
HON  = r("本","ほん")
YOMM = r("読","よ")+"みました"
YOMN = r("読","よ")+"みませんでした"
YOMK = r("読","よ")+"みましたか"
SEN  = r("先生","せん せい")
KSH  = r("教室","きょう しつ")
HANM = r("話","はな")+"しました"
HANN = r("話","はな")+"しませんでした"
HANK = r("話","はな")+"しましたか"
KAEM = r("帰","かえ")+"りました"
KAEN = r("帰","かえ")+"りませんでした"
KAEK = r("帰","かえ")+"りましたか"
SRI  = "スリランカ"
NIH  = r("日本","に ほん")
KIMM = r("来","き")+"ました"
KIMN = r("来","き")+"ませんでした"
KIMK = r("来","き")+"ましたか"
TOM  = r("友","とも")+"だち"
SHU  = r("宿題","しゅく だい")

_TIME = (f"NOTE:{KIN} = ඊයේ　/　{KES} = අද උදේ　/　{SSH} = පසුගිය සතියේ　/　"
         f"{SGE} = පසුගිය මාසයේ　/　{KYN} = පසුගිය අවුරුද්දේ")

# ---------------------------------------------------------------- 13-1 基本
P11 = dict(
  no="13", tag=None,
  title_jp="〜しました",
  title_ro='〜 shimashita &nbsp;|&nbsp; I did 〜 &nbsp;|&nbsp; <span class="si">〜 කළා</span>',
  basic=(f"{W}は {KIN} {NHG}を {BEN}しました。","Watashi wa kinou nihongo wo benkyou shimashita.",
         "I studied Japanese yesterday.","මම ඊයේ ජපන් භාෂාව ඉගෙන ගත්තා."),
  use=(f'おわった ことを{r("言","い")}うときは「ます」を「ました」に かえます。'
       f'どの どうしでも{r("同","おな")}じです。'
       f'「{KIN}」「{SSH}」「{KYN}」などの ときの ことばと いっしょに よく{r("使","つか")}います。',
       'To talk about something finished, change <b>masu</b> to <b>mashita</b>. '
       'This works for every verb. It is often used with time words such as '
       '<b>kinou</b>, <b>senshuu</b> and <b>kyonen</b>.',
       'ඉවර වුණු දෙයක් කියන්න <b>masu</b> එක <b>mashita</b> කරන්න. හැම ක්‍රියා පදයකටම එකයි. '
       '<b>kinou</b>, <b>senshuu</b>, <b>kyonen</b> වගේ කාල වචන එක්ක බොහෝවිට එනවා.'),
  pattern=["NOTE:「ます」を「ました」に かえる　/　masu &#8594; mashita",
           [(r("食","た")+"べます","tabemasu"),"TO",(TABM,"tabemashita",True)],
           [(r("来","き")+"ます","kimasu"),"TO",(KIMM,"kimashita",True)],
           _TIME],
  examples=[
    (f"{W}は {KIN} {NHG}を {BEN}しました。","Watashi wa kinou nihongo wo benkyou shimashita.","I studied Japanese yesterday.","මම ඊයේ ජපන් භාෂාව ඉගෙන ගත්තා."),
    (f"{W}は {KES} パンを {TABM}。","Watashi wa kesa pan wo tabemashita.","I ate bread this morning.","මම අද උදේ පාන් කෑවා."),
    (f"{W}は {SSH} {TOS}で {HON}を {YOMM}。","Watashi wa senshuu toshokan de hon wo yomimashita.","I read a book in the library last week.","මම පසුගිය සතියේ පුස්තකාලයේදී පොතක් කියෙව්වා."),
    (f"{SEN}は {KIN} {KSH}で {HANM}。","Sensei wa kinou kyoushitsu de hanashimashita.","The teacher spoke in the classroom yesterday.","ගුරුතුමා ඊයේ පන්ති කාමරයේදී කතා කළා."),
    (f"{W}は {SGE} {SRI}に {KAEM}。","Watashi wa sengetsu Suriranka ni kaerimashita.","I went back to Sri Lanka last month.","මම පසුගිය මාසයේ ශ්‍රී ලංකාවට ගියා."),
    (f"{TOM}は {KYN} {NIH}に {KIMM}。","Tomodachi wa kyonen Nihon ni kimashita.","My friend came to Japan last year.","මගේ යාළුවා පසුගිය අවුරුද්දේ ජපානයට ආවා."),
    (f"{WTC}は {KIN} テストを しました。","Watashitachi wa kinou tesuto wo shimashita.","We had a test yesterday.","අපි ඊයේ විභාගයක් කළා."),
  ],
  foot="〜しました",
)

# ---------------------------------------------------------------- 13-2 否定
P11N = dict(
  no="13", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜しませんでした",
  title_ro='〜 shimasen deshita &nbsp;|&nbsp; I did not 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කළේ නැහැ</span>',
  basic=(f"{W}は {KIN} {NHG}を {BEN}しませんでした。","Watashi wa kinou nihongo wo benkyou shimasen deshita.",
         "I did not study Japanese yesterday.","මම ඊයේ ජපන් භාෂාව ඉගෙන ගත්තේ නැහැ."),
  use=(f'11で ならった「ません」の うしろに「でした」を つけるだけです。'
       f'「ませんでした」で 1つの かたちだと{r("覚","おぼ")}えると かんたんです。',
       'Just add <b>deshita</b> after the <b>masen</b> you learned in pattern 11. '
       'It is easiest to remember <b>masen deshita</b> as one single ending.',
       '11 වලදී ඉගෙන ගත්ත <b>masen</b> එකට පස්සේ <b>deshita</b> දාන්න විතරයි. '
       '<b>masen deshita</b> කියලා එකම අවසානයක් විදිහට මතක තියාගන්න පහසුයි.'),
  pattern=[[("〜ます","~ masu"),"TO",("〜ました","~ mashita")],
           "NOTE:否定は「ません」＋「でした」　/　masen + deshita",
           [("〜ません","~ masen"),"TO",("〜ませんでした","~ masen deshita",True)]],
  examples=[
    (f"{W}は {KIN} {NHG}を {BEN}しませんでした。","Watashi wa kinou nihongo wo benkyou shimasen deshita.","I did not study Japanese yesterday.","මම ඊයේ ජපන් භාෂාව ඉගෙන ගත්තේ නැහැ."),
    (f"{W}は {KES} パンを {TABN}。","Watashi wa kesa pan wo tabemasen deshita.","I did not eat bread this morning.","මම අද උදේ පාන් කෑවේ නැහැ."),
    (f"{W}は {SSH} {TOS}で {HON}を {YOMN}。","Watashi wa senshuu toshokan de hon wo yomimasen deshita.","I did not read a book in the library last week.","මම පසුගිය සතියේ පුස්තකාලයේදී පොතක් කියෙව්වේ නැහැ."),
    (f"{SEN}は {KIN} {KSH}で {HANN}。","Sensei wa kinou kyoushitsu de hanashimasen deshita.","The teacher did not speak in the classroom yesterday.","ගුරුතුමා ඊයේ පන්ති කාමරයේදී කතා කළේ නැහැ."),
    (f"{W}は {SGE} {SRI}に {KAEN}。","Watashi wa sengetsu Suriranka ni kaerimasen deshita.","I did not go back to Sri Lanka last month.","මම පසුගිය මාසයේ ශ්‍රී ලංකාවට ගියේ නැහැ."),
    (f"{TOM}は {KYN} {NIH}に {KIMN}。","Tomodachi wa kyonen Nihon ni kimasen deshita.","My friend did not come to Japan last year.","මගේ යාළුවා පසුගිය අවුරුද්දේ ජපානයට ආවේ නැහැ."),
    (f"{WTC}は {KIN} テストを しませんでした。","Watashitachi wa kinou tesuto wo shimasen deshita.","We did not have a test yesterday.","අපි ඊයේ විභාගයක් කළේ නැහැ."),
  ],
  foot="〜しませんでした",
)

# ---------------------------------------------------------------- 13-3 疑問
P11Q = dict(
  no="13", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜しましたか？",
  title_ro='〜 shimashita ka &nbsp;|&nbsp; Did you 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කළාද?</span>',
  basic=(f"あなたは {KIN} {NHG}を {BEN}しましたか。","Anata wa kinou nihongo wo benkyou shimashita ka.",
         "Did you study Japanese yesterday?","ඔබ ඊයේ ජපන් භාෂාව ඉගෙන ගත්තාද?"),
  use=(f'「ました」のうしろに「か」をつけるだけです。'
       f'「{SHU}を しましたか」「ごはんを {TABK}」は、{r("毎日","まい にち")}{r("聞","き")}く{r("質問","しつ もん")}です。',
       'Just add <b>ka</b> after <b>mashita</b>. '
       '<b>Shukudai wo shimashita ka</b> ("Did you do your homework?") and '
       '<b>Gohan wo tabemashita ka</b> ("Have you eaten?") come up every single day.',
       '<b>mashita</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       '<b>Shukudai wo shimashita ka</b> ("ගෙදර වැඩ කළාද?") සහ '
       '<b>Gohan wo tabemashita ka</b> ("කෑම කෑවාද?") හැමදාම අහන ප්‍රශ්න.'),
  pattern=[[("〜は","~ wa"),("〜を","~ wo"),("しました","shimashita")],
           "ARROW",
           [("〜は","~ wa"),("〜を","~ wo"),("しましたか？","shimashita ka",True)]],
  examples=[
    (f"あなたは {KIN} {NHG}を {BEN}しましたか。","Anata wa kinou nihongo wo benkyou shimashita ka.","Did you study Japanese yesterday?","ඔබ ඊයේ ජපන් භාෂාව ඉගෙන ගත්තාද?"),
    (f"あなたは {KES} パンを {TABK}。","Anata wa kesa pan wo tabemashita ka.","Did you eat bread this morning?","ඔබ අද උදේ පාන් කෑවාද?"),
    (f"あなたは {SSH} {HON}を {YOMK}。","Anata wa senshuu hon wo yomimashita ka.","Did you read a book last week?","ඔබ පසුගිය සතියේ පොතක් කියෙව්වාද?"),
    (f"{SEN}は {KIN} {KSH}で {HANK}。","Sensei wa kinou kyoushitsu de hanashimashita ka.","Did the teacher speak in the classroom yesterday?","ගුරුතුමා ඊයේ පන්ති කාමරයේදී කතා කළාද?"),
    (f"あなたは {SGE} {SRI}に {KAEK}。","Anata wa sengetsu Suriranka ni kaerimashita ka.","Did you go back to Sri Lanka last month?","ඔබ පසුගිය මාසයේ ශ්‍රී ලංකාවට ගියාද?"),
    (f"{TOM}は {KYN} {NIH}に {KIMK}。","Tomodachi wa kyonen Nihon ni kimashita ka.","Did your friend come to Japan last year?","ඔබේ යාළුවා පසුගිය අවුරුද්දේ ජපානයට ආවාද?"),
    (f"{KIN} テストを しましたか。","Kinou tesuto wo shimashita ka.","Did you have a test yesterday?","ඔබ ඊයේ විභාගයක් කළාද?"),
  ],
  foot="〜しましたか？",
)

# ---------------------------------------------------------------- 13-4 / 13-5 答え方
_USE = (f'「はい、〜ました。」「いいえ、〜ませんでした。」と{r("答","こた")}えます。'
        f'まだ していないときは「まだです。」、もう したときは「もう しました。」も{r("使","つか")}えます。',
        'Answer with <b>Hai, 〜 mashita</b> or <b>Iie, 〜 masen deshita</b>. '
        'If you have not done it yet, <b>mada desu</b>; if you already have, <b>mou shimashita</b>.',
        '<b>Hai, 〜 mashita</b> හෝ <b>Iie, 〜 masen deshita</b> කියලා උත්තර දෙන්න. '
        'තාම කරලා නැත්නම් <b>mada desu</b>; දැනටමත් කරලා නම් <b>mou shimashita</b>.')

_PAT = [[("はい、","Hai,"),"BLANK",("ました","mashita",True)],
        [("いいえ、","Iie,"),"BLANK",("ませんでした","masen deshita",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{KIN} {NHG}を {BEN}しましたか。","Kinou nihongo wo benkyou shimashita ka.","Did you study Japanese yesterday?","ඔබ ඊයේ ජපන් භාෂාව ඉගෙන ගත්තාද?"),
         (f"はい、{BEN}しました。","Hai, benkyou shimashita.","Yes, I did.","ඔව්, ඉගෙන ගත්තා.")),
  ("QA", (f"{KES} パンを {TABK}。","Kesa pan wo tabemashita ka.","Did you eat bread this morning?","ඔබ අද උදේ පාන් කෑවාද?"),
         (f"いいえ、{TABN}。","Iie, tabemasen deshita.","No, I didn't.","නැහැ, කෑවේ නැහැ.")),
  ("QA", (f"{SSH} {HON}を {YOMK}。","Senshuu hon wo yomimashita ka.","Did you read a book last week?","ඔබ පසුගිය සතියේ පොතක් කියෙව්වාද?"),
         (f"はい、{YOMM}。","Hai, yomimashita.","Yes, I did.","ඔව්, කියෙව්වා.")),
  ("QA", (f"{SEN}は {KIN} {HANK}。","Sensei wa kinou hanashimashita ka.","Did the teacher speak yesterday?","ගුරුතුමා ඊයේ කතා කළාද?"),
         (f"いいえ、{HANN}。","Iie, hanashimasen deshita.","No, he didn't.","නැහැ, කතා කළේ නැහැ.")),
  ("QA", (f"{SGE} {SRI}に {KAEK}。","Sengetsu Suriranka ni kaerimashita ka.","Did you go back to Sri Lanka last month?","ඔබ පසුගිය මාසයේ ශ්‍රී ලංකාවට ගියාද?"),
         (f"はい、{KAEM}。","Hai, kaerimashita.","Yes, I did.","ඔව්, ගියා.")),
  ("QA", (f"{TOM}は {KYN} {NIH}に {KIMK}。","Tomodachi wa kyonen Nihon ni kimashita ka.","Did your friend come to Japan last year?","ඔබේ යාළුවා පසුගිය අවුරුද්දේ ජපානයට ආවාද?"),
         (f"いいえ、{KIMN}。","Iie, kimasen deshita.","No, he didn't.","නැහැ, ආවේ නැහැ.")),
  ("QA", (f"{SHU}を しましたか。","Shukudai wo shimashita ka.","Did you do your homework?","ඔබ ගෙදර වැඩ කළාද?"),
         ("はい、もう しました。","Hai, mou shimashita.","Yes, I already did.","ඔව්, දැනටමත් කළා.")),
  ("QA", (f"ごはんを {TABK}。","Gohan wo tabemashita ka.","Have you eaten?","ඔබ කෑම කෑවාද?"),
         ("いいえ、まだです。","Iie, mada desu.","No, not yet.","නැහැ, තාම නැහැ.")),
  ("QA", (f"{KIN} テストを しましたか。","Kinou tesuto wo shimashita ka.","Did you have a test yesterday?","ඔබ ඊයේ විභාගයක් කළාද?"),
         ("いいえ、しませんでした。","Iie, shimasen deshita.","No, we didn't.","නැහැ, කළේ නැහැ.")),
]

P11A = dict(
  no="13", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=(f"はい、{BEN}しました。　／　いいえ、{BEN}しませんでした。",
         "Hai, benkyou shimashita. / Iie, benkyou shimasen deshita.",
         "Yes, I did. / No, I didn't.",
         "ඔව්, කළා. / නැහැ, කළේ නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P11A2 = dict(
  no="13", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P11A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("もう しました。","Mou shimashita.","I already did it.","දැනටමත් කළා."),
    ("まだです。","Mada desu.","Not yet.","තාම නැහැ."),
    (f"{KIN} しました。","Kinou shimashita.","I did it yesterday.","මම ඊයේ කළා."),
    ("すみません、しませんでした。","Sumimasen, shimasen deshita.","Sorry, I didn't.","සමාවෙන්න, කළේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P11,"p13_1_shimashita"), (P11N,"p13_2_negative"), (P11Q,"p13_3_question"),
                    (P11A,"p13_4_answer"), (P11A2,"p13_5_answer2")]:
        render(p, stem)
