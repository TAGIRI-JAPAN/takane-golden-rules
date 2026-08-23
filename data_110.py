from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HASH = r("走","はし")+"っては"
KYOU = r("教室","きょう しつ")
TABE = r("食","た")+"べては"
MAD  = r("窓","まど")
AKE  = r("開","あ")+"けては"
MIZU = r("水","みず")
NON  = r("飲","の")+"んでは"
JUG  = r("授業","じゅ ぎょう")
CHU  = r("中","ちゅう")
TSUK = r("使","つか")+"っては"
KAB  = "かばん"
OI   = r("置","お")+"いては"
TSUI = "ついては"
KINS = r("禁止","きん し")
KAN  = r("看板","かん ばん")

P67 = dict(
  no="110", tag=None,
  title_jp="〜しては いけません",
  title_ro='〜 shite wa ikemasen &nbsp;|&nbsp; You must not 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න බැහැ</span>',
  basic=(f"ここで {HASH} いけません。","Koko de hashitte wa ikemasen.",
         "You must not run here.","මෙතන දුවන්න බැහැ."),
  use=(f'ルールとして {KINS}する ときの ことばです。109は おねがいで やわらかいですが、'
       f'110は つよい {KINS}で、{KAN}や がっこうの きそくに よく つかいます。',
       'This forbids something as a rule. 109 is a soft request; 110 is a strong '
       'prohibition, used on signs and in school rules.',
       'නීතියක් විදිහට තහනම් කරනවා. 109 මෘදු ඉල්ලීමක්; '
       '110 දැඩි තහනමක් — දැන්වීම් පුවරු හා පාසල් නීතිවල.'),
  pattern=[["BLANK",("しては いけません","shite wa ikemasen",True)],
           f"NOTE:て{r('形','けい')} ＋ は いけません：{r('食','た')}べて → {TABE} いけません",
           f"NOTE:109（おねがい・やわらかい）　⇔　110（{KINS}・つよい）",
           f"NOTE:かいわでは「〜ちゃ だめです」（{r('食','た')}べちゃ だめ　/　{r('飲','の')}んじゃ だめ）"],
  examples=[
    (f"ここで {HASH} いけません。","Koko de hashitte wa ikemasen.","You must not run here.","මෙතන දුවන්න බැහැ."),
    (f"{KYOU}で ものを {TABE} いけません。","Kyoushitsu de mono wo tabete wa ikemasen.","You must not eat in the classroom.","පන්ති කාමරයේ කන්න බැහැ."),
    (f"{MAD}を {AKE} いけません。","Mado wo akete wa ikemasen.","You must not open the window.","ජනේලය අරින්න බැහැ."),
    (f"この {MIZU}を {NON} いけません。","Kono mizu wo nonde wa ikemasen.","You must not drink this water.","මේ වතුර බොන්න බැහැ."),
    (f"{JUG}{CHU}に スマホを {TSUK} いけません。","Jugyouchuu ni sumaho wo tsukatte wa ikemasen.","You must not use your phone during class.","පන්තියේදී ජංගම දුරකථනය පාවිච්චි කරන්න බැහැ."),
    (f"ここに {KAB}を {OI} いけません。","Koko ni kaban wo oite wa ikemasen.","You must not put your bag here.","මෙතන බෑග් එක තියන්න බැහැ."),
    (f"うそを {TSUI} いけません。","Uso wo tsuite wa ikemasen.","You must not tell lies.","බොරු කියන්න බැහැ."),
  ],
  foot="〜しては いけません",
)

if __name__ == "__main__":
    render(P67, "p110_shitewaikemasen")
