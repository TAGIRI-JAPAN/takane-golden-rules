from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
SHU  = r("宿題","しゅく だい")
TABM = r("食","た")+"べました"
TABT = r("食","た")+"べて"
TABK = r("食","た")+"べましたか"
KANJ = r("漢字","かん じ")
OBOM = r("覚","おぼ")+"えました"
OBOT = r("覚","おぼ")+"えて"
OBOK = r("覚","おぼ")+"えましたか"
SEN  = r("先生","せん せい")
KSH  = r("教室","きょう しつ")
KIMM = r("来","き")+"ました"
KIMT = r("来","き")+"て"
KIMK = r("来","き")+"ましたか"
TOM  = r("友","とも")+"だち"
NAM  = r("名前","な まえ")
KAKM = r("書","か")+"きました"
KAKT = r("書","か")+"いて"
KAKK = r("書","か")+"きましたか"
JUG  = r("授業","じゅ ぎょう")
HAJM = r("始","はじ")+"まりました"
HAJT = r("始","はじ")+"まって"
HAJK = r("始","はじ")+"まりましたか"
KYO  = r("教科書","きょう か しょ")
KAIM = r("買","か")+"いました"
KAIK = r("買","か")+"いましたか"
HON  = r("本","ほん")
YOMK = r("読","よ")+"みましたか"

_NOTE = "NOTE:もう = දැනටමත්　/　まだ = තාම"

# ---------------------------------------------------------------- 14-1 基本
P12 = dict(
  no="14", tag=None,
  title_jp="もう 〜しました",
  title_ro='mou 〜 shimashita &nbsp;|&nbsp; I have already 〜 &nbsp;|&nbsp; '
           '<span class="si">දැනටමත් 〜 කළා</span>',
  basic=(f"{W}は もう {SHU}を しました。","Watashi wa mou shukudai wo shimashita.",
         "I have already done my homework.","මම දැනටමත් ගෙදර වැඩ කළා."),
  use=(f'「もう」は「すでに おわった」という{r("意味","い み")}です。'
       f'13の「〜しました」に「もう」を つけると、{r("今","いま")}の じてんで おわっていることが '
       f'はっきり わかります。',
       '<b>mou</b> means "already". Adding <b>mou</b> to the past form from pattern 13 makes it '
       'clear that the action is finished as of now.',
       '<b>mou</b> කියන්නේ "දැනටමත්". 13 හි අතීත ආකාරයට <b>mou</b> එකතු කළාම, '
       'දැන් වන විට ඒක ඉවරයි කියන එක පැහැදිලි වෙනවා.'),
  pattern=[[("〜は","~ wa"),("もう","mou",True),"BLANK",("しました","shimashita")],
           _NOTE],
  examples=[
    (f"{W}は もう {SHU}を しました。","Watashi wa mou shukudai wo shimashita.","I have already done my homework.","මම දැනටමත් ගෙදර වැඩ කළා."),
    (f"{W}は もう ごはんを {TABM}。","Watashi wa mou gohan wo tabemashita.","I have already eaten.","මම දැනටමත් කෑම කෑවා."),
    (f"{W}は もう この {KANJ}を {OBOM}。","Watashi wa mou kono kanji wo oboemashita.","I have already learned this kanji.","මම දැනටමත් මේ කන්ජි අකුර මතක තියාගත්තා."),
    (f"{SEN}は もう {KSH}に {KIMM}。","Sensei wa mou kyoushitsu ni kimashita.","The teacher has already come to the classroom.","ගුරුතුමා දැනටමත් පන්ති කාමරයට ආවා."),
    (f"{TOM}は もう バスに のりました。","Tomodachi wa mou basu ni norimashita.","My friend has already got on the bus.","මගේ යාළුවා දැනටමත් බස් එකට නැග්ගා."),
    (f"{W}は もう {NAM}を {KAKM}。","Watashi wa mou namae wo kakimashita.","I have already written my name.","මම දැනටමත් නම ලිව්වා."),
    (f"{JUG}は もう {HAJM}。","Jugyou wa mou hajimarimashita.","The class has already started.","පන්තිය දැනටමත් පටන් අරන්."),
  ],
  foot="もう 〜しました",
)

