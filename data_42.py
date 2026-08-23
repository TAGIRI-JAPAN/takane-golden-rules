from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
SUKI = r("好","す")+"き"
DAIS = r("大好","だい す")+"き"
KIRA = "きらい"
KARE = r("彼","かれ")
KANO = r("彼女","かの じょ")
INU  = r("犬","いぬ")
UMI  = r("海","うみ")
NIH  = r("日本","に ほん")
NHG  = r("日本語","に ほん ご")
UTA  = r("歌","うた")
AMA  = r("甘","あま")+"い"
HANA = r("花","はな")
ANE  = r("姉","あね")

P34 = dict(
  no="42", tag=None,
  title_jp=f"〜が {SUKI}です",
  title_ro='〜 ga suki desu &nbsp;|&nbsp; I like 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වලට කැමතියි</span>',
  basic=(f"{W}は クリケットが {SUKI}です。","Watashi wa kuriketto ga suki desu.",
         "I like cricket.","මම ක්‍රිකට් වලට කැමතියි."),
  use=(f'{SUKI}な もの・こと・しゅみを{r("言","い")}う ことばです。'
       f'「〜を」ではなく かならず「〜が」を つかいます。{SUKI}は な けいようしです。',
       'Use it for things and hobbies you like. Always use <b>ga</b>, never <b>wo</b>. '
       '<b>suki</b> is a na-adjective.',
       'කැමති දේවල් හා විනෝදාංශ කියන්න. හැමවිටම <b>ga</b> — <b>wo</b> කවදාවත් නෙවෙයි. '
       '<b>suki</b> කියන්නේ na-විශේෂණ පදයක්.'),
  pattern=[[("〜は","~ wa"),"BLANK",("が","ga",True),(f"{SUKI}です","suki desu",True)],
           f"NOTE:{DAIS}です　&gt;　{SUKI}です　&gt;　あまり {SUKI}じゃないです　&gt;　{KIRA}です",
           f"NOTE:な けいようし：{SUKI}です　/　{SUKI}じゃないです　/　{SUKI}な {r('食','た')}べ{r('物','もの')}"],
  examples=[
    (f"{W}は クリケットが {SUKI}です。","Watashi wa kuriketto ga suki desu.","I like cricket.","මම ක්‍රිකට් වලට කැමතියි."),
    (f"サマンさんは {INU}が {SUKI}です。","Saman-san wa inu ga suki desu.","Saman likes dogs.","සමන් බල්ලන්ට කැමතියි."),
    (f"{KARE}は カレーが {DAIS}です。","Kare wa karee ga daisuki desu.","He loves curry.","ඔහු කරි වලට ගොඩක් කැමතියි."),
    (f"{KANO}は {NIH}の アニメが {SUKI}です。","Kanojo wa Nihon no anime ga suki desu.","She likes Japanese anime.","ඇය ජපන් ඇනිමේ වලට කැමතියි."),
    (f"{ANE}は {HANA}が {SUKI}です。","Ane wa hana ga suki desu.","My older sister likes flowers.","මගේ අක්කා මල් වලට කැමතියි."),
    (f"{W}は {NHG}の {UTA}が {SUKI}です。","Watashi wa nihongo no uta ga suki desu.","I like Japanese songs.","මම ජපන් සිංදු වලට කැමතියි."),
    (f"{W}は {AMA} ものが あまり {SUKI}じゃないです。","Watashi wa amai mono ga amari suki ja nai desu.","I don't really like sweet things.","මම පැණි රස දේවලට එච්චර කැමති නැහැ."),
  ],
  foot="〜が 好きです",
)

if __name__ == "__main__":
    render(P34, "p42_gasuki")
