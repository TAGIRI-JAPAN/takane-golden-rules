from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SUW  = r("座","すわ")+"って"
HON  = r("本","ほん")
YON  = r("読","よ")+"んで"
MIZ  = r("水","みず")
NON  = r("飲","の")+"んで"
NAM  = r("名前","な まえ")
KAI  = r("書","か")+"いて"
SEN  = r("先生","せん せい")
SHIT = r("質問","しつ もん")
YAS  = r("休","やす")+"んで"
KYO  = r("教科書","きょう か しょ")
MIT  = r("見","み")+"て"
TOS  = r("図書館","と しょ かん")
NIM  = r("荷物","に もつ")
OIT  = r("置","お")+"いて"
IMA  = r("今","いま")

# ---------------------------------------------------------------- 19-1 基本
P15 = dict(
  no="19", tag=None,
  title_jp="〜しても いいです",
  title_ro='〜 shitemo ii desu &nbsp;|&nbsp; You may 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 න්න පුළුවන්</span>',
  basic=(f"ここに {SUW}も いいです。","Koko ni suwatte mo ii desu.",
         "You may sit here.","මෙතන වාඩිවෙන්න පුළුවන්."),
  use=(f'して いいと きょかする ときに つかいます。'
       f'15の「て」に「も いいです」を つけるだけです。「〜しても よいです」も{r("同","おな")}じ{r("意味","い み")}です。',
       'Use it to give permission. Just take the <b>te</b> form from pattern 15 and add '
       '<b>mo ii desu</b>. <b>shitemo yoi desu</b> means exactly the same thing.',
       'අවසර දෙන්න භාවිතා කරන්න — <b>shitemo ii desu</b> = ...න්න පුළුවන් (අවසරයි). '
       '15 හි <b>te</b> ආකාරයට <b>mo ii desu</b> දාන්න විතරයි. '
       '<b>shitemo yoi desu</b> එකත් එකම අර්ථයයි.'),
  pattern=["NOTE:15の「て」に「も いいです」を つける　/　te ＋ mo ii desu",
           [(YON,"yonde"),"TO",(f"{YON}も いいです","yonde mo ii desu",True)],
           [("（…で）","(… de)"),"BLANK",("しても いいです","shitemo ii desu")]],
  examples=[
    (f"ここに {SUW}も いいです。","Koko ni suwatte mo ii desu.","You may sit here.","මෙතන වාඩිවෙන්න පුළුවන්."),
    (f"この {HON}を {YON}も いいです。","Kono hon wo yonde mo ii desu.","You may read this book.","මේ පොත කියවන්න පුළුවන්."),
    (f"ここで {MIZ}を {NON}も いいです。","Koko de mizu wo nonde mo ii desu.","You may drink water here.","මෙතන වතුර බොන්න පුළුවන්."),
    (f"えんぴつで {NAM}を {KAI}も いいです。","Enpitsu de namae wo kaite mo ii desu.","You may write your name in pencil.","නම පැන්සලෙන් ලියන්න පුළුවන්."),
    (f"{SEN}に {SHIT}しても いいです。","Sensei ni shitsumon shite mo ii desu.","You may ask the teacher a question.","ගුරුතුමාගෙන් ප්‍රශ්නයක් අහන්න පුළුවන්."),
    (f"あした {YAS}も いいです。","Ashita yasunde mo ii desu.","You may take tomorrow off.","හෙට නිවාඩු ගන්න පුළුවන්."),
    (f"{KYO}を {MIT}も いいです。","Kyoukasho wo mite mo ii desu.","You may look at your textbook.","පෙළපොත බලන්න පුළුවන්."),
  ],
  foot="〜しても いいです",
)

