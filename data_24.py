from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

JUG  = r("授業","じゅ ぎょう")
SOTS = r("卒業式","そつ ぎょう しき")
SHOG = "お"+r("正月","しょう がつ")
KUNI = r("国","くに")
KAER = r("帰","かえ")+"ります"
NATS = r("夏休","なつ やす")+"み"
HAJM = r("始","はじ")+"まります"
HAJS = r("始","はじ")+"めましょう"
NIH  = r("日本","に ほん")
IKIT = r("行","い")+"きたい"
KAZ  = r("家族","か ぞく")
AIT  = r("会","あ")+"いたい"
BEN  = r("勉強","べん きょう")
GAK  = r("学校","がっ こう")
HAIR = r("入","はい")+"りました"
DEN  = r("電話","でん わ")
RSHU = r("来週","らい しゅう")
RNEN = r("来年","らい ねん")
GETS = r("月","げつ")+"よう"+r("日","び")
DOY  = r("土","ど")+"よう"+r("日","び")
NICH = r("日","にち")+"よう"+r("日","び")
KYON = r("去年","きょ ねん")
SANG = r("三月","さん がつ")
JUJI = r("十時","じゅう じ")
NANJ = r("何時","なん じ")
NANN = r("何日","なん にち")
NANY = r("何","なん")+"よう"+r("日","び")

# ---------------------------------------------------------------- 24-1 基本
P18 = dict(
  no="24", tag=None,
  title_jp="〜は いつですか？",
  title_ro='〜 wa itsu desu ka &nbsp;|&nbsp; When is 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කවදාද?</span>',
  basic=("テストは いつですか。","Tesuto wa itsu desu ka.",
         "When is the test?","විභාගය කවදාද?"),
  use=(f'「いつ」は{r("時","とき")}や{r("日","ひ")}にちを たずねる ことばです。'
       f'21の「{r("何","なに")}」、22の「{r("誰","だれ")}」と{r("同","おな")}じ{r("作","つく")}り{r("方","かた")}です。',
       '<b>itsu</b> asks about a time or a date. '
       'It works exactly like <b>nani</b> in pattern 21 and <b>dare</b> in pattern 22.',
       '<b>itsu</b> කියන්නේ වෙලාවක් හෝ දිනයක් අහන එක — <b>itsu desu ka</b> = කවදාද? '
       '21 හි <b>nani</b>, 22 හි <b>dare</b> වගේමයි.'),
  pattern=[[("〜は","~ wa"),("いつですか？","itsu desu ka",True)],
           f"NOTE:くわしく {r('聞','き')}くとき：{NANJ} = කීයටද　/　{NANN} = කීවෙනිදාද　/　{NANY} = මොන දවසේද"],
  examples=[
    ("テストは いつですか。","Tesuto wa itsu desu ka.","When is the test?","විභාගය කවදාද?"),
    ("しめきりは いつですか。","Shimekiri wa itsu desu ka.","When is the deadline?","නියමිත දිනය කවදාද?"),
    (f"つぎの {JUG}は いつですか。","Tsugi no jugyou wa itsu desu ka.","When is the next class?","ඊළඟ පන්තිය කවදාද?"),
    ("アルバイトは いつですか。","Arubaito wa itsu desu ka.","When is your part-time work?","ඔබේ අර්ධකාලීන රැකියාව කවදාද?"),
    (f"{SOTS}は いつですか。","Sotsugyoushiki wa itsu desu ka.","When is the graduation ceremony?","උපාධි උත්සවය කවදාද?"),
    ("クラスの パーティーは いつですか。","Kurasu no paatii wa itsu desu ka.","When is the class party?","පන්තියේ සාදය කවදාද?"),
    (f"あなたの {KUNI}の {SHOG}は いつですか。","Anata no kuni no oshougatsu wa itsu desu ka.","When is New Year in your country?","ඔබේ රටේ අලුත් අවුරුද්ද කවදාද?"),
  ],
  foot="〜は いつですか？",
)

