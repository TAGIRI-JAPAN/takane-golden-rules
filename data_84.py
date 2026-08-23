from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

REN  = r("練習","れん しゅう")
DEK  = "できます"
YASU = r("安","やす")+"ければ"
KAI  = r("買","か")+"います"
JIK  = r("時間","じ かん")
IK   = r("行","い")+"きます"
KUSU = r("薬","くすり")
NOM  = r("飲","の")+"めば"
NAO  = r("治","なお")+"ります"
BEN  = r("勉強","べん きょう")
UKA  = r("受","う")+"かります"
TEN  = r("天気","てん き")
UMI  = r("海","うみ")
DOU  = "どう すれば"
MICH = r("道","みち")
KIK  = r("聞","き")+"けば"
WAK  = "わかります"
JOU  = r("条件","じょう けん")
KAK  = r("書","か")+"けば"

P = dict(
  no="84", tag=None,
  title_jp="〜ば、〜",
  title_ro='〜 ba, 〜 &nbsp;|&nbsp; if 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 නම්, 〜</span>',
  basic=(f"たくさん {REN}すれば、{DEK}よ。","Takusan renshuu sureba, dekimasu yo.",
         "If you practise a lot, you'll be able to do it.","ගොඩක් පුහුණු වුණොත් පුළුවන් වේවි."),
  use=(f'82の「たら」と {r("同","おな")}じ {JOU}ですが、'
       f'「ば」は <b>{r("書","か")}きことば</b>や <b>ことわざ</b>で よく つかいます。'
       f'「どう すれば いいですか」は とても べんりな フレーズです。',
       'The same kind of condition as <b>tara</b> (82), but <b>ba</b> is more common in '
       'writing and set phrases. <b>Dou sureba ii desu ka</b> is a very handy sentence.',
       '82 හි <b>tara</b> වගේම කොන්දේසියක්; හැබැයි <b>ba</b> ලිවීමේදී බහුලයි. '
       '<b>Dou sureba ii desu ka</b> ගොඩක් ප්‍රයෝජනවත්.'),
  pattern=[["BLANK",("ば、","ba",True),("〜ます","~ masu")],
           f"NOTE:つくり{r('方','かた')}：{r('書','か')}く → {KAK}　/　{r('飲','の')}む → {NOM}　/　"
           f"する → すれば　/　{r('来','く')}る → {r('来','く')}れば",
           f"NOTE:い けいようし：{r('安','やす')}い → {YASU}　/　な・めいし：しずか<b>なら</b>（85）"],
  examples=[
    (f"たくさん {REN}すれば、{DEK}よ。","Takusan renshuu sureba, dekimasu yo.","If you practise a lot, you'll be able to do it.","ගොඩක් පුහුණු වුණොත් පුළුවන් වේවි."),
    (f"{YASU}、{KAI}。","Yasukereba, kaimasu.","If it's cheap, I'll buy it.","ලාබයි නම් ගන්නවා."),
    (f"{JIK}が あれば、{IK}。","Jikan ga areba, ikimasu.","If I have time, I'll go.","වෙලාව තිබුණොත් යනවා."),
    (f"{KUSU}を {NOM}、{NAO}。","Kusuri wo nomeba, naorimasu.","If you take the medicine, you'll get better.","බෙහෙත බිව්වොත් හොඳ වෙනවා."),
    (f"{BEN}すれば、テストに {UKA}。","Benkyou sureba, tesuto ni ukarimasu.","If you study, you'll pass the test.","ඉගෙන ගත්තොත් විභාගය සමත් වෙනවා."),
    (f"{TEN}が よければ、{UMI}へ {IK}。","Tenki ga yokereba, umi e ikimasu.","If the weather is good, I'll go to the sea.","කාලගුණය හොඳ නම් මුහුදට යනවා."),
    (f"{DOU} いいですか。","Dou sureba ii desu ka.","What should I do?","මම මොකද කරන්න ඕනේ?"),
  ],
  foot="〜ば、〜",
)

if __name__ == "__main__":
    render(P, "u84_ba")