# ---------------------------------------------------------------- 19-2 否定
P15N = dict(
  no="19", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜しては いけません",
  title_ro='〜 shitewa ikemasen &nbsp;|&nbsp; You must not 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 න්න බැහැ</span>',
  basic=(f"ここに {SUW}は いけません。","Koko ni suwatte wa ikemasen.",
         "You must not sit here.","මෙතන වාඩිවෙන්න බැහැ."),
  use=(f'「も」が「は」に、「いいです」が「いけません」に かわります。'
       f'とても つよい{r("禁止","きん し")}なので、{r("目上","め うえ")}の{r("人","ひと")}には つかいません。'
       f'ルールや{r("注意","ちゅう い")}を{r("伝","つた")}えるときの ことばです。',
       '<b>mo</b> becomes <b>wa</b>, and <b>ii desu</b> becomes <b>ikemasen</b>. '
       'It is a strong prohibition, so do not use it to a senior person — '
       'it is for stating rules and warnings.',
       '<b>mo</b> එක <b>wa</b> වෙනවා, <b>ii desu</b> එක <b>ikemasen</b> වෙනවා. '
       'මේක ශක්තිමත් තහනමක් නිසා වැඩිමහල් අයට කියන්න එපා — '
       'නීති සහ අනතුරු ඇඟවීම් කියන්න පාවිච්චි කරන එකක්.'),
  pattern=[[("〜ても","~ te mo"),("いいです","ii desu")],
           "ARROW",
           [("〜ては","~ te wa",True),("いけません","ikemasen",True)],
           "NOTE:も　&#8594;　は　/　いいです　&#8594;　いけません"],
  examples=[
    (f"ここに {SUW}は いけません。","Koko ni suwatte wa ikemasen.","You must not sit here.","මෙතන වාඩිවෙන්න බැහැ."),
    (f"この {HON}を {YON}は いけません。","Kono hon wo yonde wa ikemasen.","You must not read this book.","මේ පොත කියවන්න බැහැ."),
    (f"{TOS}で {MIZ}を {NON}は いけません。","Toshokan de mizu wo nonde wa ikemasen.","You must not drink water in the library.","පුස්තකාලයේ වතුර බොන්න බැහැ."),
    (f"えんぴつで {KAI}は いけません。","Enpitsu de kaite wa ikemasen.","You must not write in pencil.","පැන්සලෙන් ලියන්න බැහැ."),
    (f"{IMA} {SHIT}しては いけません。","Ima shitsumon shite wa ikemasen.","You must not ask a question now.","දැන් ප්‍රශ්න අහන්න බැහැ."),
    (f"あした {YAS}は いけません。","Ashita yasunde wa ikemasen.","You must not take tomorrow off.","හෙට නිවාඩු ගන්න බැහැ."),
    (f"テストの とき {KYO}を {MIT}は いけません。","Tesuto no toki kyoukasho wo mite wa ikemasen.","You must not look at your textbook during the test.","විභාගයේදී පෙළපොත බලන්න බැහැ."),
  ],
  foot="〜しては いけません",
)

