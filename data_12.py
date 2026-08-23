from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
NIH  = r("日本","に ほん")
IKIT = r("行","い")+"きたい"
HON  = r("本","ほん")
YOMT = r("読","よ")+"みたい"
SEN  = r("先生","せん せい")
HANT = r("話","はな")+"したい"
MIZ  = r("水","みず")
NOMT = r("飲","の")+"みたい"
SUK  = r("少","すこ")+"し"
YAST = r("休","やす")+"みたい"
KAZ  = r("家族","か ぞく")
AIT  = r("会","あ")+"いたい"
IMA  = r("今","いま")
KYO  = r("今日","きょう")
NAN  = r("何","なに")
UMI  = r("海","うみ")
TABT = r("食","た")+"べたい"

# ---------------------------------------------------------------- 12-1 基本
P8 = dict(
  no="12", tag=None,
  title_jp="〜したいです",
  title_ro='〜 shitai desu &nbsp;|&nbsp; I want to 〜 &nbsp;|&nbsp; <span class="si">〜 කරන්න ඕන</span>',
  basic=(f"{W}は {NHG}を {BEN}したいです。","Watashi wa nihongo wo benkyou shitai desu.",
         "I want to study Japanese.","මට ජපන් භාෂාව ඉගෙන ගන්න ඕන."),
  use=(f'「〜ます」の「ます」を とって「たい」を つけます。{r("自分","じ ぶん")}が したいことを{r("言","い")}うときに{r("使","つか")}います。'
       f'「〜を」が「〜が」に なることも あります。',
       'Take <b>masu</b> off the verb and add <b>tai</b>. Use it to say what you want to do. '
       'The particle <b>wo</b> often becomes <b>ga</b> with <b>tai</b>.',
       'ක්‍රියා පදයේ <b>masu</b> අයින් කරලා <b>tai</b> දාන්න — <b>tai</b> = ඕන / කැමතියි. '
       'තමන්ට කරන්න ඕන දේ කියන්න. <b>wo</b> එක බොහෝවිට <b>ga</b> බවට පත් වෙනවා.'),
  pattern=["NOTE:「ます」を とって「たい」を つける　/　masu &#8594; tai",
           [(r("行","い")+"きます","ikimasu"),"TO",(f"{IKIT}です","ikitai desu",True)],
           [(r("食","た")+"べます","tabemasu"),"TO",(f"{TABT}です","tabetai desu",True)],
           "NOTE:「〜を」は「〜が」に なることも あります　/　wo &#8594; ga（水が 飲みたいです）"],
  examples=[
    (f"{W}は {NHG}を {BEN}したいです。","Watashi wa nihongo wo benkyou shitai desu.","I want to study Japanese.","මට ජපන් භාෂාව ඉගෙන ගන්න ඕන."),
    (f"{W}は {NIH}に {IKIT}です。","Watashi wa Nihon ni ikitai desu.","I want to go to Japan.","මට ජපානයට යන්න ඕන."),
    (f"{W}は {NIH}の {HON}を {YOMT}です。","Watashi wa Nihon no hon wo yomitai desu.","I want to read Japanese books.","මට ජපන් පොත් කියවන්න ඕන."),
    (f"{W}は {SEN}と {HANT}です。","Watashi wa sensei to hanashitai desu.","I want to talk with the teacher.","මට ගුරුතුමා එක්ක කතා කරන්න ඕන."),
    (f"{W}は {MIZ}が {NOMT}です。","Watashi wa mizu ga nomitai desu.","I want to drink water.","මට වතුර බොන්න ඕන."),
    (f"{W}は {SUK} {YAST}です。","Watashi wa sukoshi yasumitai desu.","I want to rest a little.","මට ටිකක් විවේක ගන්න ඕන."),
    (f"{W}は {KAZ}に {AIT}です。","Watashi wa kazoku ni aitai desu.","I want to see my family.","මට පවුලේ අයව හම්බවෙන්න ඕන."),
  ],
  foot="〜したいです",
)

