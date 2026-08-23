from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

RAIN = r("来年","らい ねん")
NIH  = r("日本","に ほん")
IKU  = r("行","い")+"く"
KYO  = r("今日","きょう")
HAYA = r("早","はや")+"く"
NER  = r("寝","ね")+"る"
SHUM = r("週末","しゅう まつ")
IE   = r("家","いえ")
YASU = r("休","やす")+"む"
RAIG = r("来月","らい げつ")
W    = r("私","わたし")
KURU = r("車","くるま")
KAWA = r("買","か")+"わない"
DAI  = r("大学","だい がく")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
ASHI = r("明日","あ した")
SEN  = r("先生","せん せい")
KIK  = r("聞","き")+"く"
ISHI = r("意志","い し")

P55 = dict(
  no="66", tag=None,
  title_jp="〜する つもりです",
  title_ro='〜 suru tsumori desu &nbsp;|&nbsp; I intend to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න හිතාගෙන ඉන්නවා</span>',
  basic=(f"{RAIN} {NIH}へ {IKU} つもりです。","Rainen Nihon e iku tsumori desu.",
         "I intend to go to Japan next year.","ලබන අවුරුද්දේ ජපානෙට යන්න හිතාගෙන ඉන්නවා."),
  use=(f'{r("自分","じ ぶん")}の {ISHI}（そう しようと {r("決","き")}めた {r("気持","き も")}ち）を{r("言","い")}います。'
       f'64の「はずです」は そうなる はずと いう よそうで、ちがいます。',
       'It states your own intention — what you have decided to do. '
       'It is different from <b>hazu desu</b> (64), which is an expectation.',
       'තමන් තීරණය කරගත් අදහස කියනවා. '
       '64 හි <b>hazu desu</b> කියන්නේ බලාපොරොත්තුවක් — ඒක වෙනස්.'),
  pattern=[[("〜は","~ wa"),"BLANK",("つもりです","tsumori desu",True)],
           f"NOTE:ふつうけいに つけます：{IKU} つもり　/　{r('行','い')}かない つもり（＝しないと {r('決','き')}めた）",
           f"NOTE:「〜つもりでした」＝ そう {r('思','おも')}って いたが、しなかった とき"],
  examples=[
    (f"{RAIN} {NIH}へ {IKU} つもりです。","Rainen Nihon e iku tsumori desu.","I intend to go to Japan next year.","ලබන අවුරුද්දේ ජපානෙට යන්න හිතාගෙන ඉන්නවා."),
    (f"{KYO}は {HAYA} {NER} つもりです。","Kyou wa hayaku neru tsumori desu.","I'm going to go to bed early today.","අද ඉක්මනට නිදාගන්න හිතාගෙන ඉන්නවා."),
    (f"{SHUM}は {IE}で {YASU} つもりです。","Shuumatsu wa ie de yasumu tsumori desu.","I plan to rest at home this weekend.","සති අන්තයේ ගෙදර විවේක ගන්න හිතාගෙන ඉන්නවා."),
    (f"{RAIG}から アルバイトを する つもりです。","Raigetsu kara arubaito wo suru tsumori desu.","I plan to start a part-time job next month.","ලබන මාසෙ ඉඳන් අර්ධකාලීන රැකියාවක් කරන්න හිතාගෙන ඉන්නවා."),
    (f"{W}は {KURU}を {KAWA} つもりです。","Watashi wa kuruma wo kawanai tsumori desu.","I don't intend to buy a car.","මම කාරයක් ගන්න හිතාගෙන නැහැ."),
    (f"サマンさんは {DAI}に {r('入','はい')}る つもりです。","Saman-san wa daigaku ni hairu tsumori desu.","Saman plans to enter university.","සමන් විශ්වවිද්‍යාලයට යන්න හිතාගෙන ඉන්නවා."),
    (f"{ASHI} {SEN}に {KIK} つもりです。","Ashita sensei ni kiku tsumori desu.","I intend to ask the teacher tomorrow.","හෙට ගුරුතුමාගෙන් අහන්න හිතාගෙන ඉන්නවා."),
  ],
  foot="〜する つもりです",
)

if __name__ == "__main__":
    render(P55, "p66_tsumori")
