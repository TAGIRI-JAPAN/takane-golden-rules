from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN = r("先生","せん せい")
GAK = r("学校","がっ こう")
IMA = r("今","いま")
TOM = r("友","とも")+"だち"
TOS = r("図書館","と しょ かん")
KSH = r("教室","きょう しつ")
GKS = r("学生","がく せい")
KOU = r("公園","こう えん")
INU = r("犬","いぬ")
ANI = r("兄","あに")
IMO = "いもうと"
KAZ = r("家族","か ぞく")
SRI = "スリランカ"

_NOTE = "NOTE:います = ඉන්නවා（人・どうぶつ）　/　あります = තියෙනවා（物）"

# ---------------------------------------------------------------- 09-1 基本
P5 = dict(
  no="09", tag=None,
  title_jp="〜は …に います / 〜が います",
  title_ro='〜 wa … ni imasu / 〜 ga imasu &nbsp;|&nbsp; 〜 is at … / there is 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 … ඉන්නවා</span>',
  basic=(f"{SEN}は {GAK}に います。","Sensei wa gakkou ni imasu.",
         "The teacher is at school.","ගුරුතුමා පාසලේ ඉන්නවා."),
  use=(f'{r("人","ひと")}や どうぶつが「いる」ことを あらわします。{r("物","もの")}には つかいません（{r("物","もの")}は「あります」）。'
       f'{r("人","ひと")}の{r("話","はなし")}を{r("先","さき")}に するときは「〜は …に います」、{r("場所","ば しょ")}の{r("話","はなし")}を{r("先","さき")}に するときは「…に 〜が います」です。',
       'Use <b>imasu</b> for people and animals. (For things, use <b>arimasu</b>.) '
       'Start with the person when the person is the topic: <b>〜 wa … ni imasu</b>. '
       'Start with the place when the place is the topic: <b>… ni 〜 ga imasu</b>.',
       'මිනිසුන් සහ සතුන් සඳහා <b>imasu</b> භාවිතා කරන්න. (දේවල් සඳහා <b>arimasu</b>.) '
       'සිංහලෙන් වගේමයි — <b>imasu</b> = ඉන්නවා, <b>arimasu</b> = තියෙනවා. '
       'කෙනා ගැන කතා නම් <b>〜 wa … ni imasu</b>; ස්ථානය ගැන කතා නම් <b>… ni 〜 ga imasu</b>.'),
  pattern=[[("〜は","~ wa"),("…に","… ni"),("います","imasu")],
           [("…に","… ni"),("〜が","~ ga"),("います","imasu")],
           [("〜が","~ ga"),("います","imasu")],
           _NOTE],
  examples=[
    (f"{SEN}は {GAK}に います。","Sensei wa gakkou ni imasu.","The teacher is at school.","ගුරුතුමා පාසලේ ඉන්නවා."),
    (f"{r('私','わたし')}は {IMA} うちに います。","Watashi wa ima uchi ni imasu.","I am at home now.","මම දැන් ගෙදර ඉන්නවා."),
    (f"{TOM}は {TOS}に います。","Tomodachi wa toshokan ni imasu.","My friend is in the library.","මගේ යාළුවා පුස්තකාලයේ ඉන්නවා."),
    (f"{KSH}に {GKS}が います。","Kyoushitsu ni gakusei ga imasu.","There are students in the classroom.","පන්ති කාමරයේ ශිෂ්‍යයෝ ඉන්නවා."),
    (f"{KOU}に {INU}が います。","Kouen ni inu ga imasu.","There is a dog in the park.","උද්‍යානයේ බල්ලෙක් ඉන්නවා."),
    (f"{ANI}が います。","Ani ga imasu.","I have an older brother.","මට අයියෙක් ඉන්නවා."),
    (f"{IMO}が います。","Imouto ga imasu.","I have a younger sister.","මට නංගියෙක් ඉන්නවා."),
  ],
  foot="〜は …に います",
)

