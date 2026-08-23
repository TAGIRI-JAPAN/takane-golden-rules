from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TABE = r("食","た")+"べて"
BEN  = r("勉強","べん きょう")
NER  = r("寝","ね")+"る"
MIGA = "みがきます"
JUG  = r("授業","じゅ ぎょう")
OWA  = r("終","お")+"わった"
TOS  = r("図書館","と しょ かん")
IKI  = r("行","い")+"きます"
TE   = r("手","て")
ARA  = r("洗","あら")+"って"
NIH  = r("日本","に ほん")
KURU = r("来","く")+"る"
SHIG = r("仕事","し ごと")
KAI  = r("買","か")+"い"+r("物","もの")
DEK  = r("出","で")+"かける"
KAGI = "かぎ"
JISH = r("辞書","じ しょ")
SHOK = r("食事","しょく じ")
TABR = r("食","た")+"べる"
TABT = r("食","た")+"べた"

P62 = dict(
  no="71", tag=None,
  title_jp="〜して から／まえに／あとで",
  title_ro='〜 te kara / 〜 mae ni / 〜 ta ato de &nbsp;|&nbsp; after / before &nbsp;|&nbsp; '
           '<span class="si">〜 ට පස්සේ / කලින්</span>',
  basic=(f"ごはんを {TABE}から、{BEN}します。","Gohan wo tabete kara, benkyou shimasu.",
         "After eating, I study.","කෑම කාලා පස්සේ මම ඉගෙන ගන්නවා."),
  use=(f'2つの ことの じゅんばんを {r("言","い")}います。まえに は かならず '
       f'<b>じしょけい</b>、あとで は かならず <b>たけい</b>です。',
       'These say which of two things happens first. <b>mae ni</b> takes the dictionary '
       'form; <b>ato de</b> takes the ta-form.',
       'දේවල් දෙකක අනුපිළිවෙළ කියනවා. <b>mae ni</b> ට ශබ්දකෝෂ ආකාරය; '
       '<b>ato de</b> ට ta-ආකාරය.'),
  pattern=[["BLANK",("して から","shite kara",True),("〜します","~ shimasu")],
           ["BLANK",("する まえに","suru mae ni",True),("〜します","~ shimasu")],
           ["BLANK",("した あとで","shita ato de",True),("〜します","~ shimasu")],
           f"NOTE:まえに → じしょけい（{TABR} まえに）　/　あとで → たけい（{TABT} あとで）",
           f"NOTE:めいしにも つきます：{SHIG}の まえに　/　{SHOK}の あとで"],
  examples=[
    (f"ごはんを {TABE}から、{BEN}します。","Gohan wo tabete kara, benkyou shimasu.","After eating, I study.","කෑම කාලා පස්සේ මම ඉගෙන ගන්නවා."),
    (f"{NER} まえに、はを {MIGA}。","Neru mae ni, ha wo migakimasu.","I brush my teeth before I sleep.","නිදාගන්න කලින් දත් මදිනවා."),
    (f"{JUG}が {OWA} あとで、{TOS}へ {IKI}。","Jugyou ga owatta ato de, toshokan e ikimasu.","After class ends, I go to the library.","පන්තිය ඉවර වුණාට පස්සේ පුස්තකාලයට යනවා."),
    (f"{TE}を {ARA}から、{TABE} ください。","Te wo aratte kara, tabete kudasai.","Please wash your hands before eating.","අත් හෝදලා පස්සේ කන්න."),
    (f"{NIH}へ {KURU} まえに、{r('日本語','に ほん ご')}を {BEN}しました。","Nihon e kuru mae ni, nihongo wo benkyou shimashita.","I studied Japanese before coming to Japan.","ජපානෙට එන්න කලින් ජපන් භාෂාව ඉගෙන ගත්තා."),
    (f"{SHIG}の あとで、{KAI}を します。","Shigoto no ato de, kaimono wo shimasu.","After work I do the shopping.","වැඩ ඉවර වුණාට පස්සේ බඩු ගන්නවා."),
    (f"{DEK} まえに、{KAGI}を かけました。","Dekakeru mae ni, kagi wo kakemashita.","I locked the door before going out.","එළියට යන්න කලින් දොර වහලා අගුළු දැම්මා."),
  ],
  foot="〜して から／まえに／あとで",
)

if __name__ == "__main__":
    render(P62, "u71_junjo")
