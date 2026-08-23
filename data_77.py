from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN  = r("先生","せん せい")
ITT  = r("言","い")+"った"
SETS = r("説明","せつ めい")
KAI  = r("書","か")+"いて"
YAT  = "やって"
TSUK = r("作","つく")+"って"
SEN2 = r("線","せん")
HIK  = r("引","ひ")+"いて"
MI   = r("見","み")+"た"
HANA = r("話","はな")+"しました"
YAK  = r("約束","やく そく")
JISH = r("辞書","じ しょ")
YOM  = r("読","よ")+"んで"
OSHI = r("教","おし")+"えた"

P = dict(
  no="77", tag=None,
  title_jp="〜とおりに 〜",
  title_ro='〜 toori ni &nbsp;|&nbsp; just as / exactly the way 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 විදිහටම</span>',
  basic=(f"{SEN}が {ITT} とおりに して ください。","Sensei ga itta toori ni shite kudasai.",
         "Please do it just as the teacher said.","ගුරුතුමා කිව්ව විදිහටම කරන්න."),
  see_note=None,
  use=(f'「{r("同","おな")}じ ように」と いう {r("意味","い み")}です。'
       f'じしょけい・た{r("形","けい")}の どちらも つきます。'
       f'めいしには「の」が {r("入","はい")}ります（{YAK}<b>の</b> とおりに）。',
       'It means "exactly in that way". Both the dictionary form and the ta-form work. '
       'After a noun you need <b>no</b>.',
       '"හරියටම ඒ විදිහට" කියන අර්ථය. ශබ්දකෝෂ ආකාරය හා ta-ආකාරය දෙකම හරි. '
       'නාම පදයකට පස්සේ <b>no</b> ඕනේ.'),
  pattern=[["BLANK",("とおりに、","toori ni",True),("〜します","~ shimasu")],
           f"NOTE:じしょけい（{r('言','い')}う とおりに）　/　た{r('形','けい')}（{ITT} とおりに）　/　"
           f"めいし＋の（{YAK}の とおりに）",
           f"NOTE:「そのとおりです」＝「まったく その とおり」（120も {r('見','み')}て ください）"],
  examples=[
    (f"{SEN}が {ITT} とおりに して ください。","Sensei ga itta toori ni shite kudasai.","Please do it just as the teacher said.","ගුරුතුමා කිව්ව විදිහටම කරන්න."),
    (f"{SETS}の とおりに {TSUK}ました。","Setsumei no toori ni tsukurimashita.","I made it just as the instructions said.","උපදෙස් විදිහටම හැදුවා."),
    (f"{KAI} ある とおりに {YOM} ください。","Kaite aru toori ni yonde kudasai.","Please read it exactly as it is written.","ලියලා තියෙන විදිහටම කියවන්න."),
    (f"わたしが {YAT} みせる とおりに して ください。","Watashi ga yatte miseru toori ni shite kudasai.","Please do it the way I show you.","මම කරලා පෙන්නන විදිහටම කරන්න."),
    (f"{SEN2}の とおりに {HIK} ください。","Sen no toori ni hiite kudasai.","Please draw along the line.","ඉරි විදිහටම අඳින්න."),
    (f"{MI} とおりに {HANA}。","Mita toori ni hanashimashita.","I told it exactly as I saw it.","දැක්ක විදිහටම කිව්වා."),
    (f"{SEN}が {OSHI} とおりに、{JISH}を つかいました。","Sensei ga oshieta toori ni, jisho wo tsukaimashita.","I used the dictionary as the teacher taught me.","ගුරුතුමා කියලා දුන්න විදිහටම ශබ්දකෝෂය පාවිච්චි කළා."),
  ],
  foot="〜とおりに 〜",
)
P.pop("see_note")

if __name__ == "__main__":
    render(P, "u77_toorini")