# ---------------------------------------------------------------- 09-2 否定
P5N = dict(
  no="09", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜は …に いません",
  title_ro='〜 wa … ni imasen &nbsp;|&nbsp; 〜 is not at … &nbsp;|&nbsp; '
           '<span class="si">〜 … නැහැ</span>',
  basic=(f"{SEN}は {GAK}に いません。","Sensei wa gakkou ni imasen.",
         "The teacher is not at school.","ගුරුතුමා පාසලේ නැහැ."),
  use=(f'「います」を「いません」に{r("変","か")}えるだけです。'
       f'{r("否定","ひ てい")}の{r("文","ぶん")}では「が」が「は」に{r("変","か")}わることが{r("多","おお")}いです。',
       'Just change <b>imasu</b> to <b>imasen</b>. '
       'In negative sentences, <b>ga</b> usually changes to <b>wa</b>.',
       '<b>imasu</b> එක <b>imasen</b> කියලා වෙනස් කරන්න විතරයි. '
       'නිශේධන වාක්‍යවලදී <b>ga</b> එක බොහෝවිට <b>wa</b> බවට පත් වෙනවා.'),
  pattern=[[("〜は","~ wa"),("…に","… ni"),("いません","imasen",True)],
           [("…に","… ni"),("〜は","~ wa"),("いません","imasen",True)],
           [("〜は","~ wa"),("いません","imasen",True)],
           "NOTE:が　&#8594;　は　（否定の文では「が」ではなく「は」を使います）"],
  examples=[
    (f"{SEN}は {GAK}に いません。","Sensei wa gakkou ni imasen.","The teacher is not at school.","ගුරුතුමා පාසලේ නැහැ."),
    (f"{r('私','わたし')}は {IMA} うちに いません。","Watashi wa ima uchi ni imasen.","I am not at home now.","මම දැන් ගෙදර නැහැ."),
    (f"{TOM}は {TOS}に いません。","Tomodachi wa toshokan ni imasen.","My friend is not in the library.","මගේ යාළුවා පුස්තකාලයේ නැහැ."),
    (f"{KSH}に {GKS}は いません。","Kyoushitsu ni gakusei wa imasen.","There are no students in the classroom.","පන්ති කාමරයේ ශිෂ්‍යයෝ නැහැ."),
    (f"{KOU}に {INU}は いません。","Kouen ni inu wa imasen.","There is no dog in the park.","උද්‍යානයේ බල්ලෙක් නැහැ."),
    (f"{ANI}は いません。","Ani wa imasen.","I do not have an older brother.","මට අයියෙක් නැහැ."),
    (f"{IMO}は いません。","Imouto wa imasen.","I do not have a younger sister.","මට නංගියෙක් නැහැ."),
  ],
  foot="〜は …に いません",
)

