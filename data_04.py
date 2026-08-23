from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W  = r("私","わたし")
MIZ= r("水","みず"); HON=r("本","ほん"); NAM=r("名前","な まえ")
NHG= r("日本語","に ほん ご"); KYO=r("教科書","きょう か しょ")
GAK= r("学校","がっ こう"); KSH=r("私","わたし")+"の "+r("教室","きょう しつ")
TOS= r("図書館","と しょ かん")
ANA= "あなた"

P1 = dict(
  no="04", tag=None,
  title_jp="これは 〜です",
  title_ro='Kore wa 〜 desu &nbsp;|&nbsp; This is 〜 &nbsp;|&nbsp; <span class="si">මේක 〜 යි</span>',
  basic=("これは スマホ です。", "Kore wa sumaho desu.",
         "This is a smartphone.", "මේක ජංගම දුරකථනයක්."),
  use=(f'{r("近","ちか")}くにある{r("物","もの")}や{r("持","も")}っている{r("物","もの")}を{r("説明","せつめい")}するときは「これは〜です」。'
       f'{r("離","はな")}れたところにある{r("物","もの")}は「あれは〜です」を{r("使","つか")}います。',
       'Use <b>Kore wa 〜 desu</b> for something near you or in your hand. '
       'For something far away, use <b>Are wa 〜 desu</b>.',
       'ළඟ තියෙන හෝ අතේ තියෙන දෙයක් ගැන කියනවා නම් <b>Kore wa 〜 desu</b>. '
       'දුරින් තියෙන දෙයක් නම් <b>Are wa 〜 desu</b> භාවිතා කරන්න.'),
  pattern=[[("これは","Kore wa"),"BLANK",("です","desu")],
           [("あれは","Are wa"),"BLANK",("です","desu")]],
  examples=[
    (f"これは {MIZ} です。","Kore wa mizu desu.","This is water.","මේක වතුර."),
    (f"これは {W}の {HON} です。","Kore wa watashi no hon desu.","This is my book.","මේක මගේ පොත."),
    (f"これは {W}の {NAM} です。","Kore wa watashi no namae desu.","This is my name.","මේක මගේ නම."),
    (f"これは {NHG}の {KYO} です。","Kore wa nihongo no kyoukasho desu.","This is a Japanese textbook.","මේක ජපන් භාෂා පෙළපොතක්."),
    (f"あれは {GAK} です。","Are wa gakkou desu.","That is a school.","අරක පාසලක්."),
    (f"あれは {KSH} です。","Are wa watashi no kyoushitsu desu.","That is my classroom.","අරක මගේ පන්ති කාමරය."),
    (f"あれは {TOS} です。","Are wa toshokan desu.","That is a library.","අරක පුස්තකාලයක්."),
  ],
  foot="これは〜です",
)

P1N = dict(
  no="04", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="これは 〜では ありません",
  title_ro='Kore wa 〜 dewa arimasen &nbsp;|&nbsp; This is not 〜 &nbsp;|&nbsp; <span class="si">මේක 〜 නෙවෙයි</span>',
  basic=("これは スマホ では ありません。","Kore wa sumaho dewa arimasen.",
         "This is not a smartphone.","මේක ජංගම දුරකථනයක් නෙවෙයි."),
  use=(f'「です」を「では ありません」に{r("変","か")}えると{r("否定","ひ てい")}になります。'
       f'{r("話","はな")}しことばでは「じゃ ありません」「じゃ ないです」も{r("使","つか")}います。'
       f'「あれは」も{r("同","おな")}じです。',
       'Change <b>desu</b> to <b>dewa arimasen</b> to make it negative. '
       'In conversation, <b>ja arimasen</b> and <b>ja nai desu</b> are also used. '
       '<b>Are wa</b> works the same way.',
       '<b>desu</b> වෙනුවට <b>dewa arimasen</b> දැම්මාම නැහැ කියන අර්ථය එනවා. '
       'කතා කරද්දී <b>ja arimasen</b>, <b>ja nai desu</b> කියලත් කියනවා. '
       '<b>Are wa</b> එකත් එහෙමයි.'),
  pattern=[[("これは","Kore wa"),"BLANK",("です","desu")],
           "ARROW",
           [("これは","Kore wa"),"BLANK",("では ありません","dewa arimasen",True)]],
  examples=[
    (f"これは {MIZ} では ありません。","Kore wa mizu dewa arimasen.","This is not water.","මේක වතුර නෙවෙයි."),
    (f"これは {W}の {HON} では ありません。","Kore wa watashi no hon dewa arimasen.","This is not my book.","මේක මගේ පොත නෙවෙයි."),
    (f"これは {W}の {NAM} では ありません。","Kore wa watashi no namae dewa arimasen.","This is not my name.","මේක මගේ නම නෙවෙයි."),
    (f"これは {NHG}の {KYO} では ありません。","Kore wa nihongo no kyoukasho dewa arimasen.","This is not a Japanese textbook.","මේක ජපන් භාෂා පෙළපොතක් නෙවෙයි."),
    (f"あれは {GAK} では ありません。","Are wa gakkou dewa arimasen.","That is not a school.","අරක පාසලක් නෙවෙයි."),
    (f"あれは {KSH} では ありません。","Are wa watashi no kyoushitsu dewa arimasen.","That is not my classroom.","අරක මගේ පන්ති කාමරය නෙවෙයි."),
    (f"あれは {TOS} では ありません。","Are wa toshokan dewa arimasen.","That is not a library.","අරක පුස්තකාලයක් නෙවෙයි."),
  ],
  foot="これは〜では ありません",
)