# ---------------------------------------------------------------- 12-2 否定
P8N = dict(
  no="12", tag="応用 ①　否定パターン / NEGATIVE",
  title_jp="〜したく ないです / 〜したく ありません",
  title_ro='〜 shitaku nai desu / 〜 shitaku arimasen &nbsp;|&nbsp; I do not want to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න ඕන නැහැ</span>',
  basic=(f"{W}は {NHG}を {BEN}したく ないです。","Watashi wa nihongo wo benkyou shitaku nai desu.",
         "I do not want to study Japanese.","මට ජපන් භාෂාව ඉගෙන ගන්න ඕන නැහැ."),
  use=(f'「たい」は「い」でおわる ことばと{r("同","おな")}じように{r("形","かたち")}が{r("変","か")}わります。'
       f'だから{r("否定","ひ てい")}は「たく ないです」「たく ありません」の 2つです（07と{r("同","おな")}じ）。',
       '<b>tai</b> changes like an <b>-i</b> adjective, so the negative has two forms: '
       '<b>taku nai desu</b> and <b>taku arimasen</b> — exactly as in pattern 07.',
       '<b>tai</b> එක <b>-i</b> විශේෂණ පදයක් වගේ වෙනස් වෙනවා. ඒ නිසා නිශේධන ආකාර දෙකක්: '
       '<b>taku nai desu</b> සහ <b>taku arimasen</b> — 07 වගේමයි.'),
  pattern=[[("したい","shitai"),"TO",("したく ないです","shitaku nai desu",True)],
           [("したい","shitai"),"TO",("したく ありません","shitaku arimasen",True)],
           "NOTE:「たい」＝「い」でおわる ことば　/　tai behaves like an i-adjective"],
  examples=[
    (f"{W}は {NHG}を {BEN}したく ないです。","Watashi wa nihongo wo benkyou shitaku nai desu.","I do not want to study Japanese.","මට ජපන් භාෂාව ඉගෙන ගන්න ඕන නැහැ."),
    (f"{W}は {NIH}に {r('行','い')}きたく ないです。","Watashi wa Nihon ni ikitaku nai desu.","I do not want to go to Japan.","මට ජපානයට යන්න ඕන නැහැ."),
    (f"{W}は {NIH}の {HON}を {r('読','よ')}みたく ないです。","Watashi wa Nihon no hon wo yomitaku nai desu.","I do not want to read Japanese books.","මට ජපන් පොත් කියවන්න ඕන නැහැ."),
    (f"{W}は {SEN}と {r('話','はな')}したく ありません。","Watashi wa sensei to hanashitaku arimasen.","I do not want to talk with the teacher.","මට ගුරුතුමා එක්ක කතා කරන්න ඕන නැහැ."),
    (f"{W}は {MIZ}は {r('飲','の')}みたく ありません。","Watashi wa mizu wa nomitaku arimasen.","I do not want to drink water.","මට වතුර බොන්න ඕන නැහැ."),
    (f"{IMA}は {r('休','やす')}みたく ありません。","Ima wa yasumitaku arimasen.","I do not want to rest now.","දැන් විවේක ගන්න ඕන නැහැ."),
    (f"{KYO}は {r('会','あ')}いたく ありません。","Kyou wa aitaku arimasen.","I do not want to meet today.","අද හම්බවෙන්න ඕන නැහැ."),
  ],
  foot="〜したく ないです",
)

