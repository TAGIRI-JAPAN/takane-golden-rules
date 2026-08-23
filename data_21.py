from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NAN  = r("何","なん")
NANI = r("何","なに")
NAM  = r("名前","な まえ")
IMI  = r("意味","い み")
YOT  = r("予定","よ てい")
MIS  = r("店","みせ")
SHU  = r("宿題","しゅく だい")
HON  = r("本","ほん")
NICH = r("日","にち")+"よう"+r("日","び")
IMA  = r("今","いま")
TABT = r("食","た")+"べたい"
NIH  = r("日本","に ほん")
KSH  = r("教室","きょう しつ")
YON  = r("読","よ")+"んで"
BEN  = r("勉強","べん きょう")
SHUM = r("週末","しゅう まつ")
JUG  = r("授業","じゅ ぎょう")
SSH  = r("先週","せん しゅう")
KES  = r("今朝","け さ")
SEN  = r("先生","せん せい")
HAN  = r("話","はな")+"し"
JIS  = r("辞書","じ しょ")
KANJ = r("漢字","かん じ")
REN  = r("練習","れん しゅう")
BUN  = r("文法","ぶん ぽう")
TOM  = r("友","とも")+"だち"
KIN  = r("昨日","きのう")

# ---------------------------------------------------------------- 21-1 基本
P16 = dict(
  no="21", tag=None,
  title_jp=f"〜は {NAN}ですか？",
  title_ro='〜 wa nan desu ka &nbsp;|&nbsp; What is 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 මොකක්ද?</span>',
  basic=(f"これは {NAN}ですか。","Kore wa nan desu ka.",
         "What is this?","මේක මොකක්ද?"),
  use=(f'「{NANI}」は わからない ものを たずねる ことばです。'
       f'「{NAN}の＋めいし」で「どんな しゅるいか」を たずねられます。'
       f'{r("読","よ")}み{r("方","かた")}に{r("注意","ちゅう い")}：「{NAN}ですか」は なん、「{NANI}を」は なに です。',
       '<b>nani</b> asks about something you do not know. '
       '<b>nan no</b> + noun asks what kind of thing it is. '
       'Careful with the reading: 何 is <b>nan</b> in <b>nan desu ka</b>, but <b>nani</b> in <b>nani wo</b>.',
       '<b>nani</b> කියන්නේ නොදන්නා දෙයක් ගැන අහන එක — <b>nan desu ka</b> = මොකක්ද? '
       '<b>nan no</b> ＋ නාම පදය කියලා මොන වර්ගයේද කියලා අහන්න පුළුවන්. '
       'කියවීම ගැන පරිස්සම් වෙන්න: 何 එක <b>nan desu ka</b> වලදී <b>nan</b>, <b>nani wo</b> වලදී <b>nani</b>.'),
  pattern=[[("〜は","~ wa"),(f"{NAN}ですか？","nan desu ka",True)],
           [("〜は","~ wa"),(f"{NAN}の ＋ めいし ですか？","nan no + noun desu ka",True)],
           f"NOTE:{r('読','よ')}み{r('方','かた')}：{NAN}ですか＝なん　/　{NANI}を＝なに"],
  examples=[
    (f"これは {NAN}ですか。","Kore wa nan desu ka.","What is this?","මේක මොකක්ද?"),
    (f"あなたの {NAM}は {NAN}ですか。","Anata no namae wa nan desu ka.","What is your name?","ඔබේ නම මොකක්ද?"),
    (f"この ことばの {IMI}は {NAN}ですか。","Kono kotoba no imi wa nan desu ka.","What is the meaning of this word?","මේ වචනයේ තේරුම මොකක්ද?"),
    (f"あしたの {YOT}は {NAN}ですか。","Ashita no yotei wa nan desu ka.","What are your plans for tomorrow?","හෙට ඔබේ සැලසුම මොකක්ද?"),
    (f"あの {MIS}の {NAM}は {NAN}ですか。","Ano mise no namae wa nan desu ka.","What is the name of that shop?","අර කඩේ නම මොකක්ද?"),
    (f"きょうの {SHU}は {NAN}ですか。","Kyou no shukudai wa nan desu ka.","What is today's homework?","අද ගෙදර වැඩ මොකක්ද?"),
    (f"これは {NAN}の {HON}ですか。","Kore wa nan no hon desu ka.","What kind of book is this?","මේක මොන වගේ පොතක්ද?"),
  ],
  foot="〜は 何ですか？",
)

