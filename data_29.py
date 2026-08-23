from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

BEN  = r("勉強","べん きょう")
TOS  = r("図書館","と しょ かん")
IKI  = r("行","い")+"きます"
IKAN = r("行","い")+"かない"
KANJ = r("漢字","かん じ")
NIH  = r("日本","に ほん")
NHG  = r("日本語","に ほん ご")
SUMT = r("住","す")+"みたい"
HAYA = r("早","はや")+"く"
KURU = r("来","く")+"る"
KONA = r("来","こ")+"ない"
SHU  = r("宿題","しゅく だい")
TABN = r("食","た")+"べない"
TABR = r("食","た")+"べます"
SEN  = r("先生","せん せい")
KIKN = r("聞","き")+"かない"
HANN = r("話","はな")+"さない"
KYO  = r("教科書","きょう か しょ")
MINA = r("見","み")+"ない"
GAK  = r("学校","がっ こう")
ERAN = r("選","えら")+"んだ"
YASN = r("休","やす")+"んだ"
OKUR = r("遅","おく")+"れた"
KIN  = r("昨日","きのう")
JIK  = r("時間","じ かん")
YOJI = r("用事","よう じ")
CHIK = r("近","ちか")+"い"
HAT  = r("働","はたら")+"きたい"
ISOG = r("忙","いそが")+"しい"
MUZU = "むずかしい"

# ---------------------------------------------------------------- 29-1 基本
P20 = dict(
  no="29", tag=None,
  title_jp="どうして 〜？　なぜ 〜？",
  title_ro='doushite 〜 ? / naze 〜 ? &nbsp;|&nbsp; Why 〜? &nbsp;|&nbsp; '
           '<span class="si">ඇයි 〜?</span>',
  basic=(f"どうして {NHG}を {BEN}しますか。","Doushite nihongo wo benkyou shimasu ka.",
         "Why do you study Japanese?","ඔබ ඇයි ජපන් භාෂාව ඉගෙන ගන්නේ?"),
  use=(f'どちらも りゆうを たずねる ことばです。{r("意味","い み")}は{r("同","おな")}じですが、'
       f'「どうして」の ほうが よく{r("使","つか")}います。「なぜ」は かたい{r("言","い")}い{r("方","かた")}です。',
       'Both ask for a reason and mean the same thing, but <b>doushite</b> is far more common '
       'in everyday speech; <b>naze</b> sounds more formal.',
       'දෙකම හේතුව අහන වචන — තේරුම එකයි, නමුත් <b>doushite</b> දෛනික කතාවේ බහුලයි; '
       '<b>naze</b> ටිකක් විධිමත්.'),
  pattern=[[("どうして","doushite",True),("〜ますか？","~ masu ka")],
           [("なぜ","naze",True),("〜んですか？","~ n desu ka")],
           "NOTE:「んですか」を つけると、りゆうを 知りたい 気持ちが つよく なります"],
  examples=[
    (f"どうして {NHG}を {BEN}しますか。","Doushite nihongo wo benkyou shimasu ka.","Why do you study Japanese?","ඔබ ඇයි ජපන් භාෂාව ඉගෙන ගන්නේ?"),
    (f"どうして まいにち {TOS}へ {IKI}か。","Doushite mainichi toshokan e ikimasu ka.","Why do you go to the library every day?","ඔබ ඇයි හැමදාම පුස්තකාලයට යන්නේ?"),
    ("なぜ アルバイトを したいんですか。","Naze arubaito wo shitai n desu ka.","Why do you want to work part-time?","ඔබට ඇයි අර්ධකාලීන රැකියාවක් කරන්න ඕන?"),
    (f"どうして {ISOG}んですか。","Doushite isogashii n desu ka.","Why are you busy?","ඔබ ඇයි කාර්යබහුල?"),
    (f"なぜ この {KANJ}は {MUZU}んですか。","Naze kono kanji wa muzukashii n desu ka.","Why is this kanji difficult?","මේ කන්ජි අකුර ඇයි අමාරු?"),
    (f"どうして {NIH}に {SUMT}んですか。","Doushite Nihon ni sumitai n desu ka.","Why do you want to live in Japan?","ඔබට ඇයි ජපානයේ ජීවත් වෙන්න ඕන?"),
    (f"どうして いつも {HAYA} {KURU}んですか。","Doushite itsumo hayaku kuru n desu ka.","Why do you always come early?","ඔබ ඇයි හැමවෙලේම කලින් එන්නේ?"),
  ],
  foot="どうして 〜？　なぜ 〜？",
)

