from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TAK = r("高","たか")+"い"
OOK = r("大","おお")+"きい"
NIC = r("日","にち")+"よう"+r("日","び")

# ---------------------------------------------------------------- 07-1 基本
P4 = dict(
  no="07", tag=None,
  title_jp="〜は …です（2）",
  title_ro='〜 wa … desu &nbsp;|&nbsp; 〜 is … &nbsp;|&nbsp; <span class="si">〜 … යි</span>',
  basic=("この りんご は あまい です。","Kono ringo wa amai desu.",
         "This apple is sweet.","මේ ඇපල් එක පැණි රසයි."),
  use=(f'{r("形","かたち")}は 06と{r("同","おな")}じですが、{r("主語","しゅ ご")}が「{r("物","もの")}」や「{r("事柄","こと がら")}」のときです。'
       f'めいしの{r("前","まえ")}に この・その・あの をつけて、どれかを はっきりさせます。',
       'The shape is the same as pattern 06, but here the subject is a <b>thing</b> or a <b>fact</b>. '
       'Put <b>kono</b> (near me), <b>sono</b> (near you) or <b>ano</b> (over there) before the noun. '
       'For places use <b>koko / soko / asoko</b>.',
       'හැඩය 06 වගේමයි, නමුත් මෙතන උක්තය <b>දෙයක්</b> හෝ <b>කාරණයක්</b>. '
       'නාම පදයට කලින් <b>kono</b> = මේ, <b>sono</b> = ඔය, <b>ano</b> = අර දාන්න. '
       'ස්ථාන නම් <b>koko</b> = මෙතන, <b>soko</b> = ඔතන, <b>asoko</b> = අතන.'),
  pattern=[[("〜は","~ wa"),"BLANK",("です","desu")],
           "NOTE:この = මේ　/　その = ඔය　/　あの = අර　　＋　めいし　　　　ここ = මෙතන　/　そこ = ඔතන　/　あそこ = අතන"],
  examples=[
    ("この りんご は あまい です。","Kono ringo wa amai desu.","This apple is sweet.","මේ ඇපල් එක පැණි රසයි."),
    ("その にもつ は おもい です。","Sono nimotsu wa omoi desu.","That luggage is heavy.","ඔය බඩු මල්ල බරයි."),
    (f"あの ビル は {TAK} です。","Ano biru wa takai desu.","That building is tall.","අර ගොඩනැගිල්ල උසයි."),
    ("この ペン は やすい です。","Kono pen wa yasui desu.","This pen is cheap.","මේ පෑන ලාභයි."),
    ("その スープ は あつい です。","Sono suupu wa atsui desu.","That soup is hot.","ඔය සුප් එක උණුසුම්."),
    ("ここ は べんり です。","Koko wa benri desu.","This place is convenient.","මෙතන පහසුයි."),
    (f"やすみ は {NIC} です。","Yasumi wa nichiyoubi desu.","The holiday is Sunday.","නිවාඩුව ඉරිදා."),
  ],
  foot="〜は …です（2）",
)

