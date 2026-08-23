from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
GAK  = r("学校","がっ こう")
CHI  = r("近","ちか")+"く"
SUN  = r("住","す")+"んで"
ANI  = r("兄","あに")
KAI  = r("会社","かい しゃ")
HAT  = r("働","はたら")+"いて"
SEN  = r("先生","せん せい")
NAM  = r("名前","な まえ")
SHI  = r("知","し")+"って"
SHIM = r("知","し")+"りません"
OBO  = r("覚","おぼ")+"えて"
NHG  = r("日本語","に ほん ご")
KYO  = r("教科書","きょう か しょ")
MOT  = r("持","も")+"って"
TOM  = r("友","とも")+"だち"
KEK  = r("結婚","けっ こん")
KSH  = r("教室","きょう しつ")
KIT  = r("来","き")+"て"
KANJ = r("漢字","かん じ")
KARE = r("彼","かれ")

# ---------------------------------------------------------------- 16-1 基本
P10 = dict(
  no="16", tag=None,
  title_jp="〜しています（2）",
  title_ro='〜 shite imasu &nbsp;|&nbsp; a continuing state &nbsp;|&nbsp; '
           '<span class="si">〜 වී තිබෙනවා</span>',
  basic=(f"{W}は {GAK}の {CHI}に {SUN}います。","Watashi wa gakkou no chikaku ni sunde imasu.",
         "I live near the school.","මම පාසල ළඟ ජීවත් වෙනවා."),
  use=(f'15と{r("同","おな")}じ かたちですが、「{r("今","いま")} しているところ」ではなく'
       f'「ずっと つづいている じょうたい」を あらわします。'
       f'{SUN[:-2]}む・{SHI[:-2]}る・{MOT[:-2]}つ・{KEK}する などは、いつも この かたちで{r("使","つか")}います。',
       'The shape is the same as pattern 15, but here it shows a <b>continuing state</b>, not an '
       'action happening right now. Verbs like <b>sumu</b> (live), <b>shiru</b> (know), '
       '<b>motsu</b> (have) and <b>kekkon suru</b> (marry) are normally used in this form.',
       'හැඩය 15 වගේමයි, නමුත් මෙතන පෙන්නන්නේ දැන් වෙන දෙයක් නෙවෙයි — <b>දිගටම පවතින තත්ත්වයක්</b>. '
       '<b>sumu</b> (ජීවත් වෙනවා), <b>shiru</b> (දන්නවා), <b>motsu</b> (තියෙනවා), '
       '<b>kekkon suru</b> (විවාහ වෙනවා) වගේ ඒවා හැමවිටම මේ ආකාරයෙන් භාවිතා වෙනවා.'),
  pattern=["NOTE:15 = 今 しているところ　/　16 = ずっと つづいている じょうたい",
           [("〜は","~ wa"),"BLANK",("しています","shite imasu")],
           f"NOTE:{SUN}います　/　{SHI}います　/　{MOT}います　/　{KEK}して います　/　{HAT}います"],
  examples=[
    (f"{W}は {GAK}の {CHI}に {SUN}います。","Watashi wa gakkou no chikaku ni sunde imasu.","I live near the school.","මම පාසල ළඟ ජීවත් වෙනවා."),
    (f"{ANI}は {KAI}で {HAT}います。","Ani wa kaisha de hataraite imasu.","My older brother works at a company.","මගේ අයියා සමාගමක වැඩ කරනවා."),
    (f"{W}は {SEN}の {NAM}を {SHI}います。","Watashi wa sensei no namae wo shitte imasu.","I know the teacher's name.","මම ගුරුතුමාගේ නම දන්නවා."),
    (f"{W}は その ことばを {OBO}います。","Watashi wa sono kotoba wo oboete imasu.","I remember that word.","මට ඒ වචනය මතකයි."),
    (f"{W}は {NHG}の {KYO}を {MOT}います。","Watashi wa nihongo no kyoukasho wo motte imasu.","I have a Japanese textbook.","මට ජපන් භාෂා පෙළපොතක් තියෙනවා."),
    (f"{TOM}は {KEK}しています。","Tomodachi wa kekkon shite imasu.","My friend is married.","මගේ යාළුවා විවාහකයි."),
    (f"{SEN}は もう {KSH}に {KIT}います。","Sensei wa mou kyoushitsu ni kite imasu.","The teacher has already come to the classroom.","ගුරුතුමා දැනටමත් පන්ති කාමරයට ඇවිත් ඉන්නවා."),
  ],
  foot="〜しています（2）",
)

