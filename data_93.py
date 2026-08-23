from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KIP  = "きっぷ"
KAT  = r("買","か")+"って"
OKI  = "おきます"
KAIG = r("会議","かい ぎ")
MAE  = r("前","まえ")
SHIR = r("調","しら")+"べて"
JISH = r("辞書","じ しょ")
YOM  = r("読","よ")+"んで"
NAM  = r("名前","な まえ")
KAI  = r("書","か")+"いて"
MIZU = r("水","みず")
IRE  = r("入","い")+"れて"
REI  = r("冷蔵庫","れい ぞう こ")
TSUK = r("使","つか")+"って"
MOD  = r("戻","もど")+"して"
JUNB = r("準備","じゅん び")
SOCH = r("措置","そ ち")

P = dict(
  no="93", tag=None,
  title_jp="〜て おきます",
  title_ro='〜 te okimasu &nbsp;|&nbsp; do it in advance / leave it done &nbsp;|&nbsp; '
           '<span class="si">කලින්ම කරලා තියනවා</span>',
  basic=(f"きっぷを {KAT} {OKI}。","Kippu wo katte okimasu.",
         "I'll buy the ticket in advance.","ටිකට් එක කලින්ම අරගෙන තියනවා."),
  use=(f'あとで こまらない ように、<b>まえもって して {OKI}</b>と いう {r("意味","い み")}です。'
       f'78「{r("念","ねん")}の ために」と いっしょに よく つかいます。'
       f'かいわでは「〜と きます」に なります。',
       'It means doing something <b>in advance</b> so there is no trouble later. '
       'It pairs naturally with unit 78. In speech it shortens to <b>~ tokimasu</b>.',
       'පස්සේ කරදර නොවෙන්න <b>කලින්ම කරලා තියනවා</b>. '
       '78 එක්ක හොඳට යනවා. කතාබහේදී <b>~ tokimasu</b>.'),
  pattern=[["BLANK",("て おきます","te okimasu",True)],
           f"NOTE:{JUNB}（まえもって）：{KAT} {OKI}　/　{SOCH}（あとで）：{MOD}て {OKI}",
           f"NOTE:かいわ：{KAT} おく → {r('買','か')}っとく　/　"
           f"{r('見','み')}て おく → {r('見','み')}とく"],
  examples=[
    (f"きっぷを {KAT} {OKI}。","Kippu wo katte okimasu.","I'll buy the ticket in advance.","ටිකට් එක කලින්ම අරගෙන තියනවා."),
    (f"{KAIG}の {MAE}に {SHIR}て {OKI}。","Kaigi no mae ni shirabete okimasu.","I'll look it up before the meeting.","රැස්වීමට කලින් හොයලා තියනවා."),
    (f"{JISH}で ことばを {SHIR}て {OKI}ました。","Jisho de kotoba wo shirabete okimashita.","I looked the words up in advance.","වචන කලින්ම ශබ්දකෝෂයෙන් හෙව්වා."),
    (f"ここに {NAM}を {KAI} {OKI} ください。","Koko ni namae wo kaite oite kudasai.","Please write your name here beforehand.","මෙතන නම කලින්ම ලියලා තියන්න."),
    (f"{MIZU}を {REI}に {IRE}て {OKI}。","Mizu wo reizouko ni irete okimasu.","I'll put the water in the fridge.","වතුර ශීතකරණයේ දාලා තියනවා."),
    (f"{TSUK}あとで、もとに {MOD}て {OKI} ください。","Tsukatta ato de, moto ni modoshite oite kudasai.","After using it, please put it back.","පාවිච්චි කරලා ආපහු තියන්න."),
    (f"あした テストなので、{r('今日','きょう')} {r('勉強','べん きょう')}して {OKI}。","Ashita tesuto na node, kyou benkyou shite okimasu.","There's a test tomorrow, so I'll study today.","හෙට විභාගය නිසා අද ඉගෙන ගෙන තියනවා."),
  ],
  foot="〜て おきます",
)

if __name__ == "__main__":
    render(P, "u93_teoku")