# ---------------------------------------------------------------- 29-2 応用①
P20B = dict(
  no="29", tag="応用 ①　どうして 〜ないんですか？ / NEGATIVE REASON",
  title_jp="どうして 〜ないんですか？",
  title_ro='doushite 〜 nai n desu ka &nbsp;|&nbsp; Why don\'t you 〜? &nbsp;|&nbsp; '
           '<span class="si">ඇයි 〜 නොකරන්නේ?</span>',
  basic=(f"どうして {SHU}を しないんですか。","Doushite shukudai wo shinai n desu ka.",
         "Why don't you do your homework?","ඔබ ඇයි ගෙදර වැඩ කරන්නේ නැත්තේ?"),
  use=(f'しない りゆうを{r("聞","き")}くときは「ない」の かたちを{r("使","つか")}います。'
       f'「ます」を「ない」に かえて、うしろに「んですか」を つけます。',
       'To ask why someone does NOT do something, use the plain negative <b>nai</b> form. '
       'Change <b>masu</b> to <b>nai</b>, then add <b>n desu ka</b>.',
       'ඇයි නොකරන්නේ කියලා අහන්න <b>nai</b> ආකාරය භාවිතා කරන්න. '
       '<b>masu</b> එක <b>nai</b> කරලා, පස්සෙන් <b>n desu ka</b> දාන්න.'),
  pattern=[[("どうして","doushite",True),("〜ないんですか？","~ nai n desu ka")],
           f"NOTE:{IKI}→{IKAN}　/　{r('来','き')}ます→{KONA}　/　{TABR}→{TABN}　/　します→しない　/　"
           f"{r('見','み')}ます→{MINA}"],
  examples=[
    (f"どうして {SHU}を しないんですか。","Doushite shukudai wo shinai n desu ka.","Why don't you do your homework?","ඔබ ඇයි ගෙදර වැඩ කරන්නේ නැත්තේ?"),
    (f"どうして ごはんを {TABN}んですか。","Doushite gohan wo tabenai n desu ka.","Why don't you eat?","ඔබ ඇයි කෑම කන්නේ නැත්තේ?"),
    (f"なぜ {SEN}に {KIKN}んですか。","Naze sensei ni kikanai n desu ka.","Why don't you ask the teacher?","ඔබ ඇයි ගුරුතුමාගෙන් අහන්නේ නැත්තේ?"),
    (f"どうして バスが {KONA}んですか。","Doushite basu ga konai n desu ka.","Why isn't the bus coming?","බස් එක ඇයි එන්නේ නැත්තේ?"),
    (f"なぜ {NHG}で {HANN}んですか。","Naze nihongo de hanasanai n desu ka.","Why don't you speak in Japanese?","ඔබ ඇයි ජපන් භාෂාවෙන් කතා කරන්නේ නැත්තේ?"),
    ("どうして アルバイトを しないんですか。","Doushite arubaito wo shinai n desu ka.","Why don't you work part-time?","ඔබ ඇයි අර්ධකාලීන රැකියාවක් කරන්නේ නැත්තේ?"),
    (f"どうして {KYO}を {MINA}んですか。","Doushite kyoukasho wo minai n desu ka.","Why don't you look at your textbook?","ඔබ ඇයි පෙළපොත බලන්නේ නැත්තේ?"),
  ],
  foot="どうして 〜ないんですか？",
)

