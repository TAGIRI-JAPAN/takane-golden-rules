from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

DAR  = r("誰","だれ")
GKS  = r("学生","がく せい")
HITO = r("人","ひと")
SEN  = r("先生","せん せい")
KSH  = r("教室","きょう しつ")
KYO  = r("教科書","きょう か しょ")
OSHI = r("教","おし")+"えて"
DEN  = r("電話","でん わ")
TEG  = r("手紙","て がみ")
KAK  = r("書","か")+"き"
HON  = r("本","ほん")
YON  = r("読","よ")+"んで"
KIM  = r("来","き")+"ます"
KIMM = r("来","き")+"ました"
HAN  = r("話","はな")+"して"
ICH  = r("一番","いち ばん")
KAZ  = r("家族","か ぞく")
W    = r("私","わたし")
SATO = r("佐藤","さ とう")
KIN  = r("昨日","きのう")
GAK  = r("学校","がっ こう")
KUR  = "クラス"

# ---------------------------------------------------------------- 22-1 基本
P17 = dict(
  no="22", tag=None,
  title_jp=f"〜は {DAR}ですか？",
  title_ro='〜 wa dare desu ka &nbsp;|&nbsp; Who is 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කවුද?</span>',
  basic=(f"あの {GKS}は {DAR}ですか。","Ano gakusei wa dare desu ka.",
         "Who is that student?","අර ශිෂ්‍යයා කවුද?"),
  use=(f'「{DAR}」は{HITO}を たずねる ことばです。21の「{r("何","なに")}」と{r("同","おな")}じ{r("作","つく")}り{r("方","かた")}です。'
       f'「{DAR}の＋めいし」で「{DAR}の ものか」を たずねます。',
       '<b>dare</b> asks about a person. It works exactly like <b>nani</b> in pattern 21. '
       '<b>dare no</b> + noun asks whose something is.',
       '<b>dare</b> කියන්නේ කෙනෙක් ගැන අහන එක — <b>dare desu ka</b> = කවුද? '
       '21 හි <b>nani</b> වගේමයි. <b>dare no</b> ＋ නාම පදය කියලා කාගේද කියලා අහන්න.'),
  pattern=[[("〜は","~ wa"),(f"{DAR}ですか？","dare desu ka",True)],
           [("〜は","~ wa"),(f"{DAR}の ＋ めいし ですか？","dare no + noun desu ka",True)],
           f"NOTE:ていねいに {r('言','い')}うとき：{DAR} &#8594; どなた　/　polite form is donata"],
  examples=[
    (f"あの {GKS}は {DAR}ですか。","Ano gakusei wa dare desu ka.","Who is that student?","අර ශිෂ්‍යයා කවුද?"),
    (f"となりの {HITO}は {DAR}ですか。","Tonari no hito wa dare desu ka.","Who is the person next to you?","ඔබ ළඟ ඉන්න කෙනා කවුද?"),
    (f"きょうの {SEN}は {DAR}ですか。","Kyou no sensei wa dare desu ka.","Who is today's teacher?","අද ගුරුතුමා කවුද?"),
    (f"{KUR}の リーダーは {DAR}ですか。","Kurasu no riidaa wa dare desu ka.","Who is the class leader?","පන්තියේ නායකයා කවුද?"),
    (f"あの {HITO}たちは {DAR}ですか。","Ano hitotachi wa dare desu ka.","Who are those people?","අර අය කවුද?"),
    (f"この かさは {DAR}の ですか。","Kono kasa wa dare no desu ka.","Whose umbrella is this?","මේ කුඩය කාගේද?"),
    (f"これは {DAR}の {KYO}ですか。","Kore wa dare no kyoukasho desu ka.","Whose textbook is this?","මේක කාගේ පෙළපොතක්ද?"),
  ],
  foot="〜は 誰ですか？",
)

