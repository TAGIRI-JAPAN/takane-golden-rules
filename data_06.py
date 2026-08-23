from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NHG = r("日本語","に ほん ご")
KAN = r("漢字","かん じ")
KSH = r("教室","きょう しつ")
KYO = r("今日","きょう")
SEN = r("先生","せん せい")
TOS = r("図書館","と しょ かん")
AST = r("明日","あ した")
GAK = r("学校","がっ こう")

# ---------------------------------------------------------------- 06-1 基本
P3 = dict(
  no="06", tag=None,
  title_jp="〜は …です",
  title_ro='〜 wa … desu &nbsp;|&nbsp; 〜 is … &nbsp;|&nbsp; <span class="si">〜 … යි</span>',
  basic=(f"{NHG}は たのしい です。","Nihongo wa tanoshii desu.",
         "Japanese is fun.","ජපන් භාෂාව විනෝදජනකයි."),
  use=(f'{r("人","ひと")}や{r("物","もの")}の{r("様子","よう す")}・{r("状態","じょう たい")}・{r("気持","き も")}ちを{r("表","あらわ")}します。'
       f'「…」には けいようし（たのしい・しずか）や めいし（{AST}）が{r("入","はい")}ります。',
       'Use it to describe how a person or thing is. '
       'The <b>…</b> part can be an adjective (<b>tanoshii</b>, <b>shizuka</b>) or a noun (<b>ashita</b>).',
       'කෙනෙක්ගේ හෝ දෙයක තත්ත්වය කියන්න මේක භාවිතා කරන්න. '
       '<b>…</b> එකට විශේෂණ පදයක් (<b>tanoshii</b>, <b>shizuka</b>) හෝ නාම පදයක් (<b>ashita</b>) දාන්න පුළුවන්.'),
  pattern=[[("〜は","~ wa"),"BLANK",("です","desu")]],
  examples=[
    (f"{NHG}は たのしい です。","Nihongo wa tanoshii desu.","Japanese is fun.","ජපන් භාෂාව විනෝදජනකයි."),
    (f"{KAN}は むずかしい です。","Kanji wa muzukashii desu.","Kanji is difficult.","කන්ජි අකුරු අමාරුයි."),
    (f"{KSH}は あたらしい です。","Kyoushitsu wa atarashii desu.","The classroom is new.","පන්ති කාමරය අලුත්."),
    (f"{KYO}は いそがしい です。","Kyou wa isogashii desu.","Today is busy.","අද කාර්යබහුලයි."),
    (f"{SEN}は しんせつ です。","Sensei wa shinsetsu desu.","The teacher is kind.","ගුරුතුමා කරුණාවන්තයි."),
    (f"{TOS}は しずか です。","Toshokan wa shizuka desu.","The library is quiet.","පුස්තකාලය නිශ්ශබ්දයි."),
    (f"テストは {AST} です。","Tesuto wa ashita desu.","The test is tomorrow.","විභාගය හෙටයි."),
  ],
  foot="〜は …です",
)

