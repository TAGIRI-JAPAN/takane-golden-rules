from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SRI  = "スリランカ"
NIH  = r("日本","に ほん")
ATSU = r("暑","あつ")+"いです"
DEN  = r("電車","でん しゃ")
HAYA = r("速","はや")+"いです"
HON  = r("本","ほん")
KANT = r("簡単","かん たん")
KYO  = r("今日","きょう")
KINO = r("昨日","きのう")
ISO  = "いそがしいです"
W    = r("私","わたし")
NHG  = r("日本語","に ほん ご")
JOZ  = r("上手","じょう ず")
SUKI = r("好","す")+"き"
EIG  = r("英語","えい ご")
MUZU = "むずかしいです"
HOU  = r("方","ほう")

P43 = dict(
  no="48", tag=None,
  title_jp="…より 〜です",
  title_ro='... yori 〜 desu &nbsp;|&nbsp; 〜er than ... &nbsp;|&nbsp; '
           '<span class="si">... ට වඩා 〜</span>',
  basic=(f"{SRI}は {NIH}より {ATSU}。","Suriranka wa Nihon yori atsui desu.",
         "Sri Lanka is hotter than Japan.","ශ්‍රී ලංකාව ජපානයට වඩා රස්නෙයි."),
  use=(f'2つを くらべる ことばです。「Aは Bより 〜」＝ Aの {HOU}が 〜。'
       f'シンハラ{r("語","ご")}は「Bට වඩා A」で、じゅんばんが ぎゃくなので {r("注意","ちゅう い")}。',
       'Use it to compare two things: <b>A wa B yori ~</b> means A is more ~ than B. '
       'Careful — Sinhala says <b>B-ṭa vaḍā A</b>, the opposite order.',
       'දෙකක් සංසන්දනය කරන්න: <b>A wa B yori ~</b> = B ට වඩා A වැඩියි. '
       'සිංහලෙන් <b>B ට වඩා A</b> — අනුපිළිවෙළ අනිත් පැත්තයි, පරිස්සමෙන්.'),
  pattern=[[("Aは","A wa"),("Bより","B yori",True),"BLANK",("です","desu")],
           f"NOTE:{SRI}は {NIH}より {ATSU}　＝　{NIH}は {SRI}より さむいです",
           f"NOTE:「Aより Bが {SUKI}です」＝ Bの {HOU}が {SUKI}（{r('選','えら')}ぶ ときの {r('言','い')}い{r('方','かた')}）"],
  examples=[
    (f"{SRI}は {NIH}より {ATSU}。","Suriranka wa Nihon yori atsui desu.","Sri Lanka is hotter than Japan.","ශ්‍රී ලංකාව ජපානයට වඩා රස්නෙයි."),
    (f"{DEN}は バスより {HAYA}。","Densha wa basu yori hayai desu.","Trains are faster than buses.","දුම්රිය බස් එකට වඩා වේගවත්."),
    (f"この {HON}は あの {HON}より {KANT}です。","Kono hon wa ano hon yori kantan desu.","This book is easier than that one.","මේ පොත අර පොතට වඩා ලේසියි."),
    (f"{KYO}は {KINO}より {ISO}。","Kyou wa kinou yori isogashii desu.","Today is busier than yesterday.","අද ඊයේට වඩා කාර්යබහුලයි."),
    (f"サマンさんは {W}より {NHG}が {JOZ}です。","Saman-san wa watashi yori nihongo ga jouzu desu.","Saman is better at Japanese than me.","සමන් මට වඩා ජපන් භාෂාව හොඳට දන්නවා."),
    (f"{W}は カレーより ラーメンが {SUKI}です。","Watashi wa karee yori raamen ga suki desu.","I like ramen more than curry.","මම කරි වලට වඩා රාමෙන් වලට කැමතියි."),
    (f"{NHG}は {EIG}より {MUZU}。","Nihongo wa eigo yori muzukashii desu.","Japanese is harder than English.","ජපන් භාෂාව ඉංග්‍රීසියට වඩා අමාරුයි."),
  ],
  foot="…より 〜です",
)

if __name__ == "__main__":
    render(P43, "p48_yori")
