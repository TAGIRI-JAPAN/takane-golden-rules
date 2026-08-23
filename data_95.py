from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KAT  = r("買","か")+"って"
KI   = "きます"
KIM  = "きました"
IKI  = "いきます"
BEN  = r("弁当","べん とう")
MOT  = r("持","も")+"って"
SAM  = r("寒","さむ")+"く"
NAT  = "なって"
ATSU = r("暑","あつ")+"く"
NHG  = r("日本語","に ほん ご")
JOZ  = r("上手","じょう ず")
KOD  = r("子","こ")+"ども"
FUE  = r("増","ふ")+"えて"
TSUZ = r("続","つづ")+"けて"
KAER = r("帰","かえ")+"って"
HASH = r("走","はし")+"って"
IMA  = r("今","いま")
MIRA = r("未来","み らい")
KAK  = r("過去","か こ")

P = dict(
  no="95", tag=None,
  title_jp="〜て いきます／〜て きます",
  title_ro='〜 te ikimasu / te kimasu &nbsp;|&nbsp; going / coming, and change over time &nbsp;|&nbsp; '
           '<span class="si">〜 වෙලා යනවා / එනවා</span>',
  basic=(f"コンビニで {BEN}を {KAT} {KI}。","Konbini de bentou wo katte kimasu.",
         "I'll go buy a lunch box and come back.","කඩෙන් බත් පැකට් එකක් අරන් එන්නම්."),
  use=(f'{r("意味","い み")}は 2つ。①<b>{r("動作","どう さ")}＋いく／くる</b>'
       f'（{KAT} きます＝{r("買","か")}って もどる）。'
       f'②<b>{r("変化","へん か")}</b>：{r("今","いま")}から さきは「〜て いきます」、'
       f'{KAK}から {IMA}までは「〜て きます」。',
       'Two meanings. (1) action + go/come: <b>katte kimasu</b> = go, buy, come back. '
       '(2) change over time: <b>te ikimasu</b> looks forward, <b>te kimasu</b> looks back.',
       'අර්ථ දෙකයි. (1) ක්‍රියාව + යනවා/එනවා. '
       '(2) කාලයත් එක්ක වෙනස: <b>te ikimasu</b> ඉදිරියට, <b>te kimasu</b> අතීතයේ සිට දැන් දක්වා.'),
  pattern=[["BLANK",("て きます","te kimasu",True)],
           ["BLANK",("て いきます","te ikimasu",True)],
           f"NOTE:①{r('動作','どう さ')}：{KAT} きます（{r('買','か')}って もどる）　/　"
           f"{MOT} いきます（{r('持','も')}って {r('行','い')}く）",
           f"NOTE:②{r('変化','へん か')}：これから {SAM} {NAT} いきます（{MIRA}）　⇔　"
           f"だんだん {JOZ}に {NAT} きました（{KAK}→{IMA}）"],
  examples=[
    (f"コンビニで {BEN}を {KAT} {KI}。","Konbini de bentou wo katte kimasu.","I'll go buy a lunch box and come back.","කඩෙන් බත් පැකට් එකක් අරන් එන්නම්."),
    (f"かさを {MOT} {IKI}。","Kasa wo motte ikimasu.","I'll take an umbrella with me.","කුඩය අරන් යනවා."),
    (f"これから {SAM} {NAT} {IKI}。","Kore kara samuku natte ikimasu.","It will get colder from now on.","මෙතන ඉඳන් සීතල වෙලා යනවා."),
    (f"だんだん {NHG}が {JOZ}に {NAT} {KIM}。","Dandan nihongo ga jouzu ni natte kimashita.","My Japanese has gradually got better.","ටිකෙන් ටික ජපන් භාෂාව හොඳ වෙලා ආවා."),
    (f"{KOD}が {FUE} {KIM}。","Kodomo ga fuete kimashita.","The number of children has been increasing.","ළමයි ගාන වැඩි වෙලා ආවා."),
    (f"これからも {r('勉強','べん きょう')}を {TSUZ} {IKI}。","Kore kara mo benkyou wo tsuzukete ikimasu.","I'll keep studying from now on too.","මෙතන ඉඳනුත් ඉගෙනීම දිගටම කරගෙන යනවා."),
    (f"はしって {KAER} {KIM}。","Hashitte kaette kimashita.","I ran back home.","දුවගෙන ගෙදර ආවා."),
  ],
  foot="〜て いきます／〜て きます",
)

if __name__ == "__main__":
    render(P, "u95_teiku")
