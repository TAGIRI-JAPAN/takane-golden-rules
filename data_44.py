from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
HITS = r("必要","ひつ よう")
PASU = "パスポート"
REN  = r("練習","れん しゅう")
KYO  = r("教科書","きょう か しょ")
TETS = r("手伝","て つだ")+"い"
ASHI = r("明日","あ した")
KASA = "かさ"
SHOR = r("書類","しょ るい")
KYOU = r("今日","きょう")
SAIN = "サイン"
KUR  = "クラス"

P36 = dict(
  no="44", tag=None,
  title_jp=f"〜が {HITS}です",
  title_ro='〜 ga hitsuyou desu &nbsp;|&nbsp; I need 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 අවශ්‍යයි</span>',
  basic=(f"ここでは {PASU}が {HITS}です。","Koko de wa pasupooto ga hitsuyou desu.",
         "You need a passport here.","මෙතන පාස්පෝට් එක අවශ්‍යයි."),
  use=(f'ないと こまる もの・ことを{r("言","い")}う ことばです。43の「ほしい」は '
       f'「{r("気持","き も")}ち」、44の「{HITS}」は「ないと ダメ」です。まえは「〜が」です。',
       'Use it for something you cannot do without. <b>hoshii</b> (43) is a wish; '
       '<b>hitsuyou</b> is a real need. The word before it takes <b>ga</b>.',
       'නැතුව බැරි දෙයක් කියන්න. 43 හි <b>hoshii</b> = ඕනෙ (කැමැත්ත); '
       '<b>hitsuyou</b> = අවශ්‍යයි (නැතුව බැහැ). කලින් වචනයට <b>ga</b>.'),
  pattern=[[("〜は","~ wa"),"BLANK",("が","ga",True),(f"{HITS}です","hitsuyou desu",True)],
           f"NOTE:ひてい：{HITS}ありません　/　{HITS}じゃないです　（අවශ්‍ය නැහැ）",
           f"NOTE:ほしいです = ඕනෙ（したい {r('気持','き も')}ち）　/　{HITS}です = අවශ්‍යයි（ないと こまる）"],
  examples=[
    (f"ここでは {PASU}が {HITS}です。","Koko de wa pasupooto ga hitsuyou desu.","You need a passport here.","මෙතන පාස්පෝට් එක අවශ්‍යයි."),
    (f"{W}は もっと {REN}が {HITS}です。","Watashi wa motto renshuu ga hitsuyou desu.","I need more practice.","මට තව පුහුණුවීම් අවශ්‍යයි."),
    (f"この {KUR}は {KYO}が {HITS}です。","Kono kurasu wa kyoukasho ga hitsuyou desu.","You need a textbook for this class.","මේ පන්තියට පෙළපොත අවශ්‍යයි."),
    (f"サマンさんの {TETS}が {HITS}です。","Saman-san no tetsudai ga hitsuyou desu.","I need Saman's help.","සමන්ගේ උදව්ව අවශ්‍යයි."),
    (f"{ASHI}は {KASA}が {HITS}です。","Ashita wa kasa ga hitsuyou desu.","You will need an umbrella tomorrow.","හෙට කුඩය අවශ්‍යයි."),
    (f"この {SHOR}には {SAIN}が {HITS}です。","Kono shorui ni wa sain ga hitsuyou desu.","This document needs a signature.","මේ ලියවිල්ලට අත්සන අවශ්‍යයි."),
    (f"{KYOU}は {KASA}は {HITS}ありません。","Kyou wa kasa wa hitsuyou arimasen.","You don't need an umbrella today.","අද කුඩය අවශ්‍ය නැහැ."),
  ],
  foot="〜が 必要です",
)

if __name__ == "__main__":
    render(P36, "p44_hitsuyou")
