from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

DEG  = r("出口","で ぐち")
GAK  = r("学校","がっ こう")
BYO  = r("病院","びょう いん")
YUU  = r("郵便局","ゆう びん きょく")
JIM  = r("事務室","じ む しつ")
SEN  = r("先生","せん せい")
IMA  = r("今","いま")
KYO  = r("教科書","きょう か しょ")
BEN  = r("勉強","べん きょう")
IKI  = r("行","い")+"きます"
IKIM = r("行","い")+"きました"
IKIT = r("行","い")+"きたい"
HIRU = r("昼","ひる")+"ごはん"
TABS = r("食","た")+"べましょう"
KAIM = r("買","か")+"いました"
TOM  = r("友","とも")+"だち"
AIM  = r("会","あ")+"いました"
HAT  = r("働","はたら")+"いて"
KUU  = r("空港","くう こう")
MIGI = r("右","みぎ")
HIDA = r("左","ひだり")
NIKA = r("二階","に かい")
TOS  = r("図書館","と しょ かん")
SSH  = r("先週","せん しゅう")
SHUM = r("週末","しゅう まつ")
KSH  = r("教室","きょう しつ")
KAS  = "かさ"
HON  = r("本","ほん")
TAT  = r("建物","たて もの")

# ---------------------------------------------------------------- 23-1 基本
P19 = dict(
  no="23", tag=None,
  title_jp="〜は どこですか？",
  title_ro='〜 wa doko desu ka &nbsp;|&nbsp; Where is 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කොහෙද?</span>',
  basic=("バスていは どこですか。","Basutei wa doko desu ka.",
         "Where is the bus stop?","බස් නැවතුම කොහෙද?"),
  use=(f'「どこ」は{r("場所","ば しょ")}を たずねる ことばです。21〜24と{r("同","おな")}じ{r("作","つく")}り{r("方","かた")}です。'
       f'ていねいに{r("言","い")}うときは「どちら」を{r("使","つか")}います。',
       '<b>doko</b> asks about a place. Same construction as patterns 21–24. '
       'In polite speech, use <b>dochira</b> instead of <b>doko</b>.',
       '<b>doko</b> කියන්නේ ස්ථානයක් අහන එක — <b>doko desu ka</b> = කොහෙද? '
       '21–24 වගේමයි. ආචාරශීලීව නම් <b>dochira</b> කියන්න.'),
  pattern=[[("〜は","~ wa"),("どこですか？","doko desu ka",True)],
           "NOTE:ここ = මෙතන　/　そこ = ඔතන　/　あそこ = අතන　　　ていねいに 言うとき：どこ &#8594; どちら"],
  examples=[
    ("バスていは どこですか。","Basutei wa doko desu ka.","Where is the bus stop?","බස් නැවතුම කොහෙද?"),
    ("コンビニは どこですか。","Konbini wa doko desu ka.","Where is the convenience store?","පහසු කඩය කොහෙද?"),
    (f"{JIM}は どこですか。","Jimushitsu wa doko desu ka.","Where is the office?","කාර්යාලය කොහෙද?"),
    (f"{YUU}は どこですか。","Yuubinkyoku wa doko desu ka.","Where is the post office?","තැපැල් කන්තෝරුව කොහෙද?"),
    (f"あなたの {GAK}は どこですか。","Anata no gakkou wa doko desu ka.","Where is your school?","ඔබේ පාසල කොහෙද?"),
    (f"{BYO}は どこですか。","Byouin wa doko desu ka.","Where is the hospital?","රෝහල කොහෙද?"),
    (f"{DEG}は どこですか。","Deguchi wa doko desu ka.","Where is the exit?","පිටවීම කොහෙද?"),
  ],
  foot="〜は どこですか？",
)

