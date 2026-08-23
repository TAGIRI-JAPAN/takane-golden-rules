from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASHI = r("明日","あ した")
HAYA = r("早","はや")+"く"
OKI  = r("起","お")+"きなければ"
NAR  = "なりません"
SHUK = r("宿題","しゅく だい")
DAS  = r("出","だ")+"さなければ"
KUTS = r("靴","くつ")
NUG  = "ぬがなければ"
PAS  = "パスポート"
MIS  = r("見","み")+"せなければ"
NICH = r("日曜日","にち よう び")
HATA = r("働","はたら")+"かなければ"
JI   = r("時","じ")
KAER = r("帰","かえ")+"らなければ"
KIT  = r("来","こ")+"なくても"
KAK  = r("書","か")+"かなければ"
GIM  = r("義務","ぎ む")
KINS = r("禁止","きん し")
KYOK = r("許可","きょ か")

P77 = dict(
  no="111", tag=None,
  title_jp="〜なければ なりません",
  title_ro='〜 nakereba narimasen &nbsp;|&nbsp; must / have to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්නම ඕනේ</span>',
  basic=(f"{ASHI} {HAYA} {OKI} {NAR}。","Ashita hayaku okinakereba narimasen.",
         "I have to get up early tomorrow.","හෙට ඉක්මනට නැගිටින්නම ඕනේ."),
  use=(f'しなければ ならない こと（{GIM}）を {r("言","い")}います。'
       f'ない{r("形","けい")}の「い」を とって「ければ なりません」を つけます。',
       'Use it for something you have to do. Take the nai-form, drop the final <b>i</b>, '
       'and add <b>kereba narimasen</b>.',
       'කරන්නම ඕන දෙයක් කියන්න. nai-ආකාරයේ අග <b>i</b> අයින් කරලා '
       '<b>kereba narimasen</b> දාන්න.'),
  pattern=[["BLANK",("なければ なりません","nakereba narimasen",True)],
           f"NOTE:19 しても いいです（{KYOK}）　/　110 しては いけません（{KINS}）　/　"
           f"111 しなければ なりません（{GIM}）— この 3つで セットです",
           f"NOTE:つくり{r('方','かた')}：{r('書','か')}かない → {KAK} なりません　/　"
           f"かいわでは「〜なくちゃ」「〜ないと」",
           f"NOTE:はんたい（する {r('必要','ひつ よう')}が ない）は「〜なくても いいです」"],
  examples=[
    (f"{ASHI} {HAYA} {OKI} {NAR}。","Ashita hayaku okinakereba narimasen.","I have to get up early tomorrow.","හෙට ඉක්මනට නැගිටින්නම ඕනේ."),
    (f"{SHUK}を {DAS} {NAR}。","Shukudai wo dasanakereba narimasen.","I have to hand in my homework.","ගෙදර වැඩ දෙන්නම ඕනේ."),
    (f"ここで {KUTS}を {NUG} {NAR}。","Koko de kutsu wo nuganakereba narimasen.","You have to take your shoes off here.","මෙතන සපත්තු ගලවන්නම ඕනේ."),
    (f"{PAS}を {MIS} {NAR}。","Pasupooto wo misenakereba narimasen.","You have to show your passport.","පාස්පෝට් එක පෙන්නන්නම ඕනේ."),
    (f"{NICH}も {HATA} {NAR}。","Nichiyoubi mo hatarakanakereba narimasen.","I have to work on Sundays too.","ඉරිදාටත් වැඩ කරන්නම ඕනේ."),
    (f"6{JI}までに {KAER} {NAR}。","Rokuji made ni kaeranakereba narimasen.","I have to be back by six.","6ට කලින් ගෙදර යන්නම ඕනේ."),
    (f"{ASHI}は {KIT} いいです。","Ashita wa konakutemo ii desu.","You don't have to come tomorrow.","හෙට එන්න ඕන නැහැ."),
  ],
  foot="〜なければ なりません",
)

if __name__ == "__main__":
    render(P77, "u111_nakereba")
