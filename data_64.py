from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASHI = r("明日","あ した")
GAK  = r("学校","がっ こう")
KURU = r("来","く")+"る"
DEN  = r("電車","でん しゃ")
DERU = r("出","で")+"る"
SEN  = r("先生","せん せい")
KYOU = r("教室","きょう しつ")
MISE = r("店","みせ")
NICH = r("日曜日","にち よう び")
AIT  = r("開","あ")+"いて"
HON  = r("本","ほん")
TOS  = r("図書館","と しょ かん")
KAGI = "かぎ"
KAB  = "かばん"
NAKA = r("中","なか")
KINO = r("昨日","きのう")
RIYU = r("理由","り ゆう")
GAKU = r("学生","がく せい")

P41 = dict(
  no="64", tag=None,
  title_jp="〜するはずです",
  title_ro='〜 suru hazu desu &nbsp;|&nbsp; It should / is sure to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 ඇති</span>',
  basic=(f"サマンさんは {ASHI} {GAK}に {KURU}はずです。","Saman-san wa ashita gakkou ni kuru hazu desu.",
         "Saman should come to school tomorrow.","සමන් හෙට නිසැකවම පාසලට එනවා ඇති."),
  use=(f'{RIYU}が あって「きっと そうだ」と{r("言","い")}う ことばです。'
       f'シンハラ{r("語","ご")}の「ඇති」と{r("同","おな")}じ かんじです。',
       'Use it when you have a reason to be sure. It feels like the Sinhala <b>æti</b>.',
       'හේතුවක් තියෙන නිසා "නිසැකවම එහෙමයි" කියන්න. සිංහල <b>ඇති</b> එකට සමානයි.'),
  pattern=[[("〜は","~ wa"),"BLANK",("はずです","hazu desu",True)],
           [("〜は","~ wa"),"BLANK",("はずでした","hazu deshita",True)],
           f"NOTE:まえは ふつうけい：{KURU}　/　{r('来','こ')}ない　/　{r('来','き')}た　/　いい　/　しずかな　/　{GAKU}の",
           f"NOTE:はずでした ＝ そう おもって いたが、ちがった とき（〜のに）"],
  examples=[
    (f"サマンさんは {ASHI} {GAK}に {KURU}はずです。","Saman-san wa ashita gakkou ni kuru hazu desu.","Saman should come to school tomorrow.","සමන් හෙට නිසැකවම පාසලට එනවා ඇති."),
    (f"この {DEN}は 9じに {DERU}はずです。","Kono densha wa kuji ni deru hazu desu.","This train should leave at nine.","මේ දුම්රිය 9ට පිටත් වෙනවා ඇති."),
    (f"{SEN}は もう {KYOU}に いるはずです。","Sensei wa mou kyoushitsu ni iru hazu desu.","The teacher should already be in the classroom.","ගුරුතුමා දැනටමත් පන්ති කාමරයේ ඇති."),
    (f"この {MISE}は {NICH}も {AIT} いるはずです。","Kono mise wa nichiyoubi mo aite iru hazu desu.","This shop should be open on Sundays too.","මේ කඩේ ඉරිදාටත් ඇරලා ඇති."),
    (f"その {HON}は {TOS}に あるはずです。","Sono hon wa toshokan ni aru hazu desu.","That book should be in the library.","ඒ පොත පුස්තකාලයේ ඇති."),
    (f"{KAGI}は {KAB}の {NAKA}に あるはずです。","Kagi wa kaban no naka ni aru hazu desu.","The key should be in the bag.","යතුර බෑග් එකේ ඇති."),
    (f"{KINO} サマンさんも {KURU}はずでした。","Kinou Saman-san mo kuru hazu deshita.","Saman was supposed to come yesterday too.","ඊයේ සමනුත් එන්න තිබුණා."),
  ],
  foot="〜するはずです",
)

if __name__ == "__main__":
    render(P41, "p64_hazudesu")