# ---------------------------------------------------------------- 16-2 否定
P10N = dict(
  no="16", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜していません",
  title_ro='〜 shite imasen &nbsp;|&nbsp; not in that state &nbsp;|&nbsp; '
           '<span class="si">〜 වී නැහැ</span>',
  basic=(f"{W}は {GAK}の {CHI}に {SUN}いません。","Watashi wa gakkou no chikaku ni sunde imasen.",
         "I do not live near the school.","මම පාසල ළඟ ජීවත් වෙන්නේ නැහැ."),
  use=(f'かたちは 15と{r("同","おな")}じ「〜て いません」です。'
       f'ただし「{SHI}います」だけは{r("特別","とく べつ")}で、{r("否定","ひ てい")}は「{SHIM}」です。'
       f'「{SHI}いません」とは{r("言","い")}いません。ここは よく まちがえます。',
       'The form is the same <b>〜 te imasen</b> as in pattern 15. '
       'But <b>shitte imasu</b> is special: its negative is <b>shirimasen</b>, '
       'NOT <b>shitte imasen</b>. Learners get this wrong very often.',
       'ආකාරය 15 හි <b>〜 te imasen</b> එකමයි. '
       'නමුත් <b>shitte imasu</b> විශේෂයි — එහි නිශේධනය <b>shirimasen</b>, '
       '<b>shitte imasen</b> නෙවෙයි. මේක ගොඩක් අය වැරදි කරන තැනක්.'),
  pattern=[[("〜て います","~ te imasu"),"TO",("〜て いません","~ te imasen",True)],
           f"NOTE:【 ちゅうい 】「{SHI}います」の 否定だけ ちがいます　/　careful — one exception",
           [(f"{SHI}います","shitte imasu"),"TO",(f"{SHIM}","shirimasen",True)]],
  examples=[
    (f"{W}は {GAK}の {CHI}に {SUN}いません。","Watashi wa gakkou no chikaku ni sunde imasen.","I do not live near the school.","මම පාසල ළඟ ජීවත් වෙන්නේ නැහැ."),
    (f"{ANI}は {KAI}で {HAT}いません。","Ani wa kaisha de hataraite imasen.","My older brother does not work at a company.","මගේ අයියා සමාගමක වැඩ කරන්නේ නැහැ."),
    (f"{W}は {SEN}の {NAM}を {SHIM}。","Watashi wa sensei no namae wo shirimasen.","I do not know the teacher's name.","මම ගුරුතුමාගේ නම දන්නේ නැහැ."),
    (f"{W}は その ことばを {OBO}いません。","Watashi wa sono kotoba wo oboete imasen.","I do not remember that word.","මට ඒ වචනය මතක නැහැ."),
    (f"{W}は {NHG}の {KYO}を {MOT}いません。","Watashi wa nihongo no kyoukasho wo motte imasen.","I do not have a Japanese textbook.","මට ජපන් භාෂා පෙළපොතක් නැහැ."),
    (f"{TOM}は {KEK}していません。","Tomodachi wa kekkon shite imasen.","My friend is not married.","මගේ යාළුවා විවාහක නැහැ."),
    (f"{SEN}は まだ {KSH}に {KIT}いません。","Sensei wa mada kyoushitsu ni kite imasen.","The teacher has not come to the classroom yet.","ගුරුතුමා තාම පන්ති කාමරයට ඇවිත් නැහැ."),
  ],
  foot="〜していません",
)

