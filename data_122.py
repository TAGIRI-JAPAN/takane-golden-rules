from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN  = r("先生","せん せい")
MAT  = r("待","ま")+"ち"
NAR  = "なりました"
KAK  = r("書","か")+"き"
YOM  = r("読","よ")+"み"
TSUK = r("使","つか")+"い"
IRA  = "いらっしゃいます"
GOR  = "ごらんに なります"
MESH = r("召","め")+"し"+r("上","あ")+"がります"
OSSH = "おっしゃいます"
NASA = "なさいます"
SHAC = r("社長","しゃ ちょう")
KYA  = r("客","きゃく")
SON  = r("尊敬語","そん けい ご")
AIT  = r("相手","あい て")

P = dict(
  no="122", tag=None,
  title_jp="尊敬語（お〜に なります）",
  title_ro='sonkeigo &nbsp;|&nbsp; honorific — lifting the other person up &nbsp;|&nbsp; '
           '<span class="si">ගෞරව බස</span>',
  basic=(f"{SEN}が お{MAT}に {NAR}。","Sensei ga omachi ni narimashita.",
         "The teacher has been waiting.","ගුරුතුමා ඉන්නවා."),
  use=(f'{SON}は <b>{AIT}の {r("動作","どう さ")}</b>を {r("高","たか")}めて {r("言","い")}う ことばです。'
       f'{r("自分","じ ぶん")}の ことには つかいません。'
       f'{SHAC}・{SEN}・お{KYA}さまの ことを {r("話","はな")}す ときに つかいます。',
       'Honorific language raises <b>the other person\'s actions</b>. Never use it for '
       'yourself. Use it when talking about a boss, a teacher or a customer.',
       'ගෞරව බස කියන්නේ <b>අනිත් කෙනාගේ ක්‍රියාව</b> උසස් කරලා කියන එක. '
       'තමන් ගැන කවදාවත් නෙවෙයි. ලොක්කා, ගුරුතුමා, ගනුදෙනුකරු ගැන කියද්දී.'),
  pattern=[[("お","o",True),("ますけい","masu stem"),("に なります","ni narimasu",True)],
           [("〜（ら）れます","(ra)remasu",True)],
           f"NOTE:お＋ますけい＋に なります：お{MAT}に なる　/　お{KAK}に なる　/　お{YOM}に なる。"
           f"かんたんな 形は うけみと {r('同','おな')}じ「〜れます」（68）",
           f"NOTE:とくべつな 形：いる・{r('行','い')}く・{r('来','く')}る → {IRA}　/　"
           f"{r('見','み')}る → {GOR}　/　{r('食','た')}べる・{r('飲','の')}む → {MESH}　/　"
           f"{r('言','い')}う → {OSSH}　/　する → {NASA}"],
  examples=[
    (f"{SEN}が お{MAT}に {NAR}。","Sensei ga omachi ni narimashita.","The teacher has been waiting.","ගුරුතුමා ඉන්නවා."),
    (f"この {r('本','ほん')}を お{YOM}に なりましたか。","Kono hon wo oyomi ni narimashita ka.","Have you read this book?","මේ පොත කියෙව්වද?"),
    (f"{SHAC}は もう {IRA}。","Shachou wa mou irasshaimasu.","The president is already here.","සභාපතිතුමා දැනටමත් ඉන්නවා."),
    (f"{SEN}は {r('何','なん')}と {OSSH}か。","Sensei wa nan to osshaimashita ka.","What did the teacher say?","ගුරුතුමා මොකද කිව්වේ?"),
    (f"どうぞ {MESH} ください。","Douzo meshiagatte kudasai.","Please help yourself.","කරුණාකරලා කන්න."),
    (f"こちらを {GOR}。","Kochira wo goran ni narimasu ka.","Would you like to look at this?","මේක බලනවද?"),
    (f"{SEN}は もう {r('帰','かえ')}られました。","Sensei wa mou kaeraremashita.","The teacher has already gone home.","ගුරුතුමා දැනටමත් ගෙදර ගිහින්."),
  ],
  foot="尊敬語（お〜に なります）",
)

if __name__ == "__main__":
    render(P, "u122_sonkei")
