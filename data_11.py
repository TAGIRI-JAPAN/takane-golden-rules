from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
WTC  = r("私","わたし")+"たち"
MAIN = r("毎日","まい にち")
MAIA = r("毎朝","まい あさ")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
SHU  = r("宿題","しゅく だい")
TAB  = r("食","た")+"べます"
TABN = r("食","た")+"べません"
TABK = r("食","た")+"べますか"
GAK  = r("学校","がっ こう")
IKI  = r("行","い")+"きます"
IKIN = r("行","い")+"きません"
IKIK = r("行","い")+"きますか"
TOM  = r("友","とも")+"だち"
DEN  = r("電話","でん わ")
TOS  = r("図書館","と しょ かん")
HON  = r("本","ほん")
YOM  = r("読","よ")+"みます"
YOMN = r("読","よ")+"みません"
YOMK = r("読","よ")+"みますか"
KSH  = r("教室","きょう しつ")
HAN  = r("話","はな")+"します"
HANN = r("話","はな")+"しません"
HANK = r("話","はな")+"しますか"
AST  = r("明日","あ した")
KIM  = r("来","き")+"ます"

_NOTE = "NOTE:〜を = කරන දේ　/　〜で = කරන තැන　/　〜に = යන තැන・කරන කෙනා"

# ---------------------------------------------------------------- 11-1 基本
P7 = dict(
  no="11", tag=None,
  title_jp="〜します",
  title_ro='〜 shimasu &nbsp;|&nbsp; I do 〜 &nbsp;|&nbsp; <span class="si">〜 කරනවා</span>',
  basic=(f"{W}は {MAIN} {NHG}を {BEN}します。","Watashi wa mainichi nihongo wo benkyou shimasu.",
         "I study Japanese every day.","මම හැමදාම ජපන් භාෂාව ඉගෙන ගන්නවා."),
  use=(f'いつも することや、これから することを{r("言","い")}います。'
       f'「を」は{r("何","なに")}を するか、「で」は どこで するか、「に」は どこへ・だれに を あらわします。',
       'Use it for what you do regularly or what you are going to do. '
       '<b>wo</b> marks what you do, <b>de</b> marks where you do it, '
       'and <b>ni</b> marks the destination or the person you act toward.',
       'නිතර කරන දේ හෝ ඉදිරියේදී කරන දේ කියන්න. '
       '<b>wo</b> = කරන දේ, <b>de</b> = කරන තැන, <b>ni</b> = යන තැන හෝ කරන කෙනා.'),
  pattern=[[("〜は","~ wa"),("〜を","~ wo"),("します","shimasu")],
           [("〜は","~ wa"),("…で","… de"),("〜を","~ wo"),("します","shimasu")],
           _NOTE],
  examples=[
    (f"{W}は {MAIN} {NHG}を {BEN}します。","Watashi wa mainichi nihongo wo benkyou shimasu.","I study Japanese every day.","මම හැමදාම ජපන් භාෂාව ඉගෙන ගන්නවා."),
    (f"{W}は うちで {SHU}を します。","Watashi wa uchi de shukudai wo shimasu.","I do my homework at home.","මම ගෙදරදී ගෙදර වැඩ කරනවා."),
    (f"{W}は {MAIA} パンを {TAB}。","Watashi wa maiasa pan wo tabemasu.","I eat bread every morning.","මම හැම උදෑසනකම පාන් කනවා."),
    (f"{W}は {GAK}に {IKI}。","Watashi wa gakkou ni ikimasu.","I go to school.","මම පාසලට යනවා."),
    (f"{TOM}に {DEN}します。","Tomodachi ni denwa shimasu.","I call my friend.","මම යාළුවාට දුරකථනයෙන් කතා කරනවා."),
    (f"{TOS}で {HON}を {YOM}。","Toshokan de hon wo yomimasu.","I read books in the library.","මම පුස්තකාලයේදී පොත් කියවනවා."),
    (f"{WTC}は {KSH}で {NHG}を {HAN}。","Watashitachi wa kyoushitsu de nihongo wo hanashimasu.","We speak Japanese in the classroom.","අපි පන්ති කාමරයේදී ජපන් භාෂාව කතා කරනවා."),
  ],
  foot="〜します",
)

