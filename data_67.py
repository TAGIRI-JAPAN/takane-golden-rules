from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NORI = r("乗","の")+"りおくれて"
OTOS = r("落","お")+"として"
SHUK = r("宿題","しゅく だい")
IE   = r("家","いえ")
WASU = r("忘","わす")+"れて"
KEK  = "ケーキ"
ZEN  = r("全部","ぜん ぶ")
TABE = r("食","た")+"べて"
TOK  = r("時計","と けい")
KOWA = "こわれて"
KAET = r("帰","かえ")+"って"
DEN  = r("電車","でん しゃ")
NAKA = r("中","なか")
NETE = r("寝","ね")+"て"
ZAN  = r("残念","ざん ねん")
OWA  = r("終","お")+"わった"

P45 = dict(
  no="67", tag=None,
  title_jp="〜して しまいました",
  title_ro='〜 shite shimaimashita &nbsp;|&nbsp; I ended up 〜ing &nbsp;|&nbsp; '
           '<span class="si">〜 වෙලා ගියා</span>',
  basic=(f"バスに {NORI} しまいました。","Basu ni noriokurete shimaimashita.",
         "I ended up missing the bus.","මට බස් එක මිස් වුණා."),
  use=(f'て{r("形","けい")}に つけます。{r("意味","い み")}は 2つ：①{ZAN}・うっかり　②{r("完全","かん ぜん")}に {OWA}。'
       f'かいわでは「〜ちゃいました」と なります。',
       'Add it to the te-form. Two meanings: (1) regret / by accident, (2) completely finished. '
       'In conversation it becomes <b>-chaimashita</b>.',
       'te-ආකාරයට දාන්න. අර්ථ දෙකයි: (1) අනේ / නොදැනුවත්ව, (2) සම්පූර්ණයෙන් ඉවරයි. '
       'කතාබහේදී <b>-chaimashita</b> කියලා වෙනස් වෙනවා.'),
  pattern=[["BLANK",("て しまいました","te shimaimashita",True)],
           ["BLANK",("ちゃいました","chaimashita",True)],
           f"NOTE:①{ZAN}：{r('忘','わす')}れて しまいました　②{r('完全','かん ぜん')}に：{ZEN} {TABE} しまいました",
           f"NOTE:かいわ：{r('忘','わす')}れちゃいました　/　{r('飲','の')}んじゃいました（んで → んじゃ）"],
  examples=[
    (f"バスに {NORI} しまいました。","Basu ni noriokurete shimaimashita.","I ended up missing the bus.","මට බස් එක මිස් වුණා."),
    (f"コップを {OTOS} しまいました。","Koppu wo otoshite shimaimashita.","I dropped the cup.","මට කෝප්පෙ බිම වැටුණා."),
    (f"{SHUK}を {IE}に {WASU} しまいました。","Shukudai wo ie ni wasurete shimaimashita.","I left my homework at home.","මට ගෙදර වැඩ ගෙදර අමතක වුණා."),
    (f"{KEK}を {ZEN} {TABE} しまいました。","Keeki wo zenbu tabete shimaimashita.","I ate the whole cake.","මම කේක් එක ඔක්කොම කාලා දැම්මා."),
    (f"{TOK}が {KOWA} しまいました。","Tokei ga kowarete shimaimashita.","My watch broke.","මගේ ඔරලෝසුව කැඩිලා ගියා."),
    (f"サマンさんは もう {KAET} しまいました。","Saman-san wa mou kaette shimaimashita.","Saman has already gone home.","සමන් දැනටමත් ගිහිල්ලා."),
    (f"{DEN}の {NAKA}で {NETE} しまいました。","Densha no naka de nete shimaimashita.","I fell asleep on the train.","මම දුම්රියේ නිදාගෙන ගියා."),
  ],
  foot="〜して しまいました",
)

if __name__ == "__main__":
    render(P45, "p67_shimaimashita")