# ---------------------------------------------------------------- 07-2 否定
P4N = dict(
  no="07", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜は …く ありません / …く ない（です）",
  title_ro='〜 wa … ku arimasen / … ku nai desu &nbsp;|&nbsp; 〜 is not … &nbsp;|&nbsp; '
           '<span class="si">〜 … නැහැ</span>',
  basic=("この りんご は あまく ありません。","Kono ringo wa amaku arimasen.",
         "This apple is not sweet.","මේ ඇපල් එක පැණි රස නැහැ."),
  use=(f'「い」でおわる ことばの{r("否定","ひ てい")}には、2つの{r("言","い")}い{r("方","かた")}があります。'
       f'「く ありません」は ていねい、「く ない（です）」は{r("会話","かい わ")}で よく{r("使","つか")}います。{r("意味","い み")}は{r("同","おな")}じです。',
       'An <b>-i</b> word has two negative forms. <b>ku arimasen</b> is polite; '
       '<b>ku nai (desu)</b> is common in conversation. The meaning is the same.',
       '<b>-i</b> වචනයකට නිශේධන ආකාර දෙකක් තියෙනවා. <b>ku arimasen</b> වඩා ආචාරශීලීයි; '
       '<b>ku nai (desu)</b> කතාබහේදී බහුලයි. අර්ථය එකයි.'),
  pattern=[
    "NOTE:「い」でおわる ことば　/　i-adjectives",
    [("たかい","takai"),"TO",("たかく ありません","takaku arimasen",True)],
    [("たかい","takai"),"TO",("たかく ない（です）","takaku nai desu",True)],
    "NOTE:な けいようし・めいし　/　na-adjectives &amp; nouns",
    [("べんり","benri"),"TO",("べんり では ありません","benri dewa arimasen",True)],
  ],
  examples=[
    ("この りんご は あまく ありません。","Kono ringo wa amaku arimasen.","This apple is not sweet.","මේ ඇපල් එක පැණි රස නැහැ."),
    ("その にもつ は おもく ありません。","Sono nimotsu wa omoku arimasen.","That luggage is not heavy.","ඔය බඩු මල්ල බර නැහැ."),
    (f"あの ビル は {r('高','たか')}く ありません。","Ano biru wa takaku arimasen.","That building is not tall.","අර ගොඩනැගිල්ල උස නැහැ."),
    ("この ペン は やすく ない です。","Kono pen wa yasuku nai desu.","This pen is not cheap.","මේ පෑන ලාභ නැහැ."),
    ("その スープ は あつく ない です。","Sono suupu wa atsuku nai desu.","That soup is not hot.","ඔය සුප් එක උණුසුම් නැහැ."),
    ("ここ は べんり では ありません。","Koko wa benri dewa arimasen.","This place is not convenient.","මෙතන පහසු නැහැ."),
    (f"やすみ は {NIC} では ありません。","Yasumi wa nichiyoubi dewa arimasen.","The holiday is not Sunday.","නිවාඩුව ඉරිදා නෙවෙයි."),
  ],
  foot="〜は …く ありません",
)

