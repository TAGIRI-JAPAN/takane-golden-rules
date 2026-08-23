from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
WTC  = r("私","わたし")+"たちは"
GAK  = r("学生","がく せい")
ICH  = r("一年生","いち ねん せい")
DAI  = r("大学生","だい がく せい")
TOM  = r("友","とも")+"だち"
SEN  = r("先生","せん せい")
KARE = r("彼","かれ")
KANO = r("彼女","かの じょ")
SRI  = "スリランカ"+r("人","じん")
KUR  = "クラスメート"
NIH  = r("日本人","に ほん じん")

# ---------------------------------------------------------------- 05-1 基本
P2 = dict(
  no="05", tag=None,
  title_jp="私は 〜です",
  title_ro='Watashi wa 〜 desu &nbsp;|&nbsp; I am 〜 &nbsp;|&nbsp; <span class="si">මම 〜 යි</span>',
  basic=(f"{W}は {GAK} です。", "Watashi wa gakusei desu.",
         "I am a student.", "මම ශිෂ්‍යයෙක්."),
  use=(f'{r("名前","な まえ")}・{r("仕事","し ごと")}・{r("国","くに")}など、{r("自分","じ ぶん")}のことを{r("話","はな")}すときに{r("使","つか")}います。'
       f'「{r("彼","かれ")}は」「{r("彼女","かの じょ")}は」「{r("私","わたし")}たちは」も{r("同","おな")}じ{r("形","かたち")}です。',
       'Use it to talk about yourself — your name, job or country. '
       '<b>Kare wa</b> (he), <b>Kanojo wa</b> (she) and <b>Watashitachi wa</b> (we) work the same way.',
       'තමන් ගැන — නම, රැකියාව, රට — කියන්න මේක භාවිතා කරන්න. '
       '<b>Kare wa</b> (ඔහු), <b>Kanojo wa</b> (ඇය), <b>Watashitachi wa</b> (අපි) කියන ඒවත් එකම හැඩයයි.'),
  pattern=[[(f"{W}は","Watashi wa"),"BLANK",("です","desu")],
           [(f"{KARE}は / {KANO}は","Kare wa / Kanojo wa"),"BLANK",("です","desu")]],
  examples=[
    (f"{W}は {GAK} です。","Watashi wa gakusei desu.","I am a student.","මම ශිෂ්‍යයෙක්."),
    (f"{W}は {SRI} です。","Watashi wa Suriranka-jin desu.","I am Sri Lankan.","මම ශ්‍රී ලාංකිකයෙක්."),
    (f"{W}は {ICH} です。","Watashi wa ichinensei desu.","I am a first-year student.","මම පළමු වසරේ ශිෂ්‍යයෙක්."),
    (f"{KARE}は {W}の {TOM} です。","Kare wa watashi no tomodachi desu.","He is my friend.","ඔහු මගේ යාළුවා."),
    (f"{KANO}は {W}の {SEN} です。","Kanojo wa watashi no sensei desu.","She is my teacher.","ඇය මගේ ගුරුතුමිය."),
    (f"{KARE}は {DAI} です。","Kare wa daigakusei desu.","He is a university student.","ඔහු විශ්වවිද්‍යාල ශිෂ්‍යයෙක්."),
    (f"{WTC} {KUR} です。","Watashitachi wa kurasumeeto desu.","We are classmates.","අපි පන්තියේ මිතුරෝ."),
  ],
  foot="私は〜です",
)

# ---------------------------------------------------------------- 05-2 否定
P2N = dict(
  no="05", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="私は 〜では ありません",
  title_ro='Watashi wa 〜 dewa arimasen &nbsp;|&nbsp; I am not 〜 &nbsp;|&nbsp; <span class="si">මම 〜 නෙවෙයි</span>',
  basic=(f"{W}は {SEN} では ありません。","Watashi wa sensei dewa arimasen.",
         "I am not a teacher.","මම ගුරුවරයෙක් නෙවෙයි."),
  use=(f'「です」を「では ありません」に{r("変","か")}えると{r("否定","ひ てい")}になります。'
       f'{r("話","はな")}しことばでは「じゃ ありません」「じゃ ないです」も{r("使","つか")}います。',
       'Change <b>desu</b> to <b>dewa arimasen</b> to make it negative. '
       'In conversation, <b>ja arimasen</b> and <b>ja nai desu</b> are also used.',
       '<b>desu</b> වෙනුවට <b>dewa arimasen</b> දැම්මාම නැහැ කියන අර්ථය එනවා. '
       'කතා කරද්දී <b>ja arimasen</b>, <b>ja nai desu</b> කියලත් කියනවා.'),
  pattern=[[(f"{W}は","Watashi wa"),"BLANK",("です","desu")],
           "ARROW",
           [(f"{W}は","Watashi wa"),"BLANK",("では ありません","dewa arimasen",True)]],
  examples=[
    (f"{W}は {GAK} では ありません。","Watashi wa gakusei dewa arimasen.","I am not a student.","මම ශිෂ්‍යයෙක් නෙවෙයි."),
    (f"{W}は {SRI} では ありません。","Watashi wa Suriranka-jin dewa arimasen.","I am not Sri Lankan.","මම ශ්‍රී ලාංකිකයෙක් නෙවෙයි."),
    (f"{W}は {ICH} では ありません。","Watashi wa ichinensei dewa arimasen.","I am not a first-year student.","මම පළමු වසරේ ශිෂ්‍යයෙක් නෙවෙයි."),
    (f"{KARE}は {W}の {TOM} では ありません。","Kare wa watashi no tomodachi dewa arimasen.","He is not my friend.","ඔහු මගේ යාළුවා නෙවෙයි."),
    (f"{KANO}は {W}の {SEN} では ありません。","Kanojo wa watashi no sensei dewa arimasen.","She is not my teacher.","ඇය මගේ ගුරුතුමිය නෙවෙයි."),
    (f"{KARE}は {DAI} では ありません。","Kare wa daigakusei dewa arimasen.","He is not a university student.","ඔහු විශ්වවිද්‍යාල ශිෂ්‍යයෙක් නෙවෙයි."),
    (f"{WTC} {KUR} では ありません。","Watashitachi wa kurasumeeto dewa arimasen.","We are not classmates.","අපි පන්තියේ මිතුරෝ නෙවෙයි."),
  ],
  foot="私は〜では ありません",
)

