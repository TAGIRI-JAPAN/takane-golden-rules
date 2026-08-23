from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN  = r("先生","せん せい")
ASHI = r("明日","あ した")
YASU = r("休","やす")+"み"
ITT  = r("言","い")+"って いました"
KUR  = r("来","く")+"る"
TEN  = r("天気","てん き")
AME  = r("雨","あめ")
KAI  = r("会議","かい ぎ")
JI   = r("時","じ")
HAJI = r("始","はじ")+"まる"
TSUT = r("伝","つた")+"えて"
DEN  = r("電話","でん わ")
CHOK = r("直接","ちょく せつ")
DENB = r("伝聞","でん ぶん")

P = dict(
  no="56", tag=None,
  title_jp="〜と 言って いました",
  title_ro='〜 to itte imashita &nbsp;|&nbsp; (someone) said that 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කියලා කිව්වා</span>',
  basic=(f"{SEN}は {ASHI} {YASU}だと {ITT}。","Sensei wa ashita yasumi da to itte imashita.",
         "The teacher said tomorrow is a day off.","ගුරුතුමා කිව්වා හෙට නිවාඩු කියලා."),
  use=(f'<b>だれが {r("言","い")}ったか</b>を はっきり させて つたえる かたちです。'
       f'57の「だそうです」は だれが {r("言","い")}ったか {r("言","い")}いませんが、'
       f'ここは 「{SEN}は」と はっきり {r("言","い")}います。まえは ふつうけい。',
       'Use it to report what a named person said. Pattern 57 <b>da sou desu</b> does not '
       'say who; here you name the speaker. The plain form comes before <b>to</b>.',
       'කවුද කිව්වේ කියලා පැහැදිලිව කියන ක්‍රමය. 57 හි <b>da sou desu</b> කවුද කියලා '
       'කියන්නේ නැහැ; මෙතන කියනවා. <b>to</b> එකට කලින් සරල ආකාරය.'),
  pattern=[[("〜は","~ wa"),"BLANK",("と 言って いました","to itte imashita",True)],
           f"NOTE:57 だそうです（だれが {r('言','い')}ったか {r('言','い')}わない）　⇔　"
           f"56 と {ITT}（{r('言','い')}った {r('人','ひと')}を はっきり）",
           f"NOTE:たのむ とき：「〜と {TSUT} いただけませんか」"
           f"（＝つたえて ください）"],
  examples=[
    (f"{SEN}は {ASHI} {YASU}だと {ITT}。","Sensei wa ashita yasumi da to itte imashita.","The teacher said tomorrow is a day off.","ගුරුතුමා කිව්වා හෙට නිවාඩු කියලා."),
    (f"サマンさんは {ASHI} {KUR}と {ITT}。","Saman-san wa ashita kuru to itte imashita.","Saman said he is coming tomorrow.","සමන් කිව්වා හෙට එනවා කියලා."),
    (f"ニュースで {ASHI}は {AME}だと {ITT}。","Nyuusu de ashita wa ame da to itte imashita.","The news said it will rain tomorrow.","ප්‍රවෘත්තිවල කිව්වා හෙට වහිනවා කියලා."),
    (f"{KAI}は 3{JI}に {HAJI}と {ITT}。","Kaigi wa sanji ni hajimaru to itte imashita.","They said the meeting starts at three.","රැස්වීම 3ට පටන් ගන්නවා කියලා කිව්වා."),
    (f"{SEN}は {TEN}が わるいと {ITT}。","Sensei wa tenki ga warui to itte imashita.","The teacher said the weather is bad.","ගුරුතුමා කිව්වා කාලගුණය නරකයි කියලා."),
    (f"サマンさんに {DEN}したと {ITT}。","Saman-san ni denwa shita to itte imashita.","He said he called Saman.","එයා කිව්වා සමන්ට කතා කළා කියලා."),
    (f"{CHOK} {SEN}に {r('聞','き')}いて ください。","Chokusetsu sensei ni kiite kudasai.","Please ask the teacher directly.","කෙලින්ම ගුරුතුමාගෙන් අහන්න."),
  ],
  foot="〜と 言って いました",
)

if __name__ == "__main__":
    render(P, "u56_toitte")
