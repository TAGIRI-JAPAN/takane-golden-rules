from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TOS = r("図書館","と しょ かん")
GAK = r("学校","がっ こう")
NAK = r("中","なか")
KSH = r("教室","きょう しつ")
UE  = r("上","うえ")
HON = r("本","ほん")
MAE = r("前","まえ")
AST = r("明日","あ した")
KYO = r("今日","きょう")
JUG = r("授業","じゅ ぎょう")
YAK = r("約束","やく そく")
JIK = r("時間","じ かん")
CHI = r("近","ちか")+"く"
BYO = r("病院","びょう いん")
SHI = r("質問","しつ もん")
KAS = "かさ"
BAS = "バスてい"

_NOTE = "NOTE:〜の 中 = ඇතුළේ　/　〜の 上 = උඩ　/　〜の 前 = ඉස්සරහ　/　〜の そば = ළඟ"

# ---------------------------------------------------------------- 10-1 基本
P6 = dict(
  no="10", tag=None,
  title_jp="〜は …に あります / 〜が あります",
  title_ro='〜 wa … ni arimasu / 〜 ga arimasu &nbsp;|&nbsp; 〜 is at … / there is 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 … තියෙනවා</span>',
  basic=(f"{TOS}は {GAK}の {NAK}に あります。","Toshokan wa gakkou no naka ni arimasu.",
         "The library is inside the school.","පුස්තකාලය පාසල ඇතුළේ තියෙනවා."),
  use=(f'09の「います」と ペアです。「あります」は {r("物","もの")}・たてもの・ことがら（よてい）に つかいます。'
       f'「〜の {NAK}／{UE}／{MAE}／そば」で ばしょを くわしく{r("言","い")}えます。',
       'This is the pair of <b>imasu</b> in pattern 09. Use <b>arimasu</b> for things, buildings and '
       'events (plans). Use <b>〜 no naka / ue / mae / soba</b> to say exactly where.',
       'මේක 09 හි <b>imasu</b> එකේ යුගලයයි. දේවල්, ගොඩනැගිලි සහ කාරණා (වැඩසටහන්) සඳහා '
       '<b>arimasu</b> = තියෙනවා. ස්ථානය නිශ්චිතව කියන්න <b>naka / ue / mae / soba</b> භාවිතා කරන්න.'),
  pattern=[[("〜は","~ wa"),("…に","… ni"),("あります","arimasu")],
           [("…に","… ni"),("〜が","~ ga"),("あります","arimasu")],
           [("〜が","~ ga"),("あります","arimasu")],
           _NOTE],
  examples=[
    (f"{TOS}は {GAK}の {NAK}に あります。","Toshokan wa gakkou no naka ni arimasu.","The library is inside the school.","පුස්තකාලය පාසල ඇතුළේ තියෙනවා."),
    (f"{r('私','わたし')}の {KAS}は {KSH}に あります。","Watashi no kasa wa kyoushitsu ni arimasu.","My umbrella is in the classroom.","මගේ කුඩය පන්ති කාමරයේ තියෙනවා."),
    (f"つくえの {UE}に {HON}が あります。","Tsukue no ue ni hon ga arimasu.","There is a book on the desk.","මේසය උඩ පොතක් තියෙනවා."),
    (f"うちの {MAE}に {BAS}が あります。","Uchi no mae ni basutei ga arimasu.","There is a bus stop in front of my house.","අපේ ගෙදර ඉස්සරහ බස් නැවතුමක් තියෙනවා."),
    (f"{AST} {JUG}が あります。","Ashita jugyou ga arimasu.","I have class tomorrow.","හෙට පන්තියක් තියෙනවා."),
    (f"{KYO} {YAK}が あります。","Kyou yakusoku ga arimasu.","I have an appointment today.","අද පොරොන්දුවක් තියෙනවා."),
    (f"{JIK}が あります。","Jikan ga arimasu.","I have time.","මට වෙලාව තියෙනවා."),
  ],
  foot="〜は …に あります",
)