# ---------------------------------------------------------------- 21-2 応用①
P16B = dict(
  no="21", tag="応用 ①　何を 〜しますか？ / WITH VERBS",
  title_jp=f"{NANI}を 〜しますか？",
  title_ro='nani wo 〜 shimasu ka &nbsp;|&nbsp; What do you 〜? &nbsp;|&nbsp; '
           '<span class="si">මොකද 〜 කරන්නේ?</span>',
  basic=(f"{IMA} {NANI}を していますか。","Ima nani wo shite imasu ka.",
         "What are you doing now?","දැන් මොකද කරන්නේ?"),
  use=(f'11・12・15で ならった かたちの{r("前","まえ")}に「{NANI}を」を つけるだけです。あたらしい ルールは ありません。',
       'Just put <b>nani wo</b> in front of the forms you learned in patterns 11, 12 and 15. '
       'There is no new rule at all.',
       '11, 12, 15 වලදී ඉගෙන ගත්ත ආකාරවලට ඉස්සරහින් <b>nani wo</b> දාන්න විතරයි. අලුත් නීතියක් නැහැ.'),
  pattern=[[(f"{NANI}を","nani wo",True),("しますか？","shimasu ka")],
           [(f"{NANI}を","nani wo",True),("していますか？","shite imasu ka")],
           [(f"{NANI}を","nani wo",True),("したいですか？","shitai desu ka")]],
  examples=[
    (f"{NICH}に {NANI}を しますか。","Nichiyoubi ni nani wo shimasu ka.","What do you do on Sundays?","ඉරිදාට ඔබ මොකද කරන්නේ?"),
    (f"{IMA} {NANI}を していますか。","Ima nani wo shite imasu ka.","What are you doing now?","දැන් මොකද කරන්නේ?"),
    (f"ばんごはんに {NANI}を {TABT}ですか。","Bangohan ni nani wo tabetai desu ka.","What do you want to eat for dinner?","රාත්‍රී කෑමට මොනවද කන්න ඕන?"),
    (f"{NIH}で {NANI}を したいですか。","Nihon de nani wo shitai desu ka.","What do you want to do in Japan?","ජපානයේ මොකද කරන්න ඕන?"),
    (f"{KSH}で {NANI}を {YON}いますか。","Kyoushitsu de nani wo yonde imasu ka.","What are you reading in the classroom?","පන්ති කාමරයේ මොකද කියවන්නේ?"),
    (f"あした {NANI}を {BEN}しますか。","Ashita nani wo benkyou shimasu ka.","What will you study tomorrow?","හෙට මොකද ඉගෙන ගන්නේ?"),
    (f"{SHUM}に {NANI}を したいですか。","Shuumatsu ni nani wo shitai desu ka.","What do you want to do at the weekend?","සති අන්තයේ මොකද කරන්න ඕන?"),
  ],
  foot="何を 〜しますか？",
)

