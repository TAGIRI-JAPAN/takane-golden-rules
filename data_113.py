from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MIZU = r("水","みず")
SEKI = r("席","せき")
KASA = "かさ"
MEN  = "メニュー"
SAKI = r("先","さき")
GEN  = r("元気","げん き")
SUS  = r("勧","すす")+"める"

P58 = dict(
  no="113", tag=None,
  title_jp="〜を どうぞ",
  title_ro='〜 wo douzo &nbsp;|&nbsp; Here, please have 〜 &nbsp;|&nbsp; '
           '<span class="si">මෙන්න, 〜 ගන්න</span>',
  basic=("コーヒーを どうぞ。","Koohii wo douzo.",
         "Please have some coffee.","කෝපි ටිකක් ගන්න."),
  use=(f'{r("何","なに")}かを {SUS} ときの ことばです。'
       f'「どうぞ」は すすめる、「どうも」は ありがとう・すみません。ちがいに {r("注意","ちゅう い")}。',
       'Use it when you offer something. Careful: <b>douzo</b> offers something, while '
       '<b>doumo</b> means thanks or sorry.',
       'යමක් ඉදිරිපත් කරද්දී කියන වචනය. <b>douzo</b> = ඉදිරිපත් කිරීම; '
       '<b>doumo</b> = ස්තූතියි / සමාවෙන්න. පටලවා ගන්න එපා.'),
  pattern=[["BLANK",("を どうぞ","wo douzo",True)],
           [("どうぞ","douzo",True),"BLANK"],
           f"NOTE:もらう {r('人','ひと')}の へんじ：「ありがとうございます」　/　"
           f"{r('食','た')}べ{r('物','もの')}なら「いただきます」",
           f"NOTE:どうぞ ＝ すすめる　⇔　どうも ＝ ありがとう・すみません"],
  examples=[
    ("コーヒーを どうぞ。","Koohii wo douzo.","Please have some coffee.","කෝපි ටිකක් ගන්න."),
    (f"お{MIZU}を どうぞ。","Omizu wo douzo.","Here is some water.","වතුර ටිකක් ගන්න."),
    (f"こちらの {SEKI}を どうぞ。","Kochira no seki wo douzo.","Please take this seat.","මේ ආසනයේ වාඩිවෙන්න."),
    (f"この {KASA}を どうぞ。","Kono kasa wo douzo.","Please take this umbrella.","මේ කුඩය අරන් යන්න."),
    (f"{MEN}を どうぞ。","Menyuu wo douzo.","Here is the menu.","මෙන්න මෙනුව."),
    ("どうぞ こちらへ。","Douzo kochira e.","This way, please.","මෙහාට වඩින්න."),
    (f"どうぞ お{SAKI}に。","Douzo osaki ni.","Please go ahead.","ඔයා කලින් යන්න."),
  ],
  foot="〜を どうぞ",
)

if __name__ == "__main__":
    render(P58, "p113_wodouzo")