# ---------------------------------------------------------------- 12-3 疑問
P8Q = dict(
  no="12", tag="応用 ②　疑問パターン / QUESTION",
  title_jp="〜したいですか？",
  title_ro='〜 shitai desu ka &nbsp;|&nbsp; Do you want to 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න ඕනද?</span>',
  basic=(f"あなたは {NHG}を {BEN}したいですか。","Anata wa nihongo wo benkyou shitai desu ka.",
         "Do you want to study Japanese?","ඔබට ජපන් භාෂාව ඉගෙන ගන්න ඕනද?"),
  use=(f'「たいです」のうしろに「か」をつけます。'
       f'ただし{r("目上","め うえ")}の{r("人","ひと")}に「〜したいですか」は{r("少","すこ")}し しつれいです。'
       f'さそうときは「〜しませんか」の ほうが ていねいです。',
       'Add <b>ka</b> after <b>tai desu</b>. Note: asking a senior person <b>〜 shitai desu ka</b> '
       'can sound rude. When you invite someone, <b>〜 shimasen ka</b> is more polite.',
       '<b>tai desu</b> එකට පස්සේ <b>ka</b> දාන්න. නමුත් වැඩිමහල් හෝ ඉහළ තනතුරක කෙනෙකුට '
       '<b>〜 shitai desu ka</b> කියන එක ටිකක් අවිනීතයි. ආරාධනා කරනවා නම් <b>〜 shimasen ka</b> වඩා හොඳයි.'),
  pattern=[[("〜は","~ wa"),("〜を","~ wo"),("したいです","shitai desu")],
           "ARROW",
           [("〜は","~ wa"),("〜を","~ wo"),("したいですか？","shitai desu ka",True)]],
  examples=[
    (f"あなたは {NHG}を {BEN}したいですか。","Anata wa nihongo wo benkyou shitai desu ka.","Do you want to study Japanese?","ඔබට ජපන් භාෂාව ඉගෙන ගන්න ඕනද?"),
    (f"あなたは {NIH}に {IKIT}ですか。","Anata wa Nihon ni ikitai desu ka.","Do you want to go to Japan?","ඔබට ජපානයට යන්න ඕනද?"),
    (f"あなたは {NIH}の {HON}を {YOMT}ですか。","Anata wa Nihon no hon wo yomitai desu ka.","Do you want to read Japanese books?","ඔබට ජපන් පොත් කියවන්න ඕනද?"),
    (f"あなたは {SEN}と {HANT}ですか。","Anata wa sensei to hanashitai desu ka.","Do you want to talk with the teacher?","ඔබට ගුරුතුමා එක්ක කතා කරන්න ඕනද?"),
    (f"{MIZ}が {NOMT}ですか。","Mizu ga nomitai desu ka.","Do you want to drink water?","ඔබට වතුර බොන්න ඕනද?"),
    (f"{SUK} {YAST}ですか。","Sukoshi yasumitai desu ka.","Do you want to rest a little?","ඔබට ටිකක් විවේක ගන්න ඕනද?"),
    (f"{KAZ}に {AIT}ですか。","Kazoku ni aitai desu ka.","Do you want to see your family?","ඔබට පවුලේ අයව හම්බවෙන්න ඕනද?"),
  ],
  foot="〜したいですか？",
)

# ---------------------------------------------------------------- 12-4 / 12-5 答え方
_USE = (f'「はい、〜たいです。」「いいえ、〜たく ないです。」と{r("答","こた")}えます。'
        f'はっきり ことわりにくいときは「ちょっと…」と{r("言","い")}うと やわらかいです。',
        'Answer with <b>Hai, 〜 tai desu</b> or <b>Iie, 〜 taku nai desu</b>. '
        'When it is hard to refuse directly, saying <b>chotto…</b> sounds softer.',
        '<b>Hai, 〜 tai desu</b> හෝ <b>Iie, 〜 taku nai desu</b> කියලා උත්තර දෙන්න. '
        'කෙළින්ම එපා කියන්න අමාරු නම් <b>chotto…</b> කිව්වොත් වඩා මෘදුයි.')

_PAT = [[("はい、","Hai,"),"BLANK",("たいです","tai desu",True)],
        [("いいえ、","Iie,"),"BLANK",("たく ないです","taku nai desu",True)]]

_TITLE = ("はい / いいえ の 答え方",
          'Hai / Iie no kotaekata &nbsp;|&nbsp; Answering yes / no &nbsp;|&nbsp; '
          '<span class="si">ඔව් / නැහැ කියා උත්තර දීම</span>')

