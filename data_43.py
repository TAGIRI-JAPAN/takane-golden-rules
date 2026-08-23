from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
HOS  = "ほしいです"
JIT  = r("自転車","じ てん しゃ")
OOK  = r("大","おお")+"きい"
NHG  = r("日本語","に ほん ご")
JISH = r("辞書","じ しょ")
SHIZ = r("静","しず")+"かな"
HEYA = r("部屋","へ や")
TSUM = r("冷","つめ")+"たい"
MIZU = r("水","みず")
SUKO = r("少","すこ")+"し"
JIK  = r("時間","じ かん")
NAN  = r("何","なに")
IMA  = r("今","いま")
TOMO = r("友","とも")+"だち"

P35 = dict(
  no="43", tag=None,
  title_jp=f"〜が {HOS}",
  title_ro='〜 ga hoshii desu &nbsp;|&nbsp; I want 〜 &nbsp;|&nbsp; '
           '<span class="si">මට 〜 ඕනෙ</span>',
  basic=(f"{W}は {JIT}が {HOS}。","Watashi wa jitensha ga hoshii desu.",
         "I want a bicycle.","මට බයිසිකලයක් ඕනෙ."),
  use=(f'{r("自分","じ ぶん")}が {r("手","て")}に {r("入","い")}れたい ものを{r("言","い")}う ことばです。'
       f'42と{r("同","おな")}じで、まえは かならず「〜が」です。ほしいは い けいようしです。',
       'Use it for a thing you want to get. As in 42, the word before it always takes <b>ga</b>. '
       '<b>hoshii</b> is an i-adjective.',
       'ලබාගන්න ඕන දෙයක් කියන්න. 42 වගේම කලින් වචනයට හැමවිටම <b>ga</b>. '
       '<b>hoshii</b> කියන්නේ i-විශේෂණ පදයක්.'),
  pattern=[[("〜は","~ wa"),"BLANK",("が","ga",True),(HOS,"hoshii desu",True)],
           f"NOTE:い けいようし：{HOS}　/　ほしくないです　/　ほしかったです",
           f"NOTE:シンハラ{r('語','ご')}の「මට 〜 ඕනෙ」と {r('同','おな')}じ かたちです",
           f"NOTE:{r('他','ほか')}の {r('人','ひと')}のことは「サマンさんは 〜を ほしがって います」と {r('言','い')}います"],
  examples=[
    (f"{W}は {JIT}が {HOS}。","Watashi wa jitensha ga hoshii desu.","I want a bicycle.","මට බයිසිකලයක් ඕනෙ."),
    (f"{W}は {OOK} かばんが {HOS}。","Watashi wa ookii kaban ga hoshii desu.","I want a big bag.","මට ලොකු බෑග් එකක් ඕනෙ."),
    (f"{W}は {NHG}の {JISH}が {HOS}。","Watashi wa nihongo no jisho ga hoshii desu.","I want a Japanese dictionary.","මට ජපන් ශබ්දකෝෂයක් ඕනෙ."),
    (f"{W}は {SHIZ} {HEYA}が {HOS}。","Watashi wa shizukana heya ga hoshii desu.","I want a quiet room.","මට නිස්කලංක කාමරයක් ඕනෙ."),
    (f"{W}は {TSUM} {MIZU}が {HOS}。","Watashi wa tsumetai mizu ga hoshii desu.","I want some cold water.","මට සීතල වතුර ඕනෙ."),
    (f"{W}は もう {SUKO} {JIK}が {HOS}。","Watashi wa mou sukoshi jikan ga hoshii desu.","I want a little more time.","මට තව ටිකක් වෙලාව ඕනෙ."),
    (f"{IMA}、{NAN}が {HOS}か。","Ima, nani ga hoshii desu ka.","What do you want now?","දැන් ඔයාට මොකද ඕනෙ?"),
  ],
  foot="〜が ほしいです",
)

if __name__ == "__main__":
    render(P35, "p43_gahoshii")
