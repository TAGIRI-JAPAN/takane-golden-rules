from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KOE  = r("声","こえ")
OOK  = r("大","おお")+"きく"
HEYA = r("部屋","へ や")
SUZ  = r("涼","すず")+"しく"
KAM  = r("髪","かみ")
MIJI = r("短","みじか")+"く"
SHIZ = r("静","しず")+"かに"
KYO  = r("教室","きょう しつ")
KIRE = "きれいに"
WATA = r("私","わたし")
KOH  = "コーヒー"
NIM  = r("荷物","に もつ")
KAR  = "カレー"
KIME = r("決","き")+"める"
MISE = r("店","みせ")

P = dict(
  no="54", tag=None,
  title_jp="〜に します／〜く します",
  title_ro='〜 ni shimasu / 〜 ku shimasu &nbsp;|&nbsp; make it 〜 / choose 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරනවා / 〜 තෝරනවා</span>',
  basic=(f"{KOE}を もう {r('少','すこ')}し {OOK} して ください。","Koe wo mou sukoshi ookiku shite kudasai.",
         "Please make your voice a little louder.","කටහඬ ටිකක් ලොකු කරන්න."),
  use=(f'53の「なります」は しぜんに かわる こと、'
       f'54の「します」は <b>{r("人","ひと")}が かえる</b> ことです。'
       f'めいしに つけると「これに します」＝<b>{KIME}</b>と いう {r("意味","い み")}に なります。',
       'In 53 <b>narimasu</b> is a change that happens; here <b>shimasu</b> is a change '
       '<b>someone makes</b>. With a noun it means "I\'ll choose / decide on it".',
       '53 හි <b>narimasu</b> = ඉබේ වෙන වෙනස; මෙතන <b>shimasu</b> = <b>කෙනෙක් කරන</b> වෙනස. '
       'නාම පදයක් එක්ක නම් "මේක තෝරගන්නවා" කියන අර්ථය.'),
  pattern=[[("い けいようし","i-adj"),"BLANK",("く します","ku shimasu",True)],
           [("な けいようし・めいし","na-adj / noun"),"BLANK",("に します","ni shimasu",True)],
           f"NOTE:{OOK}い → {OOK} する　/　{SHIZ[:-1]}な → {SHIZ} する　/　"
           f"コーヒー → コーヒーに する（えらぶ）",
           f"NOTE:53 なります＝しぜんに かわる　⇔　54 します＝{r('人','ひと')}が かえる"],
  examples=[
    (f"{KOE}を もう {r('少','すこ')}し {OOK} して ください。","Koe wo mou sukoshi ookiku shite kudasai.","Please make your voice a little louder.","කටහඬ ටිකක් ලොකු කරන්න."),
    (f"{HEYA}を {SUZ} しました。","Heya wo suzushiku shimashita.","I made the room cooler.","කාමරය සිසිල් කළා."),
    (f"{KAM}を {MIJI} しました。","Kami wo mijikaku shimashita.","I had my hair cut short.","කොණ්ඩය කොට කළා."),
    (f"{KYO}を {KIRE} して ください。","Kyoushitsu wo kirei ni shite kudasai.","Please make the classroom clean.","පන්ති කාමරය පිරිසිදු කරන්න."),
    (f"もう {r('少','すこ')}し {SHIZ} して ください。","Mou sukoshi shizuka ni shite kudasai.","Please be a little quieter.","ටිකක් නිශ්ශබ්ද වෙන්න."),
    (f"{WATA}は {KOH}に します。","Watashi wa koohii ni shimasu.","I'll have coffee.","මම කෝපි ගන්නම්."),
    (f"この {MISE}の {KAR}に しましょう。","Kono mise no karee ni shimashou.","Let's go for the curry at this shop.","මේ කඩේ කරි එක ගමු."),
  ],
  foot="〜に します／〜く します",
)

if __name__ == "__main__":
    render(P, "u54_nishimasu")
