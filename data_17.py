from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
NIH  = r("日本","に ほん")
NHG  = r("日本語","に ほん ご")
NIHJ = r("日本人","に ほん じん")
ITT  = r("行","い")+"った"
TEG  = r("手紙","て がみ")
KAIT = r("書","か")+"いた"
HON  = r("本","ほん")
YOND = r("読","よ")+"んだ"
HANT = r("話","はな")+"した"
TABT = r("食","た")+"べた"
BEN  = r("勉強","べん きょう")
GAK  = r("学校","がっ こう")
NIK  = r("二回","に かい")
ICH  = r("一度","いち ど")
HIK  = r("飛行機","ひ こう き")
NOTT = "のった"
YAM  = r("山","やま")
NOBT = r("登","のぼ")+"った"

_TA1 = "NOTE:15の「て」を「た」に かえるだけ　/　te &#8594; ta"
_TA2 = (f"NOTE:{r('食','た')}べて→{TABT}　/　{r('読','よ')}んで→{YOND}　/　"
        f"{r('行','い')}って→{ITT}　/　{r('書','か')}いて→{KAIT}　/　して→した")

# ---------------------------------------------------------------- 17-1 基本
P13 = dict(
  no="17", tag=None,
  title_jp="〜した ことが あります",
  title_ro='〜 shita koto ga arimasu &nbsp;|&nbsp; I have 〜 before &nbsp;|&nbsp; '
           '<span class="si">〜 ලා තියෙනවා</span>',
  basic=(f"{W}は {NIH}に {ITT}ことが あります。","Watashi wa Nihon ni itta koto ga arimasu.",
         "I have been to Japan.","මම ජපානයට ගිහින් තියෙනවා."),
  use=(f'まえに{ICH}でも けいけんが あることを{r("言","い")}います。'
       f'「ました」を「た」に かえて、うしろに「ことが あります」を つけます。'
       f'「た」の{r("作","つく")}り{r("方","かた")}は 15の「て」と{r("同","おな")}じです。',
       'It says you have experienced something at least once before. Change <b>mashita</b> to the '
       'plain past <b>ta</b>, then add <b>koto ga arimasu</b>. '
       'The <b>ta</b> form follows exactly the same rules as the <b>te</b> form in pattern 15.',
       'කලින් අඩුම තරමේ එක වතාවක්වත් අත්දැකීමක් තියෙනවා කියන එක — '
       '<b>ta koto ga arimasu</b> = ...ලා තියෙනවා. '
       '<b>mashita</b> එක <b>ta</b> කරලා, පස්සෙන් <b>koto ga arimasu</b> දාන්න. '
       '<b>ta</b> හැදෙන ක්‍රමය 15 හි <b>te</b> එකට සමානයි.'),
  pattern=[_TA1,
           [("〜て","~ te"),"TO",("〜た","~ ta",True)],
           [("〜は","~ wa"),"BLANK",("た ことが あります","ta koto ga arimasu")],
           _TA2],
  examples=[
    (f"{NIH}に {ITT}ことが あります。","Nihon ni itta koto ga arimasu.","I have been to Japan.","මම ජපානයට ගිහින් තියෙනවා."),
    (f"{NHG}で {TEG}を {KAIT}ことが あります。","Nihongo de tegami wo kaita koto ga arimasu.","I have written a letter in Japanese.","මම ජපන් භාෂාවෙන් ලිපියක් ලියලා තියෙනවා."),
    (f"{NIH}の {HON}を {YOND}ことが あります。","Nihon no hon wo yonda koto ga arimasu.","I have read a Japanese book.","මම ජපන් පොතක් කියවලා තියෙනවා."),
    (f"{NIHJ}と {HANT}ことが あります。","Nihon-jin to hanashita koto ga arimasu.","I have talked with a Japanese person.","මම ජපන් ජාතිකයෙක් එක්ක කතා කරලා තියෙනවා."),
    (f"そばを {TABT}ことが あります。","Soba wo tabeta koto ga arimasu.","I have eaten soba.","මම සෝබා කාලා තියෙනවා."),
    (f"アルバイトを した ことが あります。","Arubaito wo shita koto ga arimasu.","I have worked part-time.","මම අර්ධකාලීන රැකියාවක් කරලා තියෙනවා."),
    (f"{NIH}の {GAK}で {BEN}した ことが あります。","Nihon no gakkou de benkyou shita koto ga arimasu.","I have studied at a school in Japan.","මම ජපානයේ පාසලක ඉගෙන ගෙන තියෙනවා."),
  ],
  foot="〜した ことが あります",
)

