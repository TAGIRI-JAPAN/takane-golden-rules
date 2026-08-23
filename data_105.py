from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

AKA  = r("赤","あか")+"い"
KAB  = "かばん"
KIP  = "きっぷ"
NIM  = r("二枚","に まい")
HASH = "はし"
FUK  = r("袋","ふくろ")
SUKO = r("少","すこ")+"し"
JIK  = r("時間","じ かん")
MEN  = "メニュー"
MONO = r("物","もの")
KOUI = r("行為","こう い")

P70 = dict(
  no="105", tag=None,
  title_jp="〜を ください",
  title_ro='〜 wo kudasai &nbsp;|&nbsp; Please give me 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 දෙන්න</span>',
  basic=("これを ください。","Kore wo kudasai.",
         "Please give me this one.","මේක දෙන්න."),
  io=None,
  use=(f'{MONO}を もらいたい ときの ことばです。104の「お{r("願","ねが")}いします」より '
       f'かんたんで、{r("店","みせ")}で よく つかいます。{KOUI}を たのむ ときは 106です。',
       'Use it when you want to receive a thing. Simpler than <b>onegai shimasu</b> (104) '
       'and very common in shops. To ask for an action, use 106.',
       'දෙයක් ලබාගන්න ඕන වෙලාවට. 104 හි <b>onegai shimasu</b> වලට වඩා සරලයි, '
       'කඩවල බහුලයි. ක්‍රියාවක් ඉල්ලන්නේ නම් 106.'),
  pattern=[["BLANK",("を ください","wo kudasai",True)],
           f"NOTE:105 ＝ {MONO}を もらう　⇔　106 ＝ {KOUI}を たのむ（して ください）",
           f"NOTE:104「お{r('願','ねが')}いします」の ほうが ていねいで やわらかいです"],
  examples=[
    ("これを ください。","Kore wo kudasai.","Please give me this one.","මේක දෙන්න."),
    (f"あの {AKA} {KAB}を ください。","Ano akai kaban wo kudasai.","Please give me that red bag.","අර රතු බෑග් එක දෙන්න."),
    (f"{KIP}を {NIM} ください。","Kippu wo nimai kudasai.","Two tickets, please.","ටිකට් දෙකක් දෙන්න."),
    (f"すみません、{HASH}を ください。","Sumimasen, hashi wo kudasai.","Excuse me, chopsticks please.","සමාවෙන්න, චොප්ස්ටික් දෙන්න."),
    (f"{FUK}を ください。","Fukuro wo kudasai.","Please give me a bag.","බෑග් එකක් දෙන්න."),
    (f"もう {SUKO} {JIK}を ください。","Mou sukoshi jikan wo kudasai.","Please give me a little more time.","තව ටිකක් වෙලාව දෙන්න."),
    (f"{MEN}を ください。","Menyuu wo kudasai.","The menu, please.","මෙනුව දෙන්න."),
  ],
  foot="〜を ください",
)
P70.pop("io")

if __name__ == "__main__":
    render(P70, "p105_wokudasai")
