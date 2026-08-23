from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN  = r("先生","せん せい")
GAK  = r("学生","がく せい")
NHG  = r("日本語","に ほん ご")
HANA = r("話","はな")+"させます"
HAHA = r("母","はは")
IMO  = r("妹","いもうと")
HEYA = r("部屋","へ や")
SOJ  = r("掃除","そう じ")
KANJ = r("漢字","かん じ")
KAK  = r("書","か")+"かせます"
CHIC = r("父","ちち")
OTO  = r("弟","おとうと")
TETS = r("手伝","て つだ")+"い"
FUN  = r("分","ふん")
YASU = r("休","やす")+"ませます"
W    = r("私","わたし")
KO   = r("子","こ")
YAS  = r("野菜","や さい")
TABE = r("食","た")+"べさせます"
NAM  = r("名前","な まえ")
IWA  = r("言","い")+"わせます"
JITA = r("自動詞","じ どう し")

P53 = dict(
  no="100", tag=None,
  title_jp="〜させます",
  title_ro='〜 sasemasu &nbsp;|&nbsp; make / let someone 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරවනවා</span>',
  basic=(f"{SEN}は {GAK}に {NHG}で {HANA}。","Sensei wa gakusei ni nihongo de hanasasemasu.",
         "The teacher makes the students speak in Japanese.","ගුරුතුමා ශිෂ්‍යයන්ට ජපන් භාෂාවෙන් කතා කරවනවා."),
  use=(f'ほかの {r("人","ひと")}に させる かたちです。{r("意味","い み")}は 2つ：①しじ（make）②きょか（let）。'
       f'シンハラ{r("語","ご")}の「කරවනවා」と{r("同","おな")}じ しくみです。',
       'This form makes someone else do something. Two meanings: (1) make, (2) let. '
       'It works like the Sinhala causative <b>-vanavā</b>.',
       'අනිත් කෙනාට යමක් කරවන ආකාරය. අර්ථ දෙකයි: (1) බල කරනවා, (2) අවසර දෙනවා. '
       'සිංහල <b>කරවනවා</b> වගේම.'),
  pattern=[[("〜に","~ ni"),"BLANK",("させます","sasemasu",True)],
           f"NOTE:たどうし → {r('人','ひと')}に ものを させる　/　{JITA} → {r('人','ひと')}を させる"
           f"（{GAK}を {YASU}）",
           f"NOTE:「お{r('待','ま')}たせしました」も この かたちです"],
  examples=[
    (f"{SEN}は {GAK}に {NHG}で {HANA}。","Sensei wa gakusei ni nihongo de hanasasemasu.","The teacher makes the students speak in Japanese.","ගුරුතුමා ශිෂ්‍යයන්ට ජපන් භාෂාවෙන් කතා කරවනවා."),
    (f"{HAHA}は {IMO}に {HEYA}を {SOJ}させます。","Haha wa imouto ni heya wo souji sasemasu.","My mother makes my sister clean the room.","අම්මා නංගිට කාමරය අස් කරවනවා."),
    (f"{SEN}は {W}たちに {KANJ}を {KAK}。","Sensei wa watashitachi ni kanji wo kakasemasu.","The teacher makes us write kanji.","ගුරුතුමා අපිට කන්ජි ලියවනවා."),
    (f"{CHIC}は {OTO}に {TETS}を させます。","Chichi wa otouto ni tetsudai wo sasemasu.","My father makes my brother help out.","තාත්තා මල්ලිට උදව් කරවනවා."),
    (f"{SEN}は {GAK}を 5{FUN} {YASU}。","Sensei wa gakusei wo gofun yasumasemasu.","The teacher lets the students rest for five minutes.","ගුරුතුමා ශිෂ්‍යයන්ට විනාඩි 5ක් විවේක දෙනවා."),
    (f"{W}は {KO}どもに {YAS}を {TABE}。","Watashi wa kodomo ni yasai wo tabesasemasu.","I make my child eat vegetables.","මම දරුවාට එළවළු කවනවා."),
    (f"{SEN}は {GAK}に {NAM}を {IWA}。","Sensei wa gakusei ni namae wo iwasemasu.","The teacher has the students say their names.","ගුරුතුමා ශිෂ්‍යයන්ට නම කියවනවා."),
  ],
  foot="〜させます",
)

if __name__ == "__main__":
    render(P53, "p100_sasemasu")
