from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
WTC  = r("私","わたし")+"たち"
IMA  = r("今","いま")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
HON  = r("本","ほん")
YON  = r("読","よ")+"んで"
SEN  = r("先生","せん せい")
KSH  = r("教室","きょう しつ")
HAS  = r("話","はな")+"して"
TOM  = r("友","とも")+"だち"
TAB  = r("食","た")+"べて"
GKS  = r("学生","がく せい")+"たち"
ANI  = r("兄","あに")
HAT  = r("働","はたら")+"いて"
NAN  = r("何","なに")

_NOTE_TE = ("NOTE:読みます→読んで　/　話します→話して　/　食べます→食べて　/　"
            "まちます→まって　/　はたらきます→はたらいて")

# ---------------------------------------------------------------- 15-1 基本
P9 = dict(
  no="15", tag=None,
  title_jp="〜しています（1）",
  title_ro='〜 shite imasu &nbsp;|&nbsp; I am 〜ing (now) &nbsp;|&nbsp; '
           '<span class="si">〜 මින් ඉන්නවා</span>',
  basic=(f"{W}は {IMA} {NHG}を {BEN}しています。","Watashi wa ima nihongo wo benkyou shite imasu.",
         "I am studying Japanese now.","මම දැන් ජපන් භාෂාව ඉගෙන ගනිමින් ඉන්නවා."),
  use=(f'{IMA}、しているところを あらわします。「ます」を「て」に かえて「います」を つけます。'
       f'「{IMA}」と いっしょに よく{r("使","つか")}います。11の「〜します」は しゅうかん、15は{IMA}のことです。',
       'It shows what is happening right now. Change <b>masu</b> to <b>te</b> and add <b>imasu</b>. '
       'It often appears with <b>ima</b> (now). Pattern 11 is about habits; pattern 15 is about now.',
       'දැන් සිදුවෙමින් පවතින දේ පෙන්නනවා — <b>te imasu</b> = ...මින් ඉන්නවා. '
       '<b>masu</b> එක <b>te</b> කරලා <b>imasu</b> දාන්න. <b>ima</b> (දැන්) එක්ක බොහෝවිට එනවා. '
       '11 කියන්නේ පුරුදු; 15 කියන්නේ දැන් වෙන දේ.'),
  pattern=["NOTE:「ます」を「て」に かえて「います」を つける　/　masu &#8594; te + imasu",
           [(r("食","た")+"べます","tabemasu"),"TO",(r("食","た")+"べて います","tabete imasu",True)],
           [(r("読","よ")+"みます","yomimasu"),"TO",(r("読","よ")+"んで います","yonde imasu",True)],
           _NOTE_TE],
  examples=[
    (f"{W}は {IMA} {NHG}を {BEN}しています。","Watashi wa ima nihongo wo benkyou shite imasu.","I am studying Japanese now.","මම දැන් ජපන් භාෂාව ඉගෙන ගනිමින් ඉන්නවා."),
    (f"{W}は {IMA} {HON}を {YON}います。","Watashi wa ima hon wo yonde imasu.","I am reading a book now.","මම දැන් පොතක් කියවමින් ඉන්නවා."),
    (f"{SEN}は {KSH}で {HAS}います。","Sensei wa kyoushitsu de hanashite imasu.","The teacher is talking in the classroom.","ගුරුතුමා පන්ති කාමරයේ කතා කරමින් ඉන්නවා."),
    (f"{TOM}は ごはんを {TAB}います。","Tomodachi wa gohan wo tabete imasu.","My friend is eating a meal.","මගේ යාළුවා කෑම කමින් ඉන්නවා."),
    (f"{GKS}は バスを まっています。","Gakuseitachi wa basu wo matte imasu.","The students are waiting for the bus.","ශිෂ්‍යයෝ බස් එකට බලාගෙන ඉන්නවා."),
    (f"{ANI}は {IMA} {HAT}います。","Ani wa ima hataraite imasu.","My older brother is working now.","මගේ අයියා දැන් වැඩ කරමින් ඉන්නවා."),
    (f"{WTC}は {IMA} テストを しています。","Watashitachi wa ima tesuto wo shite imasu.","We are having a test now.","අපි දැන් විභාගයක් කරමින් ඉන්නවා."),
  ],
  foot="〜しています（1）",
)

