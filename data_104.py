from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NEG  = r("願","ねが")+"いします"
HIT  = r("一","ひと")+"つ"
FUT  = r("二","ふた")+"つ"
KAIK = r("会計","かい けい")
MIZU = r("水","みず")
NAM  = r("名前","な まえ")
ASHI = r("明日","あ した")
JI   = r("時","じ")
MISE = r("店","みせ")
SHIG = r("仕事","し ごと")

P69 = dict(
  no="104", tag=None,
  title_jp=f"〜、お{NEG}",
  title_ro='〜, onegai shimasu &nbsp;|&nbsp; 〜, please &nbsp;|&nbsp; '
           '<span class="si">කරුණාකරලා 〜</span>',
  basic=(f"コーヒーを {HIT}、お{NEG}。","Koohii wo hitotsu, onegai shimasu.",
         "One coffee, please.","කරුණාකරලා කෝපි එකක් දෙන්න."),
  use=(f'{MISE}・えき・{SHIG}ばで {r("何","なに")}かを たのむ ときの ことばです。'
       f'「〜を ください」より ていねいで、どこでも つかえます。',
       'Use it to ask for something in a shop, at a station or at work. '
       'It is politer than <b>~ wo kudasai</b> and works anywhere.',
       'කඩේ, දුම්රියපොළේ, රැකියා ස්ථානයේ යමක් ඉල්ලද්දී. '
       '<b>~ wo kudasai</b> වලට වඩා ආචාරශීලීයි, හැම තැනම පාවිච්චි කරන්න පුළුවන්.'),
  pattern=[["BLANK",(f"、お{NEG}","onegai shimasu",True)],
           ["BLANK",(f"を お{NEG}","wo onegai shimasu",True)],
           f"NOTE:ともだちには かるく「〜、お{r('願','ねが')}い」と {r('言','い')}います",
           f"NOTE:「よろしく お{NEG}」は シンハラ{r('語','ご')}に ない ことばです。"
           f"あいさつとして そのまま おぼえて ください"],
  examples=[
    (f"コーヒーを {HIT}、お{NEG}。","Koohii wo hitotsu, onegai shimasu.","One coffee, please.","කරුණාකරලා කෝපි එකක් දෙන්න."),
    (f"お{KAIK}、お{NEG}。","Okaikei, onegai shimasu.","The bill, please.","කරුණාකරලා බිල දෙන්න."),
    (f"カレーを {FUT}、お{NEG}。","Karee wo futatsu, onegai shimasu.","Two curries, please.","කරුණාකරලා කරි දෙකක් දෙන්න."),
    (f"すみません、お{MIZU}を お{NEG}。","Sumimasen, omizu wo onegai shimasu.","Excuse me, water please.","සමාවෙන්න, කරුණාකරලා වතුර ටිකක් දෙන්න."),
    (f"こちらに {NAM}を お{NEG}。","Kochira ni namae wo onegai shimasu.","Your name here, please.","කරුණාකරලා මෙතන නම ලියන්න."),
    (f"{ASHI}の {r('朝','あさ')} 9{JI}に お{NEG}。","Ashita no asa kuji ni onegai shimasu.","Tomorrow at nine in the morning, please.","කරුණාකරලා හෙට උදේ 9ට."),
    (f"どうぞ よろしく お{NEG}。","Douzo yoroshiku onegai shimasu.","I look forward to working with you.","කරුණාකරලා මට උදව් කරන්න."),
  ],
  foot="〜、お願いします",
)

if __name__ == "__main__":
    render(P69, "p104_onegaishimasu")
