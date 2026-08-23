from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"せる"
KANJ = r("漢字","かん じ")
YOM  = r("読","よ")+"める"
HAYA = r("早","はや")+"く"
OKI  = r("起","お")+"きる"
MAI  = r("毎日","まい にち")
BEN  = r("勉強","べん きょう")
YAS  = r("野菜","や さい")
TAB  = r("食","た")+"べる"
JITE = r("自転車","じ てん しゃ")
NOR  = r("乗","の")+"れる"
WASU = r("忘","わす")+"れない"
NOU  = r("能力","のう りょく")
SHUK = r("習慣","しゅう かん")

P = dict(
  no="55", tag=None,
  title_jp="〜ように なります／〜ように します",
  title_ro='〜 you ni narimasu / shimasu &nbsp;|&nbsp; come to be able to / make a habit of &nbsp;|&nbsp; '
           '<span class="si">〜 පුරුදු වෙනවා</span>',
  basic=(f"{NHG}が {HAN}ように なりました。","Nihongo ga hanaseru you ni narimashita.",
         "I have become able to speak Japanese.","මට ජපන් භාෂාව කතා කරන්න පුළුවන් වුණා."),
  use=(f'じしょけい・ない{r("形","けい")}に つけます。'
       f'<b>なります</b>は {NOU}や じょうたいの <b>かわった けっか</b>、'
       f'<b>します</b>は {r("自分","じ ぶん")}で つづける <b>{SHUK}</b>です。',
       'Attach it to the dictionary or nai-form. <b>narimasu</b> = a change that has '
       'happened (ability, state); <b>shimasu</b> = a habit you keep on purpose.',
       'ශබ්දකෝෂ හෝ nai-ආකාරයට දානවා. <b>narimasu</b> = වෙච්ච වෙනස (හැකියාව); '
       '<b>shimasu</b> = තමන් දිගටම කරන පුරුද්ද.'),
  pattern=[["BLANK",("ように なりました","you ni narimashita",True)],
           ["BLANK",("ように して います","you ni shite imasu",True)],
           f"NOTE:よく つかうのは <b>{r('可能','か のう')}{r('形','けい')}</b>と いっしょ"
           f"（{HAN}ように なりました）。89を {r('見','み')}て ください",
           f"NOTE:ひてい：{WASU}ように して います（＝わすれない ように 気を つける）"],
  examples=[
    (f"{NHG}が {HAN}ように なりました。","Nihongo ga hanaseru you ni narimashita.","I have become able to speak Japanese.","මට ජපන් භාෂාව කතා කරන්න පුළුවන් වුණා."),
    (f"{KANJ}が {YOM}ように なりました。","Kanji ga yomeru you ni narimashita.","I can read kanji now.","දැන් මට කන්ජි කියවන්න පුළුවන්."),
    (f"{JITE}に {NOR}ように なりました。","Jitensha ni noreru you ni narimashita.","I can ride a bicycle now.","දැන් මට බයිසිකලේ පදින්න පුළුවන්."),
    (f"{MAI} {BEN}する ように して います。","Mainichi benkyou suru you ni shite imasu.","I make a point of studying every day.","මම හැමදාම ඉගෙන ගන්න පුරුදු වෙලා ඉන්නවා."),
    (f"{HAYA} {OKI}ように して います。","Hayaku okiru you ni shite imasu.","I try to get up early.","මම ඉක්මනට නැගිටින්න පුරුදු වෙලා ඉන්නවා."),
    (f"{YAS}を {TAB}ように して ください。","Yasai wo taberu you ni shite kudasai.","Please try to eat vegetables.","එළවළු කන්න පුරුදු වෙන්න."),
    (f"{WASU}ように して います。","Wasurenai you ni shite imasu.","I make sure not to forget.","අමතක නොවෙන්න බලාගන්නවා."),
  ],
  foot="〜ように なります／します",
)

if __name__ == "__main__":
    render(P, "u55_youni")
