from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

OSO  = r("遅","おそ")+"く"
JAM  = "おじゃま"
SEW  = r("世話","せ わ")
DEK  = "できません"
ASHI = r("明日","あ した")
REI  = r("お礼","お れい")
WABI = r("お詫","お わ")+"び"

P60 = dict(
  no="115", tag=None,
  title_jp="どうも 〜",
  title_ro='doumo 〜 &nbsp;|&nbsp; thanks / sorry / somehow &nbsp;|&nbsp; '
           '<span class="si">බොහොම 〜 / කොහොම හරි 〜</span>',
  basic=("どうも ありがとうございました。","Doumo arigatou gozaimashita.",
         "Thank you very much.","බොහොම ස්තූතියි."),
  use=(f'「どうも」には 3つの つかい{r("方","かた")}が あります：①{REI} ②{WABI} '
       f'③なんとなく（「どうも 〜ない」）。113の「どうぞ」と まちがえないで ください。',
       '<b>Doumo</b> has three uses: (1) thanks, (2) apology, (3) "somehow" '
       '(with <b>~ nai</b>). Don\'t mix it up with <b>douzo</b> in 113.',
       '<b>Doumo</b> වලට භාවිත 3ක්: (1) ස්තූතිය, (2) සමාව, (3) "කොහොම හරි" '
       '(<b>~ nai</b> එක්ක). 113 හි <b>douzo</b> එක්ක පටලවා ගන්න එපා.'),
  pattern=[[("どうも","doumo",True),"BLANK"],
           [("どうも","doumo",True),"BLANK",("ない","nai",True)],
           f"NOTE:①{REI}：どうも ありがとう　②{WABI}：どうも すみません　③なんとなく：どうも {DEK}",
           f"NOTE:「どうも。」だけでも かるい あいさつに なります"],
  examples=[
    ("どうも ありがとうございました。","Doumo arigatou gozaimashita.","Thank you very much.","බොහොම ස්තූතියි."),
    (f"どうも {OSO} なりました。","Doumo osoku narimashita.","I'm sorry I'm late.","පරක්කු වුණාට සමාවෙන්න."),
    (f"どうも {JAM}しました。","Doumo ojama shimashita.","Sorry to have bothered you.","කරදරයක් වුණාට සමාවෙන්න."),
    (f"どうも お{SEW}に なりました。","Doumo osewa ni narimashita.","Thank you for all your help.","ඔයාගේ උදව්වට බොහොම ස්තූතියි."),
    (f"どうも うまく {DEK}。","Doumo umaku dekimasen.","Somehow I just can't do it well.","කොහොම හරි හරියට කරන්න බැහැ."),
    ("どうも おかしいですね。","Doumo okashii desu ne.","Something seems odd, doesn't it.","කොහොම හරි මොකක් හරි වැරදියි වගේ."),
    (f"どうも、また {ASHI}。","Doumo, mata ashita.","Thanks — see you tomorrow.","එහෙනම්, හෙට හම්බවෙමු."),
  ],
  foot="どうも 〜",
)

if __name__ == "__main__":
    render(P60, "p115_doumo")