# ---------------------------------------------------------------- 06-2 否定
P3N = dict(
  no="06", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜は …く ありません / …では ありません",
  title_ro='〜 wa … ku arimasen / … dewa arimasen &nbsp;|&nbsp; 〜 is not … &nbsp;|&nbsp; '
           '<span class="si">〜 … නැහැ</span>',
  basic=(f"{NHG}は たのしく ありません。","Nihongo wa tanoshiku arimasen.",
         "Japanese is not fun.","ජපන් භාෂාව විනෝදජනක නැහැ."),
  use=(f'{r("否定","ひ てい")}は 2つ{r("形","かたち")}があります。「い」でおわる ことばは、さいごの「い」を「く ありません」に{r("変","か")}えます。'
       f'それ{r("以外","い がい")}（な けいようし・めいし）は「では ありません」をつけます。',
       'There are two negative forms. If the word ends in <b>-i</b>, change the final <b>i</b> to '
       '<b>ku arimasen</b>. Otherwise (na-adjectives and nouns), add <b>dewa arimasen</b>.',
       'නිශේධන ආකාර දෙකක් තියෙනවා. වචනය <b>-i</b> කියලා අවසන් වෙනවා නම්, අන්තිම <b>i</b> එක '
       '<b>ku arimasen</b> කියලා වෙනස් කරන්න. අනිත් ඒවාට (na-විශේෂණ සහ නාම පද) <b>dewa arimasen</b> එකතු කරන්න.'),
  pattern=[
    "NOTE:「い」でおわる ことば　/　i-adjectives",
    [("たのしい","tanoshii"),"TO",("たのしく ありません","tanoshiku arimasen",True)],
    "NOTE:な けいようし・めいし　/　na-adjectives &amp; nouns",
    [("しずか","shizuka"),"TO",("しずか では ありません","shizuka dewa arimasen",True)],
  ],
  examples=[
    (f"{NHG}は たのしく ありません。","Nihongo wa tanoshiku arimasen.","Japanese is not fun.","ජපන් භාෂාව විනෝදජනක නැහැ."),
    (f"{KAN}は むずかしく ありません。","Kanji wa muzukashiku arimasen.","Kanji is not difficult.","කන්ජි අකුරු අමාරු නැහැ."),
    (f"{KSH}は あたらしく ありません。","Kyoushitsu wa atarashiku arimasen.","The classroom is not new.","පන්ති කාමරය අලුත් නැහැ."),
    (f"{KYO}は いそがしく ありません。","Kyou wa isogashiku arimasen.","Today is not busy.","අද කාර්යබහුල නැහැ."),
    (f"{SEN}は しんせつ では ありません。","Sensei wa shinsetsu dewa arimasen.","The teacher is not kind.","ගුරුතුමා කරුණාවන්ත නැහැ."),
    (f"{TOS}は しずか では ありません。","Toshokan wa shizuka dewa arimasen.","The library is not quiet.","පුස්තකාලය නිශ්ශබ්ද නැහැ."),
    (f"テストは {AST} では ありません。","Tesuto wa ashita dewa arimasen.","The test is not tomorrow.","විභාගය හෙට නෙවෙයි."),
  ],
  foot="〜は …く ありません",
)

# ---------------------------------------------------------------- 06-3 疑問
P3Q = dict(
  no="06", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜は …ですか？",
  title_ro='〜 wa … desu ka &nbsp;|&nbsp; Is 〜 …? &nbsp;|&nbsp; <span class="si">〜 … ද?</span>',
  basic=(f"{NHG}は たのしい ですか。","Nihongo wa tanoshii desu ka.",
         "Is Japanese fun?","ජපන් භාෂාව විනෝදජනකද?"),
  use=(f'{r("形","かたち")}は{r("変","か")}えません。「です」のうしろに「か」をつけるだけです。'
       f'「い」でおわる ことばも、な けいようし・めいしも、{r("同","おな")}じです。',
       'The word itself does not change. Just add <b>ka</b> after <b>desu</b>. '
       'This is the same for <b>-i</b> words, na-adjectives and nouns.',
       'වචනය වෙනස් වෙන්නේ නැහැ. <b>desu</b> එකට පස්සේ <b>ka</b> එකතු කරන්න විතරයි. '
       '<b>-i</b> වචන, na-විශේෂණ, නාම පද — හැම එකටම එකයි.'),
  pattern=[[("〜は","~ wa"),"BLANK",("です","desu")],
           "ARROW",
           [("〜は","~ wa"),"BLANK",("ですか？","desu ka",True)]],
  examples=[
    (f"{NHG}は たのしい ですか。","Nihongo wa tanoshii desu ka.","Is Japanese fun?","ජපන් භාෂාව විනෝදජනකද?"),
    (f"{KAN}は むずかしい ですか。","Kanji wa muzukashii desu ka.","Is kanji difficult?","කන්ජි අකුරු අමාරුද?"),
    (f"{KSH}は あたらしい ですか。","Kyoushitsu wa atarashii desu ka.","Is the classroom new?","පන්ති කාමරය අලුත්ද?"),
    (f"{KYO}は いそがしい ですか。","Kyou wa isogashii desu ka.","Is today busy?","අද කාර්යබහුලද?"),
    (f"{SEN}は しんせつ ですか。","Sensei wa shinsetsu desu ka.","Is the teacher kind?","ගුරුතුමා කරුණාවන්තද?"),
    (f"{TOS}は しずか ですか。","Toshokan wa shizuka desu ka.","Is the library quiet?","පුස්තකාලය නිශ්ශබ්දද?"),
    (f"テストは {AST} ですか。","Tesuto wa ashita desu ka.","Is the test tomorrow?","විභාගය හෙටද?"),
  ],
  foot="〜は …ですか？",
)