# ---------------------------------------------------------------- 22-2 応用①
P17B = dict(
  no="22", tag="応用 ①　誰が 〜しますか？ / WITH VERBS",
  title_jp=f"{DAR}が 〜しますか？",
  title_ro='dare ga 〜 shimasu ka &nbsp;|&nbsp; Who does 〜? &nbsp;|&nbsp; '
           '<span class="si">කවුද 〜 කරන්නේ?</span>',
  basic=(f"{DAR}が {r('日本語','に ほん ご')}を {OSHI}いますか。","Dare ga nihongo wo oshiete imasu ka.",
         "Who is teaching Japanese?","ජපන් භාෂාව උගන්නන්නේ කවුද?"),
  use=(f'する{HITO}を たずねるときは「{DAR}が」、あいてを たずねるときは「{DAR}に」です。',
       'Use <b>dare ga</b> to ask who does the action, and <b>dare ni</b> to ask who receives it.',
       'ක්‍රියාව කරන කෙනා අහන්න <b>dare ga</b> = කවුද; ලබන කෙනා අහන්න <b>dare ni</b> = කාටද.'),
  pattern=[[(f"{DAR}が","dare ga",True),("しますか？","shimasu ka")],
           [(f"{DAR}が","dare ga",True),("していますか？","shite imasu ka")],
           [(f"{DAR}に","dare ni",True),("したいですか？","shitai desu ka")],
           f"NOTE:{DAR}が = する{HITO}　/　{DAR}に = あいて（කාටද）"],
  examples=[
    (f"{DAR}が {KSH}の そうじを しますか。","Dare ga kyoushitsu no souji wo shimasu ka.","Who cleans the classroom?","පන්ති කාමරය කවුද පිරිසිදු කරන්නේ?"),
    (f"{DAR}が {r('日本語','に ほん ご')}を {OSHI}いますか。","Dare ga nihongo wo oshiete imasu ka.","Who is teaching Japanese?","ජපන් භාෂාව උගන්නන්නේ කවුද?"),
    (f"{DAR}に {DEN}したいですか。","Dare ni denwa shitai desu ka.","Who do you want to call?","ඔබට කාටද කතා කරන්න ඕන?"),
    (f"{DAR}が バスを まっていますか。","Dare ga basu wo matte imasu ka.","Who is waiting for the bus?","බස් එකට බලාගෙන ඉන්නේ කවුද?"),
    (f"{DAR}に {TEG}を {KAK}たいですか。","Dare ni tegami wo kakitai desu ka.","Who do you want to write a letter to?","ඔබට කාට ලිපියක් ලියන්න ඕන?"),
    (f"{DAR}が この {HON}を {YON}いますか。","Dare ga kono hon wo yonde imasu ka.","Who is reading this book?","මේ පොත කියවන්නේ කවුද?"),
    (f"{DAR}が あした {KIM}か。","Dare ga ashita kimasu ka.","Who is coming tomorrow?","හෙට එන්නේ කවුද?"),
  ],
  foot="誰が 〜しますか？",
)

