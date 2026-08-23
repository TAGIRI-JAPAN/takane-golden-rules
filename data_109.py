from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HASH = r("走","はし")+"らないで"
KYOU = r("教室","きょう しつ")
TABE = r("食","た")+"べないで"
MAD  = r("窓","まど")
AKE  = r("開","あ")+"けないで"
MIZU = r("水","みず")
NOM  = r("飲","の")+"まないで"
JUG  = r("授業","じゅ ぎょう")
CHU  = r("中","ちゅう")
TSUK = r("使","つか")+"わないで"
KAB  = "かばん"
OKA  = r("置","お")+"かないで"
SHIN = r("心配","しん ぱい")
MUR  = r("無理","む り")

P66 = dict(
  no="109", tag=None,
  title_jp="〜しないで（ください）",
  title_ro='〜 shinaide (kudasai) &nbsp;|&nbsp; Please don\'t 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න එපා</span>',
  basic=(f"ここで {HASH} ください。","Koko de hashiranaide kudasai.",
         "Please don't run here.","මෙතන දුවන්න එපා."),
  use=(f'あいてに して ほしくない ことを {r("言","い")}う ことばです。'
       f'つよい きんしでは なく、おねがいの きもちです（110より やわらかい）。',
       'Use it to ask someone not to do something. It is a request, not a strong '
       'prohibition — softer than 110.',
       'අනිත් කෙනාට යමක් නොකරන්න කියන්න. දැඩි තහනමක් නෙවෙයි, ඉල්ලීමක් — '
       '110ට වඩා මෘදුයි.'),
  pattern=[["BLANK",("しないで","shinaide",True)],
           ["BLANK",("しないで ください","shinaide kudasai",True)],
           f"NOTE:ない{r('形','けい')} ＋ で：{r('食','た')}べます → {r('食','た')}べない → {TABE}",
           f"NOTE:きんしじゃない つかい{r('方','かた')}も：{SHIN}しないで　/　{MUR}しないで（やさしい きもち）"],
  examples=[
    (f"ここで {HASH} ください。","Koko de hashiranaide kudasai.","Please don't run here.","මෙතන දුවන්න එපා."),
    (f"{KYOU}で ものを {TABE} ください。","Kyoushitsu de mono wo tabenaide kudasai.","Please don't eat in the classroom.","පන්ති කාමරයේ කන්න එපා."),
    (f"{MAD}を {AKE} ください。","Mado wo akenaide kudasai.","Please don't open the window.","ජනේලය අරින්න එපා."),
    (f"この {MIZU}を {NOM} ください。","Kono mizu wo nomanaide kudasai.","Please don't drink this water.","මේ වතුර බොන්න එපා."),
    (f"{JUG}{CHU}に スマホを {TSUK} ください。","Jugyouchuu ni sumaho wo tsukawanaide kudasai.","Please don't use your phone during class.","පන්තියේදී ජංගම දුරකථනය පාවිච්චි කරන්න එපා."),
    (f"ここに {KAB}を {OKA} ください。","Koko ni kaban wo okanaide kudasai.","Please don't put your bag here.","මෙතන බෑග් එක තියන්න එපා."),
    (f"{SHIN}しないで ください。","Shinpai shinaide kudasai.","Please don't worry.","කරදර වෙන්න එපා."),
  ],
  foot="〜しないで（ください）",
)

if __name__ == "__main__":
    render(P66, "p109_shinaide")