# ---------------------------------------------------------------- 23-2 応用①
P19B = dict(
  no="23", tag="応用 ①　どこに / どこで / どこへ / WITH VERBS",
  title_jp="どこに / どこで / どこへ",
  title_ro='doko ni / de / e &nbsp;|&nbsp; where it is / where you do it / where you go '
           '&nbsp;|&nbsp; <span class="si">කොහෙද / කොහාටද</span>',
  basic=(f"どこで {BEN}しますか。","Doko de benkyou shimasu ka.",
         "Where do you study?","ඔබ කොහෙද ඉගෙන ගන්නේ?"),
  use=(f'「どこに」は いる・ある ばしょ、「どこで」は する ばしょ、「どこへ」は {IKI} ほうこうです。',
       '<b>doko ni</b> = where something is, <b>doko de</b> = where an action happens, '
       '<b>doko e</b> = where you are heading.',
       '<b>doko ni</b> = තියෙන/ඉන්න තැන, <b>doko de</b> = කරන තැන, <b>doko e</b> = යන තැන (කොහාටද).'),
  pattern=[[("どこに","doko ni",True),("いますか / ありますか？","imasu ka / arimasu ka")],
           [("どこで","doko de",True),("しますか？","shimasu ka")],
           [("どこへ","doko e",True),(f"{IKI}か？","ikimasu ka")],
           "NOTE:どこに = いる・ある ばしょ　/　どこで = する ばしょ　/　どこへ = 行く ほうこう"],
  examples=[
    (f"{SEN}は {IMA} どこに いますか。","Sensei wa ima doko ni imasu ka.","Where is the teacher now?","ගුරුතුමා දැන් කොහෙද ඉන්නේ?"),
    (f"{KYO}は どこに ありますか。","Kyoukasho wa doko ni arimasu ka.","Where is the textbook?","පෙළපොත කොහෙද තියෙන්නේ?"),
    (f"どこで {BEN}しますか。","Doko de benkyou shimasu ka.","Where do you study?","ඔබ කොහෙද ඉගෙන ගන්නේ?"),
    ("どこで アルバイトを していますか。","Doko de arubaito wo shite imasu ka.","Where do you work part-time?","ඔබ කොහෙද අර්ධකාලීන රැකියාව කරන්නේ?"),
    (f"どこへ {IKI}か。","Doko e ikimasu ka.","Where are you going?","ඔබ කොහාටද යන්නේ?"),
    (f"{SHUM} どこへ {IKIT}ですか。","Shuumatsu doko e ikitai desu ka.","Where do you want to go at the weekend?","සති අන්තයේ ඔබට කොහාටද යන්න ඕන?"),
    (f"どこで {HIRU}を {TABS}か。","Doko de hirugohan wo tabemashou ka.","Where shall we have lunch?","අපි කොහෙද දිවා කෑම කමු?"),
  ],
  foot="どこに / どこで / どこへ",
)

