from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KARE = "カレー"
KEK  = "ケーキ"
HON  = r("本","ほん")
IMA  = r("今","いま")
AME  = r("雨","あめ")
FURI = r("降","ふ")+"り"
KO   = r("子","こ")
KASA = "かさ"
MIM  = r("見","み")+"て"
KII  = r("聞","き")+"いた"
ASHI = r("明日","あ した")

P40 = dict(
  no="60", tag=None,
  title_jp="〜そうです（ようす）",
  title_ro='〜 sou desu &nbsp;|&nbsp; It looks 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වගේ පේනවා</span>',
  basic=(f"この {KARE}は からそうです。","Kono karee wa karasou desu.",
         "This curry looks spicy.","මේ කරිය සැරයි වගේ පේනවා."),
  use=(f'{MIM} 「そう {r("見","み")}える」と{r("言","い")}う ことばです。57の「そうです」（{KII} '
       f'{r("話","はなし")}）とは ちがうので {r("注意","ちゅう い")}して ください。',
       'Use it for how something <b>looks</b> to you. Be careful: this is NOT the '
       '<b>sou desu</b> of pattern 57, which passes on what you heard.',
       'දෙයක් <b>පේන</b> විදිහ කියන්න. 57 හි <b>sou desu</b> (අහපු දේ කීම) එක්ක '
       'පටලවා ගන්න එපා.'),
  pattern=[[("〜は","~ wa"),"BLANK",("そうです","sou desu",True)],
           [("〜が","~ ga"),"BLANK",("そうです","sou desu",True)],
           f"NOTE:からい → からそう　/　しずかな → しずかそう　/　{r('降','ふ')}ります → {FURI}そう"
           f"（さいごの「い」「な」「ます」を とります）",
           f"NOTE:{ASHI}は {AME}だそうです（57＝{KII}）　/　{IMA}にも {AME}が {FURI}そうです（60＝{MIM}）",
           f"NOTE:とくべつ：いい → よさそう　/　ない → なさそう　（めいしには つきません）"],
  examples=[
    (f"この {KARE}は からそうです。","Kono karee wa karasou desu.","This curry looks spicy.","මේ කරිය සැරයි වගේ පේනවා."),
    (f"その {KEK}は おいしそうです。","Sono keeki wa oishisou desu.","That cake looks delicious.","ඒ කේක් එක රසයි වගේ පේනවා."),
    ("サマンさんは うれしそうです。","Saman-san wa ureshisou desu.","Saman looks happy.","සමන් සතුටින් වගේ පේනවා."),
    (f"この {HON}は むずかしそうです。","Kono hon wa muzukashisou desu.","This book looks difficult.","මේ පොත අමාරුයි වගේ පේනවා."),
    (f"{IMA}にも {AME}が {FURI}そうです。","Ima ni mo ame ga furisou desu.","It looks like it's about to rain.","දැන් දැන් වහියි වගේ."),
    (f"あの {KO}は ねむそうです。","Ano ko wa nemusou desu.","That child looks sleepy.","අර ළමයට නිදිමතයි වගේ පේනවා."),
    (f"この {KASA}は よさそうです。","Kono kasa wa yosasou desu.","This umbrella looks good.","මේ කුඩය හොඳයි වගේ පේනවා."),
  ],
  foot="〜そうです（ようす）",
)

if __name__ == "__main__":
    render(P40, "p60_sou_yousu")