# ---------------------------------------------------------------- 19-3 疑問
P15Q = dict(
  no="19", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜しても いいですか？",
  title_ro='〜 shitemo ii desu ka &nbsp;|&nbsp; May I 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 න්න පුළුවන්ද?</span>',
  basic=(f"ここに {SUW}も いいですか。","Koko ni suwatte mo ii desu ka.",
         "May I sit here?","මට මෙතන වාඩිවෙන්න පුළුවන්ද?"),
  use=(f'{r("日本","に ほん")}の{r("生活","せい かつ")}で いちばん つかう{r("質問","しつ もん")}の ひとつです。'
       f'なにかを する まえに かならず{r("聞","き")}きましょう。'
       f'まえに「すみません」を つけると もっと ていねいです。',
       'This is one of the most useful questions in daily life in Japan. '
       'Always ask before you do something. '
       'Putting <b>sumimasen</b> in front of it makes it more polite.',
       'ජපානයේ දෛනික ජීවිතයේ වැදගත්ම ප්‍රශ්නවලින් එකක්. '
       'මොනවා හරි කරන්න කලින් අනිවාර්යයෙන් අහන්න. '
       'ඉස්සරහින් <b>sumimasen</b> දැම්මොත් වඩා ආචාරශීලීයි.'),
  pattern=[[("（…で）","(… de)"),"BLANK",("しても いいです","shitemo ii desu")],
           "ARROW",
           [("（…で）","(… de)"),"BLANK",("しても いいですか？","shitemo ii desu ka",True)]],
  examples=[
    (f"ここに {SUW}も いいですか。","Koko ni suwatte mo ii desu ka.","May I sit here?","මට මෙතන වාඩිවෙන්න පුළුවන්ද?"),
    (f"この {HON}を {YON}も いいですか。","Kono hon wo yonde mo ii desu ka.","May I read this book?","මට මේ පොත කියවන්න පුළුවන්ද?"),
    (f"ここで {MIZ}を {NON}も いいですか。","Koko de mizu wo nonde mo ii desu ka.","May I drink water here?","මට මෙතන වතුර බොන්න පුළුවන්ද?"),
    (f"えんぴつで {KAI}も いいですか。","Enpitsu de kaite mo ii desu ka.","May I write in pencil?","මට පැන්සලෙන් ලියන්න පුළුවන්ද?"),
    (f"{SHIT}しても いいですか。","Shitsumon shite mo ii desu ka.","May I ask a question?","මට ප්‍රශ්නයක් අහන්න පුළුවන්ද?"),
    (f"あした {YAS}も いいですか。","Ashita yasunde mo ii desu ka.","May I take tomorrow off?","මට හෙට නිවාඩු ගන්න පුළුවන්ද?"),
    (f"{KYO}を {MIT}も いいですか。","Kyoukasho wo mite mo ii desu ka.","May I look at my textbook?","මට පෙළපොත බලන්න පුළුවන්ද?"),
  ],
  foot="〜しても いいですか？",
)

# ---------------------------------------------------------------- 19-4 / 19-5 答え方
_USE = (f'ゆるす ときは「はい、どうぞ。」「はい、いいですよ。」。'
        f'ことわる ときは「すみません、ちょっと…。」が いちばん やわらかくて{r("安全","あん ぜん")}です。'
        f'「だめです」は つよいので、{r("友","とも")}だちにだけ つかいましょう。',
        'To allow: <b>Hai, douzo</b> or <b>Hai, ii desu yo</b>. '
        'To refuse: <b>Sumimasen, chotto…</b> is the softest and safest. '
        '<b>Dame desu</b> is strong — use it only with friends.',
        'අවසර දෙනවා නම්: <b>Hai, douzo</b> හෝ <b>Hai, ii desu yo</b>. '
        'ප්‍රතික්ෂේප කරනවා නම් <b>Sumimasen, chotto…</b> තමයි මෘදුම සහ ආරක්ෂිතම. '
        '<b>Dame desu</b> ශක්තිමතුයි — යාළුවන්ට විතරක් කියන්න.')