# ---------------------------------------------------------------- 22-3 応用②
P17C = dict(
  no="22", tag="応用 ②　誰が しましたか？ / PAST",
  title_jp=f"{DAR}が しましたか？",
  title_ro='dare ga shimashita ka &nbsp;|&nbsp; Who did 〜? &nbsp;|&nbsp; '
           '<span class="si">කවුද කළේ?</span>',
  basic=(f"{DAR}が {KSH}の そうじを しましたか。","Dare ga kyoushitsu no souji wo shimashita ka.",
         "Who cleaned the classroom?","පන්ති කාමරය පිරිසිදු කළේ කවුද?"),
  use=(f'13の「ました」と{r("組","く")}み{r("合","あ")}わせるだけです。'
       f'「{DAR}が」「{DAR}に」の{r("使","つか")}い{r("分","わ")}けは かこでも{r("同","おな")}じです。',
       'Just combine it with the past forms from pattern 13. '
       'The difference between <b>dare ga</b> and <b>dare ni</b> stays the same in the past.',
       '13 හි අතීත ආකාර එක්ක එකතු කරන්න විතරයි. '
       '<b>dare ga</b> සහ <b>dare ni</b> අතර වෙනස අතීතයේදීත් එකමයි.'),
  pattern=[[(f"{DAR}が","dare ga",True),("しましたか？","shimashita ka")],
           [(f"{DAR}が","dare ga",True),("していましたか？","shite imashita ka")],
           [(f"{DAR}に","dare ni",True),("しましたか？","shimashita ka")]],
  examples=[
    (f"{DAR}が {KSH}の そうじを しましたか。","Dare ga kyoushitsu no souji wo shimashita ka.","Who cleaned the classroom?","පන්ති කාමරය පිරිසිදු කළේ කවුද?"),
    (f"{DAR}が {KIN} {GAK}に {KIMM}か。","Dare ga kinou gakkou ni kimashita ka.","Who came to school yesterday?","ඊයේ පාසලට ආවේ කවුද?"),
    (f"{KIN} {DAR}に {DEN}しましたか。","Kinou dare ni denwa shimashita ka.","Who did you call yesterday?","ඊයේ ඔබ කාටද කතා කළේ?"),
    (f"{DAR}が この {HON}を {YON}いましたか。","Dare ga kono hon wo yonde imashita ka.","Who was reading this book?","මේ පොත කියවමින් හිටියේ කවුද?"),
    (f"{DAR}が {SEN}と {HAN}いましたか。","Dare ga sensei to hanashite imashita ka.","Who was talking with the teacher?","ගුරුතුමා එක්ක කතා කරමින් හිටියේ කවුද?"),
    (f"{DAR}に {TEG}を {KAK}ましたか。","Dare ni tegami wo kakimashita ka.","Who did you write a letter to?","ඔබ කාට ලිපියක් ලිව්වේ?"),
    (f"{DAR}が {ICH}に {KIMM}か。","Dare ga ichiban ni kimashita ka.","Who came first?","පළමුවෙන් ආවේ කවුද?"),
  ],
  foot="誰が しましたか？",
)

# ---------------------------------------------------------------- 22-4 / 22-5 答え方
_USE = (f'21と{r("同","おな")}じで「はい」「いいえ」では{r("答","こた")}えません。{HITO}の{r("名前","な まえ")}を{r("言","い")}います。'
        f'「{DAR}の」の{r("質問","しつ もん")}には「〜のです」と{r("答","こた")}えます。',
        'As in pattern 21, you never answer with <b>hai</b> or <b>iie</b> — you name the person. '
        'For a <b>dare no</b> question, answer with <b>〜 no desu</b>.',
        '21 වගේම <b>hai</b> හෝ <b>iie</b> කියලා උත්තර දෙන්නේ නැහැ — කෙනාගේ නම කියන්න. '
        '<b>dare no</b> ප්‍රශ්නයකට <b>〜 no desu</b> කියලා උත්තර දෙන්න.')

_PAT = ["NOTE:【 ちゅうい 】「はい / いいえ」では 答えません　/　never answer yes or no",
        [(f"{DAR}ですか？","dare desu ka"),"TO",(f"{HITO}の {r('名前','な まえ')}を {r('言','い')}う","name the person",True)],
        [(f"{DAR}の ですか？","dare no desu ka"),"TO",("「〜の です」と 言う","say ~ no desu",True)]]