# ---------------------------------------------------------------- 23-3 応用②
P19C = dict(
  no="23", tag="応用 ②　どこで しましたか？ / PAST",
  title_jp="どこで しましたか？",
  title_ro='doko de shimashita ka &nbsp;|&nbsp; Where did you 〜? &nbsp;|&nbsp; '
           '<span class="si">කොහෙද කළේ?</span>',
  basic=(f"どこで {r('日本語','に ほん ご')}を {BEN}しましたか。","Doko de nihongo wo benkyou shimashita ka.",
         "Where did you study Japanese?","ඔබ කොහෙද ජපන් භාෂාව ඉගෙන ගත්තේ?"),
  use=(f'13の「ました」と{r("組","く")}み{r("合","あ")}わせるだけです。'
       f'「に」「で」「へ」の{r("使","つか")}い{r("分","わ")}けは かこでも{r("同","おな")}じです。',
       'Just combine it with the past forms from pattern 13. '
       'The difference between <b>ni</b>, <b>de</b> and <b>e</b> stays exactly the same.',
       '13 හි අතීත ආකාර එක්ක එකතු කරන්න විතරයි. '
       '<b>ni</b>, <b>de</b>, <b>e</b> අතර වෙනස අතීතයේදීත් එකමයි.'),
  pattern=[[("どこに","doko ni",True),("いましたか / ありましたか？","imashita ka / arimashita ka")],
           [("どこで","doko de",True),("しましたか？","shimashita ka")],
           [("どこへ","doko e",True),(f"{IKIM}か？","ikimashita ka")]],
  examples=[
    (f"{SEN}は どこに いましたか。","Sensei wa doko ni imashita ka.","Where was the teacher?","ගුරුතුමා කොහෙද හිටියේ?"),
    (f"{KAS}は どこに ありましたか。","Kasa wa doko ni arimashita ka.","Where was the umbrella?","කුඩය කොහෙද තිබුණේ?"),
    (f"どこで {r('日本語','に ほん ご')}を {BEN}しましたか。","Doko de nihongo wo benkyou shimashita ka.","Where did you study Japanese?","ඔබ කොහෙද ජපන් භාෂාව ඉගෙන ගත්තේ?"),
    (f"どこで その {HON}を {KAIM}か。","Doko de sono hon wo kaimashita ka.","Where did you buy that book?","ඔබ ඒ පොත කොහෙන්ද ගත්තේ?"),
    (f"{SSH} どこへ {IKIM}か。","Senshuu doko e ikimashita ka.","Where did you go last week?","පසුගිය සතියේ ඔබ කොහාටද ගියේ?"),
    (f"どこで {TOM}に {AIM}か。","Doko de tomodachi ni aimashita ka.","Where did you meet your friend?","ඔබ යාළුවා කොහෙදිද හම්බවුණේ?"),
    (f"{KUU}から どこへ {IKIM}か。","Kuukou kara doko e ikimashita ka.","Where did you go from the airport?","ගුවන් තොටුපොළෙන් ඔබ කොහාටද ගියේ?"),
  ],
  foot="どこで しましたか？",
)

# ---------------------------------------------------------------- 23-4 / 23-5 答え方
_USE = (f'「どこ」の{r("質問","しつ もん")}には ばしょで{r("答","こた")}えます。「はい」「いいえ」では{r("答","こた")}えません。'
        f'{r("道","みち")}を{r("教","おし")}えるときは「まっすぐ」「{MIGI}」「{HIDA}」「となり」を{r("使","つか")}います。',
        'Answer a <b>doko</b> question with a place, never with <b>hai</b> or <b>iie</b>. '
        'To give directions, use <b>massugu</b> (straight), <b>migi</b> (right), '
        '<b>hidari</b> (left) and <b>tonari</b> (next to).',
        '<b>doko</b> ප්‍රශ්නයකට ස්ථානයක් කියලා උත්තර දෙන්න — <b>hai</b>/<b>iie</b> නෙවෙයි. '
        'පාර කියලා දෙනවා නම් <b>massugu</b> (කෙළින්), <b>migi</b> (දකුණට), '
        '<b>hidari</b> (වමට), <b>tonari</b> (ළඟ).')

_PAT = ["NOTE:【 ちゅうい 】「はい / いいえ」では 答えません　/　never answer yes or no",
        [("どこですか？","doko desu ka"),"TO",(f"ばしょを {r('言','い')}う","give a place",True)],
        f"NOTE:みちの ことば：まっすぐ = කෙළින්　/　{MIGI} = දකුණට　/　{HIDA} = වමට　/　となり = ළඟ"]