# ---------------------------------------------------------------- 14-2 否定
P12N = dict(
  no="14", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="まだ 〜していません",
  title_ro='mada 〜 shite imasen &nbsp;|&nbsp; I have not 〜 yet &nbsp;|&nbsp; '
           '<span class="si">තාම 〜 කරලා නැහැ</span>',
  basic=(f"{W}は まだ {SHU}を していません。","Watashi wa mada shukudai wo shite imasen.",
         "I have not done my homework yet.","මම තාම ගෙදර වැඩ කරලා නැහැ."),
  use=(f'ここが いちばん{r("大切","たい せつ")}です。「もう 〜しました」の{r("否定","ひ てい")}は'
       f'「〜しませんでした」ではありません。「まだ 〜して いません」を{r("使","つか")}います。'
       f'「まだ しませんでした」とは{r("言","い")}いません。',
       'This is the most important point. The negative of <b>mou 〜 shimashita</b> is NOT '
       '<b>〜 masen deshita</b>. Use <b>mada 〜 shite imasen</b>. '
       'You never say <b>mada shimasen deshita</b>.',
       'මේක තමයි වැදගත්ම කරුණ. <b>mou 〜 shimashita</b> හි නිශේධනය <b>〜 masen deshita</b> නෙවෙයි. '
       '<b>mada 〜 shite imasen</b> භාවිතා කරන්න. '
       '<b>mada shimasen deshita</b> කියලා කවදාවත් කියන්නේ නැහැ.'),
  pattern=[[("もう","mou"),"BLANK",("しました","shimashita")],
           "ARROW",
           [("まだ","mada",True),"BLANK",("して いません","shite imasen",True)],
           "NOTE:【 ちゅうい 】「まだ しませんでした」とは 言いません　/　never use masen deshita here"],
  examples=[
    (f"{W}は まだ {SHU}を していません。","Watashi wa mada shukudai wo shite imasen.","I have not done my homework yet.","මම තාම ගෙදර වැඩ කරලා නැහැ."),
    (f"{W}は まだ ごはんを {TABT}いません。","Watashi wa mada gohan wo tabete imasen.","I have not eaten yet.","මම තාම කෑම කාලා නැහැ."),
    (f"{W}は まだ この {KANJ}を {OBOT}いません。","Watashi wa mada kono kanji wo oboete imasen.","I have not learned this kanji yet.","මම තාම මේ කන්ජි අකුර මතක තියාගෙන නැහැ."),
    (f"{SEN}は まだ {KSH}に {KIMT}いません。","Sensei wa mada kyoushitsu ni kite imasen.","The teacher has not come to the classroom yet.","ගුරුතුමා තාම පන්ති කාමරයට ඇවිත් නැහැ."),
    (f"{TOM}は まだ バスに のっていません。","Tomodachi wa mada basu ni notte imasen.","My friend has not got on the bus yet.","මගේ යාළුවා තාම බස් එකට නැගලා නැහැ."),
    (f"{W}は まだ {NAM}を {KAKT}いません。","Watashi wa mada namae wo kaite imasen.","I have not written my name yet.","මම තාම නම ලියලා නැහැ."),
    (f"{JUG}は まだ {HAJT}いません。","Jugyou wa mada hajimatte imasen.","The class has not started yet.","පන්තිය තාම පටන් අරන් නැහැ."),
  ],
  foot="まだ 〜していません",
)