# ---------------------------------------------------------------- 16-3 疑問
P10Q = dict(
  no="16", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜していますか？",
  title_ro='〜 shite imasu ka &nbsp;|&nbsp; Do you 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 වී තිබෙනවාද?</span>',
  basic=(f"あなたは {GAK}の {CHI}に {SUN}いますか。","Anata wa gakkou no chikaku ni sunde imasu ka.",
         "Do you live near the school?","ඔබ පාසල ළඟ ජීවත් වෙනවාද?"),
  use=(f'「います」のうしろに「か」をつけるだけです。'
       f'「{SHI}いますか」「{MOT}いますか」は、{r("毎日","まい にち")}の{r("会話","かい わ")}で とても よく{r("使","つか")}います。',
       'Just add <b>ka</b> after <b>imasu</b>. '
       '<b>Shitte imasu ka</b> ("Do you know…?") and <b>motte imasu ka</b> ("Do you have…?") '
       'are used constantly in everyday conversation.',
       '<b>imasu</b> එකට පස්සේ <b>ka</b> දාන්න විතරයි. '
       '<b>Shitte imasu ka</b> ("දන්නවාද?") සහ <b>motte imasu ka</b> ("තියෙනවාද?") '
       'දෛනික කතාබහේදී නිතරම භාවිතා වෙනවා.'),
  pattern=[[("〜は","~ wa"),"BLANK",("しています","shite imasu")],
           "ARROW",
           [("〜は","~ wa"),"BLANK",("していますか？","shite imasu ka",True)]],
  examples=[
    (f"あなたは {GAK}の {CHI}に {SUN}いますか。","Anata wa gakkou no chikaku ni sunde imasu ka.","Do you live near the school?","ඔබ පාසල ළඟ ජීවත් වෙනවාද?"),
    (f"{KARE}は {KAI}で {HAT}いますか。","Kare wa kaisha de hataraite imasu ka.","Does he work at a company?","ඔහු සමාගමක වැඩ කරනවාද?"),
    (f"{SEN}の {NAM}を {SHI}いますか。","Sensei no namae wo shitte imasu ka.","Do you know the teacher's name?","ඔබ ගුරුතුමාගේ නම දන්නවාද?"),
    (f"その ことばを {OBO}いますか。","Sono kotoba wo oboete imasu ka.","Do you remember that word?","ඔබට ඒ වචනය මතකද?"),
    (f"{NHG}の {KYO}を {MOT}いますか。","Nihongo no kyoukasho wo motte imasu ka.","Do you have a Japanese textbook?","ඔබට ජපන් භාෂා පෙළපොතක් තියෙනවාද?"),
    (f"{TOM}は {KEK}していますか。","Tomodachi wa kekkon shite imasu ka.","Is your friend married?","ඔබේ යාළුවා විවාහකද?"),
    (f"{SEN}は もう {KIT}いますか。","Sensei wa mou kite imasu ka.","Has the teacher come yet?","ගුරුතුමා ඇවිත් ඉන්නවාද?"),
  ],
  foot="〜していますか？",
)

# ---------------------------------------------------------------- 16-4 / 16-5 答え方
_USE = (f'「はい、〜て います。」「いいえ、〜て いません。」と{r("答","こた")}えます。'
        f'「{SHI}いますか」だけは「いいえ、{SHIM}。」と{r("答","こた")}えます。',
        'Answer with <b>Hai, 〜 te imasu</b> or <b>Iie, 〜 te imasen</b>. '
        'Only for <b>shitte imasu ka</b>, the answer is <b>Iie, shirimasen</b>.',
        '<b>Hai, 〜 te imasu</b> හෝ <b>Iie, 〜 te imasen</b> කියලා උත්තර දෙන්න. '
        '<b>shitte imasu ka</b> එකට විතරක් <b>Iie, shirimasen</b> කියන්න.')

