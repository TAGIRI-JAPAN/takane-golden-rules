from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NEN  = r("念","ねん")
ICHI = r("一度","いち ど")
YOM  = r("読","よ")+"みます"
NAM  = r("名前","な まえ")
KAI  = r("書","か")+"いて"
SEN  = r("先生","せん せい")
KII  = r("聞","き")+"いて"
HAYA = r("早","はや")+"く"
DE   = r("出","で")+"ましょう"
MIZU = r("水","みず")
MOT  = r("持","も")+"って"
IKI  = r("行","い")+"きます"
JUS  = r("住所","じゅう しょ")
KAKU = r("確認","かく にん")

P65 = dict(
  no="112", tag=None,
  title_jp=f"{NEN}の ために 〜",
  title_ro='nen no tame ni 〜 &nbsp;|&nbsp; just in case &nbsp;|&nbsp; '
           '<span class="si">ආරක්ෂාවට 〜</span>',
  basic=(f"{NEN}の ために もう {ICHI} {YOM}。","Nen no tame ni mou ichido yomimasu.",
         "I'll read it once more, just in case.","ආරක්ෂාවට තව එක පාරක් කියවනවා."),
  use=(f'あとで こまらない ように、まえもって しておく ときの ことばです。'
       f'しごとや がっこうで とても よく つかいます。',
       'Use it when you do something in advance so there is no trouble later. '
       'Very common at work and at school.',
       'පස්සේ කරදරයක් නොවෙන්න කලින්ම යමක් කරද්දී කියනවා. '
       'රැකියාවේ හා පාසලේ බහුලවම භාවිතා වෙනවා.'),
  pattern=[[(f"{NEN}の ために","nen no tame ni",True),"BLANK",("します","shimasu")],
           [(f"{NEN}の ために","nen no tame ni",True),"BLANK",("して ください","shite kudasai",True)],
           f"NOTE:よく つかう どうし：{KAKU}します　/　{r('聞','き')}きます　/　{MOT} いきます　/　メモします",
           f"NOTE:にた ことば：「いちおう」は かるく、「{NEN}の ために」は ていねいです"],
  examples=[
    (f"{NEN}の ために もう {ICHI} {YOM}。","Nen no tame ni mou ichido yomimasu.","I'll read it once more, just in case.","ආරක්ෂාවට තව එක පාරක් කියවනවා."),
    (f"{NEN}の ために {NAM}を {KAI} おきます。","Nen no tame ni namae wo kaite okimasu.","I'll write down the name just in case.","ආරක්ෂාවට නම ලියලා තියන්නම්."),
    (f"{NEN}の ために {SEN}に {KII} みます。","Nen no tame ni sensei ni kiite mimasu.","I'll ask the teacher just in case.","ආරක්ෂාවට ගුරුතුමාගෙන් අහලා බලන්නම්."),
    (f"{NEN}の ために {HAYA} {DE}。","Nen no tame ni hayaku demashou.","Let's leave early just in case.","ආරක්ෂාවට ඉක්මනට පිටත් වෙමු."),
    (f"{NEN}の ために {MIZU}を {MOT} {IKI}。","Nen no tame ni mizu wo motte ikimasu.","I'll take some water just in case.","ආරක්ෂාවට වතුර අරන් යනවා."),
    (f"{NEN}の ために メモを して ください。","Nen no tame ni memo wo shite kudasai.","Please make a note just in case.","ආරක්ෂාවට සටහනක් තියාගන්න."),
    (f"{NEN}の ために {JUS}も {KAI} ください。","Nen no tame ni juusho mo kaite kudasai.","Please write your address too, just in case.","ආරක්ෂාවට ලිපිනයත් ලියන්න."),
  ],
  foot="念の ために 〜",
)

if __name__ == "__main__":
    render(P65, "p112_nennotameni")