# ---------------------------------------------------------------- 29-3 応用②
P20C = dict(
  no="29", tag="応用 ②　どうして 〜たんですか？ / PAST REASON",
  title_jp="どうして 〜たんですか？",
  title_ro='doushite 〜 ta n desu ka &nbsp;|&nbsp; Why did you 〜? &nbsp;|&nbsp; '
           '<span class="si">ඇයි 〜 කළේ?</span>',
  basic=(f"どうして この {GAK}を {ERAN}んですか。","Doushite kono gakkou wo eranda n desu ka.",
         "Why did you choose this school?","ඔබ ඇයි මේ පාසල තෝරගත්තේ?"),
  use=(f'17で ならった「た」の かたちを{r("使","つか")}います。'
       f'「ませんでした」は「なかった」に かえます。めんせつで とても よく{r("聞","き")}かれる{r("形","かたち")}です。',
       'Use the plain past <b>ta</b> form you learned in pattern 17. '
       '<b>masen deshita</b> becomes <b>nakatta</b>. You will hear this a lot in interviews.',
       '17 වලදී ඉගෙන ගත්ත <b>ta</b> ආකාරය භාවිතා කරන්න. '
       '<b>masen deshita</b> එක <b>nakatta</b> වෙනවා. සම්මුඛ පරීක්ෂණවලදී මේක නිතර අහනවා.'),
  pattern=[[("どうして","doushite",True),("〜たんですか？","~ ta n desu ka")],
           [("どうして","doushite",True),("〜なかったんですか？","~ nakatta n desu ka")],
           "NOTE:ました → た　/　ませんでした → なかった"],
  examples=[
    (f"どうして この {GAK}を {ERAN}んですか。","Doushite kono gakkou wo eranda n desu ka.","Why did you choose this school?","ඔබ ඇයි මේ පාසල තෝරගත්තේ?"),
    (f"どうして {KIN} {YASN}んですか。","Doushite kinou yasunda n desu ka.","Why were you absent yesterday?","ඔබ ඇයි ඊයේ නිවාඩු ගත්තේ?"),
    (f"なぜ {OKUR}んですか。","Naze okureta n desu ka.","Why were you late?","ඔබ ඇයි පරක්කු වුණේ?"),
    (f"どうして {NHG}を {BEN}したんですか。","Doushite nihongo wo benkyou shita n desu ka.","Why did you study Japanese?","ඔබ ඇයි ජපන් භාෂාව ඉගෙන ගත්තේ?"),
    (f"どうして {SHU}を しなかったんですか。","Doushite shukudai wo shinakatta n desu ka.","Why didn't you do your homework?","ඔබ ඇයි ගෙදර වැඩ කරලා නැත්තේ?"),
    (f"なぜ {KIN} {KONA}かったんですか。","Naze kinou konakatta n desu ka.","Why didn't you come yesterday?","ඔබ ඇයි ඊයේ ආවේ නැත්තේ?"),
    (f"なぜ {SEN}に {HANN}かったんですか。","Naze sensei ni hanasanakatta n desu ka.","Why didn't you tell the teacher?","ඔබ ඇයි ගුරුතුමාට කිව්වේ නැත්තේ?"),
  ],
  foot="どうして 〜たんですか？",
)

# ---------------------------------------------------------------- 29-4 / 29-5 答え方
_USE = (f'ここが 29で いちばん{r("大切","たい せつ")}です。「どうして」の{r("質問","しつ もん")}には'
        f'「〜からです」で{r("答","こた")}えます。「はい」「いいえ」では{r("答","こた")}えません。',
        'This is the most important point of pattern 29. Answer a <b>doushite</b> question with '
        '<b>〜 kara desu</b> ("because …"). Never with <b>hai</b> or <b>iie</b>.',
        'මේක තමයි 29 හි වැදගත්ම කරුණ. <b>doushite</b> ප්‍රශ්නයකට '
        '<b>〜 kara desu</b> ("...නිසා") කියලා උත්තර දෙන්න. <b>hai</b>/<b>iie</b> නෙවෙයි.')

_PAT = ["NOTE:【 ちゅうい 】「はい / いいえ」では 答えません　/　never answer yes or no",
        [("どうして 〜んですか？","doushite ~ n desu ka"),"TO",("〜からです","~ kara desu",True)],
        "NOTE:りゆうが 言いにくい とき：「ちょっと…」（12・19と 同じ）"]

