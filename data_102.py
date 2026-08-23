from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
SEN  = r("先生","せん せい")
HOME = r("褒","ほ")+"められました"
NAM  = r("名前","な まえ")
KIK  = r("聞","き")+"かれました"
INU  = r("犬","いぬ")
TE   = r("手","て")
KAM  = "かまれました"
KAER = r("帰","かえ")+"り"
AME  = r("雨","あめ")
FUR  = r("降","ふ")+"られました"
TONA = r("隣","となり")
HITO = r("人","ひと")
ASHI = r("足","あし")
FUM  = "ふまれました"
HON  = r("本","ほん")
OOK  = r("多","おお")+"く"
YOM  = r("読","よ")+"まれて"
GAK  = r("学校","がっ こう")
NEN  = r("年前","ねん まえ")
TAT  = r("建","た")+"てられました"
KAK  = r("書","か")+"かれる"
TAB  = r("食","た")+"べられる"
KOR  = r("来","こ")+"られる"
MEIW = r("迷惑","めい わく")

P54 = dict(
  no="102", tag=None,
  title_jp="〜されました（うけみ）",
  title_ro='〜 saremashita &nbsp;|&nbsp; was 〜ed (passive) &nbsp;|&nbsp; '
           '<span class="si">〜 කරනු ලැබුවා</span>',
  basic=(f"{W}は {SEN}に {HOME}。","Watashi wa sensei ni homeraremashita.",
         "I was praised by the teacher.","මට ගුරුතුමාගෙන් ප්‍රශංසා ලැබුණා."),
  use=(f'{r("何","なに")}かを「される」ほうから{r("言","い")}う かたちです。'
       f'シンハラ{r("語","ご")}は うけみを あまり つかわないので、ここは とくに {r("練習","れん しゅう")}が ひつようです。',
       'This says the sentence from the side that receives the action. '
       'Sinhala rarely uses the passive, so this pattern needs extra practice.',
       'ක්‍රියාව ලබන පැත්තෙන් කියන ආකාරය. '
       'සිංහලෙන් කර්ම කාරකය බහුලව භාවිතා නොවන නිසා මේකට වැඩිපුර පුහුණුවක් ඕනේ.'),
  pattern=[[("〜に","~ ni"),"BLANK",("されました","saremashita",True)],
           f"NOTE:つくり{r('方','かた')}：{r('書','か')}きます → {KAK}　/　{r('食','た')}べます → {TAB}　/　"
           f"します → される　/　{r('来','き')}ます → {KOR}",
           f"NOTE:100 させます（する ほう）　⇔　102 されます（うける ほう）",
           f"NOTE:{MEIW}の うけみ：{AME}に {FUR}（＝こまった {r('気持','き も')}ち）"],
  examples=[
    (f"{W}は {SEN}に {HOME}。","Watashi wa sensei ni homeraremashita.","I was praised by the teacher.","මට ගුරුතුමාගෙන් ප්‍රශංසා ලැබුණා."),
    (f"サマンさんは みんなに {NAM}を {KIK}。","Saman-san wa minna ni namae wo kikaremashita.","Saman was asked his name by everyone.","සමන්ගෙන් හැමෝම නම ඇහුවා."),
    (f"{INU}に {TE}を {KAM}。","Inu ni te wo kamaremashita.","I was bitten on the hand by a dog.","බල්ලෙක් අතේ හපා කෑවා."),
    (f"{KAER}に {AME}に {FUR}。","Kaeri ni ame ni furaremashita.","I got caught in the rain on the way home.","ගෙදර එද්දී වැස්සට අහුවුණා."),
    (f"{TONA}の {HITO}に {ASHI}を {FUM}。","Tonari no hito ni ashi wo fumaremashita.","The person next to me stepped on my foot.","පැත්තෙ හිටපු කෙනා මගේ කකුල මිරිකුවා."),
    (f"この {HON}は {OOK}の {HITO}に {YOM} います。","Kono hon wa ooku no hito ni yomarete imasu.","This book is read by many people.","මේ පොත ගොඩක් අය කියවනවා."),
    (f"この {GAK}は 50{NEN}に {TAT}。","Kono gakkou wa gojuunen mae ni tateraremashita.","This school was built fifty years ago.","මේ පාසල අවුරුදු 50කට කලින් හදලා තියෙනවා."),
  ],
  foot="〜されました（うけみ）",
)

if __name__ == "__main__":
    render(P54, "p102_saremashita")
