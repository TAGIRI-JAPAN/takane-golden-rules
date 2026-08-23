from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ATAM = r("頭","あたま")
ITA  = r("痛","いた")+"い"
KYO  = r("今日","きょう")
YASU = r("休","やす")+"みます"
BAS  = "バス"
OKUR = r("遅","おく")+"れた"
CHIK = r("遅刻","ち こく")
AME  = r("雨","あめ")
FUT  = r("降","ふ")+"って いる"
IKI  = r("行","い")+"きません"
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
SUKI = r("好","す")+"き"
YOTE = r("用事","よう じ")
SAKI = r("先","さき")
KAER = r("帰","かえ")+"ります"
RIYU = r("理由","り ゆう")
SHIZ_= r("静","しず")
MAI_ = r("毎日","まい にち")

P = dict(
  no="78", tag=None,
  title_jp="〜ので、〜",
  title_ro='〜 node &nbsp;|&nbsp; because / since 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 නිසා</span>',
  basic=(f"{ATAM}が {ITA}ので、{KYO}は {YASU}。","Atama ga itai node, kyou wa yasumimasu.",
         "I have a headache, so I'll rest today.","ඔලුව රිදෙන නිසා අද විවේක ගන්නවා."),
  use=(f'29で ならった「〜から」と {r("同","おな")}じ {RIYU}の ことばですが、'
       f'「ので」の ほうが <b>やわらかく ていねい</b>です。'
       f'めいし・な けいようしには「<b>な</b>ので」が つきます。',
       'Like <b>kara</b> in unit 29, this gives a reason — but <b>node</b> sounds '
       'softer and politer. Nouns and na-adjectives take <b>na node</b>.',
       '29 හි <b>kara</b> වගේම හේතුවක්; හැබැයි <b>node</b> මෘදුයි, ආචාරශීලීයි. '
       'නාම පද හා na-විශේෂණවලට <b>na node</b>.'),
  pattern=[["BLANK",("ので、","node",True),("〜します","~ shimasu")],
           f"NOTE:ふつうけい ＋ ので：{ITA}ので　/　{FUT}ので　/　{r('学生','がく せい')}<b>な</b>ので　/　"
           f"{SHIZ_}か<b>な</b>ので",
           f"NOTE:から（29）＝はっきり {RIYU}を {r('言','い')}う　⇔　ので＝やわらかい。"
           f"おねがいの まえに よく つかいます"],
  examples=[
    (f"{ATAM}が {ITA}ので、{KYO}は {YASU}。","Atama ga itai node, kyou wa yasumimasu.","I have a headache, so I'll rest today.","ඔලුව රිදෙන නිසා අද විවේක ගන්නවා."),
    (f"{BAS}が {OKUR}ので、{CHIK}しました。","Basu ga okureta node, chikoku shimashita.","The bus was late, so I was late.","බස් එක ප්‍රමාද වුණ නිසා මම පරක්කු වුණා."),
    (f"{AME}が {FUT}ので、{IKI}。","Ame ga futte iru node, ikimasen.","It's raining, so I won't go.","වහින නිසා මම යන්නේ නැහැ."),
    (f"{NHG}が {SUKI}なので、{MAI_} {BEN}します。","Nihongo ga suki na node, mainichi benkyou shimasu.","I like Japanese, so I study every day.","ජපන් භාෂාවට කැමති නිසා හැමදාම ඉගෙන ගන්නවා."),
    (f"{YOTE}が ある ので、{SAKI}に {KAER}。","Youji ga aru node, saki ni kaerimasu.","I have something to do, so I'll leave first.","වැඩක් තියෙන නිසා මම කලින් යනවා."),
    (f"よく わからないので、もう {r('一度','いち ど')} {r('説明','せつ めい')}して ください。","Yoku wakaranai node, mou ichido setsumei shite kudasai.","I don't quite understand, so please explain again.","හොඳට තේරෙන්නේ නැති නිසා ආයෙත් පැහැදිලි කරන්න."),
    (f"{r('学生','がく せい')}なので、お{r('金','かね')}が ありません。","Gakusei na node, okane ga arimasen.","I'm a student, so I have no money.","ශිෂ්‍යයෙක් නිසා සල්ලි නැහැ."),
  ],
  foot="〜ので、〜",
)

if __name__ == "__main__":
    render(P, "u78_node")
