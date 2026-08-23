from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
HON  = r("本","ほん")
AGE  = "あげます"
AGEM = "あげました"
KURE = "くれました"
SEN  = r("先生","せん せい")
JISH = r("辞書","じ しょ")
MORA = "もらいました"
HAHA = r("母","はは")
OTO  = r("弟","おとうと")
KAB  = "かばん"
DARE = r("誰","だれ")
OSHI = r("教","おし")+"えて"
UKE  = r("受","う")+"ける"

P32 = dict(
  no="34", tag=None,
  title_jp="あげます／もらいます／くれます",
  title_ro='agemasu / moraimasu / kuremasu &nbsp;|&nbsp; give &amp; receive &nbsp;|&nbsp; '
           '<span class="si">දෙනවා / ලැබෙනවා</span>',
  basic=(f"{W}は サマンさんに {HON}を {AGE}。","Watashi wa Saman-san ni hon wo agemasu.",
         "I give Saman a book.","මම සමන්ට පොතක් දෙනවා."),
  use=(f'シンハラ{r("語","ご")}は「දෙනවා」1つですが、日本語は 3つに 分けます。',
       'Sinhala has one word, <b>denavā</b>. Japanese splits it three ways.',
       'සිංහලෙන් <b>දෙනවා</b> එක වචනයයි; ජපන් භාෂාවේ තුනකට බෙදෙනවා.'),
  pattern=[[(f"{W}は","watashi wa"),("〜に","~ ni"),"BLANK",(f"を {AGE}","wo agemasu",True)],
           [(f"{W}は","watashi wa"),("〜に","~ ni"),"BLANK",("を もらいます","wo moraimasu",True)],
           [("〜は","~ wa"),(f"{W}に","watashi ni"),"BLANK",("を くれます","wo kuremasu",True)],
           f"NOTE:あげます＝{W}が {r('渡','わた')}す　/　もらいます＝{W}が {r('受','う')}け{r('取','と')}る　/　"
           f"くれます＝{r('相手','あい て')}が {W}に する",
           f"NOTE:33も なかまです（〜て あげる／〜て くれる／〜て もらう）"],
  examples=[
    (f"{W}は サマンさんに {HON}を {AGE}。","Watashi wa Saman-san ni hon wo agemasu.","I give Saman a book.","මම සමන්ට පොතක් දෙනවා."),
    (f"サマンさんは {W}に カレーを {KURE}。","Saman-san wa watashi ni karee wo kuremashita.","Saman gave me curry.","සමන් මට කරි දුන්නා."),
    (f"{W}は {SEN}に {JISH}を {MORA}。","Watashi wa sensei ni jisho wo moraimashita.","I received a dictionary from my teacher.","මට ගුරුතුමාගෙන් ශබ්දකෝෂයක් ලැබුණා."),
    (f"{HAHA}は {OTO}に {KAB}を {AGEM}。","Haha wa otouto ni kaban wo agemashita.","My mother gave my brother a bag.","අම්මා මල්ලිට බෑග් එකක් දුන්නා."),
    (f"{DARE}が これを {KURE}か。","Dare ga kore wo kuremashita ka.","Who gave you this?","මේක ඔයාට දුන්නේ කවුද?"),
    (f"サマンさんから メールを {MORA}。","Saman-san kara meeru wo moraimashita.","I got an email from Saman.","සමන්ගෙන් ඊමේල් එකක් ලැබුණා."),
    (f"{SEN}が {OSHI} {KURE}。","Sensei ga oshiete kuremashita.","The teacher taught me (for me).","ගුරුතුමා මට කියලා දුන්නා."),
  ],
  foot="あげます／もらいます／くれます",
)

if __name__ == "__main__":
    render(P32, "u34_ageru")
