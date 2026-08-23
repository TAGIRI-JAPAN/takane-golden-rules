from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MOT  = r("持","も")+"ち"
SHIM = "します"
TETS = r("手伝","て つだ")+"い"
OKU  = r("送","おく")+"り"
MAIR = r("参","まい")+"ります"
ORI  = "おります"
ITAD = "いただきます"
MOSH = r("申","もう")+"します"
ITAS = "いたします"
HAIK = r("拝見","はい けん")
SEN  = r("先生","せん せい")
KEN  = r("謙譲語","けん じょう ご")
JIB  = r("自分","じ ぶん")
NAM  = r("名前","な まえ")
SHIR = r("知","し")+"り"
ZONJ = r("存","ぞん")+"じます"

P = dict(
  no="123", tag=None,
  title_jp="謙譲語（お〜します）",
  title_ro='kenjougo &nbsp;|&nbsp; humble — lowering yourself &nbsp;|&nbsp; '
           '<span class="si">නිහතමානී බස</span>',
  basic=(f"お{MOT} {SHIM}。","Omochi shimasu.",
         "Let me carry that for you.","මම අරන් යන්නම්."),
  use=(f'{KEN}は <b>{JIB}の {r("動作","どう さ")}</b>を ひくくして、'
       f'あいてを {r("高","たか")}める ことばです。122の {r("反対","はん たい")}です。'
       f'アルバイトの めんせつや しごとで いちばん つかう ことばです。',
       'Humble language lowers <b>your own actions</b> so the other person is raised. '
       'It is the mirror of 122 — and the language you will use most in a job interview.',
       'නිහතමානී බස කියන්නේ <b>තමන්ගේ ක්‍රියාව</b> පහත් කරලා අනිත් කෙනා උසස් කරන එක. '
       '122 ට විරුද්ධයි — රැකියා සම්මුඛ පරීක්ෂණයේ වැඩිපුරම යොදන බස.'),
  pattern=[[("お","o",True),("ますけい","masu stem"),(f"{SHIM}","shimasu",True)],
           f"NOTE:お＋ますけい＋します：お{MOT} します　/　お{TETS} します　/　お{OKU} します",
           f"NOTE:とくべつな 形：{r('行','い')}く・{r('来','く')}る → {MAIR}　/　いる → {ORI}　/　"
           f"{r('食','た')}べる・もらう → {ITAD}　/　{r('言','い')}う → {MOSH}　/　"
           f"する → {ITAS}　/　{r('見','み')}る → {HAIK}します　/　{SHIR}ません → {ZONJ}",
           f"NOTE:122（あいての {r('動作','どう さ')}）　⇔　123（{JIB}の {r('動作','どう さ')}）— "
           f"ここを {r('間違','ま ちが')}えると ぎゃくの {r('意味','い み')}に なります"],
  examples=[
    (f"お{MOT} {SHIM}。","Omochi shimasu.","Let me carry that for you.","මම අරන් යන්නම්."),
    (f"サマンと {MOSH}。","Saman to moushimasu.","My name is Saman.","මගේ නම සමන්."),
    (f"あした 10{r('時','じ')}に {MAIR}。","Ashita juuji ni mairimasu.","I will come at ten tomorrow.","හෙට 10ට එන්නම්."),
    (f"{r('資料','し りょう')}を {HAIK}しました。","Shiryou wo haiken shimashita.","I have looked at the documents.","ලියකියවිලි බැලුවා."),
    (f"{SEN}に {r('辞書','じ しょ')}を {ITAD}。","Sensei ni jisho wo itadakimashita.","I received a dictionary from my teacher.","ගුරුතුමාගෙන් ශබ්දකෝෂයක් ලැබුණා."),
    (f"わたしが ご{r('案内','あん ない')} {ITAS}。","Watashi ga goannai itashimasu.","I will show you the way.","මම පාර පෙන්නන්නම්."),
    (f"すみません、{ZONJ}ませんでした。","Sumimasen, zonjimasen deshita.","I'm sorry, I didn't know.","සමාවෙන්න, දැනගෙන හිටියේ නැහැ."),
  ],
  foot="謙譲語（お〜します）",
)

if __name__ == "__main__":
    render(P, "u123_kenjou")