# ---------------------------------------------------------------- 15-2 否定
P9N = dict(
  no="15", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜していません",
  title_ro='〜 shite imasen &nbsp;|&nbsp; I am not 〜ing &nbsp;|&nbsp; '
           '<span class="si">දැන් 〜 කරන්නේ නැහැ</span>',
  basic=(f"{W}は {IMA} {NHG}を {BEN}していません。","Watashi wa ima nihongo wo benkyou shite imasen.",
         "I am not studying Japanese now.","මම දැන් ජපන් භාෂාව ඉගෙන ගන්නේ නැහැ."),
  use=(f'さいごの「います」を「いません」に{r("変","か")}えるだけです。'
       f'「て」の{r("部分","ぶ ぶん")}は{r("変","か")}わりません。09・10の「いません」と{r("同","おな")}じ かたちです。',
       'Just change the final <b>imasu</b> to <b>imasen</b>. The <b>te</b> part does not change. '
       'It is the same <b>imasen</b> you learned in patterns 09 and 10.',
       'අන්තිම <b>imasu</b> එක <b>imasen</b> කියලා වෙනස් කරන්න විතරයි. <b>te</b> කොටස වෙනස් වෙන්නේ නැහැ. '
       '09, 10 වල <b>imasen</b> එකමයි.'),
  pattern=[[("〜て います","~ te imasu"),"TO",("〜て いません","~ te imasen",True)],
           "NOTE:「て」は そのまま　/　the te part never changes",
           [(r("読","よ")+"んで います","yonde imasu"),"TO",(r("読","よ")+"んで いません","yonde imasen",True)]],
  examples=[
    (f"{W}は {IMA} {NHG}を {BEN}していません。","Watashi wa ima nihongo wo benkyou shite imasen.","I am not studying Japanese now.","මම දැන් ජපන් භාෂාව ඉගෙන ගන්නේ නැහැ."),
    (f"{W}は {IMA} {HON}を {YON}いません。","Watashi wa ima hon wo yonde imasen.","I am not reading a book now.","මම දැන් පොතක් කියවන්නේ නැහැ."),
    (f"{SEN}は {KSH}で {HAS}いません。","Sensei wa kyoushitsu de hanashite imasen.","The teacher is not talking in the classroom.","ගුරුතුමා පන්ති කාමරයේ කතා කරන්නේ නැහැ."),
    (f"{TOM}は ごはんを {TAB}いません。","Tomodachi wa gohan wo tabete imasen.","My friend is not eating a meal.","මගේ යාළුවා කෑම කන්නේ නැහැ."),
    (f"{GKS}は バスを まっていません。","Gakuseitachi wa basu wo matte imasen.","The students are not waiting for the bus.","ශිෂ්‍යයෝ බස් එකට බලාගෙන නැහැ."),
    (f"{ANI}は {IMA} {HAT}いません。","Ani wa ima hataraite imasen.","My older brother is not working now.","මගේ අයියා දැන් වැඩ කරන්නේ නැහැ."),
    (f"{WTC}は {IMA} テストを していません。","Watashitachi wa ima tesuto wo shite imasen.","We are not having a test now.","අපි දැන් විභාගයක් කරන්නේ නැහැ."),
  ],
  foot="〜していません",
)