# ---------------------------------------------------------------- 24-2 応用①
P18B = dict(
  no="24", tag="応用 ①　いつ 〜しますか？ / WITH VERBS",
  title_jp="いつ 〜しますか？",
  title_ro='itsu 〜 shimasu ka &nbsp;|&nbsp; When do you 〜? &nbsp;|&nbsp; '
           '<span class="si">කවදාද 〜 කරන්නේ?</span>',
  basic=(f"いつ {KUNI}に {KAER}か。","Itsu kuni ni kaerimasu ka.",
         "When will you go back to your country?","ඔබ කවදාද රටට යන්නේ?"),
  use=(f'「いつ」を{r("文","ぶん")}の{r("前","まえ")}に おくだけです。'
       f'「しましょうか」は あいてを さそう ときの かたちです。',
       'Just put <b>itsu</b> at the front of the sentence. '
       '<b>shimashou ka</b> is the form you use to invite someone to do it together.',
       '<b>itsu</b> එක වාක්‍යයේ මුලට දාන්න විතරයි. '
       '<b>shimashou ka</b> කියන්නේ එකට කරමුද කියලා ආරාධනා කරන ආකාරයයි.'),
  pattern=[[("いつ","itsu",True),("しますか？","shimasu ka")],
           [("いつ","itsu",True),("したいですか？","shitai desu ka")],
           [("いつ","itsu",True),("しましょうか？","shimashou ka")]],
  examples=[
    ("いつ アルバイトを しますか。","Itsu arubaito wo shimasu ka.","When do you work part-time?","ඔබ කවදාද අර්ධකාලීන රැකියාව කරන්නේ?"),
    (f"いつ {KUNI}に {KAER}か。","Itsu kuni ni kaerimasu ka.","When will you go back to your country?","ඔබ කවදාද රටට යන්නේ?"),
    (f"{NATS}は いつ {HAJM}か。","Natsuyasumi wa itsu hajimarimasu ka.","When does the summer holiday start?","ගිම්හාන නිවාඩුව කවදාද පටන් ගන්නේ?"),
    (f"いつ {NIH}に {IKIT}ですか。","Itsu Nihon ni ikitai desu ka.","When do you want to go to Japan?","ඔබට කවදාද ජපානයට යන්න ඕන?"),
    (f"いつ {KAZ}に {AIT}ですか。","Itsu kazoku ni aitai desu ka.","When do you want to see your family?","ඔබට කවදාද පවුලේ අයව හම්බවෙන්න ඕන?"),
    (f"いつ {BEN}しましょうか。","Itsu benkyou shimashou ka.","When shall we study?","අපි කවදාද ඉගෙන ගමු?"),
    (f"いつ {HAJS}か。","Itsu hajimemashou ka.","When shall we start?","අපි කවදාද පටන් ගමු?"),
  ],
  foot="いつ 〜しますか？",
)

