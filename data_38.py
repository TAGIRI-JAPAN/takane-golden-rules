from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
ISS  = r("一緒","いっ しょ")
NIM  = r("荷物","に もつ")
MOT  = r("持","も")+"ちましょうか"
MAD  = r("窓","まど")
AKE  = r("開","あ")+"けましょうか"
SEN  = r("先生","せん せい")
KIK  = r("聞","き")+"きましょうか"
HAJ  = r("始","はじ")+"めましょうか"
KAE  = r("帰","かえ")+"りましょうか"
YAS  = r("休","やす")+"みましょうか"
KASH = r("貸","か")+"しましょうか"
KAS  = "かさ"

P27 = dict(
  no="38", tag=None,
  title_jp="〜しましょうか？",
  title_ro='〜 shimashou ka &nbsp;|&nbsp; Shall we / Shall I 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කරමුද? / කරන්නද?</span>',
  basic=(f"{NIM}を {MOT}。","Nimotsu wo mochimashou ka.",
         "Shall I carry your bag?","මම බඩු අරන් යන්නද?"),
  use=(f'{r("意味","い み")}が 2つ あります。①「{ISS}に しましょう」という さそい。'
       f'②「{W}が しましょうか」という{r("申","もう")}し{r("出","で")}。37の「しませんか」は さそいだけです。',
       'It has two meanings: (1) "let’s do it together" — an invitation, and '
       '(2) "shall I do it for you?" — an offer. Pattern 37 <b>shimasen ka</b> is only an invitation.',
       'අර්ථ දෙකක් තියෙනවා: (1) "අපි එකට කරමු" කියන ආරාධනාව, '
       '(2) "මම කරන්නද?" කියන ඉදිරිපත් වීම. 37 හි <b>shimasen ka</b> කියන්නේ ආරාධනාව විතරයි.'),
  pattern=[["BLANK",("しましょうか？","shimashou ka",True)],
           f"NOTE:① {ISS}に しましょう（さそい）　　② {W}が しましょうか（{r('申','もう')}し{r('出','で')}）",
           f"NOTE:{r('答','こた')}え{r('方','かた')}：はい、おねがいします　/　いいですね　/　"
           f"だいじょうぶです　（කරුණාකරලා　/　හොඳයි නේ　/　කමක් නැහැ）"],
  examples=[
    (f"{NIM}を {MOT}。","Nimotsu wo mochimashou ka.","Shall I carry your bag?","මම බඩු අරන් යන්නද?"),
    (f"{MAD}を {AKE}。","Mado wo akemashou ka.","Shall I open the window?","මම ජනේලය අරින්නද?"),
    (f"{SEN}に {KIK}。","Sensei ni kikimashou ka.","Shall I ask the teacher?","මම ගුරුතුමාගෙන් අහන්නද?"),
    (f"{KAS}を {KASH}。","Kasa wo kashimashou ka.","Shall I lend you an umbrella?","මම කුඩය දෙන්නද?"),
    (f"そろそろ {HAJ}。","Sorosoro hajimemashou ka.","Shall we start now?","අපි දැන් පටන් ගමුද?"),
    (f"{ISS}に {KAE}。","Isshoni kaerimashou ka.","Shall we go home together?","අපි එකට ගෙදර යමුද?"),
    (f"ちょっと {YAS}。","Chotto yasumimashou ka.","Shall we take a short break?","අපි ටිකක් විවේක ගමුද?"),
  ],
  foot="〜しましょうか？",
)

if __name__ == "__main__":
    render(P27, "p38_shimashouka")