# ---------------------------------------------------------------- 09-3 疑問
P5Q = dict(
  no="09", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜は …に いますか？",
  title_ro='〜 wa … ni imasu ka &nbsp;|&nbsp; Is 〜 at …? &nbsp;|&nbsp; '
           '<span class="si">〜 … ඉන්නවාද?</span>',
  basic=(f"{SEN}は {GAK}に いますか。","Sensei wa gakkou ni imasu ka.",
         "Is the teacher at school?","ගුරුතුමා පාසලේ ඉන්නවාද?"),
  use=(f'「います」のうしろに「か」をつけるだけです。'
       f'「いますか」は、{r("人","ひと")}が どこに いるかを{r("聞","き")}くときにも、{r("家族","か ぞく")}が いるかを{r("聞","き")}くときにも{r("使","つか")}えます。',
       'Just add <b>ka</b> after <b>imasu</b>. '
       'You can use <b>imasu ka</b> both to ask where someone is and to ask whether someone has family members.',
       '<b>imasu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       'කවුරුහරි කොහෙද ඉන්නේ කියලා අහන්නත්, පවුලේ අය ඉන්නවාද කියලා අහන්නත් <b>imasu ka</b> පාවිච්චි කරන්න පුළුවන්.'),
  pattern=[[("〜は","~ wa"),("…に","… ni"),("います","imasu")],
           "ARROW",
           [("〜は","~ wa"),("…に","… ni"),("いますか？","imasu ka",True)]],
  examples=[
    (f"{SEN}は {GAK}に いますか。","Sensei wa gakkou ni imasu ka.","Is the teacher at school?","ගුරුතුමා පාසලේ ඉන්නවාද?"),
    (f"あなたは {IMA} うちに いますか。","Anata wa ima uchi ni imasu ka.","Are you at home now?","ඔබ දැන් ගෙදර ඉන්නවාද?"),
    (f"{TOM}は {TOS}に いますか。","Tomodachi wa toshokan ni imasu ka.","Is your friend in the library?","ඔබේ යාළුවා පුස්තකාලයේ ඉන්නවාද?"),
    (f"{KSH}に {GKS}が いますか。","Kyoushitsu ni gakusei ga imasu ka.","Are there students in the classroom?","පන්ති කාමරයේ ශිෂ්‍යයෝ ඉන්නවාද?"),
    (f"{KOU}に {INU}が いますか。","Kouen ni inu ga imasu ka.","Is there a dog in the park?","උද්‍යානයේ බල්ලෙක් ඉන්නවාද?"),
    (f"{ANI}が いますか。","Ani ga imasu ka.","Do you have an older brother?","ඔබට අයියෙක් ඉන්නවාද?"),
    (f"{IMO}が いますか。","Imouto ga imasu ka.","Do you have a younger sister?","ඔබට නංගියෙක් ඉන්නවාද?"),
  ],
  foot="〜は …に いますか？",
)

# ---------------------------------------------------------------- 09-4 / 09-5 答え方
_USE = (f'「はい、います。」「いいえ、いません。」が{r("基本","き ほん")}です。'
        f'くわしく{r("答","こた")}えるときは、うしろに{r("場所","ば しょ")}や{r("人","ひと")}をつけます。',
        'The basic answers are <b>Hai, imasu</b> and <b>Iie, imasen</b>. '
        'For a fuller answer, add the place or the person after it.',
        'මූලික උත්තර දෙක <b>Hai, imasu</b> සහ <b>Iie, imasen</b>. '
        'විස්තර කරනවා නම් පස්සෙන් ස්ථානය හෝ පුද්ගලයා එකතු කරන්න.')

_PAT = [[("はい、","Hai,"),"BLANK",("います","imasu",True)],
        [("いいえ、","Iie,"),"BLANK",("いません","imasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{SEN}は {GAK}に いますか。","Sensei wa gakkou ni imasu ka.","Is the teacher at school?","ගුරුතුමා පාසලේ ඉන්නවාද?"),
         ("はい、います。","Hai, imasu.","Yes, he is.","ඔව්, ඉන්නවා.")),
  ("QA", (f"あなたは {IMA} うちに いますか。","Anata wa ima uchi ni imasu ka.","Are you at home now?","ඔබ දැන් ගෙදර ඉන්නවාද?"),
         ("いいえ、いません。","Iie, imasen.","No, I'm not.","නැහැ, නැහැ.")),
  ("QA", (f"{TOM}は {TOS}に いますか。","Tomodachi wa toshokan ni imasu ka.","Is your friend in the library?","ඔබේ යාළුවා පුස්තකාලයේ ඉන්නවාද?"),
         (f"はい、{TOS}に います。","Hai, toshokan ni imasu.","Yes, he is in the library.","ඔව්, පුස්තකාලයේ ඉන්නවා.")),
  ("QA", (f"{KSH}に {GKS}が いますか。","Kyoushitsu ni gakusei ga imasu ka.","Are there students in the classroom?","පන්ති කාමරයේ ශිෂ්‍යයෝ ඉන්නවාද?"),
         (f"はい、{GKS}が います。","Hai, gakusei ga imasu.","Yes, there are students.","ඔව්, ශිෂ්‍යයෝ ඉන්නවා.")),
  ("QA", (f"{KOU}に {INU}が いますか。","Kouen ni inu ga imasu ka.","Is there a dog in the park?","උද්‍යානයේ බල්ලෙක් ඉන්නවාද?"),
         (f"いいえ、{INU}は いません。","Iie, inu wa imasen.","No, there is no dog.","නැහැ, බල්ලෙක් නැහැ.")),
  ("QA", (f"{ANI}が いますか。","Ani ga imasu ka.","Do you have an older brother?","ඔබට අයියෙක් ඉන්නවාද?"),
         (f"はい、{ANI}が います。","Hai, ani ga imasu.","Yes, I have an older brother.","ඔව්, මට අයියෙක් ඉන්නවා.")),
  ("QA", (f"{IMO}が いますか。","Imouto ga imasu ka.","Do you have a younger sister?","ඔබට නංගියෙක් ඉන්නවාද?"),
         (f"いいえ、{IMO}は いません。","Iie, imouto wa imasen.","No, I don't have a younger sister.","නැහැ, මට නංගියෙක් නැහැ.")),
  ("QA", (f"ここに {SEN}が いますか。","Koko ni sensei ga imasu ka.","Is the teacher here?","ගුරුතුමා මෙතන ඉන්නවාද?"),
         ("いいえ、いません。","Iie, imasen.","No, he isn't.","නැහැ, නැහැ.")),
  ("QA", (f"{KAZ}は {SRI}に いますか。","Kazoku wa Suriranka ni imasu ka.","Is your family in Sri Lanka?","ඔබේ පවුල ශ්‍රී ලංකාවේ ඉන්නවාද?"),
         (f"はい、{SRI}に います。","Hai, Suriranka ni imasu.","Yes, they are in Sri Lanka.","ඔව්, ශ්‍රී ලංකාවේ ඉන්නවා.")),
]

P5A = dict(
  no="09", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、います。　／　いいえ、いません。","Hai, imasu. / Iie, imasen.",
         "Yes, there is. / No, there isn't.","ඔව්, ඉන්නවා. / නැහැ, නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P5A2 = dict(
  no="09", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P5A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{IMA} いません。","Ima imasen.","He / She is not here now.","දැන් නැහැ."),
    ("だれも いません。","Dare mo imasen.","There is nobody.","කවුරුවත් නැහැ."),
    (f"{r('少','すこ')}し まってください。","Sukoshi matte kudasai.","Please wait a moment.","ටිකක් ඉන්න."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P5,"p09_1_imasu"), (P5N,"p09_2_negative"), (P5Q,"p09_3_question"),
                    (P5A,"p09_4_answer"), (P5A2,"p09_5_answer2")]:
        render(p, stem)
