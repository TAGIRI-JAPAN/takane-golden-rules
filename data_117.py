from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KARE = "カレー"
KYO  = r("今日","きょう")
ISO  = "いそがしくないです"
HEYA = r("部屋","へ や")
SHIZ = r("静","しず")+"か"
BEN  = r("便利","べん り")
W    = r("私","わたし")
MIM  = r("見","み")+"ません"
HAN  = r("話","はな")+"しません"
HEN  = r("辺","へん")
HITO = r("人","ひと")
IMA  = "いません"
ZEN  = r("全然","ぜん ぜん")

P48 = dict(
  no="117", tag=None,
  title_jp="あまり 〜ないです",
  title_ro='amari 〜 nai desu &nbsp;|&nbsp; not very 〜 &nbsp;|&nbsp; '
           '<span class="si">එච්චර 〜 නැහැ</span>',
  basic=(f"この {KARE}は あまり からくないです。","Kono karee wa amari karakunai desu.",
         "This curry isn't very spicy.","මේ කරිය එච්චර සැර නැහැ."),
  use=(f'「あまり」は かならず ひていと いっしょに つかいます。'
       f'「あまり おいしいです」は まちがいです。かいわでは「あんまり」に なります。',
       '<b>amari</b> must always be paired with a negative. '
       '"amari oishii desu" is wrong. In conversation it becomes <b>anmari</b>.',
       '<b>amari</b> හැමවිටම නෙගටිව් එක්ක යනවා. '
       '"amari oishii desu" වැරදියි. කතාබහේදී <b>anmari</b>.'),
  pattern=[[("〜は","~ wa"),("あまり","amari",True),"BLANK",("ないです","nai desu",True)],
           f"NOTE:69の ハシゴ：いつも　&gt;　よく　&gt;　ときどき　&gt;　あまり 〜ません　&gt;　{ZEN} 〜ません",
           f"NOTE:い けいようし → からくないです　/　な けいようし・めいし → {SHIZ}じゃないです"],
  examples=[
    (f"この {KARE}は あまり からくないです。","Kono karee wa amari karakunai desu.","This curry isn't very spicy.","මේ කරිය එච්චර සැර නැහැ."),
    (f"{KYO}は あまり {ISO}。","Kyou wa amari isogashikunai desu.","I'm not very busy today.","අද එච්චර කාර්යබහුල නැහැ."),
    (f"この {HEYA}は あまり {SHIZ}じゃないです。","Kono heya wa amari shizuka ja nai desu.","This room isn't very quiet.","මේ කාමරය එච්චර නිස්කලංක නැහැ."),
    (f"ここは あまり {BEN}じゃないです。","Koko wa amari benri ja nai desu.","It isn't very convenient here.","මෙතන එච්චර පහසු නැහැ."),
    (f"{W}は あまり テレビを {MIM}。","Watashi wa amari terebi wo mimasen.","I don't watch much TV.","මම එච්චර රූපවාහිනී බලන්නේ නැහැ."),
    (f"サマンさんは あまり {HAN}。","Saman-san wa amari hanashimasen.","Saman doesn't talk much.","සමන් එච්චර කතා කරන්නේ නැහැ."),
    (f"この {HEN}は あまり {HITO}が {IMA}。","Kono hen wa amari hito ga imasen.","There aren't many people around here.","මේ පැත්තේ එච්චර මිනිස්සු නැහැ."),
  ],
  foot="あまり 〜ないです",
)

if __name__ == "__main__":
    render(P48, "p117_amari")
