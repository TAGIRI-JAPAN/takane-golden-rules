from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KANG = r("考","かんが")+"えさせて"
TSUK = r("使","つか")+"わせて"
KYO  = r("今日","きょう")
HAYA = r("早","はや")+"く"
KAER = r("帰","かえ")+"らせて"
ASHI = r("明日","あ した")
YASU = r("休","やす")+"ませて"
HANA = r("話","はなし")
KIK  = r("聞","き")+"かせて"
W    = r("私","わたし")
NIM  = r("荷物","に もつ")
MOT  = r("持","も")+"たせて"
DEN  = r("電話","でん わ")
ICHI = r("一度","いち ど")
TETS = r("手伝","て つだ")+"わせて"
KAK  = r("書","か")+"かせる"
TAB  = r("食","た")+"べさせる"
KOS  = r("来","こ")+"させる"

P52 = dict(
  no="101", tag=None,
  title_jp="〜させて ください",
  title_ro='〜 sasete kudasai &nbsp;|&nbsp; Please let me 〜 &nbsp;|&nbsp; '
           '<span class="si">මට 〜 කරන්න දෙන්න</span>',
  basic=(f"ちょっと {KANG} ください。","Chotto kangaesasete kudasai.",
         "Please let me think for a moment.","මට ටිකක් හිතන්න දෙන්න."),
  use=(f'{r("自分","じ ぶん")}が したい ことを ていねいに {r("申","もう")}し{r("出","で")}る ときの ことばです。'
       f'つくり{r("方","かた")}は 100と{r("同","おな")}じ しえきけいです。',
       'Use it to politely offer or ask to do something yourself. '
       'The form is the causative, the same as in 100.',
       'තමන් කරන්න කැමති දෙයක් ආචාරශීලීව ඉල්ලන්න. '
       'හැඩය 100 හි හේතුකාරක ආකාරයමයි.'),
  pattern=[[(f"（{W}に）","watashi ni"),"BLANK",("させて ください","sasete kudasai",True)],
           f"NOTE:つくり{r('方','かた')}：{r('書','か')}きます → {KAK}　/　{r('食','た')}べます → {TAB}　/　"
           f"します → させる　/　{r('来','き')}ます → {KOS}",
           f"NOTE:もっと ていねいに：「〜させて いただけませんか」"],
  examples=[
    (f"ちょっと {KANG} ください。","Chotto kangaesasete kudasai.","Please let me think for a moment.","මට ටිකක් හිතන්න දෙන්න."),
    (f"この パソコンを {TSUK} ください。","Kono pasokon wo tsukawasete kudasai.","Please let me use this computer.","මට මේ පරිගණකය පාවිච්චි කරන්න දෙන්න."),
    (f"{KYO}は {HAYA} {KAER} ください。","Kyou wa hayaku kaerasete kudasai.","Please let me go home early today.","අද මට ඉක්මනට ගෙදර යන්න දෙන්න."),
    (f"{ASHI} {YASU} ください。","Ashita yasumasete kudasai.","Please let me take tomorrow off.","හෙට මට නිවාඩු දෙන්න."),
    (f"その {HANA}を {KIK} ください。","Sono hanashi wo kikasete kudasai.","Please let me hear that story.","මට ඒ කතාව අහන්න දෙන්න."),
    (f"{W}に {NIM}を {MOT} ください。","Watashi ni nimotsu wo motasete kudasai.","Please let me carry your bag.","මට බඩු අරන් යන්න දෙන්න."),
    (f"もう {ICHI} {W}に {TETS} ください。","Mou ichido watashi ni tetsudawasete kudasai.","Please let me help you once more.","තව එක් වතාවක් මට උදව් කරන්න දෙන්න."),
  ],
  foot="〜させて ください",
)

if __name__ == "__main__":
    render(P52, "p101_sasetekudasai")