# ---------------------------------------------------------------- 15-3 疑問
P9Q = dict(
  no="15", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜していますか？",
  title_ro='〜 shite imasu ka &nbsp;|&nbsp; Are you 〜ing? &nbsp;|&nbsp; '
           '<span class="si">දැන් 〜 කරනවාද?</span>',
  basic=(f"あなたは {IMA} {NHG}を {BEN}していますか。","Anata wa ima nihongo wo benkyou shite imasu ka.",
         "Are you studying Japanese now?","ඔබ දැන් ජපන් භාෂාව ඉගෙන ගන්නවාද?"),
  use=(f'「います」のうしろに「か」をつけるだけです。'
       f'「{IMA} {NAN}を していますか」は、{r("電話","でん わ")}や メッセージで とても よく{r("使","つか")}う{r("質問","しつ もん")}です。',
       'Just add <b>ka</b> after <b>imasu</b>. '
       '<b>Ima nani wo shite imasu ka</b> ("What are you doing now?") is a very common question '
       'on the phone and in messages.',
       '<b>imasu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       '<b>Ima nani wo shite imasu ka</b> ("දැන් මොකද කරන්නේ?") කියන එක දුරකථනයේදී සහ '
       'පණිවිඩවලදී ගොඩක් භාවිතා වෙනවා.'),
  pattern=[[("〜は","~ wa"),("〜を","~ wo"),("しています","shite imasu")],
           "ARROW",
           [("〜は","~ wa"),("〜を","~ wo"),("していますか？","shite imasu ka",True)]],
  examples=[
    (f"あなたは {IMA} {NHG}を {BEN}していますか。","Anata wa ima nihongo wo benkyou shite imasu ka.","Are you studying Japanese now?","ඔබ දැන් ජපන් භාෂාව ඉගෙන ගන්නවාද?"),
    (f"あなたは {IMA} {HON}を {YON}いますか。","Anata wa ima hon wo yonde imasu ka.","Are you reading a book now?","ඔබ දැන් පොතක් කියවනවාද?"),
    (f"{SEN}は {KSH}で {HAS}いますか。","Sensei wa kyoushitsu de hanashite imasu ka.","Is the teacher talking in the classroom?","ගුරුතුමා පන්ති කාමරයේ කතා කරනවාද?"),
    (f"{TOM}は ごはんを {TAB}いますか。","Tomodachi wa gohan wo tabete imasu ka.","Is your friend eating a meal?","ඔබේ යාළුවා කෑම කනවාද?"),
    (f"{GKS}は バスを まっていますか。","Gakuseitachi wa basu wo matte imasu ka.","Are the students waiting for the bus?","ශිෂ්‍යයෝ බස් එකට බලාගෙන ඉන්නවාද?"),
    (f"{ANI}は {IMA} {HAT}いますか。","Ani wa ima hataraite imasu ka.","Is your older brother working now?","ඔබේ අයියා දැන් වැඩ කරනවාද?"),
    (f"{IMA} {NAN}を していますか。","Ima nani wo shite imasu ka.","What are you doing now?","දැන් මොකද කරන්නේ?"),
  ],
  foot="〜していますか？",
)

# ---------------------------------------------------------------- 15-4 / 15-5 答え方
_USE = (f'「はい、〜て います。」「いいえ、〜て いません。」と{r("答","こた")}えます。'
        f'「{IMA} {NAN}を していますか」には、はい・いいえではなく、している ことを{r("言","い")}います。',
        'Answer with <b>Hai, 〜 te imasu</b> or <b>Iie, 〜 te imasen</b>. '
        'For <b>Ima nani wo shite imasu ka</b>, do not answer yes or no — say what you are doing.',
        '<b>Hai, 〜 te imasu</b> හෝ <b>Iie, 〜 te imasen</b> කියලා උත්තර දෙන්න. '
        '<b>Ima nani wo shite imasu ka</b> කියන ප්‍රශ්නයට ඔව්/නැහැ නෙවෙයි — කරන දේ කියන්න.')