# ---------------------------------------------------------------- 24-3 応用②
P18C = dict(
  no="24", tag="応用 ②　いつ 〜しましたか？ / PAST・FROM・UNTIL",
  title_jp="いつ 〜しましたか？",
  title_ro='itsu 〜 shimashita ka &nbsp;|&nbsp; When did you 〜? &nbsp;|&nbsp; '
           '<span class="si">කවදාද කළේ?</span>',
  basic=("テストは いつでしたか。","Tesuto wa itsu deshita ka.",
         "When was the test?","විභාගය කවදාද තිබුණේ?"),
  use=(f'かこは「いつでしたか」「いつ 〜しましたか」です。'
       f'「いつから」「いつまで」を{r("使","つか")}うと、はじめと おわりを{r("聞","き")}けます。',
       'For the past, use <b>itsu deshita ka</b> or <b>itsu 〜 mashita ka</b>. '
       'With <b>itsu kara</b> and <b>itsu made</b> you can ask about the start and the end.',
       'අතීතයට <b>itsu deshita ka</b> හෝ <b>itsu 〜 mashita ka</b>. '
       '<b>itsu kara</b> සහ <b>itsu made</b> පාවිච්චි කරලා පටන් ගැනීම සහ අවසානය අහන්න පුළුවන්.'),
  pattern=[[("〜は","~ wa"),("いつでしたか？","itsu deshita ka",True)],
           [("いつ","itsu",True),("しましたか？","shimashita ka")],
           [("いつから","itsu kara",True),("していますか？","shite imasu ka")],
           "NOTE:いつから = කවදා ඉඳලා　/　いつまで = කවද වෙනකන්"],
  examples=[
    ("テストは いつでしたか。","Tesuto wa itsu deshita ka.","When was the test?","විභාගය කවදාද තිබුණේ?"),
    ("しめきりは いつでしたか。","Shimekiri wa itsu deshita ka.","When was the deadline?","නියමිත දිනය කවදාද තිබුණේ?"),
    (f"いつ この {GAK}に {HAIR}か。","Itsu kono gakkou ni hairimashita ka.","When did you enter this school?","ඔබ කවදාද මේ පාසලට ඇතුළු වුණේ?"),
    (f"いつ アルバイトを {r('始','はじ')}めましたか。","Itsu arubaito wo hajimemashita ka.","When did you start your part-time job?","ඔබ කවදාද අර්ධකාලීන රැකියාව පටන් ගත්තේ?"),
    (f"いつ {KAZ}に {DEN}しましたか。","Itsu kazoku ni denwa shimashita ka.","When did you call your family?","ඔබ කවදාද පවුලට කතා කළේ?"),
    (f"いつから {r('日本語','に ほん ご')}を {BEN}していますか。","Itsu kara nihongo wo benkyou shite imasu ka.","Since when have you been studying Japanese?","ඔබ කවදා ඉඳලාද ජපන් භාෂාව ඉගෙන ගන්නේ?"),
    (f"いつまで {NIH}に いますか。","Itsu made Nihon ni imasu ka.","Until when will you be in Japan?","ඔබ කවද වෙනකන්ද ජපානයේ ඉන්නේ?"),
  ],
  foot="いつ 〜しましたか？",
)

# ---------------------------------------------------------------- 24-4 / 24-5 答え方
_USE = (f'「いつ」の{r("質問","しつ もん")}には{r("時","とき")}や{r("日","ひ")}にちで{r("答","こた")}えます。'
        f'「はい」「いいえ」では{r("答","こた")}えません。まだ きまっていない ときは「まだ わかりません」です。',
        'Answer an <b>itsu</b> question with a time or a date — never with <b>hai</b> or <b>iie</b>. '
        'If it is not decided yet, say <b>mada wakarimasen</b>.',
        '<b>itsu</b> ප්‍රශ්නයකට වෙලාවක් හෝ දිනයක් කියලා උත්තර දෙන්න — '
        '<b>hai</b> හෝ <b>iie</b> නෙවෙයි. තාම තීරණය වෙලා නැත්නම් <b>mada wakarimasen</b>.')

_PAT = ["NOTE:【 ちゅうい 】「はい / いいえ」では 答えません　/　never answer yes or no",
        [("いつですか？","itsu desu ka"),"TO",(f"{r('時','とき')}や {r('日','ひ')}にちを {r('言','い')}う","give a time or date",True)],
        f"NOTE:よく つかう {r('答','こた')}え：あした　/　{RSHU}　/　{r('来月','らい げつ')}　/　{GETS}　/　{JUJI}から"]