# ---------------------------------------------------------------- 10-2 否定
P6N = dict(
  no="10", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜は …に ありません",
  title_ro='〜 wa … ni arimasen &nbsp;|&nbsp; 〜 is not at … &nbsp;|&nbsp; '
           '<span class="si">〜 … නැහැ</span>',
  basic=(f"{TOS}は {GAK}の {NAK}に ありません。","Toshokan wa gakkou no naka ni arimasen.",
         "The library is not inside the school.","පුස්තකාලය පාසල ඇතුළේ නැහැ."),
  use=(f'「あります」を「ありません」に{r("変","か")}えるだけです。'
       f'09の「いません」と{r("同","おな")}じで、{r("否定","ひ てい")}の{r("文","ぶん")}では「が」が「は」に{r("変","か")}わります。',
       'Just change <b>arimasu</b> to <b>arimasen</b>. '
       'As with <b>imasen</b> in pattern 09, <b>ga</b> changes to <b>wa</b> in negative sentences.',
       '<b>arimasu</b> එක <b>arimasen</b> කියලා වෙනස් කරන්න විතරයි. '
       '09 හි <b>imasen</b> වගේම, නිශේධන වාක්‍යවලදී <b>ga</b> එක <b>wa</b> බවට පත් වෙනවා.'),
  pattern=[[("〜は","~ wa"),("…に","… ni"),("ありません","arimasen",True)],
           [("…に","… ni"),("〜は","~ wa"),("ありません","arimasen",True)],
           [("〜は","~ wa"),("ありません","arimasen",True)],
           "NOTE:が　&#8594;　は　（否定の文では「が」ではなく「は」を使います）"],
  examples=[
    (f"{TOS}は {GAK}の {NAK}に ありません。","Toshokan wa gakkou no naka ni arimasen.","The library is not inside the school.","පුස්තකාලය පාසල ඇතුළේ නැහැ."),
    (f"{r('私','わたし')}の {KAS}は {KSH}に ありません。","Watashi no kasa wa kyoushitsu ni arimasen.","My umbrella is not in the classroom.","මගේ කුඩය පන්ති කාමරයේ නැහැ."),
    (f"つくえの {UE}に {HON}は ありません。","Tsukue no ue ni hon wa arimasen.","There is no book on the desk.","මේසය උඩ පොතක් නැහැ."),
    (f"うちの {MAE}に {BAS}は ありません。","Uchi no mae ni basutei wa arimasen.","There is no bus stop in front of my house.","අපේ ගෙදර ඉස්සරහ බස් නැවතුමක් නැහැ."),
    (f"{AST} {JUG}は ありません。","Ashita jugyou wa arimasen.","I do not have class tomorrow.","හෙට පන්තියක් නැහැ."),
    (f"{KYO} {YAK}は ありません。","Kyou yakusoku wa arimasen.","I do not have an appointment today.","අද පොරොන්දුවක් නැහැ."),
    (f"{JIK}は ありません。","Jikan wa arimasen.","I do not have time.","මට වෙලාව නැහැ."),
  ],
  foot="〜は …に ありません",
)

# ---------------------------------------------------------------- 10-3 疑問
P6Q = dict(
  no="10", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜は …に ありますか？",
  title_ro='〜 wa … ni arimasu ka &nbsp;|&nbsp; Is there 〜 at …? &nbsp;|&nbsp; '
           '<span class="si">〜 … තියෙනවාද?</span>',
  basic=(f"{TOS}は {GAK}の {NAK}に ありますか。","Toshokan wa gakkou no naka ni arimasu ka.",
         "Is the library inside the school?","පුස්තකාලය පාසල ඇතුළේ තියෙනවාද?"),
  use=(f'「あります」のうしろに「か」をつけるだけです。'
       f'{r("店","みせ")}や{r("道","みち")}で よく{r("使","つか")}います。「〜は ありますか？」は「ありますか、ください」の{r("前","まえ")}に{r("使","つか")}う{r("大切","たい せつ")}な{r("表現","ひょう げん")}です。',
       'Just add <b>ka</b> after <b>arimasu</b>. You will use this a lot in shops and on the street — '
       '<b>〜 wa arimasu ka</b> is how you ask whether something is available.',
       '<b>arimasu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. කඩවලදී සහ පාරේදී මේක ගොඩක් වැදගත් — '
       '<b>〜 wa arimasu ka</b> කියන්නේ "මේක තියෙනවාද?" කියලා අහන ක්‍රමයයි.'),
  pattern=[[("〜は","~ wa"),("…に","… ni"),("あります","arimasu")],
           "ARROW",
           [("〜は","~ wa"),("…に","… ni"),("ありますか？","arimasu ka",True)]],
  examples=[
    (f"{TOS}は {GAK}の {NAK}に ありますか。","Toshokan wa gakkou no naka ni arimasu ka.","Is the library inside the school?","පුස්තකාලය පාසල ඇතුළේ තියෙනවාද?"),
    (f"{KAS}は {KSH}に ありますか。","Kasa wa kyoushitsu ni arimasu ka.","Is the umbrella in the classroom?","කුඩය පන්ති කාමරයේ තියෙනවාද?"),
    (f"つくえの {UE}に {HON}が ありますか。","Tsukue no ue ni hon ga arimasu ka.","Is there a book on the desk?","මේසය උඩ පොතක් තියෙනවාද?"),
    (f"うちの {MAE}に {BAS}が ありますか。","Uchi no mae ni basutei ga arimasu ka.","Is there a bus stop in front of your house?","ඔබේ ගෙදර ඉස්සරහ බස් නැවතුමක් තියෙනවාද?"),
    (f"{AST} {JUG}が ありますか。","Ashita jugyou ga arimasu ka.","Do you have class tomorrow?","හෙට පන්තියක් තියෙනවාද?"),
    (f"{KYO} {YAK}が ありますか。","Kyou yakusoku ga arimasu ka.","Do you have an appointment today?","අද පොරොන්දුවක් තියෙනවාද?"),
    (f"{JIK}が ありますか。","Jikan ga arimasu ka.","Do you have time?","ඔබට වෙලාව තියෙනවාද?"),
  ],
  foot="〜は …に ありますか？",
)