# ---------------------------------------------------------------- 06-4 / 06-5 答え方
_USE = (f'「はい」「いいえ」のあとに、もういちど {r("文","ぶん")}を いいます。'
        f'いいえのときは、「く ありません」か「では ありません」を{r("使","つか")}います。',
        'After <b>hai</b> or <b>iie</b>, say the sentence again. '
        'For <b>iie</b>, use <b>ku arimasen</b> or <b>dewa arimasen</b>.',
        '<b>hai</b> හෝ <b>iie</b> කියලා පස්සේ, වාක්‍යය ආයෙත් කියන්න. '
        '<b>iie</b> නම් <b>ku arimasen</b> හෝ <b>dewa arimasen</b> භාවිතා කරන්න.')

_PAT = [[("はい、","Hai,"),"BLANK",("です","desu",True)],
        [("いいえ、","Iie,"),"BLANK",("く ありません / では ありません","ku arimasen / dewa arimasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{NHG}は たのしい ですか。","Nihongo wa tanoshii desu ka.","Is Japanese fun?","ජපන් භාෂාව විනෝදජනකද?"),
         ("はい、たのしい です。","Hai, tanoshii desu.","Yes, it is fun.","ඔව්, විනෝදජනකයි.")),
  ("QA", (f"{KAN}は むずかしい ですか。","Kanji wa muzukashii desu ka.","Is kanji difficult?","කන්ජි අකුරු අමාරුද?"),
         ("いいえ、むずかしく ありません。","Iie, muzukashiku arimasen.","No, it is not difficult.","නැහැ, අමාරු නැහැ.")),
  ("QA", (f"{KSH}は あたらしい ですか。","Kyoushitsu wa atarashii desu ka.","Is the classroom new?","පන්ති කාමරය අලුත්ද?"),
         ("はい、あたらしい です。","Hai, atarashii desu.","Yes, it is new.","ඔව්, අලුත්.")),
  ("QA", (f"{KYO}は いそがしい ですか。","Kyou wa isogashii desu ka.","Is today busy?","අද කාර්යබහුලද?"),
         ("いいえ、いそがしく ありません。","Iie, isogashiku arimasen.","No, it is not busy.","නැහැ, කාර්යබහුල නැහැ.")),
  ("QA", (f"{SEN}は しんせつ ですか。","Sensei wa shinsetsu desu ka.","Is the teacher kind?","ගුරුතුමා කරුණාවන්තද?"),
         ("はい、しんせつ です。","Hai, shinsetsu desu.","Yes, he is kind.","ඔව්, කරුණාවන්තයි.")),
  ("QA", (f"{TOS}は しずか ですか。","Toshokan wa shizuka desu ka.","Is the library quiet?","පුස්තකාලය නිශ්ශබ්දද?"),
         ("いいえ、しずか では ありません。","Iie, shizuka dewa arimasen.","No, it is not quiet.","නැහැ, නිශ්ශබ්ද නැහැ.")),
  ("QA", (f"テストは {AST} ですか。","Tesuto wa ashita desu ka.","Is the test tomorrow?","විභාගය හෙටද?"),
         (f"はい、{AST} です。","Hai, ashita desu.","Yes, it is tomorrow.","ඔව්, හෙටයි.")),
  ("QA", (f"{GAK}は とおい ですか。","Gakkou wa tooi desu ka.","Is the school far?","පාසල දුරද?"),
         ("いいえ、とおく ありません。","Iie, tooku arimasen.","No, it is not far.","නැහැ, දුර නැහැ.")),
  ("QA", (f"{KYO}は さむい ですか。","Kyou wa samui desu ka.","Is it cold today?","අද සීතලද?"),
         ("はい、さむい です。","Hai, samui desu.","Yes, it is cold.","ඔව්, සීතලයි.")),
]

P3A = dict(
  no="06", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、たのしい です。　／　いいえ、たのしく ありません。",
         "Hai, tanoshii desu. / Iie, tanoshiku arimasen.",
         "Yes, it is fun. / No, it is not fun.",
         "ඔව්, විනෝදජනකයි. / නැහැ, විනෝදජනක නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P3A2 = dict(
  no="06", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P3A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("はい、とても。","Hai, totemo.","Yes, very.","ඔව්, ගොඩක්."),
    ("いいえ、ぜんぜん。","Iie, zenzen.","No, not at all.","නැහැ, කිසිසේත්ම නැහැ."),
    ("すこし。","Sukoshi.","A little.","ටිකක්."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P3,"p06_1_wa_desu"), (P3N,"p06_2_negative"), (P3Q,"p06_3_question"),
                    (P3A,"p06_4_answer"), (P3A2,"p06_5_answer2")]:
        render(p, stem)
