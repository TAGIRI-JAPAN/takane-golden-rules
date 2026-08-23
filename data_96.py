from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HON  = r("本","ほん")
YOM  = r("読","よ")+"み"
HAJI = "はじめました"
OWA  = "おわりました"
TSUZ = "つづけて います"
AME  = r("雨","あめ")
FUR  = r("降","ふ")+"り"
DAS  = "だしました"
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
TAB  = r("食","た")+"べ"
KAK  = r("書","か")+"き"
REP  = "レポート"
JUG  = r("授業","じゅ ぎょう")
UTA  = r("歌","うた")+"い"
NAK  = r("泣","な")+"き"

P = dict(
  no="96", tag=None,
  title_jp="〜はじめます／〜おわります／〜つづけます",
  title_ro='hajimemasu / owarimasu / tsuzukemasu &nbsp;|&nbsp; start / finish / keep on 〜ing &nbsp;|&nbsp; '
           '<span class="si">පටන් ගන්නවා / ඉවර කරනවා / දිගටම කරනවා</span>',
  basic=(f"{HON}を {YOM}{HAJI}。","Hon wo yomihajimemashita.",
         "I started reading a book.","මම පොත කියවන්න පටන් ගත්තා."),
  use=(f'ますけいの「ます」を とって、うしろに どうしを つけると '
       f'1つの どうしに なります。<b>はじめ・おわり・とちゅう</b>を あらわします。'
       f'46「すぎます」・42「やすいです」と {r("同","おな")}じ つくり方です。',
       'Drop <b>masu</b> and attach another verb to make a compound verb showing the '
       '<b>beginning, end or continuation</b> of an action — the same build as 42 and 46.',
       '<b>masu</b> අයින් කරලා තව ක්‍රියාවක් දාලා එක ක්‍රියාවක් හදනවා — '
       '<b>පටන් ගැනීම, ඉවර වීම, දිගටම යාම</b>. 42, 46 වගේම හැඩය.'),
  pattern=[["BLANK",("はじめます","hajimemasu",True)],
           ["BLANK",("おわります／つづけます","owarimasu / tsuzukemasu",True)],
           f"NOTE:ますけいの「ます」を とる：{r('読','よ')}みます → {YOM}＋はじめる　/　"
           f"{r('食','た')}べます → {TAB}＋おわる　/　{r('書','か')}きます → {KAK}＋つづける",
           f"NOTE:「〜だします」は <b>きゅうに はじまる</b>ときです"
           f"（{AME}が {FUR}{DAS}＝きゅうに {r('降','ふ')}りはじめた）"],
  examples=[
    (f"{HON}を {YOM}{HAJI}。","Hon wo yomihajimemashita.","I started reading a book.","මම පොත කියවන්න පටන් ගත්තා."),
    (f"{r('去年','きょ ねん')}から {NHG}を {BEN}し{HAJI}。","Kyonen kara nihongo wo benkyou shihajimemashita.","I started studying Japanese last year.","පහුගිය අවුරුද්දේ ඉඳන් ජපන් භාෂාව ඉගෙන ගන්න පටන් ගත්තා."),
    (f"ごはんを {TAB}{OWA}。","Gohan wo tabeowarimashita.","I finished eating.","මම කෑම ඉවර කළා."),
    (f"{REP}を {KAK}{OWA}か。","Repooto wo kakiowarimashita ka.","Have you finished writing the report?","වාර්තාව ලියලා ඉවරද?"),
    (f"3{r('時間','じ かん')} {BEN}し{TSUZ}。","Sanjikan benkyou shitsuzukete imasu.","I've been studying for three hours.","පැය තුනක් දිගටම ඉගෙන ගන්නවා."),
    (f"{AME}が きゅうに {FUR}{DAS}。","Ame ga kyuu ni furidashimashita.","It suddenly started to rain.","හදිසියේම වහින්න පටන් ගත්තා."),
    (f"{JUG}が はじまる まえに、{HON}を {YOM}ましょう。","Jugyou ga hajimaru mae ni, hon wo yomimashou.","Let's read before class starts.","පන්තිය පටන් ගන්න කලින් පොත කියවමු."),
  ],
  foot="〜はじめます／おわります／つづけます",
)

if __name__ == "__main__":
    render(P, "u96_fukugou")