P1Q = dict(
  no="04", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="これは 〜ですか？",
  title_ro='Kore wa 〜 desu ka &nbsp;|&nbsp; Is this 〜? &nbsp;|&nbsp; <span class="si">මේක 〜 ද?</span>',
  basic=("これは スマホ ですか。","Kore wa sumaho desu ka.",
         "Is this a smartphone?","මේක ජංගම දුරකථනයක්ද?"),
  use=(f'{r("文","ぶん")}の{r("最後","さい ご")}に「か」をつけると{r("質問","しつ もん")}になります。'
       f'{r("最後","さい ご")}を{r("少","すこ")}し{r("上","あ")}げて{r("言","い")}います。',
       'Add <b>ka</b> at the end of the sentence to make a question. '
       'Raise your voice a little at the end.',
       'වාක්‍යයේ අගට <b>ka</b> එකතු කළාම ප්‍රශ්නයක් වෙනවා. අගදී ස්වරය ටිකක් උස්සන්න.'),
  pattern=[[("これは","Kore wa"),"BLANK",("です","desu")],
           "ARROW",
           [("これは","Kore wa"),"BLANK",("ですか？","desu ka",True)]],
  examples=[
    (f"これは {MIZ} ですか。","Kore wa mizu desu ka.","Is this water?","මේක වතුරද?"),
    (f"これは {ANA}の {HON} ですか。","Kore wa anata no hon desu ka.","Is this your book?","මේක ඔබේ පොතද?"),
    (f"これは {ANA}の {NAM} ですか。","Kore wa anata no namae desu ka.","Is this your name?","මේක ඔබේ නමද?"),
    (f"これは {NHG}の {KYO} ですか。","Kore wa nihongo no kyoukasho desu ka.","Is this a Japanese textbook?","මේක ජපන් භාෂා පෙළපොතක්ද?"),
    (f"あれは {GAK} ですか。","Are wa gakkou desu ka.","Is that a school?","අරක පාසලක්ද?"),
    (f"あれは {ANA}の {r('教室','きょう しつ')} ですか。","Are wa anata no kyoushitsu desu ka.","Is that your classroom?","අරක ඔබේ පන්ති කාමරයද?"),
    (f"あれは {TOS} ですか。","Are wa toshokan desu ka.","Is that a library?","අරක පුස්තකාලයක්ද?"),
  ],
  foot="これは〜ですか？",
)


# ---------------------------------------------------------------- 04-4 / 04-5 答え方
_A_USE = (f'「〜ですか」の{r("質問","しつ もん")}には「はい」か「いいえ」で{r("答","こた")}えます。'
          f'みじかく{r("答","こた")}えるときは「はい、そうです。／いいえ、ちがいます。」。'
          f'くわしく{r("答","こた")}えるときは、うしろに{r("文","ぶん")}をつけます。',
          'Answer a <b>〜 desu ka</b> question with <b>hai</b> or <b>iie</b>. '
          'For a short answer say <b>Hai, sou desu / Iie, chigaimasu</b>. '
          'For a fuller answer, add the sentence after it.',
          '<b>〜 desu ka</b> ප්‍රශ්නයකට <b>hai</b> හෝ <b>iie</b> කියලා උත්තර දෙන්න. '
          'කෙටියෙන් නම් <b>Hai, sou desu / Iie, chigaimasu</b>. '
          'විස්තර කරනවා නම් පස්සෙන් වාක්‍යය එකතු කරන්න.')

