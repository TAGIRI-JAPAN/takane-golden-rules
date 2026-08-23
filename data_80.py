from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MISE = r("店","みせ")
YASU = r("安","やす")+"い"
CHIK = r("近","ちか")+"い"
HEYA = r("部屋","へ や")
HIRO = r("広","ひろ")+"い"
AKA  = r("明","あか")+"るい"
SEN  = r("先生","せん せい")
SHIN = r("親切","しん せつ")
OSHI = r("教","おし")+"え"
JOZ  = r("上手","じょう ず")
KYO  = r("今日","きょう")
AME  = r("雨","あめ")
SAM  = r("寒","さむ")+"い"
IE   = r("家","いえ")
IMAS = "います"
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
TANO = "たのしい"
YAKU = r("役","やく")
TAT  = r("立","た")+"つ"
RIYU = r("理由","り ゆう")

P = dict(
  no="80", tag=None,
  title_jp="〜し、〜し",
  title_ro='〜 shi, 〜 shi &nbsp;|&nbsp; and (listing reasons) &nbsp;|&nbsp; '
           '<span class="si">〜 ත්, 〜 ත්</span>',
  basic=(f"この {MISE}は {YASU}し、{CHIK}し、よく {r('行','い')}きます。",
         "Kono mise wa yasui shi, chikai shi, yoku ikimasu.",
         "This shop is cheap and close, so I often go.","මේ කඩේ ලාබයි, ළඟයි, ඒ නිසා නිතරම යනවා."),
  use=(f'{RIYU}や とくちょうを <b>いくつも ならべる</b> ときに つかいます。'
       f'「〜て、〜」（75）より、「ほかにも ある」と いう {r("気持","き も")}ちが つよいです。'
       f'まえは ふつうけい。',
       'Use it to line up several reasons or features. Compared with <b>~ te</b> (75), '
       'it adds the feeling "and there is more". The plain form comes before it.',
       'හේතු හෝ ලක්ෂණ <b>කිහිපයක් පෙළගස්සන්න</b>. 75 හි <b>~ te</b> වලට වඩා '
       '"තව තියෙනවා" කියන හැඟීම ශක්තිමත්. කලින් සරල ආකාරය.'),
  pattern=[["BLANK",("し、","shi",True),"BLANK",("し、〜","shi",True)],
           f"NOTE:ふつうけい ＋ し：{YASU}し　/　{SHIN}<b>だ</b>し　/　"
           f"{r('学生','がく せい')}<b>だ</b>し　/　{r('行','い')}くし",
           f"NOTE:さいごに {RIYU}の けつろんが 来ます（〜し、〜し、<b>だから</b> 〜）"],
  examples=[
    (f"この {MISE}は {YASU}し、{CHIK}し、よく {r('行','い')}きます。","Kono mise wa yasui shi, chikai shi, yoku ikimasu.","This shop is cheap and close, so I often go.","මේ කඩේ ලාබයි, ළඟයි, ඒ නිසා නිතරම යනවා."),
    (f"この {HEYA}は {HIRO}し、{AKA}し、いいですね。","Kono heya wa hiroi shi, akarui shi, ii desu ne.","This room is big and bright — nice, isn't it.","මේ කාමරය ලොකුයි, එළියයි, හොඳයි නේ."),
    (f"{SEN}は {SHIN}だし、{OSHI}方も {JOZ}です。","Sensei wa shinsetsu da shi, oshiekata mo jouzu desu.","The teacher is kind and teaches well.","ගුරුතුමා කරුණාවන්තයි, උගන්නන්නත් හොඳයි."),
    (f"{KYO}は {AME}だし、{SAM}し、{IE}に {IMAS}。","Kyou wa ame da shi, samui shi, ie ni imasu.","It's raining and cold today, so I'll stay home.","අද වහිනවා, සීතලයි, ඒ නිසා ගෙදර ඉන්නවා."),
    (f"{NHG}は {TANO}し、{YAKU}に {TAT}し、{BEN}して います。","Nihongo wa tanoshii shi, yaku ni tatsu shi, benkyou shite imasu.","Japanese is fun and useful, so I'm studying it.","ජපන් භාෂාව විනෝදජනකයි, වැඩදායකයි, ඒ නිසා ඉගෙන ගන්නවා."),
    (f"サマンさんは クリケットも できるし、{r('歌','うた')}も {JOZ}です。","Saman-san wa kuriketto mo dekiru shi, uta mo jouzu desu.","Saman can play cricket and sings well too.","සමන්ට ක්‍රිකට් පුළුවන්, සිංදුත් හොඳයි."),
    (f"お{r('金','かね')}も ないし、{r('時間','じ かん')}も ありません。","Okane mo nai shi, jikan mo arimasen.","I have no money and no time.","සල්ලිත් නැහැ, වෙලාවත් නැහැ."),
  ],
  foot="〜し、〜し",
)

if __name__ == "__main__":
    render(P, "u80_shi")