_PAT = [[("はい、","Hai,"),"BLANK",("て います","te imasu",True)],
        [("いいえ、","Iie,"),"BLANK",("て いません","te imasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{IMA} {NHG}を {BEN}していますか。","Ima nihongo wo benkyou shite imasu ka.","Are you studying Japanese now?","ඔබ දැන් ජපන් භාෂාව ඉගෙන ගන්නවාද?"),
         (f"はい、{BEN}しています。","Hai, benkyou shite imasu.","Yes, I am.","ඔව්, ඉගෙන ගන්නවා.")),
  ("QA", (f"{IMA} {HON}を {YON}いますか。","Ima hon wo yonde imasu ka.","Are you reading a book now?","ඔබ දැන් පොතක් කියවනවාද?"),
         (f"いいえ、{YON}いません。","Iie, yonde imasen.","No, I'm not.","නැහැ, කියවන්නේ නැහැ.")),
  ("QA", (f"{SEN}は {KSH}で {HAS}いますか。","Sensei wa kyoushitsu de hanashite imasu ka.","Is the teacher talking in the classroom?","ගුරුතුමා පන්ති කාමරයේ කතා කරනවාද?"),
         (f"はい、{HAS}います。","Hai, hanashite imasu.","Yes, he is.","ඔව්, කතා කරනවා.")),
  ("QA", (f"{TOM}は ごはんを {TAB}いますか。","Tomodachi wa gohan wo tabete imasu ka.","Is your friend eating a meal?","ඔබේ යාළුවා කෑම කනවාද?"),
         (f"いいえ、{TAB}いません。","Iie, tabete imasen.","No, he isn't.","නැහැ, කන්නේ නැහැ.")),
  ("QA", (f"{GKS}は バスを まっていますか。","Gakuseitachi wa basu wo matte imasu ka.","Are the students waiting for the bus?","ශිෂ්‍යයෝ බස් එකට බලාගෙන ඉන්නවාද?"),
         ("はい、まっています。","Hai, matte imasu.","Yes, they are.","ඔව්, බලාගෙන ඉන්නවා.")),
  ("QA", (f"{ANI}は {IMA} {HAT}いますか。","Ani wa ima hataraite imasu ka.","Is your older brother working now?","ඔබේ අයියා දැන් වැඩ කරනවාද?"),
         (f"はい、{HAT}います。","Hai, hataraite imasu.","Yes, he is.","ඔව්, වැඩ කරනවා.")),
  ("QA", (f"{IMA} {NAN}を していますか。","Ima nani wo shite imasu ka.","What are you doing now?","දැන් මොකද කරන්නේ?"),
         (f"{r('宿題','しゅく だい')}を しています。","Shukudai wo shite imasu.","I'm doing my homework.","මම ගෙදර වැඩ කරමින් ඉන්නවා.")),
  ("QA", (f"{SEN}は {IMA} どこに いますか。","Sensei wa ima doko ni imasu ka.","Where is the teacher now?","ගුරුතුමා දැන් කොහෙද?"),
         (f"{KSH}で {HAS}います。","Kyoushitsu de hanashite imasu.","He is talking in the classroom.","පන්ති කාමරයේ කතා කරමින් ඉන්නවා.")),
  ("QA", (f"{IMA} いそがしいですか。","Ima isogashii desu ka.","Are you busy now?","ඔබ දැන් කාර්යබහුලද?"),
         (f"はい、{BEN}しています。","Hai, benkyou shite imasu.","Yes, I'm studying.","ඔව්, මම ඉගෙන ගනිමින් ඉන්නවා.")),
]

P9A = dict(
  no="15", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=(f"はい、{BEN}しています。　／　いいえ、{BEN}していません。",
         "Hai, benkyou shite imasu. / Iie, benkyou shite imasen.",
         "Yes, I am studying. / No, I am not studying.",
         "ඔව්, ඉගෙන ගන්නවා. / නැහැ, ඉගෙන ගන්නේ නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P9A2 = dict(
  no="15", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P9A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{IMA} {r('忙','いそが')}しいです。","Ima isogashii desu.","I'm busy now.","දැන් කාර්යබහුලයි."),
    ("なにも していません。","Nani mo shite imasen.","I'm not doing anything.","මොකුත් කරන්නේ නැහැ."),
    (f"{r('少','すこ')}し まってください。","Sukoshi matte kudasai.","Please wait a moment.","ටිකක් ඉන්න."),
    (f"あとで {r('電話','でん わ')}します。","Ato de denwa shimasu.","I'll call you later.","පස්සේ කතා කරන්නම්."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P9,"p15_1_shiteimasu"), (P9N,"p15_2_negative"), (P9Q,"p15_3_question"),
                    (P9A,"p15_4_answer"), (P9A2,"p15_5_answer2")]:
        render(p, stem)