# ---------------------------------------------------------------- 14-3 疑問
P12Q = dict(
  no="14", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="もう 〜しましたか？",
  title_ro='mou 〜 shimashita ka &nbsp;|&nbsp; Have you 〜 yet? &nbsp;|&nbsp; '
           '<span class="si">දැනටමත් 〜 කළාද?</span>',
  basic=(f"あなたは もう {SHU}を しましたか。","Anata wa mou shukudai wo shimashita ka.",
         "Have you done your homework yet?","ඔබ දැනටමත් ගෙදර වැඩ කළාද?"),
  use=(f'「もう 〜しましたか」は、{r("相手","あい て")}が すでに したかどうかを{r("聞","き")}きます。'
       f'{r("学校","がっ こう")}でも{r("仕事","し ごと")}でも{r("毎日","まい にち")}{r("使","つか")}う、とても{r("大切","たい せつ")}な{r("質問","しつ もん")}です。',
       '<b>mou 〜 shimashita ka</b> asks whether the other person has already done something. '
       'You will use it every day, at school and at work.',
       '<b>mou 〜 shimashita ka</b> කියලා අහන්නේ අනිත් කෙනා දැනටමත් ඒක කරලාද කියලා. '
       'පාසලේදීත් රැකියාවේදීත් හැමදාම භාවිතා වෙන ඉතා වැදගත් ප්‍රශ්නයක්.'),
  pattern=[[("〜は","~ wa"),("もう","mou",True),"BLANK",("しました","shimashita")],
           "ARROW",
           [("〜は","~ wa"),("もう","mou",True),"BLANK",("しましたか？","shimashita ka",True)]],
  examples=[
    (f"あなたは もう {SHU}を しましたか。","Anata wa mou shukudai wo shimashita ka.","Have you done your homework yet?","ඔබ දැනටමත් ගෙදර වැඩ කළාද?"),
    (f"あなたは もう ごはんを {TABK}。","Anata wa mou gohan wo tabemashita ka.","Have you eaten yet?","ඔබ දැනටමත් කෑම කෑවාද?"),
    (f"あなたは もう この {KANJ}を {OBOK}。","Anata wa mou kono kanji wo oboemashita ka.","Have you learned this kanji yet?","ඔබ දැනටමත් මේ කන්ජි අකුර මතක තියාගත්තාද?"),
    (f"{SEN}は もう {KSH}に {KIMK}。","Sensei wa mou kyoushitsu ni kimashita ka.","Has the teacher come to the classroom yet?","ගුරුතුමා දැනටමත් පන්ති කාමරයට ආවාද?"),
    (f"{TOM}は もう バスに のりましたか。","Tomodachi wa mou basu ni norimashita ka.","Has your friend got on the bus yet?","ඔබේ යාළුවා දැනටමත් බස් එකට නැග්ගාද?"),
    (f"あなたは もう {NAM}を {KAKK}。","Anata wa mou namae wo kakimashita ka.","Have you written your name yet?","ඔබ දැනටමත් නම ලිව්වාද?"),
    (f"{JUG}は もう {HAJK}。","Jugyou wa mou hajimarimashita ka.","Has the class started yet?","පන්තිය දැනටමත් පටන් අරන්ද?"),
  ],
  foot="もう 〜しましたか？",
)

# ---------------------------------------------------------------- 14-4 / 14-5 答え方
_USE = (f'「はい」は「もう 〜しました。」、「いいえ」は「まだです。」か「まだ 〜して いません。」です。'
        f'いちばん みじかくて{r("便利","べん り")}なのは「まだです。」の ひとことです。',
        'For yes, say <b>Hai, mou 〜 shimashita</b>. For no, say <b>mada desu</b> or '
        '<b>mada 〜 shite imasen</b>. The shortest and most useful reply is just <b>mada desu</b>.',
        'ඔව් නම් <b>Hai, mou 〜 shimashita</b>. නැහැ නම් <b>mada desu</b> හෝ '
        '<b>mada 〜 shite imasen</b>. කෙටිම සහ ප්‍රයෝජනවත්ම උත්තරය <b>mada desu</b> විතරයි.')

