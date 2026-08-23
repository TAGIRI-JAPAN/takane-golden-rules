from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ATAM = r("頭","あたま")
ITA  = r("痛","いた")+"い"
JIT  = r("実","じつ")
ASHI = r("明日","あ した")
YASU = r("休","やす")+"み"
DOKO = "どこ"
IKI  = r("行","い")+"きます"
KAN  = r("漢字","かん じ")
YOM  = r("読","よ")+"めない"
CHOT = "ちょっと"
TETS = r("手伝","て つだ")+"って"
KUR  = r("車","くるま")
KOW  = "こわれた"
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
JOUK = r("状況","じょう きょう")
RIYU = r("理由","り ゆう")

P = dict(
  no="30", tag=None,
  title_jp="〜んです",
  title_ro='〜 n desu &nbsp;|&nbsp; explaining a situation or reason &nbsp;|&nbsp; '
           '<span class="si">〜 නිසා තමයි</span>',
  basic=(f"{ATAM}が {ITA}んです。","Atama ga itai n desu.",
         "The thing is, I have a headache.","මගේ ඔලුව රිදෙනවා."),
  use=(f'ただの じじつでは なく、{JOUK}や {RIYU}を <b>せつめいする</b> ときに つけます。'
       f'まえは ふつうけい。めいし・な けいようしには「な」が {r("入","はい")}ります。',
       'Add it when you are explaining a situation or a reason, not just stating a fact. '
       'It follows the plain form; nouns and na-adjectives take <b>na</b>.',
       'හුදෙක් කරුණක් නෙවෙයි, තත්ත්වයක් හෝ හේතුවක් <b>පැහැදිලි කරද්දී</b> දානවා. '
       'සරල ආකාරයට පස්සේ; නාම පද හා na-විශේෂණවලට <b>na</b>.'),
  pattern=[["BLANK",("んです","n desu",True)],
           ["BLANK",("んですか？","n desu ka",True)],
           f"NOTE:ふつうけい ＋ んです：{ITA}んです　/　{IKI}→{r('行','い')}くんです　/　"
           f"{YASU}<b>な</b>んです　/　しずか<b>な</b>んです",
           f"NOTE:かいわでは「〜んだ」。{r('聞','き')}く ときは「どうしたんですか」"
           f"「どうして 〜んですか」"],
  examples=[
    (f"{ATAM}が {ITA}んです。","Atama ga itai n desu.","The thing is, I have a headache.","මගේ ඔලුව රිදෙනවා."),
    ("どうしたんですか。","Doushita n desu ka.","What's the matter?","මොකද වුණේ?"),
    (f"{ASHI}は {YASU}なんです。","Ashita wa yasumi na n desu.","Actually, tomorrow is a day off.","හෙට නිවාඩු දවසක්."),
    (f"この {KAN}が {YOM}んですが…","Kono kanji ga yomenai n desu ga…","I can't read this kanji, you see…","මට මේ කන්ජි කියවන්න බැහැ නේ…"),
    (f"{CHOT} {TETS} いただけませんか。","Chotto tetsudatte itadakemasen ka.","Could you help me a little?","ටිකක් උදව් කරන්න පුළුවන්ද?"),
    (f"{KUR}が {KOW}んです。","Kuruma ga kowareta n desu.","My car has broken down.","මගේ කාරය කැඩිලා."),
    (f"どうして {NHG}を {BEN}して いるんですか。","Doushite nihongo wo benkyou shite iru n desu ka.","Why are you studying Japanese?","ඇයි ඔයා ජපන් භාෂාව ඉගෙන ගන්නේ?"),
  ],
  foot="〜んです",
)

if __name__ == "__main__":
    render(P, "u30_ndesu")
