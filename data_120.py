from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MON  = r("問題","もん だい")
DEK  = "できませんでした"
NET  = r("寝","ね")+"て"
RENR = r("連絡","れん らく")
NEWS = "ニュース"
SHIR = r("知","し")+"りませんでした"
HEYA = r("部屋","へ や")
HITO = r("人","ひと")
OKO  = r("怒","おこ")+"りません"
ONA  = r("同","おな")+"じ"
KAB  = "かばん"
MOT  = r("持","も")+"って"
ZEN  = r("全然","ぜん ぜん")

P51 = dict(
  no="120", tag=None,
  title_jp="まったく 〜ないです",
  title_ro='mattaku 〜 nai desu &nbsp;|&nbsp; not 〜 at all &nbsp;|&nbsp; '
           '<span class="si">කිසිසේත්ම 〜 නැහැ</span>',
  basic=(f"この {MON}は まったく {DEK}。","Kono mondai wa mattaku dekimasen deshita.",
         "I couldn't do this question at all.","මේ ප්‍රශ්නය කිසිසේත්ම කරන්න බැරි වුණා."),
  use=(f'0パーセントの ひていです。117の「あまり」より ずっと つよく、'
       f'「{ZEN} 〜ない」と{r("同","おな")}じ {r("意味","い み")}です。',
       'A 0% negative — much stronger than <b>amari</b> (117), and the same as '
       '<b>zenzen ~ nai</b>.',
       '0% නෙගටිව් එකක්. 117 හි <b>amari</b> වලට වඩා ගොඩක් ශක්තිමත්; '
       '<b>zenzen ~ nai</b> එකම අර්ථයයි.'),
  pattern=[[("まったく","mattaku",True),"BLANK",("ないです","nai desu",True)],
           f"NOTE:つよさ：あまり 〜ない（117）　&lt;　まったく 〜ない（120）＝ {ZEN} 〜ない（0％）",
           f"NOTE:ひていで ない ときも あります：まったく {ONA}です　/　まったく その とおりです"],
  examples=[
    (f"この {MON}は まったく {DEK}。","Kono mondai wa mattaku dekimasen deshita.","I couldn't do this question at all.","මේ ප්‍රශ්නය කිසිසේත්ම කරන්න බැරි වුණා."),
    (f"きのうから まったく {NET} いません。","Kinou kara mattaku nete imasen.","I haven't slept at all since yesterday.","ඊයේ ඉඳන් කිසිසේත්ම නිදාගෙන නැහැ."),
    (f"サマンさんから {RENR}が まったく ありません。","Saman-san kara renraku ga mattaku arimasen.","There is no word from Saman at all.","සමන්ගෙන් කිසිම පණිවිඩයක් නැහැ."),
    (f"その {NEWS}は まったく {SHIR}。","Sono nyuusu wa mattaku shirimasen deshita.","I didn't know that news at all.","ඒ ප්‍රවෘත්තිය කිසිසේත්ම දැනගෙන හිටියේ නැහැ."),
    (f"この {HEYA}には まったく {HITO}が いません。","Kono heya ni wa mattaku hito ga imasen.","There is nobody at all in this room.","මේ කාමරයේ කිසිම කෙනෙක් නැහැ."),
    (f"サマンさんは まったく {OKO}。","Saman-san wa mattaku okorimasen.","Saman never gets angry at all.","සමන් කිසිසේත්ම කේන්ති ගන්නේ නැහැ."),
    (f"まったく {ONA} {KAB}を {MOT} います。","Mattaku onaji kaban wo motte imasu.","I have exactly the same bag.","මට හරියටම ඒ වගේම බෑග් එකක් තියෙනවා."),
  ],
  foot="まったく 〜ないです",
)

if __name__ == "__main__":
    render(P51, "p120_mattaku")
