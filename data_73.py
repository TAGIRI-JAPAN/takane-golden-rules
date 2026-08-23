from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NAT  = r("夏","なつ")
YASU = r("休","やす")+"み"
RYO  = r("旅行","りょ こう")
AKA  = r("赤","あか")+"ちゃん"
NET  = r("寝","ね")+"て"
SOJ  = r("掃除","そう じ")
SEN  = r("先生","せん せい")
RUSU = r("留守","る す")
DEN  = r("電話","でん わ")
JI   = r("時","じ")
DAS  = r("出","だ")+"して"
KIN  = r("金曜日","きん よう び")
SHUK = r("宿題","しゅく だい")
KAER = r("帰","かえ")+"って"
MAT  = r("待","ま")+"って"

P = dict(
  no="73", tag=None,
  title_jp="〜あいだに／〜までに",
  title_ro='〜 aida ni / 〜 made ni &nbsp;|&nbsp; while 〜 / by 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 අතරතුර / 〜 වෙනකම්</span>',
  basic=(f"{AKA}が {NET} いる あいだに、{SOJ}を しました。",
         "Akachan ga nete iru aida ni, souji wo shimashita.",
         "While the baby was asleep, I cleaned.","බබා නිදාගෙන ඉන්න අතරතුර මම කාමරය අස් කළා."),
  use=(f'<b>あいだに</b>＝その {r("間","あいだ")}に 1{r("回","かい")} する こと。'
       f'<b>までに</b>＝その 時までに おわらせる こと（きげん）。'
       f'「まで」（ずっと）と「までに」（きげん）は ちがいます。',
       '<b>aida ni</b> = you do it once within that time. <b>made ni</b> = a deadline. '
       'Careful: <b>made</b> (continuously until) and <b>made ni</b> (by) are different.',
       '<b>aida ni</b> = ඒ කාලය ඇතුළත එක් වතාවක් කරනවා. <b>made ni</b> = නියමිත වෙලාව. '
       '<b>made</b> (දිගටම) සහ <b>made ni</b> (ඒ වෙනකම්) වෙනස්.'),
  pattern=[["BLANK",("あいだに、","aida ni",True),("〜します","~ shimasu")],
           ["BLANK",("までに、","made ni",True),("〜します","~ shimasu")],
           f"NOTE:3{JI}<b>まで</b> {MAT}います（3{JI}まで ずっと）　⇔　"
           f"3{JI}<b>までに</b> {KAER}ます（3{JI}が きげん）",
           f"NOTE:めいしには「の」：{NAT}{YASU}<b>の</b> あいだに　/　{KIN}<b>までに</b>"],
  examples=[
    (f"{AKA}が {NET} いる あいだに、{SOJ}を しました。","Akachan ga nete iru aida ni, souji wo shimashita.","While the baby was asleep, I cleaned.","බබා නිදාගෙන ඉන්න අතරතුර මම කාමරය අස් කළා."),
    (f"{NAT}{YASU}の あいだに、{RYO}を したいです。","Natsuyasumi no aida ni, ryokou wo shitai desu.","I want to travel during the summer holidays.","ගිම්හාන නිවාඩුවේ අතරතුර සංචාරයක් යන්න ඕන."),
    (f"{SEN}が {RUSU}の あいだに、{DEN}が ありました。","Sensei ga rusu no aida ni, denwa ga arimashita.","There was a call while the teacher was out.","ගුරුතුමා නැති අතරතුර කෝල් එකක් ආවා."),
    (f"{SHUK}は {KIN}までに {DAS} ください。","Shukudai wa kinyoubi made ni dashite kudasai.","Please hand in the homework by Friday.","ගෙදර වැඩ සිකුරාදා වෙනකම් දෙන්න."),
    (f"6{JI}までに {KAER}ます。","Rokuji made ni kaerimasu.","I'll be back by six.","6ට කලින් ගෙදර එනවා."),
    (f"3{JI}まで ここで {MAT}います。","Sanji made koko de matte imasu.","I'll wait here until three.","3 වෙනකම් මෙතන ඉන්නවා."),
    (f"バスが {r('来','く')}る までに、きっぷを {r('買','か')}いましょう。","Basu ga kuru made ni, kippu wo kaimashou.","Let's buy tickets before the bus comes.","බස් එක එනකම් ටිකට් ගමු."),
  ],
  foot="〜あいだに／〜までに",
)

if __name__ == "__main__":
    render(P, "u73_aidani")
