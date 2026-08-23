from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

AME  = r("雨","あめ")
FUT  = r("降","ふ")+"ったら"
IKI  = r("行","い")+"きません"
NIH  = r("日本","に ほん")
ITT  = r("行","い")+"ったら"
RENR = r("連絡","れん らく")
JIK  = r("時間","じ かん")
TETS = r("手伝","て つだ")+"って"
YASU = r("安","やす")+"かったら"
YASK = r("安","やす")+"かった"
KAI  = r("買","か")+"います"
KIK  = r("聞","き")+"いて"
SAI  = r("歳","さい")
KUNI = r("国","くに")
KAER = r("帰","かえ")+"ります"
GAK  = r("学校","がっ こう")
DEN  = r("電話","でん わ")
SHIZ = r("静","しず")+"か"

P64 = dict(
  no="82", tag=None,
  title_jp="〜たら 〜",
  title_ro='〜 tara 〜 &nbsp;|&nbsp; if / when 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 නම් / 〜 ට පස්සේ</span>',
  basic=(f"{AME}が {FUT}、{IKI}。","Ame ga futtara, ikimasen.",
         "If it rains, I won't go.","වහිනවා නම් මම යන්නේ නැහැ."),
  use=(f'じょうけんを {r("言","い")}う いちばん つかいやすい かたちです。'
       f'た{r("形","けい")}に「ら」を つけるだけ。うしろに おねがい・めいれい・'
       f'{r("自分","じ ぶん")}の いしが 来ても だいじょうぶです。',
       'This is the easiest way to say "if / when". Just add <b>ra</b> to the ta-form. '
       'A request, an order or your own intention can follow it.',
       '"නම්" කියන්න ලේසිම ක්‍රමය. ta-ආකාරයට <b>ra</b> දාන්න විතරයි. '
       'පස්සේ ඉල්ලීමක්, අණක් හෝ තමන්ගේ අදහසක් ආවත් කමක් නැහැ.'),
  pattern=[["BLANK",("たら","tara",True),("〜します","~ shimasu")],
           f"NOTE:た{r('形','けい')} ＋ ら：{r('食','た')}べた → {r('食','た')}べたら　/　"
           f"{YASK} → {YASU}　/　{SHIZ}だった → {SHIZ}だったら",
           f"NOTE:「〜たら」は 「もし」（if）にも 「〜した あと」（when）にも つかえます"],
  examples=[
    (f"{AME}が {FUT}、{IKI}。","Ame ga futtara, ikimasen.","If it rains, I won't go.","වහිනවා නම් මම යන්නේ නැහැ."),
    (f"{NIH}へ {ITT}、{RENR}して ください。","Nihon e ittara, renraku shite kudasai.","When you get to Japan, please get in touch.","ජපානෙට ගියාම කතා කරන්න."),
    (f"{JIK}が あったら、{TETS} ください。","Jikan ga attara, tetsudatte kudasai.","If you have time, please help me.","වෙලාව තිබුණොත් උදව් කරන්න."),
    (f"{YASU}、{KAI}。","Yasukattara, kaimasu.","If it's cheap, I'll buy it.","ලාබයි නම් මම ගන්නවා."),
    (f"わからなかったら、{KIK} ください。","Wakaranakattara, kiite kudasai.","If you don't understand, please ask.","තේරෙන්නේ නැත්නම් අහන්න."),
    (f"32{SAI}に なったら、{KUNI}へ {KAER}。","Sanjissai ni nattara, kuni e kaerimasu.","When I turn thirty, I'll go back home.","අවුරුදු 32 වුණාම මම රට යනවා."),
    (f"{GAK}に ついたら、{DEN}します。","Gakkou ni tsuitara, denwa shimasu.","I'll call you when I get to school.","පාසලට ගියාම කතා කරන්නම්."),
  ],
  foot="〜たら 〜",
)

if __name__ == "__main__":
    render(P64, "u82_tara")
