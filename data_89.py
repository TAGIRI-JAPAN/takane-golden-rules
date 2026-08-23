from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"せます"
KANJ = r("漢字","かん じ")
YOM  = r("読","よ")+"めます"
JITE = r("自転車","じ てん しゃ")
NOR  = r("乗","の")+"れます"
KARA = r("辛","から")+"い"
TAB  = r("食","た")+"べられません"
KOK  = "ここから"
UMI  = r("海","うみ")
MIE  = r("見","み")+"えます"
KOE  = r("声","こえ")
KIK  = r("聞","き")+"こえません"
KAK  = r("書","か")+"けます"
KOR  = r("来","こ")+"られます"
DEK  = "できます"
NOU  = r("能力","のう りょく")
SEN_ = r("先生","せん せい")

P = dict(
  no="89", tag=None,
  title_jp="可能形（〜えます／〜られます）",
  title_ro='potential form &nbsp;|&nbsp; can do / be able to &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න පුළුවන්</span>',
  basic=(f"{r('私','わたし')}は {NHG}が {HAN}。","Watashi wa nihongo ga hanasemasu.",
         "I can speak Japanese.","මට ජපන් භාෂාව කතා කරන්න පුළුවන්."),
  use=(f'18の「〜する ことが {DEK}」と {r("同","おな")}じ {r("意味","い み")}ですが、'
       f'こちらの ほうが みじかくて よく つかわれます。'
       f'まえの 「を」は ふつう <b>「が」</b>に かわります。',
       'Same meaning as <b>~ koto ga dekimasu</b> in 18, but shorter and far more common. '
       'The object particle <b>wo</b> usually changes to <b>ga</b>.',
       '18 හි <b>~ koto ga dekimasu</b> එකම අර්ථය; හැබැයි මේක කෙටියි, බහුලයි. '
       'කර්ම නිපාතය <b>wo</b> සාමාන්‍යයෙන් <b>ga</b> වෙනවා.'),
  pattern=[[("〜は","~ wa"),("〜が","~ ga",True),"BLANK",("えます／られます","emasu / raremasu",True)],
           f"NOTE:Iグループ：{r('書','か')}く → {KAK}　/　{r('話','はな')}す → {HAN}　"
           f"IIグループ：{r('食','た')}べる → {r('食','た')}べられます　"
           f"IIIグループ：する → {DEK}　/　{r('来','く')}る → {KOR}",
           f"NOTE:{r('見','み')}る・{r('聞','き')}くは とくべつ："
           f"{MIE}（{r('自然','し ぜん')}に {r('目','め')}に {r('入','はい')}る）　/　"
           f"{r('聞','き')}こえます（{r('自然','し ぜん')}に {r('耳','みみ')}に {r('入','はい')}る）"],
  examples=[
    (f"{r('私','わたし')}は {NHG}が {HAN}。","Watashi wa nihongo ga hanasemasu.","I can speak Japanese.","මට ජපන් භාෂාව කතා කරන්න පුළුවන්."),
    (f"この {KANJ}が {YOM}か。","Kono kanji ga yomemasu ka.","Can you read this kanji?","මේ කන්ජි කියවන්න පුළුවන්ද?"),
    (f"サマンさんは {JITE}に {NOR}。","Saman-san wa jitensha ni noremasu.","Saman can ride a bicycle.","සමන්ට බයිසිකලේ පදින්න පුළුවන්."),
    (f"{r('私','わたし')}は {KARA} ものが {TAB}。","Watashi wa karai mono ga taberaremasen.","I can't eat spicy food.","මට සැර දේවල් කන්න බැහැ."),
    (f"{KOK} {UMI}が {MIE}。","Koko kara umi ga miemasu.","You can see the sea from here.","මෙතනින් මුහුද පේනවා."),
    (f"{SEN_}の {KOE}が {KIK}。","Sensei no koe ga kikoemasen.","I can't hear the teacher's voice.","ගුරුතුමාගේ කටහඬ ඇහෙන්නේ නැහැ."),
    (f"あした 3{r('時','じ')}に {KOR}か。","Ashita sanji ni koraremasu ka.","Can you come at three tomorrow?","හෙට 3ට එන්න පුළුවන්ද?"),
  ],
  foot="可能形（〜えます／〜られます）",
)

if __name__ == "__main__":
    render(P, "u89_kanou")