# ---------------------------------------------------------------- 17-2 否定
P13N = dict(
  no="17", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜した ことが ありません",
  title_ro='〜 shita koto ga arimasen &nbsp;|&nbsp; I have never 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 ලා නැහැ</span>',
  basic=(f"{W}は {NIH}に {ITT}ことが ありません。","Watashi wa Nihon ni itta koto ga arimasen.",
         "I have never been to Japan.","මම ජපානයට ගිහින් නැහැ."),
  use=(f'10で ならった「あります」を「ありません」に かえるだけです。'
       f'「{ICH}も ありません」と{r("言","い")}うと「1かいも ない」と はっきり{r("伝","つた")}わります。',
       'Just change the <b>arimasu</b> you learned in pattern 10 to <b>arimasen</b>. '
       'Saying <b>ichido mo arimasen</b> makes it clear that you have never done it, not even once.',
       '10 වලදී ඉගෙන ගත්ත <b>arimasu</b> එක <b>arimasen</b> කරන්න විතරයි. '
       '<b>ichido mo arimasen</b> කිව්වොත් "එක වතාවක්වත් නැහැ" කියලා පැහැදිලිව කියවෙනවා.'),
  pattern=[[("〜た ことが","~ ta koto ga"),("あります","arimasu")],
           "ARROW",
           [("〜た ことが","~ ta koto ga"),("ありません","arimasen",True)],
           f"NOTE:{ICH}も ありません = එක වතාවක්වත් නැහැ（not even once）"],
  examples=[
    (f"{NIH}に {ITT}ことが ありません。","Nihon ni itta koto ga arimasen.","I have never been to Japan.","මම ජපානයට ගිහින් නැහැ."),
    (f"{NHG}で {TEG}を {KAIT}ことが ありません。","Nihongo de tegami wo kaita koto ga arimasen.","I have never written a letter in Japanese.","මම ජපන් භාෂාවෙන් ලිපියක් ලියලා නැහැ."),
    (f"{NIH}の {HON}を {YOND}ことが ありません。","Nihon no hon wo yonda koto ga arimasen.","I have never read a Japanese book.","මම ජපන් පොතක් කියවලා නැහැ."),
    (f"{NIHJ}と {HANT}ことが ありません。","Nihon-jin to hanashita koto ga arimasen.","I have never talked with a Japanese person.","මම ජපන් ජාතිකයෙක් එක්ක කතා කරලා නැහැ."),
    (f"そばを {ICH}も {TABT}ことが ありません。","Soba wo ichido mo tabeta koto ga arimasen.","I have never eaten soba, not even once.","මම සෝබා එක වතාවක්වත් කාලා නැහැ."),
    (f"アルバイトを した ことが ありません。","Arubaito wo shita koto ga arimasen.","I have never worked part-time.","මම අර්ධකාලීන රැකියාවක් කරලා නැහැ."),
    (f"{NIH}の {GAK}で {BEN}した ことが ありません。","Nihon no gakkou de benkyou shita koto ga arimasen.","I have never studied at a school in Japan.","මම ජපානයේ පාසලක ඉගෙන ගෙන නැහැ."),
  ],
  foot="〜した ことが ありません",
)