# ---------------------------------------------------------------- 05-3 疑問
P2Q = dict(
  no="05", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="あなたは 〜ですか？",
  title_ro='Anata wa 〜 desu ka &nbsp;|&nbsp; Are you 〜? &nbsp;|&nbsp; <span class="si">ඔබ 〜 ද?</span>',
  basic=(f"あなたは {GAK} ですか。","Anata wa gakusei desu ka.",
         "Are you a student?","ඔබ ශිෂ්‍යයෙක්ද?"),
  use=(f'{r("相手","あい て")}のことを{r("聞","き")}くときは「あなたは〜ですか」。'
       f'{r("名前","な まえ")}がわかっているときは「あなた」より{r("名前","な まえ")}で{r("呼","よ")}ぶほうが{r("自然","し ぜん")}です。',
       'To ask about the person you are talking to, use <b>Anata wa 〜 desu ka</b>. '
       'If you know their name, using the name instead of <b>anata</b> sounds more natural.',
       'කතා කරන කෙනා ගැන අහන්න <b>Anata wa 〜 desu ka</b>. '
       'නම දන්නවා නම් <b>anata</b> වෙනුවට නම කියන එක වඩා ස්වාභාවිකයි.'),
  pattern=[[("あなたは","Anata wa"),"BLANK",("です","desu")],
           "ARROW",
           [("あなたは","Anata wa"),"BLANK",("ですか？","desu ka",True)]],
  examples=[
    (f"あなたは {GAK} ですか。","Anata wa gakusei desu ka.","Are you a student?","ඔබ ශිෂ්‍යයෙක්ද?"),
    (f"あなたは {SRI} ですか。","Anata wa Suriranka-jin desu ka.","Are you Sri Lankan?","ඔබ ශ්‍රී ලාංකිකයෙක්ද?"),
    (f"あなたは {ICH} ですか。","Anata wa ichinensei desu ka.","Are you a first-year student?","ඔබ පළමු වසරේ ශිෂ්‍යයෙක්ද?"),
    (f"{KARE}は あなたの {TOM} ですか。","Kare wa anata no tomodachi desu ka.","Is he your friend?","ඔහු ඔබේ යාළුවාද?"),
    (f"{KANO}は あなたの {SEN} ですか。","Kanojo wa anata no sensei desu ka.","Is she your teacher?","ඇය ඔබේ ගුරුතුමියද?"),
    (f"{KARE}は {DAI} ですか。","Kare wa daigakusei desu ka.","Is he a university student?","ඔහු විශ්වවිද්‍යාල ශිෂ්‍යයෙක්ද?"),
    (f"あなたたちは {KUR} ですか。","Anatatachi wa kurasumeeto desu ka.","Are you classmates?","ඔබලා පන්තියේ මිතුරෝද?"),
  ],
  foot="あなたは〜ですか？",
)