# ---------------------------------------------------------------- 11-2 否定
P7N = dict(
  no="11", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜しません",
  title_ro='〜 shimasen &nbsp;|&nbsp; I do not 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්නේ නැහැ</span>',
  basic=(f"{W}は {MAIN} {NHG}を {BEN}しません。","Watashi wa mainichi nihongo wo benkyou shimasen.",
         "I do not study Japanese every day.","මම හැමදාම ජපන් භාෂාව ඉගෙන ගන්නේ නැහැ."),
  use=(f'さいごの「ます」を「ません」に{r("変","か")}えるだけです。'
       f'どの どうしでも{r("同","おな")}じです（します→しません、{TAB}→{TABN}、{IKI}→{IKIN}）。',
       'Just change the final <b>masu</b> to <b>masen</b>. '
       'This works for every verb: <b>shimasu → shimasen</b>, <b>tabemasu → tabemasen</b>, '
       '<b>ikimasu → ikimasen</b>.',
       'අන්තිම <b>masu</b> එක <b>masen</b> කියලා වෙනස් කරන්න විතරයි. '
       'හැම ක්‍රියා පදයකටම එකයි: <b>shimasu → shimasen</b>, <b>tabemasu → tabemasen</b>, '
       '<b>ikimasu → ikimasen</b>.'),
  pattern=[[("〜ます","~ masu"),"TO",("〜ません","~ masen",True)],
           "NOTE:どの どうしでも 同じ　/　the same for every verb",
           [(f"{BEN}します","benkyou shimasu"),"TO",(f"{BEN}しません","benkyou shimasen",True)]],
  examples=[
    (f"{W}は {MAIN} {NHG}を {BEN}しません。","Watashi wa mainichi nihongo wo benkyou shimasen.","I do not study Japanese every day.","මම හැමදාම ජපන් භාෂාව ඉගෙන ගන්නේ නැහැ."),
    (f"{W}は うちで {SHU}を しません。","Watashi wa uchi de shukudai wo shimasen.","I do not do my homework at home.","මම ගෙදරදී ගෙදර වැඩ කරන්නේ නැහැ."),
    (f"{W}は {MAIA} パンを {TABN}。","Watashi wa maiasa pan wo tabemasen.","I do not eat bread every morning.","මම හැම උදෑසනකම පාන් කන්නේ නැහැ."),
    (f"{W}は {GAK}に {IKIN}。","Watashi wa gakkou ni ikimasen.","I do not go to school.","මම පාසලට යන්නේ නැහැ."),
    (f"{TOM}に {DEN}しません。","Tomodachi ni denwa shimasen.","I do not call my friend.","මම යාළුවාට දුරකථනයෙන් කතා කරන්නේ නැහැ."),
    (f"{TOS}で {HON}を {YOMN}。","Toshokan de hon wo yomimasen.","I do not read books in the library.","මම පුස්තකාලයේදී පොත් කියවන්නේ නැහැ."),
    (f"{WTC}は {KSH}で {NHG}を {HANN}。","Watashitachi wa kyoushitsu de nihongo wo hanashimasen.","We do not speak Japanese in the classroom.","අපි පන්ති කාමරයේදී ජපන් භාෂාව කතා කරන්නේ නැහැ."),
  ],
  foot="〜しません",
)