# ---------------------------------------------------------------- 17-3 疑問
P13Q = dict(
  no="17", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜した ことが ありますか？",
  title_ro='〜 shita koto ga arimasu ka &nbsp;|&nbsp; Have you ever 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 ලා තියෙනවාද?</span>',
  basic=(f"あなたは {NIH}に {ITT}ことが ありますか。","Anata wa Nihon ni itta koto ga arimasu ka.",
         "Have you ever been to Japan?","ඔබ ජපානයට ගිහින් තියෙනවාද?"),
  use=(f'「ありますか」で、けいけんが あるかどうかを{r("聞","き")}きます。'
       f'{r("初","はじ")}めて{r("会","あ")}った{r("人","ひと")}と{r("話","はな")}すときに とても{r("便利","べん り")}な{r("質問","しつ もん")}です。',
       'Use <b>arimasu ka</b> to ask whether someone has ever done something. '
       'It is a very handy question when you are talking with someone for the first time.',
       '<b>arimasu ka</b> කියලා අහන්නේ අත්දැකීමක් තියෙනවාද කියලා. '
       'මුලින්ම හමුවෙන කෙනෙක් එක්ක කතා කරද්දී ගොඩක් ප්‍රයෝජනවත් ප්‍රශ්නයක්.'),
  pattern=[[("〜た ことが","~ ta koto ga"),("あります","arimasu")],
           "ARROW",
           [("〜た ことが","~ ta koto ga"),("ありますか？","arimasu ka",True)]],
  examples=[
    (f"あなたは {NIH}に {ITT}ことが ありますか。","Anata wa Nihon ni itta koto ga arimasu ka.","Have you ever been to Japan?","ඔබ ජපානයට ගිහින් තියෙනවාද?"),
    (f"{NHG}で {TEG}を {KAIT}ことが ありますか。","Nihongo de tegami wo kaita koto ga arimasu ka.","Have you ever written a letter in Japanese?","ඔබ ජපන් භාෂාවෙන් ලිපියක් ලියලා තියෙනවාද?"),
    (f"{NIH}の {HON}を {YOND}ことが ありますか。","Nihon no hon wo yonda koto ga arimasu ka.","Have you ever read a Japanese book?","ඔබ ජපන් පොතක් කියවලා තියෙනවාද?"),
    (f"{NIHJ}と {HANT}ことが ありますか。","Nihon-jin to hanashita koto ga arimasu ka.","Have you ever talked with a Japanese person?","ඔබ ජපන් ජාතිකයෙක් එක්ක කතා කරලා තියෙනවාද?"),
    (f"そばを {TABT}ことが ありますか。","Soba wo tabeta koto ga arimasu ka.","Have you ever eaten soba?","ඔබ සෝබා කාලා තියෙනවාද?"),
    (f"アルバイトを した ことが ありますか。","Arubaito wo shita koto ga arimasu ka.","Have you ever worked part-time?","ඔබ අර්ධකාලීන රැකියාවක් කරලා තියෙනවාද?"),
    (f"{NIH}の {GAK}で {BEN}した ことが ありますか。","Nihon no gakkou de benkyou shita koto ga arimasu ka.","Have you ever studied at a school in Japan?","ඔබ ජපානයේ පාසලක ඉගෙන ගෙන තියෙනවාද?"),
  ],
  foot="〜した ことが ありますか？",
)

# ---------------------------------------------------------------- 17-4 / 17-5 答え方
_USE = (f'「はい、あります。」「いいえ、ありません。」だけで{r("答","こた")}えられます。'
        f'かいすうを つけると もっと よく{r("伝","つた")}わります（{ICH}だけ・{NIK}・よく）。',
        'You can answer with just <b>Hai, arimasu</b> or <b>Iie, arimasen</b>. '
        'Adding how many times makes it clearer: <b>ichido dake</b> (only once), '
        '<b>nikai</b> (twice), <b>yoku</b> (often).',
        '<b>Hai, arimasu</b> හෝ <b>Iie, arimasen</b> කියලා විතරක් උත්තර දෙන්න පුළුවන්. '
        'වාර ගණන දැම්මොත් වඩා පැහැදිලියි: <b>ichido dake</b> (එක වතාවක් විතරයි), '
        '<b>nikai</b> (දෙපාරක්), <b>yoku</b> (නිතරම).')

