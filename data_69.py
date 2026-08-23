from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
WTC  = r("私","わたし")+"たち"
TOS  = r("図書館","と しょ かん")
BEN  = r("勉強","べん きょう")
NHG  = r("日本語","に ほん ご")
MIM  = r("見","み")+"ます"
KARE = r("彼","かれ")
SHIT = r("質問","しつ もん")
KAIM = r("買","か")+"い"+r("物","もの")
HAN  = r("話","はな")+"します"
RYO  = r("料理","りょう り")
TSUK = r("作","つく")+"ります"
ASA  = r("朝","あさ")
SAN  = r("散歩","さん ぽ")

P31 = dict(
  no="69", tag=None,
  title_jp="よく 〜します",
  title_ro='yoku 〜 shimasu &nbsp;|&nbsp; I often 〜 &nbsp;|&nbsp; '
           '<span class="si">නිතරම 〜 කරනවා</span>',
  basic=(f"{W}は よく {TOS}で {BEN}します。","Watashi wa yoku toshokan de benkyou shimasu.",
         "I often study in the library.","මම නිතරම පුස්තකාලයේ ඉගෙන ගන්නවා."),
  use=(f'することの ひんど（どのくらい するか）を{r("言","い")}う ことばです。'
       f'「よく」は ひんどが{r("高","たか")}く、「いつも」より{r("少","すこ")}し{r("少","すく")}ないです。',
       'It says how often you do something. <b>yoku</b> means "often" — '
       'a little less than <b>itsumo</b> (always).',
       'යමක් කොපමණ වාරයක් කරනවාද කියන එක. <b>yoku</b> = නිතරම — '
       '<b>itsumo</b> (හැමවිටම) වලට වඩා ටිකක් අඩුයි.'),
  pattern=[[("〜は","~ wa"),("よく","yoku",True),"BLANK",("します","shimasu")],
           "NOTE:いつも　&gt;　よく　&gt;　ときどき　&gt;　あまり 〜ません　&gt;　ぜんぜん 〜ません",
           "NOTE:いつも = හැමවිටම　/　よく = නිතරම　/　ときどき = සමහර වෙලාවට　/　"
           "あまり = එච්චර　/　ぜんぜん = කිසිසේත්ම"],
  examples=[
    (f"{W}は よく {TOS}で {BEN}します。","Watashi wa yoku toshokan de benkyou shimasu.","I often study in the library.","මම නිතරම පුස්තකාලයේ ඉගෙන ගන්නවා."),
    (f"{W}は よく {NHG}の ドラマを {MIM}。","Watashi wa yoku nihongo no dorama wo mimasu.","I often watch Japanese dramas.","මම නිතරම ජපන් නාට්‍ය බලනවා."),
    (f"{KARE}は よく {SHIT}します。","Kare wa yoku shitsumon shimasu.","He often asks questions.","ඔහු නිතරම ප්‍රශ්න අහනවා."),
    (f"{W}は よく コンビニで {KAIM}します。","Watashi wa yoku konbini de kaimono shimasu.","I often shop at the convenience store.","මම නිතරම පහසු කඩයෙන් බඩු ගන්නවා."),
    (f"{WTC}は よく {NHG}で {HAN}。","Watashitachi wa yoku nihongo de hanashimasu.","We often talk in Japanese.","අපි නිතරම ජපන් භාෂාවෙන් කතා කරනවා."),
    (f"{W}は よく {RYO}を {TSUK}。","Watashi wa yoku ryouri wo tsukurimasu.","I often cook.","මම නිතරම උයනවා."),
    (f"{W}は {ASA} よく {SAN}します。","Watashi wa asa yoku sanpo shimasu.","I often take a walk in the morning.","මම උදේට නිතරම ඇවිදිනවා."),
  ],
  foot="よく 〜します",
)

if __name__ == "__main__":
    render(P31, "p69_yoku")