_PAT = [[("はい、もう","Hai, mou"),"BLANK",("しました","shimashita",True)],
        [("いいえ、まだ","Iie, mada"),"BLANK",("して いません","shite imasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"もう {SHU}を しましたか。","Mou shukudai wo shimashita ka.","Have you done your homework yet?","ඔබ දැනටමත් ගෙදර වැඩ කළාද?"),
         ("はい、もう しました。","Hai, mou shimashita.","Yes, I already have.","ඔව්, දැනටමත් කළා.")),
  ("QA", (f"もう ごはんを {TABK}。","Mou gohan wo tabemashita ka.","Have you eaten yet?","ඔබ දැනටමත් කෑම කෑවාද?"),
         ("いいえ、まだです。","Iie, mada desu.","No, not yet.","නැහැ, තාම නැහැ.")),
  ("QA", (f"もう この {KANJ}を {OBOK}。","Mou kono kanji wo oboemashita ka.","Have you learned this kanji yet?","ඔබ දැනටමත් මේ කන්ජි අකුර මතක තියාගත්තාද?"),
         (f"はい、もう {OBOM}。","Hai, mou oboemashita.","Yes, I have.","ඔව්, දැනටමත් මතක තියාගත්තා.")),
  ("QA", (f"{SEN}は もう {KIMK}。","Sensei wa mou kimashita ka.","Has the teacher come yet?","ගුරුතුමා දැනටමත් ආවාද?"),
         (f"いいえ、まだ {KIMT}いません。","Iie, mada kite imasen.","No, he hasn't come yet.","නැහැ, තාම ඇවිත් නැහැ.")),
  ("QA", (f"もう バスに のりましたか。","Mou basu ni norimashita ka.","Have you got on the bus yet?","ඔබ දැනටමත් බස් එකට නැග්ගාද?"),
         ("はい、もう のりました。","Hai, mou norimashita.","Yes, I have.","ඔව්, දැනටමත් නැග්ගා.")),
  ("QA", (f"もう {NAM}を {KAKK}。","Mou namae wo kakimashita ka.","Have you written your name yet?","ඔබ දැනටමත් නම ලිව්වාද?"),
         (f"いいえ、まだ {KAKT}いません。","Iie, mada kaite imasen.","No, I haven't written it yet.","නැහැ, තාම ලියලා නැහැ.")),
  ("QA", (f"{JUG}は もう {HAJK}。","Jugyou wa mou hajimarimashita ka.","Has the class started yet?","පන්තිය දැනටමත් පටන් අරන්ද?"),
         (f"はい、もう {HAJM}。","Hai, mou hajimarimashita.","Yes, it has already started.","ඔව්, දැනටමත් පටන් අරන්.")),
  ("QA", (f"もう {KYO}を {KAIK}。","Mou kyoukasho wo kaimashita ka.","Have you bought the textbook yet?","ඔබ දැනටමත් පෙළපොත ගත්තාද?"),
         (f"はい、もう {KAIM}。","Hai, mou kaimashita.","Yes, I have.","ඔව්, දැනටමත් ගත්තා.")),
  ("QA", (f"もう その {HON}を {YOMK}。","Mou sono hon wo yomimashita ka.","Have you read that book yet?","ඔබ දැනටමත් ඒ පොත කියෙව්වාද?"),
         ("いいえ、まだです。","Iie, mada desu.","No, not yet.","නැහැ, තාම නැහැ.")),
]

P12A = dict(
  no="14", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、もう しました。　／　いいえ、まだです。","Hai, mou shimashita. / Iie, mada desu.",
         "Yes, I already have. / No, not yet.","ඔව්, දැනටමත් කළා. / නැහැ, තාම නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P12A2 = dict(
  no="14", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P12A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("はい、さっき しました。","Hai, sakki shimashita.","Yes, I did it just now.","ඔව්, දැන් ටිකකට කලින් කළා."),
    ("まだです。","Mada desu.","Not yet.","තාම නැහැ."),
    ("これから します。","Kore kara shimasu.","I'll do it now.","දැන් කරන්නම්."),
    (f"もう {r('終','お')}わりました。","Mou owarimashita.","It's already finished.","දැනටමත් ඉවරයි."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P12,"p14_1_mou"), (P12N,"p14_2_negative"), (P12Q,"p14_3_question"),
                    (P12A,"p14_4_answer"), (P12A2,"p14_5_answer2")]:
        render(p, stem)
