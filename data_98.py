from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NIH  = r("日本","に ほん")
HATA = r("働","はたら")+"く"
TAME = "ために"
BEN  = r("勉強","べん きょう")
KAZ  = r("家族","か ぞく")
KANE = r("金","かね")
TAM  = r("貯","た")+"めて"
KAI  = r("買","か")+"い"
MONO = r("物","もの")
IKI  = r("行","い")+"きます"
TOS  = r("図書館","と しょ かん")
KARI = r("借","か")+"り"
SHOK = r("食事","しょく じ")
KEN  = r("健康","けん こう")
YAS  = r("野菜","や さい")
TAB  = r("食","た")+"べます"
MOKU = r("目的","もく てき")
EKI  = r("駅","えき")
MUKA = r("迎","むか")+"え"

P = dict(
  no="98", tag=None,
  title_jp="〜ために／〜に 行きます",
  title_ro='〜 tame ni / 〜 ni ikimasu &nbsp;|&nbsp; in order to 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 සඳහා</span>',
  basic=(f"{NIH}で {HATA} {TAME}、{r('日本語','に ほん ご')}を {BEN}して います。",
         "Nihon de hataraku tame ni, nihongo wo benkyou shite imasu.",
         "I'm studying Japanese in order to work in Japan.","ජපානේ වැඩ කරන්න ජපන් භාෂාව ඉගෙන ගන්නවා."),
  use=(f'{MOKU}を {r("言","い")}う ことばです。「ために」の {r("前","まえ")}は じしょけい、'
       f'めいしには「の」。<b>{r("行","い")}く・{r("来","く")}る・{r("帰","かえ")}る</b>と いっしょの ときは、'
       f'みじかく <b>「ますけい ＋ に {IKI}」</b>と {r("言","い")}えます。',
       'This states a purpose. Use the dictionary form before <b>tame ni</b> (nouns take '
       '<b>no</b>). With <b>iku / kuru / kaeru</b> you can shorten it to '
       '<b>masu-stem + ni ikimasu</b>.',
       'අරමුණක් කියනවා. <b>tame ni</b> ට කලින් ශබ්දකෝෂ ආකාරය (නාම පදවලට <b>no</b>). '
       '<b>iku / kuru / kaeru</b> එක්ක නම් <b>masu-stem + ni ikimasu</b> කියලා කෙටි කරන්න පුළුවන්.'),
  pattern=[["BLANK",(f"{TAME}、","tame ni",True),("〜します","~ shimasu")],
           [("ますけい","masu stem"),"BLANK",(f"に {IKI}","ni ikimasu",True)],
           f"NOTE:じしょけい ＋ ために（{HATA} ために）　/　めいし ＋ の ために（{KAZ}の ために）",
           f"NOTE:{r('買','か')}います → {KAI}<b>に</b> {IKI}　/　"
           f"{r('見','み')}ます → {r('見','み')}<b>に</b> {IKI}　/　"
           f"{BEN}します → {BEN}<b>に</b> {IKI}"],
  examples=[
    (f"{NIH}で {HATA} {TAME}、{r('日本語','に ほん ご')}を {BEN}して います。","Nihon de hataraku tame ni, nihongo wo benkyou shite imasu.","I'm studying Japanese in order to work in Japan.","ජපානේ වැඩ කරන්න ජපන් භාෂාව ඉගෙන ගන්නවා."),
    (f"{KAZ}の {TAME}、お{KANE}を {TAM} います。","Kazoku no tame ni, okane wo tamete imasu.","I'm saving money for my family.","පවුල වෙනුවෙන් සල්ලි එකතු කරනවා."),
    (f"{KEN}の {TAME}、{YAS}を {TAB}。","Kenkou no tame ni, yasai wo tabemasu.","I eat vegetables for my health.","සෞඛ්‍යය වෙනුවෙන් එළවළු කනවා."),
    (f"コンビニへ {KAI}{MONO}に {IKI}。","Konbini e kaimono ni ikimasu.","I'm going to the convenience store to shop.","කඩේට බඩු ගන්න යනවා."),
    (f"{TOS}へ {r('本','ほん')}を {KARI}に {IKI}。","Toshokan e hon wo kari ni ikimasu.","I'm going to the library to borrow a book.","පුස්තකාලයට පොතක් ගන්න යනවා."),
    (f"{EKI}へ サマンさんを {MUKA}に {IKI}。","Eki e Saman-san wo mukae ni ikimasu.","I'm going to the station to meet Saman.","දුම්රියපොළට සමන්ව හම්බවෙන්න යනවා."),
    (f"{SHOK}に {IKI}ませんか。","Shokuji ni ikimasen ka.","Shall we go for a meal?","කෑමක් ගන්න යමුද?"),
  ],
  foot="〜ために／〜に 行きます",
)

if __name__ == "__main__":
    render(P, "u98_tameni")