_A_PAT = [[("はい、","Hai,"),"BLANK",("です","desu",True)],
          [("いいえ、","Iie,"),"BLANK",("では ありません","dewa arimasen",True)]]

_A_TITLE = ("はい / いいえ の 答え方",
            'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
            '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"これは {MIZ} ですか。","Kore wa mizu desu ka.","Is this water?","මේක වතුරද?"),
         ("はい、そうです。","Hai, sou desu.","Yes, it is.","ඔව්, එහෙමයි.")),
  ("QA", (f"これは {ANA}の {HON} ですか。","Kore wa anata no hon desu ka.","Is this your book?","මේක ඔබේ පොතද?"),
         ("いいえ、ちがいます。","Iie, chigaimasu.","No, it isn't.","නැහැ, එහෙම නෙවෙයි.")),
  ("QA", (f"これは {ANA}の {NAM} ですか。","Kore wa anata no namae desu ka.","Is this your name?","මේක ඔබේ නමද?"),
         (f"はい、{W}の {NAM} です。","Hai, watashi no namae desu.","Yes, it is my name.","ඔව්, ඒක මගේ නම.")),
  ("QA", (f"これは {NHG}の {KYO} ですか。","Kore wa nihongo no kyoukasho desu ka.","Is this a Japanese textbook?","මේක ජපන් භාෂා පෙළපොතක්ද?"),
         (f"はい、{NHG}の {KYO} です。","Hai, nihongo no kyoukasho desu.","Yes, it is a Japanese textbook.","ඔව්, ඒක ජපන් භාෂා පෙළපොතක්.")),
  ("QA", (f"あれは {GAK} ですか。","Are wa gakkou desu ka.","Is that a school?","අරක පාසලක්ද?"),
         (f"いいえ、{GAK} では ありません。","Iie, gakkou dewa arimasen.","No, it is not a school.","නැහැ, ඒක පාසලක් නෙවෙයි.")),
  ("QA", (f"あれは {ANA}の {r('教室','きょう しつ')} ですか。","Are wa anata no kyoushitsu desu ka.","Is that your classroom?","අරක ඔබේ පන්ති කාමරයද?"),
         (f"はい、{W}の {r('教室','きょう しつ')} です。","Hai, watashi no kyoushitsu desu.","Yes, it is my classroom.","ඔව්, ඒක මගේ පන්ති කාමරය.")),
  ("QA", (f"あれは {TOS} ですか。","Are wa toshokan desu ka.","Is that a library?","අරක පුස්තකාලයක්ද?"),
         (f"いいえ、{TOS} では ありません。","Iie, toshokan dewa arimasen.","No, it is not a library.","නැහැ, ඒක පුස්තකාලයක් නෙවෙයි.")),
  ("QA", (f"これは {ANA}の えんぴつ ですか。","Kore wa anata no enpitsu desu ka.","Is this your pencil?","මේක ඔබේ පැන්සලද?"),
         (f"はい、{W}の えんぴつ です。","Hai, watashi no enpitsu desu.","Yes, it is my pencil.","ඔව්, ඒක මගේ පැන්සල.")),
  ("QA", (f"これは {NHG}の {HON} ですか。","Kore wa nihongo no hon desu ka.","Is this a Japanese book?","මේක ජපන් භාෂා පොතක්ද?"),
         (f"いいえ、{NHG}の {HON} では ありません。","Iie, nihongo no hon dewa arimasen.","No, it is not a Japanese book.","නැහැ, ඒක ජපන් භාෂා පොතක් නෙවෙයි.")),
]

P1A = dict(
  no="04", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_A_TITLE[0], title_ro=_A_TITLE[1],
  basic=("はい、そうです。　／　いいえ、ちがいます。","Hai, sou desu. / Iie, chigaimasu.",
         "Yes, that's right. / No, that's not right.","ඔව්, එහෙමයි. / නැහැ, එහෙම නෙවෙයි."),
  use=_A_USE, pattern=_A_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P1A2 = dict(
  no="04", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_A_TITLE[0], title_ro=_A_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P1A["basic"], use=_A_USE, pattern=_A_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("はい。","Hai.","Yes.","ඔව්."),
    ("いいえ。","Iie.","No.","නැහැ."),
    ("そうです。","Sou desu.","That's right.","එහෙමයි."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P1,"p04_1_kore"), (P1N,"p04_2_negative"), (P1Q,"p04_3_question"), (P1A,"p04_4_answer"), (P1A2,"p04_5_answer2")]:
        render(p, stem)