_QA = [
  ("QA", (f"どうして {NHG}を {BEN}しますか。","Doushite nihongo wo benkyou shimasu ka.","Why do you study Japanese?","ඔබ ඇයි ජපන් භාෂාව ඉගෙන ගන්නේ?"),
         (f"{NIH}で {HAT}からです。","Nihon de hatarakitai kara desu.","Because I want to work in Japan.","මට ජපානයේ වැඩ කරන්න ඕන නිසා.")),
  ("QA", (f"どうして まいにち {TOS}へ {IKI}か。","Doushite mainichi toshokan e ikimasu ka.","Why do you go to the library every day?","ඔබ ඇයි හැමදාම පුස්තකාලයට යන්නේ?"),
         ("テストが あるからです。","Tesuto ga aru kara desu.","Because I have a test.","විභාගයක් තියෙන නිසා.")),
  ("QA", (f"どうして {ISOG}んですか。","Doushite isogashii n desu ka.","Why are you busy?","ඔබ ඇයි කාර්යබහුල?"),
         (f"テストが {CHIK}からです。","Tesuto ga chikai kara desu.","Because the test is soon.","විභාගය ළඟ නිසා.")),
  ("QA", (f"どうして {SHU}を しないんですか。","Doushite shukudai wo shinai n desu ka.","Why don't you do your homework?","ඔබ ඇයි ගෙදර වැඩ කරන්නේ නැත්තේ?"),
         (f"{JIK}が ないからです。","Jikan ga nai kara desu.","Because I don't have time.","වෙලාව නැති නිසා.")),
  ("QA", (f"なぜ アルバイトを したいんですか。","Naze arubaito wo shitai n desu ka.","Why do you want to work part-time?","ඔබට ඇයි අර්ධකාලීන රැකියාවක් කරන්න ඕන?"),
         (f"{NHG}を {r('話','はな')}したいからです。","Nihongo wo hanashitai kara desu.","Because I want to speak Japanese.","මට ජපන් භාෂාව කතා කරන්න ඕන නිසා.")),
  ("QA", (f"どうして {KIN} {YASN}んですか。","Doushite kinou yasunda n desu ka.","Why were you absent yesterday?","ඔබ ඇයි ඊයේ නිවාඩු ගත්තේ?"),
         (f"{YOJI}が あったからです。","Youji ga atta kara desu.","Because I had something to do.","වැඩක් තිබුණු නිසා.")),
  ("QA", (f"なぜ {OKUR}んですか。","Naze okureta n desu ka.","Why were you late?","ඔබ ඇයි පරක්කු වුණේ?"),
         (f"すみません、バスが {OKUR}からです。","Sumimasen, basu ga okureta kara desu.","Sorry — because the bus was late.","සමාවෙන්න, බස් එක පරක්කු වුණු නිසා.")),
  ("QA", (f"どうして この {GAK}を {ERAN}んですか。","Doushite kono gakkou wo eranda n desu ka.","Why did you choose this school?","ඔබ ඇයි මේ පාසල තෝරගත්තේ?"),
         (f"{SEN}が いいからです。","Sensei ga ii kara desu.","Because the teachers are good.","ගුරුවරු හොඳ නිසා.")),
  ("QA", (f"どうして バスが {KONA}んですか。","Doushite basu ga konai n desu ka.","Why isn't the bus coming?","බස් එක ඇයි එන්නේ නැත්තේ?"),
         ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ.")),
]

_TITLE_RO = ('Doushite no shitsumon no kotaekata &nbsp;|&nbsp; Answering a "why" question &nbsp;|&nbsp; '
             '<span class="si">"ඇයි?" ප්‍රශ්නයට උත්තර දීම</span>')

P20A = dict(
  no="29", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp="〜からです",
  title_ro=_TITLE_RO,
  basic=(f"どうして {BEN}しますか。　&#8594;　{NIH}で {HAT}からです。",
         "Doushite benkyou shimasu ka. → Nihon de hatarakitai kara desu.",
         "Why do you study? → Because I want to work in Japan.",
         "ඔබ ඇයි ඉගෙන ගන්නේ? → මට ජපානයේ වැඩ කරන්න ඕන නිසා."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="〜からです",
)

P20A2 = dict(
  no="29", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp="〜からです",
  title_ro=_TITLE_RO,
  skip=("basic","use","pattern"), start=4,
  basic=P20A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("〜からです。","~ kara desu.","Because ~.","...නිසා යි."),
    ("ちょっと…。","Chotto…","It's a bit hard to say.","ඒක ටිකක්…"),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
    ("すみません。","Sumimasen.","I'm sorry.","සමාවෙන්න."),
  ],
  foot="〜からです",
)

if __name__ == "__main__":
    for p, stem in [(P20,"p29_1_doushite"), (P20B,"p29_2_negative"), (P20C,"p29_3_past"),
                    (P20A,"p29_4_answer"), (P20A2,"p29_5_answer2")]:
        render(p, stem)