_PAT = [[("はい、","Hai,"),"BLANK",("て います","te imasu",True)],
        [("いいえ、","Iie,"),"BLANK",("て いません","te imasen",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{GAK}の {CHI}に {SUN}いますか。","Gakkou no chikaku ni sunde imasu ka.","Do you live near the school?","ඔබ පාසල ළඟ ජීවත් වෙනවාද?"),
         (f"はい、{SUN}います。","Hai, sunde imasu.","Yes, I do.","ඔව්, ජීවත් වෙනවා.")),
  ("QA", (f"{KARE}は {KAI}で {HAT}いますか。","Kare wa kaisha de hataraite imasu ka.","Does he work at a company?","ඔහු සමාගමක වැඩ කරනවාද?"),
         (f"いいえ、{HAT}いません。","Iie, hataraite imasen.","No, he doesn't.","නැහැ, වැඩ කරන්නේ නැහැ.")),
  ("QA", (f"{SEN}の {NAM}を {SHI}いますか。","Sensei no namae wo shitte imasu ka.","Do you know the teacher's name?","ඔබ ගුරුතුමාගේ නම දන්නවාද?"),
         (f"いいえ、{SHIM}。","Iie, shirimasen.","No, I don't know it.","නැහැ, දන්නේ නැහැ.")),
  ("QA", (f"その ことばを {OBO}いますか。","Sono kotoba wo oboete imasu ka.","Do you remember that word?","ඔබට ඒ වචනය මතකද?"),
         (f"はい、{OBO}います。","Hai, oboete imasu.","Yes, I do.","ඔව්, මතකයි.")),
  ("QA", (f"{NHG}の {KYO}を {MOT}いますか。","Nihongo no kyoukasho wo motte imasu ka.","Do you have a Japanese textbook?","ඔබට ජපන් භාෂා පෙළපොතක් තියෙනවාද?"),
         (f"はい、{MOT}います。","Hai, motte imasu.","Yes, I do.","ඔව්, තියෙනවා.")),
  ("QA", (f"{TOM}は {KEK}していますか。","Tomodachi wa kekkon shite imasu ka.","Is your friend married?","ඔබේ යාළුවා විවාහකද?"),
         (f"いいえ、{KEK}していません。","Iie, kekkon shite imasen.","No, he isn't.","නැහැ, විවාහක නැහැ.")),
  ("QA", (f"{SEN}は もう {KIT}いますか。","Sensei wa mou kite imasu ka.","Has the teacher come yet?","ගුරුතුමා ඇවිත් ඉන්නවාද?"),
         (f"はい、もう {KIT}います。","Hai, mou kite imasu.","Yes, he is already here.","ඔව්, දැනටමත් ඇවිත් ඉන්නවා.")),
  ("QA", (f"この {KANJ}を {SHI}いますか。","Kono kanji wo shitte imasu ka.","Do you know this kanji?","ඔබ මේ කන්ජි අකුර දන්නවාද?"),
         (f"はい、{SHI}います。","Hai, shitte imasu.","Yes, I know it.","ඔව්, දන්නවා.")),
  ("QA", (f"ペンを {MOT}いますか。","Pen wo motte imasu ka.","Do you have a pen?","ඔබට පෑනක් තියෙනවාද?"),
         (f"いいえ、{MOT}いません。","Iie, motte imasen.","No, I don't.","නැහැ, නැහැ.")),
]

P10A = dict(
  no="16", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=(f"はい、{SHI}います。　／　いいえ、{SHIM}。",
         "Hai, shitte imasu. / Iie, shirimasen.",
         "Yes, I know. / No, I don't know.",
         "ඔව්, දන්නවා. / නැහැ, දන්නේ නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P10A2 = dict(
  no="16", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P10A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    (f"{SHI}います。","Shitte imasu.","I know it.","මම දන්නවා."),
    (f"{SHIM}。","Shirimasen.","I don't know.","මම දන්නේ නැහැ."),
    (f"{r('忘','わす')}れました。","Wasuremashita.","I've forgotten.","මට අමතක වුණා."),
    (f"{MOT}いません。","Motte imasen.","I don't have it.","මට නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P10,"p16_1_joutai"), (P10N,"p16_2_negative"), (P10Q,"p16_3_question"),
                    (P10A,"p16_4_answer"), (P10A2,"p16_5_answer2")]:
        render(p, stem)
