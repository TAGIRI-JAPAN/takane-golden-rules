from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ATO  = r("後","あと")
HANA = r("話","はな")+"しましょう"
ISS  = r("一緒","いっ しょ")
TSUK = r("作","つく")+"ります"
TOS  = r("図書館","と しょ かん")
BEN  = r("勉強","べん きょう")
OKU  = r("送","おく")+"ります"
OSHI = r("教","おし")+"えて"
ASHI = r("明日","あ した")
RAIS = r("来週","らい しゅう")
KOND = r("今度","こん ど")

P62 = dict(
  no="116", tag=None,
  title_jp="また 〜",
  title_ro='mata 〜 &nbsp;|&nbsp; 〜 again &nbsp;|&nbsp; '
           '<span class="si">ආයෙත් 〜</span>',
  basic=(f"また {ATO}で {HANA}。","Mata ato de hanashimashou.",
         "Let's talk again later.","ආයෙත් පස්සේ කතා කරමු."),
  use=(f'もう {r("一度","いち ど")} すると いう ときの ことばです。'
       f'「また」＝again、「まだ」＝still／yet。1{r("字","じ")}で {r("意味","い み")}が かわるので {r("注意","ちゅう い")}。',
       'Use it when something happens once more. Careful: <b>mata</b> = again, but '
       '<b>mada</b> = still / not yet. One letter changes everything.',
       'ආයෙත් වතාවක් කියද්දී පාවිච්චි කරන්න. පරිස්සමෙන්: <b>mata</b> = ආයෙත්, '
       '<b>mada</b> = තාම. එක අකුරකින් අර්ථය වෙනස්.'),
  pattern=[[("また","mata",True),"BLANK",("します","shimasu")],
           [("また","mata",True),"BLANK",("しましょう","shimashou",True)],
           [("また","mata",True),"BLANK",("して ください","shite kudasai",True)],
           f"NOTE:わかれる あいさつ：また {ASHI}　/　また {RAIS}　/　また {KOND}　/　じゃ、また"],
  examples=[
    (f"また {ATO}で {HANA}。","Mata ato de hanashimashou.","Let's talk again later.","ආයෙත් පස්සේ කතා කරමු."),
    (f"また {ISS}に クリケットを しましょう。","Mata isshoni kuriketto wo shimashou.","Let's play cricket together again.","ආයෙත් එකට ක්‍රිකට් ගහමු."),
    (f"また カレーを {TSUK}。","Mata karee wo tsukurimasu.","I'll make curry again.","ආයෙත් කරි උයන්නම්."),
    (f"また {TOS}で {BEN}しましょう。","Mata toshokan de benkyou shimashou.","Let's study at the library again.","ආයෙත් පුස්තකාලයේ ඉගෙන ගමු."),
    (f"また メールを {OKU}。","Mata meeru wo okurimasu.","I'll send you an email again.","ආයෙත් ඊමේල් එකක් එවන්නම්."),
    (f"また {OSHI} くださいね。","Mata oshiete kudasai ne.","Please teach me again.","ආයෙත් කියලා දෙන්න."),
    (f"では、また {ASHI}。","Dewa, mata ashita.","Well then, see you tomorrow.","එහෙනම්, ආයෙත් හෙට හම්බවෙමු."),
  ],
  foot="また 〜",
)

if __name__ == "__main__":
    render(P62, "p116_mata")