_QA = [
  ("QA", ("バスていは どこですか。","Basutei wa doko desu ka.","Where is the bus stop?","බස් නැවතුම කොහෙද?"),
         ("あそこです。","Asoko desu.","Over there.","අතන.")),
  ("QA", ("コンビニは どこですか。","Konbini wa doko desu ka.","Where is the convenience store?","පහසු කඩය කොහෙද?"),
         (f"まっすぐ {r('行','い')}って、{MIGI}です。","Massugu itte, migi desu.","Go straight, then right.","කෙළින් ගිහින්, දකුණට.")),
  ("QA", (f"{JIM}は どこですか。","Jimushitsu wa doko desu ka.","Where is the office?","කාර්යාලය කොහෙද?"),
         (f"{NIKA}です。","Nikai desu.","On the second floor.","දෙවෙනි තට්ටුවේ.")),
  ("QA", (f"{DEG}は どこですか。","Deguchi wa doko desu ka.","Where is the exit?","පිටවීම කොහෙද?"),
         (f"{HIDA}に あります。","Hidari ni arimasu.","It's on the left.","වම් පැත්තේ තියෙනවා.")),
  ("QA", (f"{SEN}は {IMA} どこに いますか。","Sensei wa ima doko ni imasu ka.","Where is the teacher now?","ගුරුතුමා දැන් කොහෙද ඉන්නේ?"),
         (f"{KSH}に います。","Kyoushitsu ni imasu.","He is in the classroom.","පන්ති කාමරයේ ඉන්නවා.")),
  ("QA", (f"どこで {BEN}しますか。","Doko de benkyou shimasu ka.","Where do you study?","ඔබ කොහෙද ඉගෙන ගන්නේ?"),
         (f"{TOS}で {BEN}します。","Toshokan de benkyou shimasu.","I study in the library.","මම පුස්තකාලයේ ඉගෙන ගන්නවා.")),
  ("QA", (f"どこへ {IKI}か。","Doko e ikimasu ka.","Where are you going?","ඔබ කොහාටද යන්නේ?"),
         (f"{GAK}へ {IKI}。","Gakkou e ikimasu.","I'm going to school.","මම පාසලට යනවා.")),
  ("QA", (f"{SSH} どこへ {IKIM}か。","Senshuu doko e ikimashita ka.","Where did you go last week?","පසුගිය සතියේ ඔබ කොහාටද ගියේ?"),
         (f"{TOM}の うちへ {IKIM}。","Tomodachi no uchi e ikimashita.","I went to my friend's house.","මම යාළුවාගේ ගෙදර ගියා.")),
  ("QA", (f"どこで {HAT}いましたか。","Doko de hataraite imashita ka.","Where were you working?","ඔබ කොහෙද වැඩ කරමින් හිටියේ?"),
         (f"コンビニで {HAT}いました。","Konbini de hataraite imashita.","I was working at a convenience store.","මම පහසු කඩයක වැඩ කරමින් හිටියා.")),
]

_TITLE_RO = ('Doko no shitsumon no kotaekata &nbsp;|&nbsp; Answering a "where" question &nbsp;|&nbsp; '
             '<span class="si">"කොහෙද?" ප්‍රශ්නයට උත්තර දීම</span>')

P19A = dict(
  no="23", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp="どこ の 質問の 答え方",
  title_ro=_TITLE_RO,
  basic=("バスていは どこですか。　&#8594;　あそこです。",
         "Basutei wa doko desu ka. → Asoko desu.",
         "Where is the bus stop? → Over there.","බස් නැවතුම කොහෙද? → අතන."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="どこ の 質問の 答え方",
)

P19A2 = dict(
  no="23", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp="どこ の 質問の 答え方",
  title_ro=_TITLE_RO,
  skip=("basic","use","pattern"), start=4,
  basic=P19A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("あそこです。","Asoko desu.","Over there.","අතන."),
    ("まっすぐです。","Massugu desu.","Straight ahead.","කෙළින්."),
    (f"となりの {TAT}です。","Tonari no tatemono desu.","The building next door.","ළඟ තියෙන ගොඩනැගිල්ල."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="どこ の 質問の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P19,"p23_1_doko"), (P19B,"p23_2_verbs"), (P19C,"p23_3_past"),
                    (P19A,"p23_4_answer"), (P19A2,"p23_5_answer2")]:
        render(p, stem)
