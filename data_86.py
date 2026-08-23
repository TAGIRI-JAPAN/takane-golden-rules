from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

AME  = r("雨","あめ")
FUT  = r("降","ふ")+"っても"
IKI  = r("行","い")+"きます"
TAKA = r("高","たか")+"くても"
KAI  = r("買","か")+"います"
YOM  = r("読","よ")+"んでも"
WAK  = "わかりません"
BEN  = r("勉強","べん きょう")
OBOE = r("覚","おぼ")+"えられません"
NICH = r("日曜日","にち よう び")
HATA = r("働","はたら")+"きます"
DAR  = r("誰","だれ")
KI   = r("来","き")+"ても"
DAI  = "だいじょうぶです"
SAM  = r("寒","さむ")+"くても"
SAN  = r("散歩","さん ぽ")
GYAK = r("逆","ぎゃく")
JOU  = r("条件","じょう けん")

P = dict(
  no="86", tag=None,
  title_jp="〜ても、〜",
  title_ro='〜 temo &nbsp;|&nbsp; even if 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 උනත්</span>',
  basic=(f"{AME}が {FUT}、{IKI}。","Ame ga futtemo, ikimasu.",
         "Even if it rains, I'll go.","වහිනවා උනත් මම යනවා."),
  use=(f'82〜85は「A なら B」でしたが、86は <b>{GYAK}</b>です。'
       f'「A でも かんけいなく B する」と いう {GYAK}の {JOU}を あらわします。'
       f'て{r("形","けい")}に「も」を つけるだけです。',
       'Units 82–85 were "if A then B"; 86 is the opposite: "B happens regardless of A". '
       'Just add <b>mo</b> to the te-form.',
       '82–85 කිව්වේ "A නම් B"; 86 ඊට විරුද්ධයි: "A උනත් B වෙනවා". '
       'te-ආකාරයට <b>mo</b> දාන්න විතරයි.'),
  pattern=[["BLANK",("ても、","temo",True),("〜ます","~ masu")],
           f"NOTE:て{r('形','けい')} ＋ も：{r('降','ふ')}って → {FUT}　/　"
           f"い けいようし：{r('高','たか')}い → {TAKA}　/　な・めいし：しずか<b>でも</b>",
           f"NOTE:{DAR}が {KI}　/　いつ {KI}　/　どこへ {r('行','い')}っても "
           f"— {r('疑問','ぎ もん')}しと いっしょに よく つかいます"],
  examples=[
    (f"{AME}が {FUT}、{IKI}。","Ame ga futtemo, ikimasu.","Even if it rains, I'll go.","වහිනවා උනත් මම යනවා."),
    (f"{TAKA}、これを {KAI}。","Takakutemo, kore wo kaimasu.","Even if it's expensive, I'll buy this.","ගණන් උනත් මම මේක ගන්නවා."),
    (f"{YOM}、よく {WAK}。","Yondemo, yoku wakarimasen.","Even if I read it, I don't really understand.","කියෙව්වත් හොඳට තේරෙන්නේ නැහැ."),
    (f"{BEN}しても、すぐ {OBOE}。","Benkyou shitemo, sugu oboeraremasen.","Even if I study, I can't memorise it quickly.","ඉගෙන ගත්තත් ඉක්මනට මතක තියාගන්න බැහැ."),
    (f"{NICH}でも {HATA}。","Nichiyoubi demo hatarakimasu.","I work even on Sundays.","ඉරිදා උනත් වැඩ කරනවා."),
    (f"{DAR}が {KI}、{DAI}。","Dare ga kitemo, daijoubu desu.","No matter who comes, it's fine.","කවුරු ආවත් කමක් නැහැ."),
    (f"{SAM}、まいあさ {SAN}します。","Samukutemo, maiasa sanpo shimasu.","Even if it's cold, I take a walk every morning.","සීතල උනත් හැම උදෑසනකම ඇවිදිනවා."),
  ],
  foot="〜ても、〜",
)

if __name__ == "__main__":
    render(P, "u86_temo")