# ---------------------------------------------------------------- 21-3 応用②
P16C = dict(
  no="21", tag="応用 ②　何を 〜しましたか？ / PAST",
  title_jp=f"{NANI}を しましたか？",
  title_ro='nani wo shimashita ka &nbsp;|&nbsp; What did you 〜? &nbsp;|&nbsp; '
           '<span class="si">මොකද කළේ?</span>',
  basic=(f"{KIN}の {SHU}は {NAN}でしたか。","Kinou no shukudai wa nan deshita ka.",
         "What was yesterday's homework?","ඊයේ ගෙදර වැඩ මොකක්ද?"),
  use=(f'13の「ました」と{r("組","く")}み{r("合","あ")}わせます。'
       f'「です」の かこは「でした」なので、「{NAN}ですか」は「{NAN}でしたか」に なります。',
       'Combine it with the past forms from pattern 13. The past of <b>desu</b> is <b>deshita</b>, '
       'so <b>nan desu ka</b> becomes <b>nan deshita ka</b>.',
       '13 හි අතීත ආකාර එක්ක එකතු කරන්න. <b>desu</b> හි අතීතය <b>deshita</b> නිසා '
       '<b>nan desu ka</b> එක <b>nan deshita ka</b> වෙනවා.'),
  pattern=[[("〜は","~ wa"),(f"{NAN}でしたか？","nan deshita ka",True)],
           [(f"{NANI}を","nani wo",True),("しましたか？","shimashita ka")],
           [(f"{NANI}を","nani wo",True),("していましたか？","shite imashita ka")]],
  examples=[
    (f"{KIN}の {SHU}は {NAN}でしたか。","Kinou no shukudai wa nan deshita ka.","What was yesterday's homework?","ඊයේ ගෙදර වැඩ මොකක්ද?"),
    (f"きょうの {JUG}は {NAN}でしたか。","Kyou no jugyou wa nan deshita ka.","What was today's class?","අද පන්තිය මොකක්ද?"),
    (f"{SSH} {NANI}を しましたか。","Senshuu nani wo shimashita ka.","What did you do last week?","පසුගිය සතියේ මොකද කළේ?"),
    (f"{KES} {NANI}を {r('食','た')}べましたか。","Kesa nani wo tabemashita ka.","What did you eat this morning?","අද උදේ මොනවද කෑවේ?"),
    (f"{KSH}で {NANI}を していましたか。","Kyoushitsu de nani wo shite imashita ka.","What were you doing in the classroom?","පන්ති කාමරයේ මොකද කරමින් හිටියේ?"),
    (f"{SEN}は {NANI}を {HAN}ましたか。","Sensei wa nani wo hanashimashita ka.","What did the teacher talk about?","ගුරුතුමා මොකද කතා කළේ?"),
    (f"さっき {NANI}を {YON}いましたか。","Sakki nani wo yonde imashita ka.","What were you reading a moment ago?","ටිකකට කලින් මොකද කියවමින් හිටියේ?"),
  ],
  foot="何を 〜しましたか？",
)

# ---------------------------------------------------------------- 21-4 / 21-5 答え方
_USE = (f'ここが いちばん{r("大切","たい せつ")}です。「{NANI}」の{r("質問","しつ もん")}には'
        f'「はい」「いいえ」で{r("答","こた")}えません。かならず ものや ことを{r("言","い")}います。',
        'This is the most important point: you cannot answer a <b>nani</b> question with '
        '<b>hai</b> or <b>iie</b> — you must name the thing.',
        'මේක තමයි වැදගත්ම කරුණ. <b>nani</b> ප්‍රශ්නයකට <b>hai</b> හෝ <b>iie</b> කියලා '
        'උත්තර දෙන්න බැහැ — දේ නම් කරන්නම ඕන.')

_PAT = ["NOTE:【 ちゅうい 】「はい / いいえ」では 答えません　/　never answer yes or no",
        [(f"{NAN}ですか？","nan desu ka"),"TO",("ものの 名前を 言う","name the thing",True)],
        [(f"{NANI}を しますか？","nani wo shimasu ka"),"TO",("する ことを 言う","name the action",True)]]

