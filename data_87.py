from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NHG  = r("日本語","に ほん ご")
MUZU = "むずかしいです"
IKI  = r("行","い")+"きたいです"
JIK  = r("時間","じ かん")
MIZU = r("水","みず")
DEN  = r("電話","でん わ")
YASU = r("安","やす")+"いです"
SHIT = r("失礼","しつ れい")
NAM  = r("名前","な まえ")
KAI  = r("会話","かい わ")
KAK  = r("書","か")+"きことば"
MAE  = r("前","まえ")+"おき"

P65 = dict(
  no="87", tag=None,
  title_jp="〜が、〜／〜けど、〜",
  title_ro='〜 ga / 〜 kedo &nbsp;|&nbsp; but / and (joining two sentences) &nbsp;|&nbsp; '
           '<span class="si">〜 නමුත් 〜</span>',
  basic=(f"この カレーは からいですが、おいしいです。","Kono karee wa karai desu ga, oishii desu.",
         "This curry is spicy, but it's delicious.","මේ කරිය සැරයි, නමුත් රසයි."),
  use=(f'2つの 文を つなぐ いちばん {r("基本","き ほん")}の ことばです。'
       f'「が」は ていねい・{KAK}、「けど」は {KAI}で つかいます。',
       'This is the most basic way to join two sentences. <b>ga</b> is polite and used in '
       'writing; <b>kedo</b> is used in conversation.',
       'වාක්‍ය දෙකක් සම්බන්ධ කරන මූලිකම ක්‍රමය. <b>ga</b> ආචාරශීලීයි, ලිවීමට; '
       '<b>kedo</b> කතාබහට.'),
  pattern=[["BLANK",("が、","ga",True),("〜です","~ desu")],
           ["BLANK",("けど、","kedo",True),("〜です","~ desu")],
           f"NOTE:「が」＝ていねい・{KAK}　/　「けど」＝{KAI}。{r('意味','い み')}は {r('同','おな')}じです",
           f"NOTE:はんたいの {r('意味','い み')}だけでなく、{MAE}にも つかいます"
           f"（すみませんが…／{SHIT}ですが…）"],
  examples=[
    ("この カレーは からいですが、おいしいです。","Kono karee wa karai desu ga, oishii desu.","This curry is spicy, but it's delicious.","මේ කරිය සැරයි, නමුත් රසයි."),
    (f"{NHG}は {MUZU}けど、たのしいです。","Nihongo wa muzukashii kedo, tanoshii desu.","Japanese is hard, but it's fun.","ජපන් භාෂාව අමාරුයි, ඒත් විනෝදජනකයි."),
    (f"{IKI}が、{JIK}が ありません。","Ikitai desu ga, jikan ga arimasen.","I want to go, but I have no time.","මට යන්න ඕන, නමුත් වෙලාව නැහැ."),
    (f"すみませんが、お{MIZU}を ください。","Sumimasen ga, omizu wo kudasai.","Excuse me, could I have some water.","සමාවෙන්න, වතුර ටිකක් දෙන්න."),
    (f"{DEN}しましたが、いませんでした。","Denwa shimashita ga, imasen deshita.","I called, but he wasn't there.","මම කතා කළා, ඒත් හිටියේ නැහැ."),
    (f"この {r('店','みせ')}は {YASU}けど、あまり おいしくないです。","Kono mise wa yasui kedo, amari oishikunai desu.","This shop is cheap, but not very tasty.","මේ කඩේ ලාබයි, ඒත් එච්චර රසවත් නැහැ."),
    (f"{SHIT}ですが、お{NAM}は？","Shitsurei desu ga, onamae wa?","Excuse me, may I ask your name?","සමාවෙන්න, ඔයාගේ නම මොකක්ද?"),
  ],
  foot="〜が、〜／〜けど、〜",
)

if __name__ == "__main__":
    render(P65, "u87_gakedo")
