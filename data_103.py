from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HAYA = r("早","はや")+"く"
OKI  = r("起","お")+"きなさい"
TE   = r("手","て")
ARA  = r("洗","あら")+"いなさい"
YOKU = "よく"
KIKI = r("聞","き")+"きなさい"
NAM  = r("名前","な まえ")
KAKI = r("書","か")+"きなさい"
ZEN  = r("全部","ぜん ぶ")
TABE = r("食","た")+"べなさい"
NE   = r("寝","ね")+"なさい"
HON  = r("本","ほん")
YOMI = r("読","よ")+"みなさい"
GOH  = "ごはん"
OYA  = r("親","おや")
SEN  = r("先生","せん せい")
UE   = r("上","うえ")
HITO = r("人","ひと")

P47 = dict(
  no="103", tag=None,
  title_jp="〜しなさい",
  title_ro='〜 shinasai &nbsp;|&nbsp; Do 〜 (instruction) &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න (අණ කිරීම)</span>',
  basic=(f"{HAYA} {OKI}。","Hayaku okinasai.",
         "Get up early.","ඉක්මනට නැගිටින්න."),
  use=(f'{OYA}や{SEN}が {r("子","こ")}どもや{r("生徒","せい と")}に しじする ときの ことばです。'
       f'{UE}の {HITO}には つかえません。その ときは「〜て ください」です。',
       'Parents and teachers use it to tell children or students what to do. '
       'Never use it to someone above you — say <b>-te kudasai</b> instead.',
       'දෙමාපියන් හා ගුරුවරු ළමයින්ට කියන විදිහ. '
       'ඔබට වඩා ලොකු කෙනෙකුට කවදාවත් නෙවෙයි — එතකොට <b>-te kudasai</b>.'),
  pattern=[["BLANK",("しなさい","shinasai",True)],
           f"NOTE:ますけい ＋ なさい：{r('書','か')}きます → {KAKI}　/　{r('食','た')}べます → {TABE}　/　"
           f"します → しなさい　/　{r('来','き')}ます → {r('来','き')}なさい",
           f"NOTE:テストの しじにも よく {r('出','で')}ます（「{r('答','こた')}えを {KAKI}」）"],
  examples=[
    (f"{HAYA} {OKI}。","Hayaku okinasai.","Get up early.","ඉක්මනට නැගිටින්න."),
    (f"{TE}を {ARA}。","Te wo arainasai.","Wash your hands.","අත් හෝදන්න."),
    (f"{YOKU} {KIKI}。","Yoku kikinasai.","Listen carefully.","හොඳට අහන්න."),
    (f"ここに {NAM}を {KAKI}。","Koko ni namae wo kakinasai.","Write your name here.","මෙතන නම ලියන්න."),
    (f"{GOH}を {ZEN} {TABE}。","Gohan wo zenbu tabenasai.","Eat all your rice.","බත් ඔක්කොම කන්න."),
    (f"{HAYA} {NE}。","Hayaku nenasai.","Go to bed early.","ඉක්මනට නිදාගන්න."),
    (f"この {HON}を {YOMI}。","Kono hon wo yominasai.","Read this book.","මේ පොත කියවන්න."),
  ],
  foot="〜しなさい",
)

if __name__ == "__main__":
    render(P47, "p103_shinasai")
