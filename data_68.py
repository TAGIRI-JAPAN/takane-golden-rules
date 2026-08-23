from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MAE  = r("前","まえ")
SUN  = r("住","す")+"んで"
DAI  = r("大学","だい がく")
BEN  = r("勉強","べん きょう")
GAK  = r("学校","がっ こう")
ITT  = r("行","い")+"って"
KOU  = r("公園","こう えん")
KIM  = r("来","き")+"ました"
NIH  = r("日本","に ほん")
MIM  = r("見","み")+"ました"
NHG  = r("日本語","に ほん ご")
IMA  = r("今","いま")
SRI  = "スリランカ"

P30 = dict(
  no="68", tag=None,
  title_jp=f"{MAE}は 〜しました〔していました〕",
  title_ro='Mae wa 〜 shimashita / shite imashita &nbsp;|&nbsp; I used to 〜 &nbsp;|&nbsp; '
           '<span class="si">කලින් 〜 කළා</span>',
  basic=(f"{MAE}は {SRI}に {SUN}いました。","Mae wa Suriranka ni sunde imashita.",
         "I used to live in Sri Lanka.","කලින් මම ශ්‍රී ලංකාවේ ජීවත් වුණා."),
  use=(f'「{MAE}は」を つけると、まえに していた ことを{r("言","い")}えます。'
       f'「していました」は ずっと つづいた しゅうかん・じょうたい、「しました」は おわった できごとです。',
       'Adding <b>mae wa</b> lets you talk about what you used to do. '
       '<b>shite imashita</b> is a habit or state that continued; '
       '<b>shimashita</b> is a finished event.',
       '<b>mae wa</b> දාලා කලින් කරපු දේ කියන්න පුළුවන්. '
       '<b>shite imashita</b> = දිගටම තිබුණු පුරුද්දක් හෝ තත්ත්වයක්; '
       '<b>shimashita</b> = ඉවර වුණු සිද්ධියක්.'),
  pattern=[[(f"{MAE}は","mae wa",True),"BLANK",("しました","shimashita")],
           [(f"{MAE}は","mae wa",True),"BLANK",("していました","shite imashita")],
           "NOTE:していました = ずっと つづいた しゅうかん・じょうたい　/　しました = おわった できごと",
           f"NOTE:どちらも「{IMA}は ちがいます」という {r('気持','き も')}ちが {r('入','はい')}ります"],
  examples=[
    (f"{MAE}は {SRI}に {SUN}いました。","Mae wa Suriranka ni sunde imashita.","I used to live in Sri Lanka.","කලින් මම ශ්‍රී ලංකාවේ ජීවත් වුණා."),
    (f"{MAE}は まいにち クリケットを していました。","Mae wa mainichi kuriketto wo shite imashita.","I used to play cricket every day.","කලින් මම හැමදාම ක්‍රිකට් ක්‍රීඩා කළා."),
    (f"{MAE}は {DAI}で {BEN}していました。","Mae wa daigaku de benkyou shite imashita.","I used to study at university.","කලින් මම විශ්වවිද්‍යාලයේ ඉගෙන ගත්තා."),
    (f"{MAE}は バスで {GAK}に {ITT}いました。","Mae wa basu de gakkou ni itte imashita.","I used to go to school by bus.","කලින් මම බස් එකෙන් පාසලට ගියා."),
    (f"{MAE}は この {KOU}に よく {KIM}。","Mae wa kono kouen ni yoku kimashita.","I often used to come to this park.","කලින් මම නිතරම මේ උද්‍යානයට ආවා."),
    (f"{MAE}は {NIH}の アニメを よく {MIM}。","Mae wa Nihon no anime wo yoku mimashita.","I used to watch Japanese anime a lot.","කලින් මම ජපන් ඇනිමේ ගොඩක් බැලුවා."),
    (f"{MAE}は {NHG}が わかりませんでした。","Mae wa nihongo ga wakarimasen deshita.","I didn't understand Japanese before.","කලින් මට ජපන් භාෂාව තේරුණේ නැහැ."),
  ],
  foot="前は 〜しました〔していました〕",
)

if __name__ == "__main__":
    render(P30, "p68_maewa")
