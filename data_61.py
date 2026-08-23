from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MIZU = r("水","みず")
KOBO = "こぼれそうです"
KAB  = "かばん"
TOR  = "とれそうです"
JUG  = r("授業","じゅ ぎょう")
OWA  = r("終","お")+"わりそうです"
KI   = r("木","き")
TAO  = "たおれそうです"
IMA  = r("今","いま")
NAK  = r("泣","な")+"きそうです"
SHIK = r("試験","し けん")
GOK  = r("合格","ごう かく")
W    = r("私","わたし")
DEK  = "できそうです"
FUR  = r("降","ふ")+"りそう"
YOU  = r("様子","よう す")

P57 = dict(
  no="61", tag=None,
  title_jp="〜しそうです（もうすぐ）",
  title_ro='〜 shisou desu &nbsp;|&nbsp; about to 〜 &nbsp;|&nbsp; '
           '<span class="si">දැන් දැන් 〜 වෙයි වගේ</span>',
  basic=(f"コップの {MIZU}が {KOBO}。","Koppu no mizu ga koboresou desu.",
         "The water in the cup is about to spill.","කෝප්පෙ වතුර දැන් දැන් වැගිරෙයි වගේ."),
  use=(f'60の「そうです」は けいようしで「{YOU}」でしたが、61は どうしに つけて '
       f'「もうすぐ そうなる」と{r("言","い")}います。',
       'In 60 <b>sou desu</b> went with adjectives to describe how something looks. '
       'Here it goes with verbs to say something is about to happen.',
       '60 හි <b>sou desu</b> විශේෂණ එක්ක "පේන විදිහ" කිව්වා. '
       'මෙතන ක්‍රියා එක්ක "දැන් දැන් වෙයි" කියනවා.'),
  pattern=[[("〜が","~ ga"),"BLANK",("しそうです","shisou desu",True)],
           f"NOTE:ますけい ＋ そう：{r('降','ふ')}ります → {FUR}　/　{r('終','お')}わります → "
           f"{r('終','お')}わりそう　/　こぼれます → こぼれそう",
           f"NOTE:60（けいようし・{YOU}）　⇔　61（どうし・もうすぐ そうなる）"],
  examples=[
    (f"コップの {MIZU}が {KOBO}。","Koppu no mizu ga koboresou desu.","The water in the cup is about to spill.","කෝප්පෙ වතුර දැන් දැන් වැගිරෙයි වගේ."),
    (f"{KAB}の ボタンが {TOR}。","Kaban no botan ga toresou desu.","The button on the bag is about to come off.","බෑග් එකේ බොත්තම ගැලවෙන්න යනවා."),
    (f"{JUG}が もうすぐ {OWA}。","Jugyou ga mousugu owarisou desu.","The class is about to finish.","පන්තිය දැන් දැන් ඉවර වෙයි වගේ."),
    (f"あの {KI}が {TAO}。","Ano ki ga taoresou desu.","That tree looks about to fall.","අර ගහ කඩාවැටෙන්න යනවා."),
    (f"サマンさんは {IMA}にも {NAK}。","Saman-san wa ima ni mo nakisou desu.","Saman looks about to cry.","සමන් දැන් දැන් අඬයි වගේ."),
    (f"この {SHIK}は {GOK}しそうです。","Kono shiken wa goukaku shisou desu.","It looks like I'll pass this exam.","මේ විභාගය සමත් වෙයි වගේ."),
    (f"これなら {W}にも {DEK}。","Kore nara watashi ni mo dekisou desu.","If it's this, it looks like I can do it too.","මේක නම් මටත් කරන්න පුළුවන් වගේ."),
  ],
  foot="〜しそうです（もうすぐ）",
)

if __name__ == "__main__":
    render(P57, "p61_shisou")