# ---------------------------------------------------------------- 07-3 疑問
P4Q = dict(
  no="07", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜は …ですか？",
  title_ro='〜 wa … desu ka &nbsp;|&nbsp; Is 〜 …? &nbsp;|&nbsp; <span class="si">〜 … ද?</span>',
  basic=("この りんご は あまい ですか。","Kono ringo wa amai desu ka.",
         "Is this apple sweet?","මේ ඇපල් එක පැණි රසද?"),
  use=(f'ことばの{r("形","かたち")}は{r("変","か")}えず、「です」のうしろに「か」をつけるだけです。'
       f'{r("相手","あい て")}の{r("近","ちか")}くにある{r("物","もの")}を{r("聞","き")}くときは「その」「そこ」を{r("使","つか")}います。',
       'The word does not change — just add <b>ka</b> after <b>desu</b>. '
       'When you ask about something near the listener, use <b>sono</b> or <b>soko</b>.',
       'වචනය වෙනස් වෙන්නේ නැහැ — <b>desu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       'අහන කෙනා ළඟ තියෙන දෙයක් ගැන අහනවා නම් <b>sono</b> හෝ <b>soko</b> භාවිතා කරන්න.'),
  pattern=[[("〜は","~ wa"),"BLANK",("です","desu")],
           "ARROW",
           [("〜は","~ wa"),"BLANK",("ですか？","desu ka",True)]],
  examples=[
    ("この りんご は あまい ですか。","Kono ringo wa amai desu ka.","Is this apple sweet?","මේ ඇපල් එක පැණි රසද?"),
    ("その にもつ は おもい ですか。","Sono nimotsu wa omoi desu ka.","Is that luggage heavy?","ඔය බඩු මල්ල බරද?"),
    (f"あの ビル は {TAK} ですか。","Ano biru wa takai desu ka.","Is that building tall?","අර ගොඩනැගිල්ල උසද?"),
    ("この ペン は やすい ですか。","Kono pen wa yasui desu ka.","Is this pen cheap?","මේ පෑන ලාභද?"),
    ("その スープ は あつい ですか。","Sono suupu wa atsui desu ka.","Is that soup hot?","ඔය සුප් එක උණුසුම්ද?"),
    ("ここ は べんり ですか。","Koko wa benri desu ka.","Is this place convenient?","මෙතන පහසුද?"),
    (f"やすみ は {NIC} ですか。","Yasumi wa nichiyoubi desu ka.","Is the holiday Sunday?","නිවාඩුව ඉරිදාද?"),
  ],
  foot="〜は …ですか？",
)

# ---------------------------------------------------------------- 07-4 / 07-5 答え方
_USE = (f'「はい」「いいえ」のあとに、もういちど{r("文","ぶん")}を いいます。'
        f'いいえのときは「く ありません」「く ない です」「では ありません」を{r("使","つか")}います。',
        'After <b>hai</b> or <b>iie</b>, say the sentence again. '
        'For <b>iie</b>, use <b>ku arimasen</b>, <b>ku nai desu</b> or <b>dewa arimasen</b>.',
        '<b>hai</b> හෝ <b>iie</b> කියලා පස්සේ වාක්‍යය ආයෙත් කියන්න. '
        '<b>iie</b> නම් <b>ku arimasen</b>, <b>ku nai desu</b> හෝ <b>dewa arimasen</b> භාවිතා කරන්න.')

_PAT = [[("はい、","Hai,"),"BLANK",("です","desu",True)],
        [("いいえ、","Iie,"),"BLANK",("く ありません / では ありません","ku arimasen / dewa arimasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", ("この りんご は あまい ですか。","Kono ringo wa amai desu ka.","Is this apple sweet?","මේ ඇපල් එක පැණි රසද?"),
         ("はい、あまい です。","Hai, amai desu.","Yes, it is sweet.","ඔව්, පැණි රසයි.")),
  ("QA", ("その にもつ は おもい ですか。","Sono nimotsu wa omoi desu ka.","Is that luggage heavy?","ඔය බඩු මල්ල බරද?"),
         ("いいえ、おもく ありません。","Iie, omoku arimasen.","No, it is not heavy.","නැහැ, බර නැහැ.")),
  ("QA", (f"あの ビル は {TAK} ですか。","Ano biru wa takai desu ka.","Is that building tall?","අර ගොඩනැගිල්ල උසද?"),
         (f"はい、とても {TAK} です。","Hai, totemo takai desu.","Yes, it is very tall.","ඔව්, ගොඩක් උසයි.")),
  ("QA", ("この ペン は やすい ですか。","Kono pen wa yasui desu ka.","Is this pen cheap?","මේ පෑන ලාභද?"),
         ("いいえ、やすく ない です。","Iie, yasuku nai desu.","No, it is not cheap.","නැහැ, ලාභ නැහැ.")),
  ("QA", ("その スープ は あつい ですか。","Sono suupu wa atsui desu ka.","Is that soup hot?","ඔය සුප් එක උණුසුම්ද?"),
         ("はい、あつい です。","Hai, atsui desu.","Yes, it is hot.","ඔව්, උණුසුම්.")),
  ("QA", ("ここ は べんり ですか。","Koko wa benri desu ka.","Is this place convenient?","මෙතන පහසුද?"),
         ("いいえ、べんり では ありません。","Iie, benri dewa arimasen.","No, it is not convenient.","නැහැ, පහසු නැහැ.")),
  ("QA", (f"やすみ は {NIC} ですか。","Yasumi wa nichiyoubi desu ka.","Is the holiday Sunday?","නිවාඩුව ඉරිදාද?"),
         (f"はい、{NIC} です。","Hai, nichiyoubi desu.","Yes, it is Sunday.","ඔව්, ඉරිදා.")),
  ("QA", (f"その にもつ は {OOK} ですか。","Sono nimotsu wa ookii desu ka.","Is that luggage big?","ඔය බඩු මල්ල ලොකුද?"),
         (f"いいえ、{r('大','おお')}きく ありません。","Iie, ookiku arimasen.","No, it is not big.","නැහැ, ලොකු නැහැ.")),
  ("QA", ("あの ビル は ゆうめい ですか。","Ano biru wa yuumei desu ka.","Is that building famous?","අර ගොඩනැගිල්ල ප්‍රසිද්ධද?"),
         ("はい、ゆうめい です。","Hai, yuumei desu.","Yes, it is famous.","ඔව්, ප්‍රසිද්ධයි.")),
]

P4A = dict(
  no="07", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=("はい、あまい です。　／　いいえ、あまく ありません。",
         "Hai, amai desu. / Iie, amaku arimasen.",
         "Yes, it is sweet. / No, it is not sweet.",
         "ඔව්, පැණි රසයි. / නැහැ, පැණි රස නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P4A2 = dict(
  no="07", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P4A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("そうですね。","Sou desu ne.","Let me see. / Well…","එහෙමද… / හොඳයි…"),
    ("はい、すこし。","Hai, sukoshi.","Yes, a little.","ඔව්, ටිකක්."),
    ("いいえ、あまり。","Iie, amari.","No, not really.","නැහැ, එච්චර නැහැ."),
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P4,"p07_1_wa_desu2"), (P4N,"p07_2_negative"), (P4Q,"p07_3_question"),
                    (P4A,"p07_4_answer"), (P4A2,"p07_5_answer2")]:
        render(p, stem)
