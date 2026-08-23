from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TSUK = r("使","つか")+"います"
TSUY = r("使","つか")+"いやすい"
JISH = r("辞書","じ しょ")
HIK  = r("引","ひ")+"きやすい"
KUTS = r("靴","くつ")
ARU  = r("歩","ある")+"きやすい"
HANA = r("話","はな")+"しやすい"
SEN  = r("先生","せん せい")
JI   = r("字","じ")
YOM  = r("読","よ")+"みやすい"
NHG  = r("日本語","に ほん ご")
OBOE = r("覚","おぼ")+"えやすい"
MICH = r("道","みち")
SUB  = r("滑","すべ")+"りやすい"
KOT  = r("言葉","こと ば")
IIM  = r("言","い")+"います"
IIY  = r("言","い")+"いやすい"
TAB  = r("食","た")+"べやすい"
RYO  = r("料理","りょう り")

P32 = dict(
  no="46", tag=None,
  title_jp="〜しやすいです",
  title_ro='〜 shiyasui desu &nbsp;|&nbsp; easy to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න ලේසියි</span>',
  basic=(f"この スプーンは {TSUY}です。","Kono supuun wa tsukaiyasui desu.",
         "This spoon is easy to use.","මේ හැන්ද පාවිච්චි කරන්න ලේසියි."),
  use=(f'ますけいの「ます」を とって「やすい」を つけると「かんたんに できる」と{r("言","い")}えます。'
       f'ぜんぶで い けいようしと{r("同","おな")}じ かたちに なります。',
       'Drop <b>masu</b> from the <b>masu</b>-form and add <b>yasui</b> to say something is '
       'easy to do. The whole word then behaves like an i-adjective.',
       '<b>masu</b> ආකාරයෙන් <b>masu</b> අයින් කරලා <b>yasui</b> දැම්මම "ලේසියෙන් කරන්න පුළුවන්" '
       'කියන අර්ථය. මුළු වචනයම i-විශේෂණ පදයක් වගේ හැසිරෙනවා.'),
  pattern=[[("〜は","~ wa"),"BLANK",("やすいです","yasui desu",True)],
           f"NOTE:{TSUK} → {r('使','つか')}い＋やすい　/　{IIM} → {r('言','い')}い＋やすい　/　"
           f"{r('食','た')}べます → {r('食','た')}べ＋やすい",
           f"NOTE:い けいようしと{r('同','おな')}じ：やすいです　/　やすくないです　/　やすかったです"],
  examples=[
    (f"この スプーンは {TSUY}です。","Kono supuun wa tsukaiyasui desu.","This spoon is easy to use.","මේ හැන්ද පාවිච්චි කරන්න ලේසියි."),
    (f"この {JISH}は {HIK}です。","Kono jisho wa hikiyasui desu.","This dictionary is easy to look things up in.","මේ ශබ්දකෝෂය බලන්න ලේසියි."),
    (f"この {KUTS}は {ARU}です。","Kono kutsu wa arukiyasui desu.","These shoes are easy to walk in.","මේ සපත්තු ඇඳගෙන ඇවිදින්න ලේසියි."),
    (f"サマンさんは {HANA}です。","Saman-san wa hanashiyasui desu.","Saman is easy to talk to.","සමන් එක්ක කතා කරන්න ලේසියි."),
    (f"{SEN}の {JI}は {YOM}です。","Sensei no ji wa yomiyasui desu.","The teacher's handwriting is easy to read.","ගුරුතුමාගේ අකුරු කියවන්න ලේසියි."),
    (f"この {NHG}の {KOT}は {OBOE}です。","Kono nihongo no kotoba wa oboeyasui desu.","This Japanese word is easy to remember.","මේ ජපන් වචනය මතක තියාගන්න ලේසියි."),
    (f"この {MICH}は {SUB}です。","Kono michi wa suberiyasui desu.","This road is slippery (easy to slip on).","මේ පාරේ ලිස්සන්න ලේසියි."),
  ],
  foot="〜しやすいです",
)

if __name__ == "__main__":
    render(P32, "p46_shiyasui")
