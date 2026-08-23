from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN  = r("先生","せん せい")
KOE  = r("声","こえ")
KIK  = r("聞","き")+"こえます"
JI   = r("字","じ")
CHII = r("小","ちい")+"さくて"
MIE  = r("見","み")+"えません"
MACH = r("町","まち")
SHIT = r("知","し")+"って"
KANG = r("考","かんが")+"えて"
KOTA = r("答","こた")+"えて"
NEM  = r("寝","ね")+"ました"
OBO  = r("覚","おぼ")+"えて"
WAK  = "わかりませんでした"
HIND = r("頻度","ひん ど")
TEID = r("程度","てい ど")

P50 = dict(
  no="119", tag=None,
  title_jp="よく 〜（ていど）",
  title_ro='yoku 〜 &nbsp;|&nbsp; well / clearly &nbsp;|&nbsp; '
           '<span class="si">හොඳට 〜</span>',
  basic=(f"{SEN}の {KOE}が よく {KIK}。","Sensei no koe ga yoku kikoemasu.",
         "I can hear the teacher clearly.","ගුරුතුමාගේ කටහඬ හොඳට ඇහෙනවා."),
  use=(f'69の「よく」は {HIND}（often）でしたが、ここの「よく」は {TEID}（well）です。'
       f'わかる・{r("見","み")}える・{r("聞","き")}こえる・{r("知","し")}る などと いっしょに つかいます。',
       'In 69 <b>yoku</b> meant "often"; here it means "well / clearly". '
       'It goes with verbs like understand, see, hear and know.',
       '69 හි <b>yoku</b> කියන්නේ "නිතරම"; මෙතන "හොඳට". '
       'තේරෙනවා, පේනවා, ඇහෙනවා, දන්නවා වගේ ක්‍රියා එක්ක.'),
  pattern=[[("よく","yoku",True),"BLANK",("ます","masu")],
           [("よく","yoku",True),"BLANK",("ません","masen",True)],
           f"NOTE:69 よく＝{HIND}（クリケットを よく します）　/　119 よく＝{TEID}（よく わかります）",
           f"NOTE:「よく わかりません」は「わかりません」より やわらかい {r('言','い')}い{r('方','かた')}です"],
  examples=[
    (f"{SEN}の {KOE}が よく {KIK}。","Sensei no koe ga yoku kikoemasu.","I can hear the teacher clearly.","ගුරුතුමාගේ කටහඬ හොඳට ඇහෙනවා."),
    (f"この {JI}は {CHII} よく {MIE}。","Kono ji wa chiisakute yoku miemasen.","This writing is small and I can't see it well.","මේ අකුරු පොඩියි, හොඳට පේන්නේ නැහැ."),
    (f"サマンさんは この {MACH}を よく {SHIT} います。","Saman-san wa kono machi wo yoku shitte imasu.","Saman knows this town well.","සමන් මේ නගරය හොඳට දන්නවා."),
    (f"よく {KANG}から {KOTA} ください。","Yoku kangaete kara kotaete kudasai.","Think carefully before you answer.","හොඳට හිතලා උත්තර දෙන්න."),
    (f"きのうは よく {NEM}。","Kinou wa yoku nemashita.","I slept well yesterday.","ඊයේ මම හොඳට නිදාගත්තා."),
    (f"その ことは よく {OBO} いません。","Sono koto wa yoku oboete imasen.","I don't remember that well.","ඒ ගැන හොඳට මතක නැහැ."),
    (f"すみません、よく {WAK}。","Sumimasen, yoku wakarimasen deshita.","Sorry, I didn't quite understand.","සමාවෙන්න, හොඳට තේරුණේ නැහැ."),
  ],
  foot="よく 〜（ていど）",
)

if __name__ == "__main__":
    render(P50, "p119_yoku_teido")
