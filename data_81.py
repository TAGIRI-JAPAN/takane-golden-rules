from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

YASU = r("休","やす")+"みの"
HI   = r("日","ひ")
HON  = r("本","ほん")
YON  = r("読","よ")+"んだり"
ONG  = r("音楽","おん がく")
KII  = r("聞","き")+"いたり"
SOJ  = r("掃除","そう じ")
SEN  = r("洗濯","せん たく")
KYO  = r("教室","きょう しつ")
TAB  = r("食","た")+"べたり"
NON  = r("飲","の")+"んだり"
AME  = r("雨","あめ")
FUT  = r("降","ふ")+"ったり"
YAN  = "やんだり"
IT   = r("行","い")+"ったり"
KI   = r("来","き")+"たり"
NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"したり"
KAI  = r("書","か")+"いたり"
REI  = r("例","れい")

P = dict(
  no="81", tag=None,
  title_jp="〜たり 〜たり します",
  title_ro='〜 tari 〜 tari shimasu &nbsp;|&nbsp; doing things like A and B &nbsp;|&nbsp; '
           '<span class="si">〜 කරනවා, 〜 කරනවා වගේ දේවල්</span>',
  basic=(f"{YASU} {HI}は {HON}を {YON}、{ONG}を {KII} します。",
         "Yasumi no hi wa hon wo yondari, ongaku wo kiitari shimasu.",
         "On days off I read books, listen to music and so on.","නිවාඩු දවසට පොත් කියවනවා, සංගීතය අහනවා වගේ දේවල් කරනවා."),
  use=(f'いくつかの ことを <b>{REI}として</b> ならべる かたちです。'
       f'「ぜんぶ」ではなく「たとえば こんな こと」と いう {r("意味","い み")}に なります。'
       f'さいごは かならず <b>します</b>で おわります。',
       'Use it to list a couple of activities <b>as examples</b> — "things like A and B", '
       'not a complete list. It always ends with <b>shimasu</b>.',
       'දේවල් කිහිපයක් <b>උදාහරණ විදිහට</b> පෙළගස්සනවා — "A, B වගේ දේවල්". '
       'අගට හැමවිටම <b>shimasu</b>.'),
  pattern=[["BLANK",("たり、","tari",True),"BLANK",("たり します","tari shimasu",True)],
           f"NOTE:た{r('形','けい')} ＋ り：{r('読','よ')}んだ → {YON}　/　"
           f"{r('食','た')}べた → {TAB}　/　した → したり",
           f"NOTE:はんたいの ことばを ならべると「くりかえし」：{FUT} {YAN}　/　{IT} {KI}"],
  examples=[
    (f"{YASU} {HI}は {HON}を {YON}、{ONG}を {KII} します。","Yasumi no hi wa hon wo yondari, ongaku wo kiitari shimasu.","On days off I read books, listen to music and so on.","නිවාඩු දවසට පොත් කියවනවා, සංගීතය අහනවා වගේ දේවල් කරනවා."),
    (f"にちようびは {SOJ}したり、{SEN}したり します。","Nichiyoubi wa souji shitari, sentaku shitari shimasu.","On Sundays I clean, do laundry and so on.","ඉරිදාට කාමරය අස් කරනවා, ඇඳුම් හෝදනවා වගේ දේවල් කරනවා."),
    (f"{KYO}で {TAB}、{NON} しないで ください。","Kyoushitsu de tabetari, nondari shinaide kudasai.","Please don't eat or drink in the classroom.","පන්ති කාමරයේ කන්න, බොන්න එපා."),
    (f"{NHG}で {HAN}、{KAI} します。","Nihongo de hanashitari, kaitari shimasu.","I speak and write in Japanese.","ජපන් භාෂාවෙන් කතා කරනවා, ලියනවා."),
    (f"{AME}が {FUT} {YAN} して います。","Ame ga futtari yandari shite imasu.","It keeps raining on and off.","වැස්ස වහිනවා නවතිනවා වෙනවා."),
    (f"サマンさんは よく {IT} {KI} して います。","Saman-san wa yoku ittari kitari shite imasu.","Saman keeps going back and forth.","සමන් නිතරම ගිහින් එනවා."),
    (f"やすみに クリケットを したり、カレーを {r('作','つく')}ったり しました。","Yasumi ni kuriketto wo shitari, karee wo tsukuttari shimashita.","On my day off I played cricket and made curry.","නිවාඩුවට ක්‍රිකට් ගැහුවා, කරි උයුවා."),
  ],
  foot="〜たり 〜たり します",
)

if __name__ == "__main__":
    render(P, "u81_taritari")
