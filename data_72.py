from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NIH  = r("日本","に ほん")
IKU  = r("行","い")+"く"
ITT  = r("行","い")+"った"
KAB  = "かばん"
KAT  = r("買","か")+"いました"
WAK  = "わかい"
KOD  = r("子","こ")+"ども"
HIMA = "ひまな"
HON  = r("本","ほん")
YOM  = r("読","よ")+"みます"
GAK  = r("学生","がく せい")
SAM  = r("寒","さむ")+"い"
UWA  = r("上着","うわ ぎ")
KI   = r("着","き")+"ます"
NEM  = r("眠","ねむ")+"い"
KOH  = "コーヒー"
NOM  = r("飲","の")+"みます"
DER  = r("出","で")+"る"
KAGI = "かぎ"

P = dict(
  no="72", tag=None,
  title_jp="〜とき、〜",
  title_ro='〜 toki, 〜 &nbsp;|&nbsp; when 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වෙලාවේ</span>',
  basic=(f"{NIH}へ {IKU} とき、パスポートが いります。","Nihon e iku toki, pasupooto ga irimasu.",
         "When you go to Japan, you need a passport.","ජපානෙට යනකොට පාස්පෝට් එක ඕනේ."),
  use=(f'2つの ことが <b>{r("同","おな")}じ とき</b>に おこる ことを {r("言","い")}います。'
       f'「とき」の {r("前","まえ")}が <b>じしょけい</b>なら まだ して いない、'
       f'<b>た{r("形","けい")}</b>なら もう した ことです。ここが いちばん {r("大切","たい せつ")}です。',
       'It says two things happen at the same time. The <b>dictionary form</b> before '
       '<b>toki</b> means "not yet done"; the <b>ta-form</b> means "already done".',
       'දේවල් දෙකක් එකවර වෙනවා කියනවා. <b>toki</b> ට කලින් ශබ්දකෝෂ ආකාරය = තාම කරලා නැහැ; '
       '<b>ta-ආකාරය</b> = දැනටමත් කරලා.'),
  pattern=[["BLANK",("とき、","toki",True),("〜します","~ shimasu")],
           f"NOTE:{NIH}へ <b>{IKU}</b> とき ＝ {r('行','い')}く {r('前','まえ')}（まだ 日本に いない）　/　"
           f"{NIH}へ <b>{ITT}</b> とき ＝ ついた あと（もう 日本に いる）",
           f"NOTE:めいし・けいようし：{GAK}<b>の</b> とき　/　{HIMA} とき　/　{SAM} とき"],
  examples=[
    (f"{NIH}へ {IKU} とき、パスポートが いります。","Nihon e iku toki, pasupooto ga irimasu.","When you go to Japan, you need a passport.","ජපානෙට යනකොට පාස්පෝට් එක ඕනේ."),
    (f"{NIH}へ {ITT} とき、この {KAB}を {KAT}。","Nihon e itta toki, kono kaban wo kaimashita.","When I was in Japan, I bought this bag.","ජපානේ ගියාම මේ බෑග් එක ගත්තා."),
    (f"{SAM} とき、{UWA}を {KI}。","Samui toki, uwagi wo kimasu.","When it's cold, I put on a jacket.","සීතල වෙලාවට ජැකට් එකක් අඳිනවා."),
    (f"{HIMA} とき、{HON}を {YOM}。","Himana toki, hon wo yomimasu.","When I'm free, I read books.","නිදහස් වෙලාවට පොත් කියවනවා."),
    (f"{GAK}の とき、よく クリケットを しました。","Gakusei no toki, yoku kuriketto wo shimashita.","When I was a student, I played cricket a lot.","ශිෂ්‍යයෙක් වෙලා හිටිය කාලේ ගොඩක් ක්‍රිකට් ගැහුවා."),
    (f"{NEM} とき、{KOH}を {NOM}。","Nemui toki, koohii wo nomimasu.","When I'm sleepy, I drink coffee.","නිදිමත වෙලාවට කෝපි බොනවා."),
    (f"{r('出','で')}かける とき、{KAGI}を かけて ください。","Dekakeru toki, kagi wo kakete kudasai.","When you go out, please lock the door.","එළියට යනකොට දොර වහන්න."),
  ],
  foot="〜とき、〜",
)

if __name__ == "__main__":
    render(P, "u72_toki")
