from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HAI  = r("入","はい")+"って"
TSUK = r("使","つか")+"って"
YASU = r("休","やす")+"んで"
KIT  = r("来","き")+"て"
MAT  = r("待","ま")+"ち"
KAK  = r("書","か")+"き"
KI   = r("気","き")
TSU  = "つけて"
KEIG = r("敬語","けい ご")
TAB  = r("食","た")+"べる"
NOM  = r("飲","の")+"む"
MES  = r("召","め")+"し"+r("上","あ")+"がって"
MIR  = r("見","み")+"る"
GOR  = "ごらん"

P59 = dict(
  no="114", tag=None,
  title_jp="どうぞ 〜して ください",
  title_ro='douzo 〜 shite kudasai &nbsp;|&nbsp; Please go ahead and 〜 &nbsp;|&nbsp; '
           '<span class="si">කරුණාකරලා 〜 කරන්න</span>',
  basic=(f"どうぞ {HAI} ください。","Douzo haitte kudasai.",
         "Please come in.","කරුණාකරලා ඇතුළට එන්න."),
  use=(f'113の「どうぞ」に どうしを つけた かたちです。お{r("客","きゃく")}さまには '
       f'「お＋ますけい＋ください」に すると、もっと ていねいな {KEIG}に なります。',
       'This adds a verb to the <b>douzo</b> of 113. For customers, '
       '<b>o + masu-stem + kudasai</b> makes it more polite (honorific).',
       '113 හි <b>douzo</b> එකට ක්‍රියාවක් එකතු කරනවා. '
       'ගනුදෙනුකරුවන්ට <b>o + masu + kudasai</b> කිව්වොත් තව ගෞරවනීයයි.'),
  pattern=[[("どうぞ","douzo",True),"BLANK",("して ください","shite kudasai",True)],
           [("どうぞ","douzo",True),("お","o",True),"BLANK",("ください","kudasai",True)],
           f"NOTE:{r('待','ま')}ちます → お{MAT} ください　/　{r('書','か')}きます → お{KAK} ください",
           f"NOTE:とくべつ：{TAB}・{NOM} → {MES} ください　/　{MIR} → {GOR} ください"],
  examples=[
    (f"どうぞ {HAI} ください。","Douzo haitte kudasai.","Please come in.","කරුණාකරලා ඇතුළට එන්න."),
    (f"どうぞ {TSUK} ください。","Douzo tsukatte kudasai.","Please use it.","කරුණාකරලා පාවිච්චි කරන්න."),
    (f"どうぞ ゆっくり {YASU} ください。","Douzo yukkuri yasunde kudasai.","Please take a good rest.","කරුණාකරලා හොඳට විවේක ගන්න."),
    (f"どうぞ こちらに {KIT} ください。","Douzo kochira ni kite kudasai.","Please come over here.","කරුණාකරලා මෙහාට එන්න."),
    (f"どうぞ お{MAT} ください。","Douzo omachi kudasai.","Please wait a moment.","කරුණාකරලා ටිකක් ඉන්න."),
    (f"どうぞ ここに お{KAK} ください。","Douzo koko ni okaki kudasai.","Please write here.","කරුණාකරලා මෙතන ලියන්න."),
    (f"どうぞ {KI}を {TSU} ください。","Douzo ki wo tsukete kudasai.","Please take care.","පරිස්සමෙන් යන්න."),
  ],
  foot="どうぞ 〜して ください",
)

if __name__ == "__main__":
    render(P59, "p114_douzoshite")
