from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HASH = r("走","はし")+"れ"
TOM  = r("止","と")+"まれ"
HAI  = r("入","はい")+"るな"
SUW  = r("吸","す")+"うな"
GANB = "がんばれ"
KIK  = r("聞","き")+"け"
DAS  = r("出","だ")+"すな"
KAN  = r("看板","かん ばん")
SEN  = r("先生","せん せい")
TSUY = r("強","つよ")+"い"
SHIJ = r("指示","し じ")
YOM  = r("読","よ")+"む"
KAKI = r("書","か")+"け"
KOR  = r("来","こ")+"い"
SHIR = "しろ"

P = dict(
  no="91", tag=None,
  title_jp="命令形・禁止形",
  title_ro='imperative &amp; prohibitive &nbsp;|&nbsp; Do it! / Don\'t! &nbsp;|&nbsp; '
           '<span class="si">අණ කිරීම / තහනම</span>',
  basic=(f"ここに {HAI}。","Koko ni hairu na.",
         "Do not enter here.","මෙතනට ඇතුළු වෙන්න එපා."),
  use=(f'いちばん {TSUY} {SHIJ}の かたちです。'
       f'ふだんの かいわでは <b>つかいません</b>。'
       f'でも {KAN}・{r("注意","ちゅう い")}がき・スポーツの おうえんで <b>{YOM}</b> ひつようが あります。',
       'This is the strongest way to order someone. You will <b>not use it</b> in normal '
       'conversation — but you must be able to <b>read</b> it on signs and notices.',
       'ශක්තිමත්ම අණ කිරීමේ ආකාරය. සාමාන්‍ය කතාබහේ <b>පාවිච්චි කරන්නේ නැහැ</b> — '
       'හැබැයි දැන්වීම් පුවරු කියවන්න මේක <b>දැනගන්නම ඕනේ</b>.'),
  pattern=[["BLANK",("しろ（めいれい）","shiro",True)],
           ["BLANK",("するな（きんし）","suru na",True)],
           f"NOTE:めいれい：{r('書','か')}く → {KAKI}　/　{r('食','た')}べる → {r('食','た')}べろ　/　"
           f"する → {SHIR}　/　{r('来','く')}る → {KOR}　　きんし：じしょけい ＋ な",
           f"NOTE:69「しなさい」＜ 91「しろ」。{SEN}や {r('親','おや')}でも "
           f"ふつうは 69か「〜て ください」（72）を つかいます"],
  examples=[
    (f"ここに {HAI}。","Koko ni hairu na.","Do not enter here.","මෙතනට ඇතුළු වෙන්න එපා."),
    (f"{TOM}。","Tomare.","Stop.","නවතින්න."),
    (f"ここで タバコを {SUW}。","Koko de tabako wo suu na.","Don't smoke here.","මෙතන දුම් බොන්න එපා."),
    (f"{GANB}！","Ganbare!","Go for it!","දිගටම කරන්න!"),
    (f"よく {KIK}。","Yoku kike.","Listen carefully.","හොඳට අහන්න."),
    (f"ゴミを {DAS}。","Gomi wo dasu na.","Don't put rubbish out (here).","කුණු දාන්න එපා."),
    (f"はやく {HASH}。","Hayaku hashire.","Run fast.","ඉක්මනට දුවන්න."),
  ],
  foot="命令形・禁止形",
)

if __name__ == "__main__":
    render(P, "u91_meirei")