_QA = [
  ("QA", (f"あの {GKS}は {DAR}ですか。","Ano gakusei wa dare desu ka.","Who is that student?","අර ශිෂ්‍යයා කවුද?"),
         ("サマンさんです。","Saman-san desu.","That's Saman.","ඒක සමන්.")),
  ("QA", (f"となりの {HITO}は {DAR}ですか。","Tonari no hito wa dare desu ka.","Who is the person next to you?","ඔබ ළඟ ඉන්න කෙනා කවුද?"),
         (f"{W}の クラスメートです。","Watashi no kurasumeeto desu.","She is my classmate.","ඒක මගේ පන්තියේ මිතුරෙක්.")),
  ("QA", (f"きょうの {SEN}は {DAR}ですか。","Kyou no sensei wa dare desu ka.","Who is today's teacher?","අද ගුරුතුමා කවුද?"),
         (f"{SATO}{SEN}です。","Satou-sensei desu.","It's Mr Sato.","ඒක සතෝ ගුරුතුමා.")),
  ("QA", (f"この かさは {DAR}の ですか。","Kono kasa wa dare no desu ka.","Whose umbrella is this?","මේ කුඩය කාගේද?"),
         (f"{W}の です。","Watashi no desu.","It's mine.","ඒක මගේ.")),
  ("QA", (f"これは {DAR}の {KYO}ですか。","Kore wa dare no kyoukasho desu ka.","Whose textbook is this?","මේක කාගේ පෙළපොතක්ද?"),
         (f"サマンさんの {KYO}です。","Saman-san no kyoukasho desu.","It's Saman's textbook.","ඒක සමන්ගේ පෙළපොත.")),
  ("QA", (f"{DAR}が {r('日本語','に ほん ご')}を {OSHI}いますか。","Dare ga nihongo wo oshiete imasu ka.","Who is teaching Japanese?","ජපන් භාෂාව උගන්නන්නේ කවුද?"),
         (f"{SATO}{SEN}が {OSHI}います。","Satou-sensei ga oshiete imasu.","Mr Sato is teaching it.","සතෝ ගුරුතුමා උගන්නනවා.")),
  ("QA", (f"{KIN} {DAR}に {DEN}しましたか。","Kinou dare ni denwa shimashita ka.","Who did you call yesterday?","ඊයේ ඔබ කාටද කතා කළේ?"),
         (f"{KAZ}に {DEN}しました。","Kazoku ni denwa shimashita.","I called my family.","මම මගේ පවුලට කතා කළා.")),
  ("QA", (f"{KUR}の リーダーは {DAR}ですか。","Kurasu no riidaa wa dare desu ka.","Who is the class leader?","පන්තියේ නායකයා කවුද?"),
         (f"{W}です。","Watashi desu.","It's me.","ඒක මම.")),
  ("QA", (f"{DAR}が {ICH}に {KIMM}か。","Dare ga ichiban ni kimashita ka.","Who came first?","පළමුවෙන් ආවේ කවුද?"),
         ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ.")),
]

_TITLE_RO = ('Dare no shitsumon no kotaekata &nbsp;|&nbsp; Answering a "who" question &nbsp;|&nbsp; '
             '<span class="si">"කවුද?" ප්‍රශ්නයට උත්තර දීම</span>')

P17A = dict(
  no="22", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=f"{DAR}の 質問の 答え方",
  title_ro=_TITLE_RO,
  basic=(f"あの {GKS}は {DAR}ですか。　&#8594;　サマンさんです。",
         "Ano gakusei wa dare desu ka. → Saman-san desu.",
         "Who is that student? → That's Saman.","අර ශිෂ්‍යයා කවුද? → ඒක සමන්."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="誰の 質問の 答え方",
)

P17A2 = dict(
  no="22", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=f"{DAR}の 質問の 答え方",
  title_ro=_TITLE_RO,
  skip=("basic","use","pattern"), start=4,
  basic=P17A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{W}です。","Watashi desu.","It's me.","ඒක මම."),
    (f"{W}の です。","Watashi no desu.","It's mine.","ඒක මගේ."),
    (f"{r('知','し')}らない {HITO}です。","Shiranai hito desu.","Someone I don't know.","මම දන්නේ නැති කෙනෙක්."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="誰の 質問の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P17,"p22_1_dare"), (P17B,"p22_2_verbs"), (P17C,"p22_3_past"),
                    (P17A,"p22_4_answer"), (P17A2,"p22_5_answer2")]:
        render(p, stem)
