from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASA  = r("朝","あさ")
OKI  = r("起","お")+"きて"
KAO  = r("顔","かお")
ARA  = r("洗","あら")+"って"
GAK  = r("学校","がっ こう")
IKI  = r("行","い")+"きます"
TAK  = r("高","たか")+"くて"
KAB  = "かばん"
SHIN = r("親切","しん せつ")
ATAM = r("頭","あたま")
YOM  = r("読","よ")+"んで"
BAS  = "バス"
OKUR = r("遅","おく")+"れて"
CHIK = r("遅刻","ち こく")
GENI = r("原因","げん いん")
JUN  = r("順番","じゅん ばん")
HON_ = r("本","ほん")

P = dict(
  no="75", tag=None,
  title_jp="〜て、〜（文を つなぐ）",
  title_ro='〜 te, 〜 &nbsp;|&nbsp; and then / and so &nbsp;|&nbsp; '
           '<span class="si">〜 කරලා, 〜</span>',
  basic=(f"{ASA} {OKI}、{KAO}を {ARA}、{GAK}へ {IKI}。",
         "Asa okite, kao wo aratte, gakkou e ikimasu.",
         "I get up, wash my face and go to school.","උදේ නැගිටලා, මූණ හෝදලා, පාසලට යනවා."),
  use=(f'て{r("形","けい")}で 文を つなぐと、みじかい 文を いくつも ならべずに すみます。'
       f'{r("意味","い み")}は ①{JUN}（そして）②{GENI}（だから）の 2つです。',
       'Joining sentences with the te-form saves you from a string of short sentences. '
       'It carries two meanings: (1) sequence, (2) cause.',
       'te-ආකාරයෙන් වාක්‍ය සම්බන්ධ කරද්දී කෙටි වාක්‍ය ගොඩක් අවශ්‍ය නැහැ. '
       'අර්ථ දෙකයි: (1) පිළිවෙළ, (2) හේතුව.'),
  pattern=[["BLANK",("て、","te",True),"BLANK",("ます","masu")],
           f"NOTE:①{JUN}：{OKI}、{ARA}、{IKI}　②{GENI}：{BAS}が {OKUR}、{CHIK}しました",
           f"NOTE:けいようし：い→<b>くて</b>（{TAK} {r('大','おお')}きい）　/　"
           f"な・めいし→<b>で</b>（{SHIN}で いい {r('人','ひと')}）"],
  examples=[
    (f"{ASA} {OKI}、{KAO}を {ARA}、{GAK}へ {IKI}。","Asa okite, kao wo aratte, gakkou e ikimasu.","I get up, wash my face and go to school.","උදේ නැගිටලා, මූණ හෝදලා, පාසලට යනවා."),
    (f"この {KAB}は {TAK} {r('重','おも')}いです。","Kono kaban wa takakute omoi desu.","This bag is expensive and heavy.","මේ බෑග් එක ගණන් සහ බරයි."),
    (f"サマンさんは {SHIN}で、おもしろい {r('人','ひと')}です。","Saman-san wa shinsetsu de, omoshiroi hito desu.","Saman is kind and interesting.","සමන් කරුණාවන්තයි, විනෝදජනකයි."),
    (f"{BAS}が {OKUR}、{CHIK}しました。","Basu ga okurete, chikoku shimashita.","The bus was late, so I was late.","බස් එක ප්‍රමාද වෙලා, මම පරක්කු වුණා."),
    (f"{HON_}を {YOM}、ねました。","Hon wo yonde, nemashita.","I read a book and went to sleep.","පොතක් කියවලා, නිදාගත්තා."),
    (f"{ATAM}が いたくて、{r('休','やす')}みました。","Atama ga itakute, yasumimashita.","I had a headache, so I took a rest.","ඔලුව රිදිලා, විවේක ගත්තා."),
    (f"カレーを {r('作','つく')}って、{r('友','とも')}だちと {r('食','た')}べました。","Karee wo tsukutte, tomodachi to tabemashita.","I made curry and ate it with a friend.","කරි උයලා, යාළුවා එක්ක කෑවා."),
  ],
  foot="〜て、〜（文を つなぐ）",
)

if __name__ == "__main__":
    render(P, "u75_tekei")