# ---------------------------------------------------------------- 11-3 疑問
P7Q = dict(
  no="11", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜しますか？",
  title_ro='〜 shimasu ka &nbsp;|&nbsp; Do you 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කරනවාද?</span>',
  basic=(f"あなたは {MAIN} {NHG}を {BEN}しますか。","Anata wa mainichi nihongo wo benkyou shimasu ka.",
         "Do you study Japanese every day?","ඔබ හැමදාම ජපන් භාෂාව ඉගෙන ගන්නවාද?"),
  use=(f'「ます」のうしろに「か」をつけるだけです。'
       f'{r("相手","あい て")}の しゅうかんを{r("聞","き")}くときにも、これからの よていを{r("聞","き")}くときにも{r("使","つか")}えます。',
       'Just add <b>ka</b> after <b>masu</b>. '
       'You can use it both to ask about someone’s habits and to ask about their plans.',
       '<b>masu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       'කෙනෙක්ගේ පුරුදු ගැන අහන්නත්, ඉදිරි සැලසුම් ගැන අහන්නත් පාවිච්චි කරන්න පුළුවන්.'),
  pattern=[[("〜は","~ wa"),("〜を","~ wo"),("します","shimasu")],
           "ARROW",
           [("〜は","~ wa"),("〜を","~ wo"),("しますか？","shimasu ka",True)]],
  examples=[
    (f"あなたは {MAIN} {NHG}を {BEN}しますか。","Anata wa mainichi nihongo wo benkyou shimasu ka.","Do you study Japanese every day?","ඔබ හැමදාම ජපන් භාෂාව ඉගෙන ගන්නවාද?"),
    (f"あなたは うちで {SHU}を しますか。","Anata wa uchi de shukudai wo shimasu ka.","Do you do your homework at home?","ඔබ ගෙදරදී ගෙදර වැඩ කරනවාද?"),
    (f"あなたは {MAIA} パンを {TABK}。","Anata wa maiasa pan wo tabemasu ka.","Do you eat bread every morning?","ඔබ හැම උදෑසනකම පාන් කනවාද?"),
    (f"あなたは {GAK}に {IKIK}。","Anata wa gakkou ni ikimasu ka.","Do you go to school?","ඔබ පාසලට යනවාද?"),
    (f"{TOM}に {DEN}しますか。","Tomodachi ni denwa shimasu ka.","Do you call your friend?","ඔබ යාළුවාට දුරකථනයෙන් කතා කරනවාද?"),
    (f"{TOS}で {HON}を {YOMK}。","Toshokan de hon wo yomimasu ka.","Do you read books in the library?","ඔබ පුස්තකාලයේදී පොත් කියවනවාද?"),
    (f"{KSH}で {NHG}を {HANK}。","Kyoushitsu de nihongo wo hanashimasu ka.","Do you speak Japanese in the classroom?","ඔබ පන්ති කාමරයේදී ජපන් භාෂාව කතා කරනවාද?"),
  ],
  foot="〜しますか？",
)

# ---------------------------------------------------------------- 11-4 / 11-5 答え方
_USE = (f'「はい、〜ます。」「いいえ、〜ません。」と{r("答","こた")}えます。'
        f'{r("質問","しつ もん")}に{r("使","つか")}われた どうしを、そのまま{r("使","つか")}うのが{r("大切","たい せつ")}です。',
        'Answer with <b>Hai, 〜 masu</b> or <b>Iie, 〜 masen</b>. '
        'The important point is to reuse the same verb that was in the question.',
        '<b>Hai, 〜 masu</b> හෝ <b>Iie, 〜 masen</b> කියලා උත්තර දෙන්න. '
        'ප්‍රශ්නයේ තිබුණු ක්‍රියා පදයම නැවත භාවිතා කරන එක වැදගත්.')

_PAT = [[("はい、","Hai,"),"BLANK",("ます","masu",True)],
        [("いいえ、","Iie,"),"BLANK",("ません","masen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"あなたは {MAIN} {NHG}を {BEN}しますか。","Anata wa mainichi nihongo wo benkyou shimasu ka.","Do you study Japanese every day?","ඔබ හැමදාම ජපන් භාෂාව ඉගෙන ගන්නවාද?"),
         (f"はい、{BEN}します。","Hai, benkyou shimasu.","Yes, I do.","ඔව්, ඉගෙන ගන්නවා.")),
  ("QA", (f"あなたは うちで {SHU}を しますか。","Anata wa uchi de shukudai wo shimasu ka.","Do you do your homework at home?","ඔබ ගෙදරදී ගෙදර වැඩ කරනවාද?"),
         ("いいえ、しません。","Iie, shimasen.","No, I don't.","නැහැ, කරන්නේ නැහැ.")),
  ("QA", (f"あなたは {MAIA} パンを {TABK}。","Anata wa maiasa pan wo tabemasu ka.","Do you eat bread every morning?","ඔබ හැම උදෑසනකම පාන් කනවාද?"),
         (f"はい、{TAB}。","Hai, tabemasu.","Yes, I do.","ඔව්, කනවා.")),
  ("QA", (f"あなたは {GAK}に {IKIK}。","Anata wa gakkou ni ikimasu ka.","Do you go to school?","ඔබ පාසලට යනවාද?"),
         (f"いいえ、{IKIN}。","Iie, ikimasen.","No, I don't.","නැහැ, යන්නේ නැහැ.")),
  ("QA", (f"{TOM}に {DEN}しますか。","Tomodachi ni denwa shimasu ka.","Do you call your friend?","ඔබ යාළුවාට දුරකථනයෙන් කතා කරනවාද?"),
         (f"はい、{DEN}します。","Hai, denwa shimasu.","Yes, I do.","ඔව්, කතා කරනවා.")),
  ("QA", (f"{TOS}で {HON}を {YOMK}。","Toshokan de hon wo yomimasu ka.","Do you read books in the library?","ඔබ පුස්තකාලයේදී පොත් කියවනවාද?"),
         (f"いいえ、{YOMN}。","Iie, yomimasen.","No, I don't.","නැහැ, කියවන්නේ නැහැ.")),
  ("QA", (f"{KSH}で {NHG}を {HANK}。","Kyoushitsu de nihongo wo hanashimasu ka.","Do you speak Japanese in the classroom?","ඔබ පන්ති කාමරයේදී ජපන් භාෂාව කතා කරනවාද?"),
         (f"はい、{HAN}。","Hai, hanashimasu.","Yes, I do.","ඔව්, කතා කරනවා.")),
  ("QA", (f"{AST} {GAK}に {KIM}か。","Ashita gakkou ni kimasu ka.","Are you coming to school tomorrow?","ඔබ හෙට පාසලට එනවාද?"),
         (f"はい、{KIM}。","Hai, kimasu.","Yes, I am.","ඔව්, එනවා.")),
  ("QA", (f"{r('今日','きょう')} アルバイトを しますか。","Kyou arubaito wo shimasu ka.","Are you working part-time today?","ඔබ අද අර්ධකාලීන රැකියාව කරනවාද?"),
         ("いいえ、しません。","Iie, shimasen.","No, I'm not.","නැහැ, කරන්නේ නැහැ.")),
]

P7A = dict(
  no="11", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=(f"はい、{BEN}します。　／　いいえ、{BEN}しません。",
         "Hai, benkyou shimasu. / Iie, benkyou shimasen.",
         "Yes, I study. / No, I do not study.",
         "ඔව්, ඉගෙන ගන්නවා. / නැහැ, ඉගෙන ගන්නේ නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P7A2 = dict(
  no="11", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P7A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("ときどき します。","Tokidoki shimasu.","I sometimes do.","සමහර වෙලාවට කරනවා."),
    ("よく します。","Yoku shimasu.","I often do.","නිතරම කරනවා."),
    ("あまり しません。","Amari shimasen.","I don't do it much.","එච්චර කරන්නේ නැහැ."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P7,"p11_1_shimasu"), (P7N,"p11_2_negative"), (P7Q,"p11_3_question"),
                    (P7A,"p11_4_answer"), (P7A2,"p11_5_answer2")]:
        render(p, stem)