# ---------------------------------------------------------------- 05-4 答え方
P2A = dict(
  no="05", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp="はい / いいえ の 答え方",
  title_ro='Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; <span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>',
  basic=("はい、そうです。　／　いいえ、ちがいます。","Hai, sou desu. / Iie, chigaimasu.",
         "Yes, that's right. / No, that's not right.","ඔව්, එහෙමයි. / නැහැ, එහෙම නෙවෙයි."),
  use=(f'「〜ですか」の{r("質問","しつ もん")}には「はい」か「いいえ」で{r("答","こた")}えます。'
       f'みじかく{r("答","こた")}えるときは「はい、そうです。／いいえ、ちがいます。」。'
       f'くわしく{r("答","こた")}えるときは、うしろに{r("文","ぶん")}をつけます。',
       'Answer a <b>〜 desu ka</b> question with <b>hai</b> or <b>iie</b>. '
       'For a short answer say <b>Hai, sou desu / Iie, chigaimasu</b>. '
       'For a fuller answer, add the sentence after it.',
       '<b>〜 desu ka</b> ප්‍රශ්නයකට <b>hai</b> හෝ <b>iie</b> කියලා උත්තර දෙන්න. '
       'කෙටියෙන් නම් <b>Hai, sou desu / Iie, chigaimasu</b>. '
       'විස්තර කරනවා නම් පස්සෙන් වාක්‍යය එකතු කරන්න.'),
  pattern=[[("はい、","Hai,"),"BLANK",("です","desu",True)],
           [("いいえ、","Iie,"),"BLANK",("では ありません","dewa arimasen",True)]],
  examples=[
    ("QA", (f"あなたは {GAK} ですか。","Anata wa gakusei desu ka.","Are you a student?","ඔබ ශිෂ්‍යයෙක්ද?"),
           ("はい、そうです。","Hai, sou desu.","Yes, I am.","ඔව්, එහෙමයි.")),
    ("QA", (f"あなたは {SEN} ですか。","Anata wa sensei desu ka.","Are you a teacher?","ඔබ ගුරුවරයෙක්ද?"),
           ("いいえ、ちがいます。","Iie, chigaimasu.","No, I'm not.","නැහැ, එහෙම නෙවෙයි.")),
    ("QA", (f"あなたは {SRI} ですか。","Anata wa Suriranka-jin desu ka.","Are you Sri Lankan?","ඔබ ශ්‍රී ලාංකිකයෙක්ද?"),
           (f"はい、{SRI} です。","Hai, Suriranka-jin desu.","Yes, I am Sri Lankan.","ඔව්, මම ශ්‍රී ලාංකිකයෙක්.")),
    ("QA", (f"{KARE}は あなたの {TOM} ですか。","Kare wa anata no tomodachi desu ka.","Is he your friend?","ඔහු ඔබේ යාළුවාද?"),
           (f"はい、{W}の {TOM} です。","Hai, watashi no tomodachi desu.","Yes, he is my friend.","ඔව්, ඔහු මගේ යාළුවා.")),
  ],
  foot="はい / いいえ の 答え方",
)

P2A2 = dict(
  no="05", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp="はい / いいえ の 答え方",
  title_ro='Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; <span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>',
  skip=("basic","use","pattern"),
  start=4,
  basic=P2A["basic"], use=P2A["use"], pattern=P2A["pattern"],
  examples=[
    ("QA", (f"{KANO}は あなたの {SEN} ですか。","Kanojo wa anata no sensei desu ka.","Is she your teacher?","ඇය ඔබේ ගුරුතුමියද?"),
           (f"いいえ、{W}の {SEN} では ありません。","Iie, watashi no sensei dewa arimasen.","No, she is not my teacher.","නැහැ, ඇය මගේ ගුරුතුමිය නෙවෙයි.")),
    ("QA", (f"あなたは {ICH} ですか。","Anata wa ichinensei desu ka.","Are you a first-year student?","ඔබ පළමු වසරේ ශිෂ්‍යයෙක්ද?"),
           (f"いいえ、{ICH} では ありません。","Iie, ichinensei dewa arimasen.","No, I am not a first-year student.","නැහැ, මම පළමු වසරේ ශිෂ්‍යයෙක් නෙවෙයි.")),
    ("QA", (f"あなたたちは {KUR} ですか。","Anatatachi wa kurasumeeto desu ka.","Are you classmates?","ඔබලා පන්තියේ මිතුරෝද?"),
           (f"はい、{KUR} です。","Hai, kurasumeeto desu.","Yes, we are classmates.","ඔව්, අපි පන්තියේ මිතුරෝ.")),
    ("QA", (f"あなたの {SEN}は {NIH} ですか。","Anata no sensei wa Nihon-jin desu ka.","Is your teacher Japanese?","ඔබේ ගුරුවරයා ජපන් ජාතිකද?"),
           (f"はい、{NIH} です。","Hai, Nihon-jin desu.","Yes, she is Japanese.","ඔව්, ඇය ජපන් ජාතිකයි.")),
    ("QA", (f"{KARE}は {GAK} ですか。","Kare wa gakusei desu ka.","Is he a student?","ඔහු ශිෂ්‍යයෙක්ද?"),
           (f"いいえ、{GAK} では ありません。","Iie, gakusei dewa arimasen.","No, he is not a student.","නැහැ, ඔහු ශිෂ්‍යයෙක් නෙවෙයි.")),
  ],
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
    for p, stem in [(P2,"p05_1_watashi"), (P2N,"p05_2_negative"),
                    (P2Q,"p05_3_question"), (P2A,"p05_4_answer"), (P2A2,"p05_5_answer2")]:
        render(p, stem)
