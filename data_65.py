from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASHI = r("明日","あ した")
AME  = r("雨","あめ")
FURU = r("降","ふ")+"る"
SHIR = r("知","し")+"らない"
MUZU = "むずかしい"
HITO = r("人","ひと")
SEN  = r("先生","せん せい")
HEYA = r("部屋","へ や")
SHIZ = r("静","しず")+"か"
OKUR = r("遅","おく")+"れる"
KAET = r("帰","かえ")+"った"
GAKU = r("学生","がく せい")

P44 = dict(
  no="65", tag=None,
  title_jp="〜かもしれません",
  title_ro='〜 kamo shiremasen &nbsp;|&nbsp; It might 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වෙන්න පුළුවන්</span>',
  basic=(f"{ASHI} {AME}が {FURU}かもしれません。","Ashita ame ga furu kamo shiremasen.",
         "It might rain tomorrow.","හෙට වහින්න පුළුවන්."),
  use=(f'「そうなる かのうせいが ある」と{r("言","い")}う ことばです。64の「はずです」より '
       f'ずっと よわく、じしんが ない ときに つかいます。',
       'Use it when something is possible. It is much weaker than <b>hazu desu</b> (64) — '
       'you are not sure at all.',
       'යමක් වෙන්න පුළුවන් කියන්න. 64 හි <b>hazu desu</b> වලට වඩා ගොඩක් දුර්වලයි — '
       'විශ්වාසයක් නැති වෙලාවට.'),
  pattern=[[("〜は","~ wa"),"BLANK",("かもしれません","kamo shiremasen",True)],
           f"NOTE:つよさ：きっと 〜はずです（64）　&gt;　〜でしょう　&gt;　〜かもしれません（65）",
           f"NOTE:58と{r('同','おな')}じで、めいし・な けいようしに「だ」は つきません"
           f"（{GAKU}かもしれません　○）"],
  examples=[
    (f"{ASHI} {AME}が {FURU}かもしれません。","Ashita ame ga furu kamo shiremasen.","It might rain tomorrow.","හෙට වහින්න පුළුවන්."),
    (f"サマンさんは まだ {SHIR}かもしれません。","Saman-san wa mada shiranai kamo shiremasen.","Saman might not know yet.","සමන් තාම දන්නේ නැති වෙන්න පුළුවන්."),
    (f"テストは {MUZU}かもしれません。","Tesuto wa muzukashii kamo shiremasen.","The test might be difficult.","විභාගය අමාරු වෙන්න පුළුවන්."),
    (f"あの {HITO}は {SEN}かもしれません。","Ano hito wa sensei kamo shiremasen.","That person might be a teacher.","අර කෙනා ගුරුවරයෙක් වෙන්න පුළුවන්."),
    (f"この {HEYA}は {SHIZ}かもしれません。","Kono heya wa shizuka kamo shiremasen.","This room might be quiet.","මේ කාමරය නිස්කලංක වෙන්න පුළුවන්."),
    (f"バスが {OKUR}かもしれません。","Basu ga okureru kamo shiremasen.","The bus might be late.","බස් එක ප්‍රමාද වෙන්න පුළුවන්."),
    (f"サマンさんは もう {KAET}かもしれません。","Saman-san wa mou kaetta kamo shiremasen.","Saman might have already gone home.","සමන් දැනටමත් ගිහින් වෙන්න පුළුවන්."),
  ],
  foot="〜かもしれません",
)

if __name__ == "__main__":
    render(P44, "p65_kamoshiremasen")
