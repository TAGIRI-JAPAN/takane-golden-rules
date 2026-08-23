from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
IMA  = r("今","いま")
OKI  = r("起","お")+"きた"
ABI  = r("浴","あ")+"びた"
DEN  = r("電話","でん わ")
JUG  = r("授業","じゅ ぎょう")
HAJI = r("始","はじ")+"まった"
NOTT = r("乗","の")+"った"
REP  = "レポート"
KAI  = r("書","か")+"いた"
KITA = r("来","き")+"た"
SUR  = "する"
SHIT = "している"
BAK  = "ばかり"

P46 = dict(
  no="70", tag=None,
  title_jp="〜した ところです",
  title_ro='〜 shita tokoro desu &nbsp;|&nbsp; I have just 〜 &nbsp;|&nbsp; '
           '<span class="si">දැන් තමයි 〜 කළේ</span>',
  basic=(f"{W}は {IMA} {OKI} ところです。","Watashi wa ima okita tokoro desu.",
         "I have just woken up.","දැන් තමයි මම නැගිට්ටේ."),
  use=(f'た{r("形","けい")}に つけて「たった{r("今","いま")} おわった」と{r("言","い")}います。'
       f'「{IMA}」「ちょうど」「さっき」と いっしょに よく つかいます。',
       'Add it to the ta-form to say something finished just now. '
       'Often used with <b>ima</b>, <b>choudo</b> or <b>sakki</b>.',
       'ta-ආකාරයට දාලා "දැන් තමයි ඉවර වුණේ" කියන්න. '
       '<b>ima</b>, <b>choudo</b>, <b>sakki</b> එක්ක බහුලව.'),
  pattern=[["BLANK",("した ところです","shita tokoro desu",True)],
           f"NOTE:3つの ところ：{SUR} ところ（これから）　/　{SHIT} ところ（{IMA} している）　/　"
           f"した ところ（{IMA} おわった）",
           f"NOTE:〜した{BAK}です も にて いますが、こちらは {r('少','すこ')}し {r('前','まえ')}でも つかえます"],
  examples=[
    (f"{W}は {IMA} {OKI} ところです。","Watashi wa ima okita tokoro desu.","I have just woken up.","දැන් තමයි මම නැගිට්ටේ."),
    (f"シャワーを {ABI} ところです。","Shawaa wo abita tokoro desu.","I have just taken a shower.","දැන් තමයි නාලා ඉවර වුණේ."),
    (f"さっき サマンさんに {DEN}を した ところです。","Sakki Saman-san ni denwa wo shita tokoro desu.","I just called Saman.","දැන් තමයි සමන්ට කතා කළේ."),
    (f"{JUG}が {HAJI} ところです。","Jugyou ga hajimatta tokoro desu.","The class has just started.","දැන් තමයි පන්තිය පටන් ගත්තේ."),
    (f"{IMA} バスに {NOTT} ところです。","Ima basu ni notta tokoro desu.","I have just got on the bus.","දැන් තමයි බස් එකට නැග්ගේ."),
    (f"{REP}を {KAI} ところです。","Repooto wo kaita tokoro desu.","I have just finished writing the report.","දැන් තමයි වාර්තාව ලිව්වේ."),
    (f"サマンさんは {IMA} {KITA} ところです。","Saman-san wa ima kita tokoro desu.","Saman has just arrived.","දැන් තමයි සමන් ආවේ."),
  ],
  foot="〜した ところです",
)

if __name__ == "__main__":
    render(P46, "p70_tokorodesu")