_QA = [
  ("QA", (f"これは {NAN}ですか。","Kore wa nan desu ka.","What is this?","මේක මොකක්ද?"),
         (f"それは {JIS}です。","Sore wa jisho desu.","That is a dictionary.","ඒක ශබ්දකෝෂයක්.")),
  ("QA", (f"あなたの {NAM}は {NAN}ですか。","Anata no namae wa nan desu ka.","What is your name?","ඔබේ නම මොකක්ද?"),
         ("サマンです。","Saman desu.","I'm Saman.","මම සමන්.")),
  ("QA", (f"この ことばの {IMI}は {NAN}ですか。","Kono kotoba no imi wa nan desu ka.","What is the meaning of this word?","මේ වචනයේ තේරුම මොකක්ද?"),
         ("すみません、わかりません。","Sumimasen, wakarimasen.","Sorry, I don't know.","සමාවෙන්න, මම දන්නේ නැහැ.")),
  ("QA", (f"きょうの {SHU}は {NAN}ですか。","Kyou no shukudai wa nan desu ka.","What is today's homework?","අද ගෙදර වැඩ මොකක්ද?"),
         (f"{KANJ}の {REN}です。","Kanji no renshuu desu.","Kanji practice.","කන්ජි අභ්‍යාස.")),
  ("QA", (f"{NICH}に {NANI}を しますか。","Nichiyoubi ni nani wo shimasu ka.","What do you do on Sundays?","ඉරිදාට ඔබ මොකද කරන්නේ?"),
         ("アルバイトを します。","Arubaito wo shimasu.","I work part-time.","මම අර්ධකාලීන රැකියාව කරනවා.")),
  ("QA", (f"{IMA} {NANI}を していますか。","Ima nani wo shite imasu ka.","What are you doing now?","දැන් මොකද කරන්නේ?"),
         (f"{r('日本語','に ほん ご')}を {BEN}しています。","Nihongo wo benkyou shite imasu.","I'm studying Japanese.","මම ජපන් භාෂාව ඉගෙන ගනිමින් ඉන්නවා.")),
  ("QA", (f"ばんごはんに {NANI}を {TABT}ですか。","Bangohan ni nani wo tabetai desu ka.","What do you want to eat for dinner?","රාත්‍රී කෑමට මොනවද කන්න ඕන?"),
         (f"カレーが {TABT}です。","Karee ga tabetai desu.","I want to eat curry.","මට කරි කන්න ඕන.")),
  ("QA", (f"{KIN}の {JUG}は {NAN}でしたか。","Kinou no jugyou wa nan deshita ka.","What was yesterday's class?","ඊයේ පන්තිය මොකක්ද?"),
         (f"{BUN}の {JUG}でした。","Bunpou no jugyou deshita.","It was a grammar class.","ඒක ව්‍යාකරණ පන්තියක්.")),
  ("QA", (f"{SSH} {NANI}を しましたか。","Senshuu nani wo shimashita ka.","What did you do last week?","පසුගිය සතියේ මොකද කළේ?"),
         (f"{TOM}と {HAN}ました。","Tomodachi to hanashimashita.","I talked with my friends.","මම යාළුවො එක්ක කතා කළා.")),
]

_TITLE_RO = ('Nani no shitsumon no kotaekata &nbsp;|&nbsp; Answering a "what" question &nbsp;|&nbsp; '
             '<span class="si">"මොකක්ද?" ප්‍රශ්නයට උත්තර දීම</span>')

P16A = dict(
  no="21", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=f"{NANI}の 質問の 答え方",
  title_ro=_TITLE_RO,
  basic=(f"これは {NAN}ですか。　&#8594;　それは {JIS}です。","Kore wa nan desu ka. → Sore wa jisho desu.",
         "What is this? → That is a dictionary.","මේක මොකක්ද? → ඒක ශබ්දකෝෂයක්."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="何の 質問の 答え方",
)

P16A2 = dict(
  no="21", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=f"{NANI}の 質問の 答え方",
  title_ro=_TITLE_RO,
  skip=("basic","use","pattern"), start=4,
  basic=P16A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("わかりません。","Wakarimasen.","I don't know.","මම දන්නේ නැහැ."),
    ("まだ きめて いません。","Mada kimete imasen.","I haven't decided yet.","තාම තීරණය කරලා නැහැ."),
    (f"{NAN}でも いいです。","Nan demo ii desu.","Anything is fine.","මොකක් හරි කමක් නැහැ."),
    (f"もう {r('一度','いち ど')} おねがいします。","Mou ichido onegaishimasu.","Once more, please.","ආයෙත් වතාවක් කියන්න."),
  ],
  foot="何の 質問の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P16,"p21_1_nan"), (P16B,"p21_2_verbs"), (P16C,"p21_3_past"),
                    (P16A,"p21_4_answer"), (P16A2,"p21_5_answer2")]:
        render(p, stem)