_QA = [
  ("QA", ("テストは いつですか。","Tesuto wa itsu desu ka.","When is the test?","විභාගය කවදාද?"),
         (f"{RSHU}の {GETS}です。","Raishuu no getsuyoubi desu.","Next Monday.","ලබන සතියේ සඳුදා.")),
  ("QA", ("しめきりは いつですか。","Shimekiri wa itsu desu ka.","When is the deadline?","නියමිත දිනය කවදාද?"),
         ("あしたです。","Ashita desu.","Tomorrow.","හෙට.")),
  ("QA", (f"つぎの {JUG}は いつですか。","Tsugi no jugyou wa itsu desu ka.","When is the next class?","ඊළඟ පන්තිය කවදාද?"),
         (f"{JUJI}からです。","Juuji kara desu.","From ten o'clock.","දහයේ ඉඳලා.")),
  ("QA", ("アルバイトは いつですか。","Arubaito wa itsu desu ka.","When is your part-time work?","ඔබේ අර්ධකාලීන රැකියාව කවදාද?"),
         (f"{DOY}と {NICH}です。","Doyoubi to nichiyoubi desu.","Saturday and Sunday.","සෙනසුරාදා සහ ඉරිදා.")),
  ("QA", (f"いつ {KUNI}に {KAER}か。","Itsu kuni ni kaerimasu ka.","When will you go back to your country?","ඔබ කවදාද රටට යන්නේ?"),
         (f"{RNEN} {KAER}。","Rainen kaerimasu.","I'll go back next year.","ලබන අවුරුද්දේ යනවා.")),
  ("QA", (f"いつ {KAZ}に {AIT}ですか。","Itsu kazoku ni aitai desu ka.","When do you want to see your family?","ඔබට කවදාද පවුලේ අයව හම්බවෙන්න ඕන?"),
         (f"{NATS}に {AIT}です。","Natsuyasumi ni aitai desu.","During the summer holiday.","ගිම්හාන නිවාඩුවේදී.")),
  ("QA", (f"いつから {r('日本語','に ほん ご')}を {BEN}していますか。","Itsu kara nihongo wo benkyou shite imasu ka.","Since when have you been studying Japanese?","ඔබ කවදා ඉඳලාද ජපන් භාෂාව ඉගෙන ගන්නේ?"),
         (f"{KYON}から {BEN}しています。","Kyonen kara benkyou shite imasu.","Since last year.","පසුගිය අවුරුද්දේ ඉඳලා.")),
  ("QA", (f"いつまで {NIH}に いますか。","Itsu made Nihon ni imasu ka.","Until when will you be in Japan?","ඔබ කවද වෙනකන්ද ජපානයේ ඉන්නේ?"),
         (f"{RNEN}の {SANG}までです。","Rainen no sangatsu made desu.","Until March next year.","ලබන අවුරුද්දේ මාර්තු වෙනකන්.")),
  ("QA", (f"{SOTS}は いつですか。","Sotsugyoushiki wa itsu desu ka.","When is the graduation ceremony?","උපාධි උත්සවය කවදාද?"),
         ("まだ わかりません。","Mada wakarimasen.","I don't know yet.","තාම දන්නේ නැහැ.")),
]

_TITLE_RO = ('Itsu no shitsumon no kotaekata &nbsp;|&nbsp; Answering a "when" question &nbsp;|&nbsp; '
             '<span class="si">"කවදාද?" ප්‍රශ්නයට උත්තර දීම</span>')

P18A = dict(
  no="24", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp="いつ の 質問の 答え方",
  title_ro=_TITLE_RO,
  basic=(f"テストは いつですか。　&#8594;　{RSHU}の {GETS}です。",
         "Tesuto wa itsu desu ka. → Raishuu no getsuyoubi desu.",
         "When is the test? → Next Monday.","විභාගය කවදාද? → ලබන සතියේ සඳුදා."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="いつ の 質問の 答え方",
)

P18A2 = dict(
  no="24", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp="いつ の 質問の 答え方",
  title_ro=_TITLE_RO,
  skip=("basic","use","pattern"), start=4,
  basic=P18A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{RSHU}です。","Raishuu desu.","Next week.","ලබන සතියේ."),
    ("あさってです。","Asatte desu.","The day after tomorrow.","අනිද්දා."),
    ("いつでも いいです。","Itsu demo ii desu.","Any time is fine.","කවදා හරි කමක් නැහැ."),
    ("まだ わかりません。","Mada wakarimasen.","I don't know yet.","තාම දන්නේ නැහැ."),
  ],
  foot="いつ の 質問の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P18,"p24_1_itsu"), (P18B,"p24_2_verbs"), (P18C,"p24_3_past"),
                    (P18A,"p24_4_answer"), (P18A2,"p24_5_answer2")]:
        render(p, stem)
