from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASHI = r("明日","あ した")
TEN  = r("天気","てん き")
YORO = r("喜","よろこ")+"びます"
DEK  = "できます"
HON  = r("本","ほん")
YAK  = r("役","やく")
TAT  = r("立","た")+"ちます"
AE   = r("会","あ")+"えます"
W    = r("私","わたし")
NIH  = r("日本","に ほん")
IKI  = r("行","い")+"きます"
RENR = r("連絡","れん らく")
KETS = r("決意","けつ い")
YAKU = r("約束","やく そく")
YOSO = r("予想","よ そう")

P64 = dict(
  no="63", tag=None,
  title_jp="きっと 〜",
  title_ro='kitto 〜 &nbsp;|&nbsp; surely / I\'m sure 〜 &nbsp;|&nbsp; '
           '<span class="si">අනිවාර්යයෙන්ම 〜</span>',
  basic=(f"{ASHI}は きっと いい {TEN}ですよ。","Ashita wa kitto ii tenki desu yo.",
         "I'm sure the weather will be nice tomorrow.","හෙට අනිවාර්යයෙන්ම කාලගුණය හොඳයි."),
  use=(f'62の「たぶん」より ずっと つよい きもちです（90パーセント{r("以上","い じょう")}）。'
       f'{YOSO}・{KETS}・{YAKU}の 3つに つかいます。',
       'Much stronger than <b>tabun</b> in 62 (over 90%). '
       'Use it for a prediction, a decision, or a promise.',
       '62 හි <b>tabun</b> වලට වඩා ගොඩක් ශක්තිමත් (90%ට වඩා). '
       'අනුමානය, තීරණය, පොරොන්දුව යන තුනටම.'),
  pattern=[[("〜は","~ wa"),("きっと","kitto",True),"BLANK",("します","shimasu")],
           f"NOTE:つよさ：たぶん（62・60〜80％）　&lt;　きっと（63・90％{r('以上','い じょう')}）",
           f"NOTE:「〜よ」を つけると、あいてを はげます きもちに なります"],
  examples=[
    (f"{ASHI}は きっと いい {TEN}ですよ。","Ashita wa kitto ii tenki desu yo.","I'm sure the weather will be nice tomorrow.","හෙට අනිවාර්යයෙන්ම කාලගුණය හොඳයි."),
    (f"サマンさんは きっと {YORO}よ。","Saman-san wa kitto yorokobimasu yo.","I'm sure Saman will be happy.","සමන් අනිවාර්යයෙන්ම සතුටු වේවි."),
    (f"だいじょうぶ、きっと {DEK}よ。","Daijoubu, kitto dekimasu yo.","It's fine — I'm sure you can do it.","කමක් නැහැ, අනිවාර්යයෙන්ම පුළුවන් වේවි."),
    (f"この {HON}は きっと {YAK}に {TAT}よ。","Kono hon wa kitto yaku ni tachimasu yo.","I'm sure this book will be useful.","මේ පොත අනිවාර්යයෙන්ම වැඩදායකයි."),
    (f"きっと また {AE}よ。","Kitto mata aemasu yo.","I'm sure we'll meet again.","අනිවාර්යයෙන්ම ආයෙත් හම්බවෙන්න පුළුවන්."),
    (f"{W}は きっと {NIH}へ {IKI}。","Watashi wa kitto Nihon e ikimasu.","I will definitely go to Japan.","මම අනිවාර්යයෙන්ම ජපානෙට යනවා."),
    (f"きっと {RENR}しますね。","Kitto renraku shimasu ne.","I'll definitely be in touch.","අනිවාර්යයෙන්ම කතා කරන්නම්."),
  ],
  foot="きっと 〜",
)

if __name__ == "__main__":
    render(P64, "p63_kitto")