_PAT = [[("はい、","Hai,"),"BLANK",("あります","arimasu",True)],
        [("いいえ、","Iie,"),"BLANK",("ありません","arimasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{NIH}に {ITT}ことが ありますか。","Nihon ni itta koto ga arimasu ka.","Have you ever been to Japan?","ඔබ ජපානයට ගිහින් තියෙනවාද?"),
         ("はい、あります。","Hai, arimasu.","Yes, I have.","ඔව්, තියෙනවා.")),
  ("QA", (f"{NHG}で {TEG}を {KAIT}ことが ありますか。","Nihongo de tegami wo kaita koto ga arimasu ka.","Have you ever written a letter in Japanese?","ඔබ ජපන් භාෂාවෙන් ලිපියක් ලියලා තියෙනවාද?"),
         ("いいえ、ありません。","Iie, arimasen.","No, I haven't.","නැහැ, නැහැ.")),
  ("QA", (f"{NIH}の {HON}を {YOND}ことが ありますか。","Nihon no hon wo yonda koto ga arimasu ka.","Have you ever read a Japanese book?","ඔබ ජපන් පොතක් කියවලා තියෙනවාද?"),
         (f"はい、{NIK} あります。","Hai, nikai arimasu.","Yes, twice.","ඔව්, දෙපාරක්.")),
  ("QA", (f"{NIHJ}と {HANT}ことが ありますか。","Nihon-jin to hanashita koto ga arimasu ka.","Have you ever talked with a Japanese person?","ඔබ ජපන් ජාතිකයෙක් එක්ක කතා කරලා තියෙනවාද?"),
         ("はい、よく あります。","Hai, yoku arimasu.","Yes, often.","ඔව්, නිතරම.")),
  ("QA", (f"そばを {TABT}ことが ありますか。","Soba wo tabeta koto ga arimasu ka.","Have you ever eaten soba?","ඔබ සෝබා කාලා තියෙනවාද?"),
         (f"いいえ、{ICH}も ありません。","Iie, ichido mo arimasen.","No, never.","නැහැ, කවදාවත් නැහැ.")),
  ("QA", (f"アルバイトを した ことが ありますか。","Arubaito wo shita koto ga arimasu ka.","Have you ever worked part-time?","ඔබ අර්ධකාලීන රැකියාවක් කරලා තියෙනවාද?"),
         (f"はい、{ICH}だけ あります。","Hai, ichido dake arimasu.","Yes, only once.","ඔව්, එක වතාවක් විතරයි.")),
  ("QA", (f"{NIH}の {GAK}で {BEN}した ことが ありますか。","Nihon no gakkou de benkyou shita koto ga arimasu ka.","Have you ever studied at a school in Japan?","ඔබ ජපානයේ පාසලක ඉගෙන ගෙන තියෙනවාද?"),
         ("いいえ、ありません。","Iie, arimasen.","No, I haven't.","නැහැ, නැහැ.")),
  ("QA", (f"{HIK}に {NOTT}ことが ありますか。","Hikouki ni notta koto ga arimasu ka.","Have you ever been on a plane?","ඔබ ගුවන් යානයක නැගලා තියෙනවාද?"),
         ("はい、あります。","Hai, arimasu.","Yes, I have.","ඔව්, තියෙනවා.")),
  ("QA", (f"{YAM}に {NOBT}ことが ありますか。","Yama ni nobotta koto ga arimasu ka.","Have you ever climbed a mountain?","ඔබ කන්දකට නැගලා තියෙනවාද?"),
         ("いいえ、ありません。","Iie, arimasen.","No, I haven't.","නැහැ, නැහැ.")),
]

P13A = dict(
  no="17", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、あります。　／　いいえ、ありません。","Hai, arimasu. / Iie, arimasen.",
         "Yes, I have. / No, I haven't.","ඔව්, තියෙනවා. / නැහැ, නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P13A2 = dict(
  no="17", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P13A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{ICH}も ありません。","Ichido mo arimasen.","Never, not even once.","කවදාවත් නැහැ."),
    (f"{ICH}だけ あります。","Ichido dake arimasu.","Only once.","එක වතාවක් විතරයි."),
    ("よく あります。","Yoku arimasu.","Often.","නිතරම."),
    ("ぜひ したいです。","Zehi shitai desu.","I'd love to try it.","අනිවාර්යයෙන් කරන්න ඕන."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P13,"p17_1_keiken"), (P13N,"p17_2_negative"), (P13Q,"p17_3_question"),
                    (P13A,"p17_4_answer"), (P13A2,"p17_5_answer2")]:
        render(p, stem)