_QA = [
  ("QA", (f"{NHG}を {BEN}したいですか。","Nihongo wo benkyou shitai desu ka.","Do you want to study Japanese?","ඔබට ජපන් භාෂාව ඉගෙන ගන්න ඕනද?"),
         (f"はい、{BEN}したいです。","Hai, benkyou shitai desu.","Yes, I do.","ඔව්, ඉගෙන ගන්න ඕන.")),
  ("QA", (f"{NIH}に {IKIT}ですか。","Nihon ni ikitai desu ka.","Do you want to go to Japan?","ඔබට ජපානයට යන්න ඕනද?"),
         (f"はい、{IKIT}です。","Hai, ikitai desu.","Yes, I do.","ඔව්, යන්න ඕන.")),
  ("QA", (f"{NIH}の {HON}を {YOMT}ですか。","Nihon no hon wo yomitai desu ka.","Do you want to read Japanese books?","ඔබට ජපන් පොත් කියවන්න ඕනද?"),
         (f"いいえ、{r('読','よ')}みたく ないです。","Iie, yomitaku nai desu.","No, I don't.","නැහැ, කියවන්න ඕන නැහැ.")),
  ("QA", (f"{SEN}と {HANT}ですか。","Sensei to hanashitai desu ka.","Do you want to talk with the teacher?","ඔබට ගුරුතුමා එක්ක කතා කරන්න ඕනද?"),
         (f"はい、{HANT}です。","Hai, hanashitai desu.","Yes, I do.","ඔව්, කතා කරන්න ඕන.")),
  ("QA", (f"{MIZ}が {NOMT}ですか。","Mizu ga nomitai desu ka.","Do you want to drink water?","ඔබට වතුර බොන්න ඕනද?"),
         (f"いいえ、{r('飲','の')}みたく ありません。","Iie, nomitaku arimasen.","No, I don't.","නැහැ, බොන්න ඕන නැහැ.")),
  ("QA", (f"{SUK} {YAST}ですか。","Sukoshi yasumitai desu ka.","Do you want to rest a little?","ඔබට ටිකක් විවේක ගන්න ඕනද?"),
         (f"はい、{YAST}です。","Hai, yasumitai desu.","Yes, I do.","ඔව්, විවේක ගන්න ඕන.")),
  ("QA", (f"{KAZ}に {AIT}ですか。","Kazoku ni aitai desu ka.","Do you want to see your family?","ඔබට පවුලේ අයව හම්බවෙන්න ඕනද?"),
         (f"はい、とても {AIT}です。","Hai, totemo aitai desu.","Yes, very much.","ඔව්, ගොඩක් හම්බවෙන්න ඕන.")),
  ("QA", (f"{NAN}が {TABT}ですか。","Nani ga tabetai desu ka.","What do you want to eat?","ඔබට මොනවද කන්න ඕන?"),
         (f"ラーメンが {TABT}です。","Raamen ga tabetai desu.","I want to eat ramen.","මට රාමෙන් කන්න ඕන.")),
  ("QA", (f"どこに {IKIT}ですか。","Doko ni ikitai desu ka.","Where do you want to go?","ඔබට කොහෙද යන්න ඕන?"),
         (f"{UMI}に {IKIT}です。","Umi ni ikitai desu.","I want to go to the sea.","මට මුහුදට යන්න ඕන.")),
]

P8A = dict(
  no="12", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  basic=(f"はい、{BEN}したいです。　／　いいえ、{BEN}したく ないです。",
         "Hai, benkyou shitai desu. / Iie, benkyou shitaku nai desu.",
         "Yes, I want to. / No, I don't want to.",
         "ඔව්, ඕන. / නැහැ, ඕන නැහැ."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="はい / いいえ の 答え方",
)

P8A2 = dict(
  no="12", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp=_TITLE[0], title_ro=_TITLE[1],
  skip=("basic","use","pattern"), start=4,
  basic=P8A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("ちょっと…。","Chotto…","Well, I'd rather not.","අනේ… (මෘදුව එපා කීම)"),
    ("また 今度。","Mata kondo.","Maybe another time.","ආයෙත් වතාවක්."),
    ("ぜひ！","Zehi!","I'd love to!","අනිවාර්යයෙන්ම!"),
    ("まだ わかりません。","Mada wakarimasen.","I don't know yet.","තාම දන්නේ නැහැ."),
  ],
  foot="はい / いいえ の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P8,"p12_1_shitai"), (P8N,"p12_2_negative"), (P8Q,"p12_3_question"),
                    (P8A,"p12_4_answer"), (P8A2,"p12_5_answer2")]:
        render(p, stem)
