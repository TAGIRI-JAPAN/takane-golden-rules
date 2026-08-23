from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

BEN  = r("勉強","べん きょう")
DEK  = "できませんでした"
YAK  = r("約束","やく そく")
KI   = r("来","き")+"ません"
AME  = r("雨","あめ")
FUT  = r("降","ふ")+"って いる"
KASA = "かさ"
MOT  = r("持","も")+"って"
IKI  = r("行","い")+"きました"
YASU = r("安","やす")+"い"
KAWA = r("買","か")+"いませんでした"
DEN  = r("電話","でん わ")
DE   = r("出","で")+"ません"
NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"しません"
KUSU = r("薬","くすり")
NAO  = r("治","なお")+"りません"
ZAN  = r("残念","ざん ねん")
IGAI = r("意外","い がい")

P = dict(
  no="79", tag=None,
  title_jp="〜のに、〜",
  title_ro='〜 noni &nbsp;|&nbsp; even though / although 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 උනත්</span>',
  basic=(f"たくさん {BEN}したのに、{DEK}。","Takusan benkyou shita noni, dekimasen deshita.",
         "Even though I studied a lot, I couldn't do it.","ගොඩක් ඉගෙන ගත්තත් කරන්න බැරි වුණා."),
  use=(f'「そう なる はずなのに、ならなかった」と いう {ZAN}・{IGAI}の {r("気持","き も")}ちが '
       f'{r("入","はい")}ります。87の「〜が、〜けど」より {r("気持","き も")}ちが つよいです。'
       f'めいし・な けいようしには「<b>な</b>のに」。',
       'It carries a feeling of disappointment or surprise: "it should have been so, but '
       'it was not". Stronger than <b>ga / kedo</b> in 87. Nouns take <b>na noni</b>.',
       'බලාපොරොත්තු වුණ දේ නොවුණාම දැනෙන කලකිරීම හෝ පුදුමය. '
       '87 හි <b>ga / kedo</b> වලට වඩා හැඟීම ශක්තිමත්. නාම පදවලට <b>na noni</b>.'),
  pattern=[["BLANK",("のに、","noni",True),("〜ました","~ mashita")],
           f"NOTE:ふつうけい ＋ のに：{BEN}したのに　/　{YASU}のに　/　"
           f"{r('元気','げん き')}<b>な</b>のに　/　{r('学生','がく せい')}<b>な</b>のに",
           f"NOTE:87 が・けど（ただ はんたい）　⇔　79 のに（{ZAN}・{IGAI}の {r('気持','き も')}ち）"],
  examples=[
    (f"たくさん {BEN}したのに、{DEK}。","Takusan benkyou shita noni, dekimasen deshita.","Even though I studied a lot, I couldn't do it.","ගොඩක් ඉගෙන ගත්තත් කරන්න බැරි වුණා."),
    (f"{YAK}したのに、サマンさんは {KI}。","Yakusoku shita noni, Saman-san wa kimasen.","Even though we promised, Saman isn't coming.","පොරොන්දු වුණත් සමන් එන්නේ නැහැ."),
    (f"{AME}が {FUT}のに、{KASA}を {MOT}ないで {IKI}。","Ame ga futte iru noni, kasa wo motanaide ikimashita.","Even though it's raining, he went without an umbrella.","වහිනවා උනත් කුඩය නැතුව ගියා."),
    (f"{YASU}のに、だれも {KAWA}。","Yasui noni, dare mo kaimasen deshita.","Even though it was cheap, nobody bought it.","ලාබ උනත් කවුරුත් ගත්තේ නැහැ."),
    (f"{DEN}したのに、{DE}。","Denwa shita noni, demasen.","Even though I called, he doesn't answer.","කතා කළත් උත්තර දෙන්නේ නැහැ."),
    (f"{r('日本人','に ほん じん')}なのに、{NHG}を あまり {HAN}。","Nihonjin na noni, nihongo wo amari hanashimasen.","Even though he's Japanese, he hardly speaks Japanese.","ජපන් ජාතිකයෙක් උනත් ජපන් භාෂාව එච්චර කතා කරන්නේ නැහැ."),
    (f"{KUSU}を {r('飲','の')}んだのに、{NAO}。","Kusuri wo nonda noni, naorimasen.","Even though I took the medicine, I'm not better.","බෙහෙත් බිව්වත් හොඳ වෙන්නේ නැහැ."),
  ],
  foot="〜のに、〜",
)

if __name__ == "__main__":
    render(P, "u79_noni")