# ---------------------------------------------------------------- 10-4 / 10-5 答え方
_USE = (f'「はい、あります。」「いいえ、ありません。」が{r("基本","き ほん")}です。'
        f'くわしく{r("答","こた")}えるときは、うしろに ばしょや{r("物","もの")}をつけます。',
        'The basic answers are <b>Hai, arimasu</b> and <b>Iie, arimasen</b>. '
        'For a fuller answer, add the place or the thing after it.',
        'මූලික උත්තර දෙක <b>Hai, arimasu</b> සහ <b>Iie, arimasen</b>. '
        'විස්තර කරනවා නම් පස්සෙන් ස්ථානය හෝ දේ එකතු කරන්න.')

_PAT = [[("はい、","Hai,"),"BLANK",("あります","arimasu",True)],
        [("いいえ、","Iie,"),"BLANK",("ありません","arimasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{TOS}は {GAK}の {NAK}に ありますか。","Toshokan wa gakkou no naka ni arimasu ka.","Is the library inside the school?","පුස්තකාලය පාසල ඇතුළේ තියෙනවාද?"),
         ("はい、あります。","Hai, arimasu.","Yes, there is.","ඔව්, තියෙනවා.")),
  ("QA", (f"{KAS}は {KSH}に ありますか。","Kasa wa kyoushitsu ni arimasu ka.","Is the umbrella in the classroom?","කුඩය පන්ති කාමරයේ තියෙනවාද?"),
         ("いいえ、ありません。","Iie, arimasen.","No, it isn't.","නැහැ, නැහැ.")),
  ("QA", (f"つくえの {UE}に {HON}が ありますか。","Tsukue no ue ni hon ga arimasu ka.","Is there a book on the desk?","මේසය උඩ පොතක් තියෙනවාද?"),
         (f"はい、{HON}が あります。","Hai, hon ga arimasu.","Yes, there is a book.","ඔව්, පොතක් තියෙනවා.")),
  ("QA", (f"うちの {MAE}に {BAS}が ありますか。","Uchi no mae ni basutei ga arimasu ka.","Is there a bus stop in front of your house?","ඔබේ ගෙදර ඉස්සරහ බස් නැවතුමක් තියෙනවාද?"),
         (f"いいえ、{BAS}は ありません。","Iie, basutei wa arimasen.","No, there is no bus stop.","නැහැ, බස් නැවතුමක් නැහැ.")),
  ("QA", (f"{AST} {JUG}が ありますか。","Ashita jugyou ga arimasu ka.","Do you have class tomorrow?","හෙට පන්තියක් තියෙනවාද?"),
         ("はい、あります。","Hai, arimasu.","Yes, I do.","ඔව්, තියෙනවා.")),
  ("QA", (f"{KYO} {YAK}が ありますか。","Kyou yakusoku ga arimasu ka.","Do you have an appointment today?","අද පොරොන්දුවක් තියෙනවාද?"),
         (f"いいえ、{YAK}は ありません。","Iie, yakusoku wa arimasen.","No, I don't.","නැහැ, පොරොන්දුවක් නැහැ.")),
  ("QA", (f"{JIK}が ありますか。","Jikan ga arimasu ka.","Do you have time?","ඔබට වෙලාව තියෙනවාද?"),
         (f"はい、{JIK}が あります。","Hai, jikan ga arimasu.","Yes, I have time.","ඔව්, මට වෙලාව තියෙනවා.")),
  ("QA", (f"この {CHI}に {BYO}が ありますか。","Kono chikaku ni byouin ga arimasu ka.","Is there a hospital near here?","මේ ළඟ රෝහලක් තියෙනවාද?"),
         ("はい、あります。","Hai, arimasu.","Yes, there is.","ඔව්, තියෙනවා.")),
  ("QA", (f"{SHI}が ありますか。","Shitsumon ga arimasu ka.","Do you have a question?","ඔබට ප්‍රශ්නයක් තියෙනවාද?"),
         ("いいえ、ありません。","Iie, arimasen.","No, I don't.","නැහැ, නැහැ.")),
]

P6A = dict(
  no="10", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、あります。　／　いいえ、ありません。","Hai, arimasu. / Iie, arimasen.",
         "Yes, there is. / No, there isn't.","ඔව්, තියෙනවා. / නැහැ, නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P6A2 = dict(
  no="10", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P6A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("ここに あります。","Koko ni arimasu.","It's here.","මෙතන තියෙනවා."),
    ("あそこに あります。","Asoko ni arimasu.","It's over there.","අතන තියෙනවා."),
    (f"{SHI}が あります。","Shitsumon ga arimasu.","I have a question.","මට ප්‍රශ්නයක් තියෙනවා."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P6,"p10_1_arimasu"), (P6N,"p10_2_negative"), (P6Q,"p10_3_question"),
                    (P6A,"p10_4_answer"), (P6A2,"p10_5_answer2")]:
        render(p, stem)