_PAT = [[("はい、","Hai,"),("どうぞ","douzo",True)],
        [("すみません、","Sumimasen,"),("ちょっと…","chotto…",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Allowing and refusing &nbsp;|&nbsp; '
          '<span class="si">අවසර දීම / ප්‍රතික්ෂේප කිරීම</span>')

_QA = [
  ("QA", (f"ここに {SUW}も いいですか。","Koko ni suwatte mo ii desu ka.","May I sit here?","මට මෙතන වාඩිවෙන්න පුළුවන්ද?"),
         ("はい、どうぞ。","Hai, douzo.","Yes, go ahead.","ඔව්, කරන්න.")),
  ("QA", (f"この {HON}を {YON}も いいですか。","Kono hon wo yonde mo ii desu ka.","May I read this book?","මට මේ පොත කියවන්න පුළුවන්ද?"),
         ("はい、いいですよ。","Hai, ii desu yo.","Sure, that's fine.","ඔව්, කමක් නැහැ.")),
  ("QA", (f"ここで {MIZ}を {NON}も いいですか。","Koko de mizu wo nonde mo ii desu ka.","May I drink water here?","මට මෙතන වතුර බොන්න පුළුවන්ද?"),
         ("すみません、ちょっと…。","Sumimasen, chotto…","Sorry, I'm afraid not.","සමාවෙන්න, ඒක ටිකක්…")),
  ("QA", (f"えんぴつで {KAI}も いいですか。","Enpitsu de kaite mo ii desu ka.","May I write in pencil?","මට පැන්සලෙන් ලියන්න පුළුවන්ද?"),
         ("いいえ、いけません。","Iie, ikemasen.","No, you must not.","නැහැ, බැහැ.")),
  ("QA", (f"{SHIT}しても いいですか。","Shitsumon shite mo ii desu ka.","May I ask a question?","මට ප්‍රශ්නයක් අහන්න පුළුවන්ද?"),
         ("はい、どうぞ。","Hai, douzo.","Yes, please do.","ඔව්, අහන්න.")),
  ("QA", (f"あした {YAS}も いいですか。","Ashita yasunde mo ii desu ka.","May I take tomorrow off?","මට හෙට නිවාඩු ගන්න පුළුවන්ද?"),
         ("はい、いいですよ。","Hai, ii desu yo.","Yes, that's fine.","ඔව්, කමක් නැහැ.")),
  ("QA", (f"{KYO}を {MIT}も いいですか。","Kyoukasho wo mite mo ii desu ka.","May I look at my textbook?","මට පෙළපොත බලන්න පුළුවන්ද?"),
         (f"いいえ、{MIT}は いけません。","Iie, mite wa ikemasen.","No, you must not look at it.","නැහැ, බලන්න බැහැ.")),
  ("QA", ("トイレを つかっても いいですか。","Toire wo tsukatte mo ii desu ka.","May I use the toilet?","මට වැසිකිළිය පාවිච්චි කරන්න පුළුවන්ද?"),
         ("はい、どうぞ。","Hai, douzo.","Yes, go ahead.","ඔව්, කරන්න.")),
  ("QA", (f"ここに {NIM}を {OIT}も いいですか。","Koko ni nimotsu wo oite mo ii desu ka.","May I put my bag here?","මට මගේ බඩු මෙතන තියන්න පුළුවන්ද?"),
         ("すみません、ちょっと…。","Sumimasen, chotto…","Sorry, I'm afraid not.","සමාවෙන්න, ඒක ටිකක්…")),
]

P15A = dict(
  no="19", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp="どうぞ / ちょっと… の 答え方",
  title_ro=_TITLE[1],
  basic=("はい、どうぞ。　／　すみません、ちょっと…。","Hai, douzo. / Sumimasen, chotto…",
         "Yes, go ahead. / Sorry, I'm afraid not.","ඔව්, කරන්න. / සමාවෙන්න, ඒක ටිකක්…"),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="どうぞ / ちょっと…",
)

P15A2 = dict(
  no="19", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp="どうぞ / ちょっと… の 答え方",
  title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P15A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("はい、どうぞ。","Hai, douzo.","Yes, go ahead.","ඔව්, කරන්න."),
    ("はい、いいですよ。","Hai, ii desu yo.","Sure, that's fine.","ඔව්, කමක් නැහැ."),
    ("すみません、ちょっと…。","Sumimasen, chotto…","Sorry, I'm afraid not.","සමාවෙන්න, ඒක ටිකක්…"),
    ("だめです。","Dame desu.","No, you can't.","බැහැ."),
  ],
  foot="どうぞ / ちょっと…",
)

if __name__ == "__main__":
    for p, stem in [(P15,"p19_1_temoii"), (P15N,"p19_2_negative"), (P15Q,"p19_3_question"),
                    (P15A,"p19_4_answer"), (P15A2,"p19_5_answer2")]:
        render(p, stem)
