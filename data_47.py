from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TSUK = r("使","つか")+"います"
TSUZ = r("使","つか")+"いづらい"
JISH = r("辞書","じ しょ")
HIK  = r("引","ひ")+"きづらい"
KUTS = r("靴","くつ")
ARU  = r("歩","ある")+"きにくい"
KOE  = r("声","こえ")
KIK  = r("聞","き")+"きづらい"
JI   = r("字","じ")
YOM  = r("読","よ")+"みにくい"
KANJ = r("漢字","かん じ")
OBOE = r("覚","おぼ")+"えにくい"
DOA  = "ドア"
AKE  = r("開","あ")+"けにくい"
NIK  = r("肉","にく")
TAB  = r("食","た")+"べにくい"
KAT  = r("硬","かた")+"くて"
IIM  = r("言","い")+"います"
IIZ  = r("言","い")+"いづらい"
KIM  = r("気持","き も")+"ち"
SEN  = r("先生","せん せい")
CHII = r("小","ちい")+"さくて"

P33 = dict(
  no="47", tag=None,
  title_jp="〜しづらいです〔〜しにくいです〕",
  title_ro='〜 shizurai / shinikui desu &nbsp;|&nbsp; hard to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න අමාරුයි</span>',
  basic=(f"この スプーンは {TSUZ}です。","Kono supuun wa tsukaizurai desu.",
         "This spoon is hard to use.","මේ හැන්ද පාවිච්චි කරන්න අමාරුයි."),
  use=(f'46の はんたいです。「やすい」の かわりに「づらい」か「にくい」を つけます。'
       f'「づらい」は {KIM}の めんで つらい とき、「にくい」は ものや かたちの もんだいの ときに よく つかいます。',
       'The opposite of 46. Use <b>zurai</b> or <b>nikui</b> instead of <b>yasui</b>. '
       '<b>zurai</b> often means it feels hard for you; <b>nikui</b> often means the thing itself is awkward.',
       '46ට විරුද්ධයි. <b>yasui</b> වෙනුවට <b>zurai</b> හෝ <b>nikui</b> දාන්න. '
       '<b>zurai</b> = තමන්ට දැනෙන අමාරුව; <b>nikui</b> = දේම හැදිලා තියෙන විදිහෙන් අමාරු.'),
  pattern=[[("〜は","~ wa"),"BLANK",("づらいです","zurai desu",True)],
           [("〜は","~ wa"),"BLANK",("にくいです","nikui desu",True)],
           f"NOTE:{TSUK} → {r('使','つか')}い＋づらい／にくい　/　い けいようしと{r('同','おな')}じ："
           f"づらくないです　/　にくかったです"],
  examples=[
    (f"この スプーンは {TSUZ}です。","Kono supuun wa tsukaizurai desu.","This spoon is hard to use.","මේ හැන්ද පාවිච්චි කරන්න අමාරුයි."),
    (f"この {JISH}は {HIK}です。","Kono jisho wa hikizurai desu.","This dictionary is hard to look things up in.","මේ ශබ්දකෝෂය බලන්න අමාරුයි."),
    (f"{SEN}の {KOE}が {KIK}です。","Sensei no koe ga kikizurai desu.","The teacher's voice is hard to hear.","ගුරුතුමාගේ කටහඬ අහගන්න අමාරුයි."),
    (f"その ことは ちょっと {IIZ}です。","Sono koto wa chotto iizurai desu.","That is a little hard to say.","ඒ දේ ටිකක් කියන්න අමාරුයි."),
    (f"この {KUTS}は {ARU}です。","Kono kutsu wa arukinikui desu.","These shoes are hard to walk in.","මේ සපත්තු ඇඳගෙන ඇවිදින්න අමාරුයි."),
    (f"この {JI}は {CHII} {YOM}です。","Kono ji wa chiisakute yominikui desu.","This writing is small and hard to read.","මේ අකුරු පොඩියි, කියවන්න අමාරුයි."),
    (f"この {KANJ}は {OBOE}です。","Kono kanji wa oboenikui desu.","This kanji is hard to remember.","මේ කන්ජි අකුර මතක තියාගන්න අමාරුයි."),
  ],
  foot="〜しづらいです〔〜しにくいです〕",
)

if __name__ == "__main__":
    render(P33, "p47_shizurai")
