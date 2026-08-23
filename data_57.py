from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASHI = r("明日","あ した")
AME  = r("雨","あめ")
MISE = r("店","みせ")
JOZ  = r("上手","じょう ず")
SEN  = r("先生","せん せい")
RAIS = r("来週","らい しゅう")
KUNI = r("国","くに")
KAER = r("帰","かえ")+"る"
KARE = r("彼","かれ")
ATAR = r("新","あたら")+"しい"
KURU = r("車","くるま")
KATT = r("買","か")+"った"
NICH = r("日曜日","にち よう び")
AIT  = r("開","あ")+"いて"
KINO = r("昨日","きのう")
KANT = r("簡単","かん たん")
KII  = r("聞","き")+"いた"
OMO  = r("思","おも")+"います"

P37 = dict(
  no="57", tag=None,
  title_jp="〜だそうです",
  title_ro='〜 da sou desu &nbsp;|&nbsp; I hear (that) 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 ලු</span>',
  basic=(f"{ASHI}は {AME}だそうです。","Ashita wa ame da sou desu.",
         "I hear it will rain tomorrow.","හෙට වහිනවලු."),
  use=(f'{KII} ことを ほかの {r("人","ひと")}に つたえる ことばです。'
       f'シンハラ{r("語","ご")}の「ලු」と {r("同","おな")}じ はたらきです。39の「〜と {OMO}」は '
       f'{r("自分","じ ぶん")}の かんがえです。',
       'Use it to pass on what you heard. It works just like the Sinhala <b>-lu</b>. '
       'Pattern 39 <b>to omoimasu</b> is your own idea, not hearsay.',
       'අහපු දේ අනිත් අයට කියන්න. සිංහල <b>ලු</b> එකම වැඩේ කරනවා. '
       '39 හි <b>to omoimasu</b> කියන්නේ තමන්ගේ අදහස.'),
  pattern=[[("〜は","~ wa"),"BLANK",("だそうです","da sou desu",True)],
           [("〜は","~ wa"),"BLANK",("するそうです","suru sou desu",True)],
           [("〜は","~ wa"),"BLANK",("したそうです","shita sou desu",True)],
           f"NOTE:めいし・な けいようし → だそうです　/　い けいようし・どうし → そうです"],
  examples=[
    (f"{ASHI}は {AME}だそうです。","Ashita wa ame da sou desu.","I hear it will rain tomorrow.","හෙට වහිනවලු."),
    (f"あの {MISE}の カレーは おいしいそうです。","Ano mise no karee wa oishii sou desu.","I hear the curry at that shop is good.","අර කඩේ කරිය රසයිලු."),
    (f"サマンさんは クリケットが {JOZ}だそうです。","Saman-san wa kuriketto ga jouzu da sou desu.","I hear Saman is good at cricket.","සමන් ක්‍රිකට් හොඳට කරනවලු."),
    (f"{SEN}は {RAIS} {KUNI}へ {KAER}そうです。","Sensei wa raishuu kuni e kaeru sou desu.","I hear the teacher will go home next week.","ගුරුතුමා ලබන සතියේ රටට යනවලු."),
    (f"{KARE}は {ATAR} {KURU}を {KATT}そうです。","Kare wa atarashii kuruma wo katta sou desu.","I hear he bought a new car.","ඔහු අලුත් කාරයක් අරගෙනලු."),
    (f"あの {MISE}は {NICH} {AIT} いないそうです。","Ano mise wa nichiyoubi aite inai sou desu.","I hear that shop isn't open on Sundays.","අර කඩේ ඉරිදාට වහලා තියෙනවලු."),
    (f"{KINO}の テストは {KANT}だったそうです。","Kinou no tesuto wa kantan datta sou desu.","I hear yesterday's test was easy.","ඊයේ විභාගය ලේසි වුණාලු."),
  ],
  foot="〜だそうです",
)

if __name__ == "__main__":
    render(P37, "p57_dasoudesu")
