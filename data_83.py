from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

BOT  = "ボタン"
OS   = r("押","お")+"す"
DE   = r("出","で")+"ます"
HARU = r("春","はる")
NAR  = "なると"
HANA = r("花","はな")
SAK  = r("咲","さ")+"きます"
MIG  = r("右","みぎ")
MAG  = r("曲","ま")+"がる"
EKI  = r("駅","えき")
KOK  = "この こうさてん"
HAYA = r("早","はや")+"く"
IK   = r("行","い")+"かないと"
MAA  = r("間","ま")+"に"+r("合","あ")+"いません"
KUS  = r("薬","くすり")
NOM  = r("飲","の")+"むと"
YOK  = "よく なります"
SHIZ = r("自然","し ぜん")
KEK  = r("結果","けっ か")
IRE  = r("入","い")+"れると"

P = dict(
  no="83", tag=None,
  title_jp="〜と、〜",
  title_ro='〜 to, 〜 &nbsp;|&nbsp; whenever / if A then always B &nbsp;|&nbsp; '
           '<span class="si">〜 කළාම, 〜</span>',
  basic=(f"この {BOT}を {OS}と、きっぷが {DE}。","Kono botan wo osu to, kippu ga demasu.",
         "If you press this button, a ticket comes out.","මේ බොත්තම එබුවම ටිකට් එක එනවා."),
  use=(f'「A すると かならず B に なる」と いう <b>{SHIZ}な {KEK}</b>を {r("言","い")}います。'
       f'{r("機械","き かい")}・{r("道","みち")}あんない・{SHIZ}の ことに つかいます。'
       f'まえは <b>じしょけい</b>か <b>ない{r("形","けい")}</b>です。',
       'It states a natural result: "whenever A, B always happens". Used for machines, '
       'directions and nature. The dictionary form or nai-form comes before <b>to</b>.',
       '"A කළාම හැමවිටම B වෙනවා" කියන <b>ස්වාභාවික ප්‍රතිඵලය</b>. '
       'යන්ත්‍ර, පාර කීම, ස්වභාවධර්මය. කලින් ශබ්දකෝෂ ආකාරය හෝ nai-ආකාරය.'),
  pattern=[["BLANK",("と、","to",True),("〜ます","~ masu")],
           f"NOTE:うしろに <b>めいれい・おねがい・いし</b>は {r('置','お')}けません。"
           f"「〜と、{r('行','い')}って ください」× → 82の「〜たら」を つかいます",
           f"NOTE:82 たら（1{r('回','かい')}の じょうけん）　⇔　83 と（いつも {r('同','おな')}じ {KEK}）"],
  examples=[
    (f"この {BOT}を {OS}と、きっぷが {DE}。","Kono botan wo osu to, kippu ga demasu.","If you press this button, a ticket comes out.","මේ බොත්තම එබුවම ටිකට් එක එනවා."),
    (f"{HARU}に {NAR}、{HANA}が {SAK}。","Haru ni naru to, hana ga sakimasu.","When spring comes, the flowers bloom.","වසන්තය ආවම මල් පිපෙනවා."),
    (f"{KOK}を {MIG}に {MAG}と、{EKI}が あります。","Kono kousaten wo migi ni magaru to, eki ga arimasu.","If you turn right at this crossing, there's the station.","මේ හන්දියෙන් දකුණට හැරුණම දුම්රියපොළ තියෙනවා."),
    (f"{KUS}を {NOM}、{YOK}。","Kusuri wo nomu to, yoku narimasu.","If you take the medicine, you get better.","බෙහෙත බිව්වම හොඳ වෙනවා."),
    (f"{HAYA} {IK}、{MAA}。","Hayaku ikanai to, ma ni aimasen.","If you don't go early, you won't make it.","ඉක්මනට ගියේ නැත්නම් වෙලාවට යන්න බැහැ."),
    (f"さとうを {IRE}、あまく なります。","Satou wo ireru to, amaku narimasu.","If you add sugar, it gets sweet.","සීනි දැම්මම පැණි රස වෙනවා."),
    (f"この まどを {r('開','あ')}けると、{r('海','うみ')}が {r('見','み')}えます。","Kono mado wo akeru to, umi ga miemasu.","If you open this window, you can see the sea.","මේ ජනේලය ඇරියම මුහුද පේනවා."),
  ],
  foot="〜と、〜",
)

if __name__ == "__main__":
    render(P, "u83_to_jouken")
