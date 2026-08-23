from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NIH  = r("日本","に ほん")
IKO  = r("行","い")+"こう"
OMO  = r("思","おも")+"って います"
DAI  = r("大学","だい がく")
HAIR = r("入","はい")+"ろう"
KURU = r("車","くるま")
KAO  = r("買","か")+"おう"
YASU = r("休","やす")+"もう"
HAJI = r("始","はじ")+"めよう"
BEN  = r("勉強","べん きょう")
SHIY = "しよう"
KAER = r("帰","かえ")+"ろう"
ISHI = r("意志","い し")
KEIK = r("計画","けい かく")
TABE = r("食","た")+"べよう"

P = dict(
  no="90", tag=None,
  title_jp="意向形（〜よう）＋と 思って います",
  title_ro='volitional + to omotte imasu &nbsp;|&nbsp; I\'m thinking of 〜ing &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න හිතාගෙන ඉන්නවා</span>',
  basic=(f"{r('来年','らい ねん')} {NIH}へ {IKO}と {OMO}。","Rainen Nihon e ikou to omotte imasu.",
         "I'm thinking of going to Japan next year.","ලබන අවුරුද්දේ ජපානෙට යන්න හිතාගෙන ඉන්නවා."),
  use=(f'「〜ましょう」の ふつうけいが <b>{r("意向","い こう")}{r("形","けい")}</b>です。'
       f'これに「と {OMO}」を つけると、じぶんの {KEIK}を ひかえめに {r("言","い")}えます。'
       f'57の「つもりです」より すこし やわらかいです。',
       'The plain form of <b>~ mashou</b> is the volitional. Adding <b>to omotte imasu</b> '
       'lets you state your plan modestly — softer than <b>tsumori</b> in 57.',
       '<b>~ mashou</b> එකේ සරල ආකාරය තමයි volitional. ඒකට <b>to omotte imasu</b> දැම්මම '
       'තමන්ගේ සැලසුම මෘදුව කියන්න පුළුවන් — 57 හි <b>tsumori</b> වලට වඩා මෘදුයි.'),
  pattern=[["BLANK",("（よ）うと","(y)ou to",True),(f"{OMO}","omotte imasu",True)],
           f"NOTE:Iグループ：{r('行','い')}く → {IKO}　/　{r('買','か')}う → {KAO}　"
           f"IIグループ：{r('食','た')}べる → {TABE}　"
           f"IIIグループ：する → {SHIY}　/　{r('来','く')}る → {r('来','こ')}よう",
           f"NOTE:57 つもりです（つよい {ISHI}）　⇔　90 と {OMO}（まだ かんがえて いる）"],
  examples=[
    (f"{r('来年','らい ねん')} {NIH}へ {IKO}と {OMO}。","Rainen Nihon e ikou to omotte imasu.","I'm thinking of going to Japan next year.","ලබන අවුරුද්දේ ජපානෙට යන්න හිතාගෙන ඉන්නවා."),
    (f"{DAI}に {HAIR}と {OMO}。","Daigaku ni hairou to omotte imasu.","I'm thinking of going to university.","විශ්වවිද්‍යාලයට යන්න හිතාගෙන ඉන්නවා."),
    (f"{KURU}を {KAO}と {OMO}。","Kuruma wo kaou to omotte imasu.","I'm thinking of buying a car.","කාරයක් ගන්න හිතාගෙන ඉන්නවා."),
    (f"{r('今日','きょう')}は はやく {YASU}と {OMO}。","Kyou wa hayaku yasumou to omotte imasu.","I'm thinking of resting early today.","අද ඉක්මනට විවේක ගන්න හිතාගෙන ඉන්නවා."),
    (f"アルバイトを {HAJI}と {OMO}。","Arubaito wo hajimeyou to omotte imasu.","I'm thinking of starting a part-time job.","අර්ධකාලීන රැකියාවක් පටන් ගන්න හිතාගෙන ඉන්නවා."),
    (f"{r('毎日','まい にち')} {BEN}{SHIY}と {OMO}。","Mainichi benkyou shiyou to omotte imasu.","I'm thinking of studying every day.","හැමදාම ඉගෙන ගන්න හිතාගෙන ඉන්නවා."),
    (f"そろそろ {KAER}。","Sorosoro kaerou.","Let's head home soon.","දැන් ගෙදර යමු."),
  ],
  foot="意向形（〜よう）＋と 思って います",
)

if __name__ == "__main__":
    render(P, "u90_ikou")
