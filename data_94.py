from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MAD  = r("窓","まど")
AKE  = r("開","あ")+"けて"
ARI  = "あります"
KAB  = r("壁","かべ")
CHIZ = r("地図","ち ず")
HAT  = r("貼","は")+"って"
KUR  = r("車","くるま")
TOM  = r("止","と")+"めて"
NAM  = r("名前","な まえ")
KAI  = r("書","か")+"いて"
REI  = r("冷蔵庫","れい ぞう こ")
NOM  = r("飲","の")+"み"+r("物","もの")
IRE  = r("入","い")+"れて"
DEN  = r("電気","でん き")
TSUKE= "つけて"
TADO = r("他動詞","た どう し")
JOUT = r("状態","じょう たい")
JUNB = r("準備","じゅん び")

P = dict(
  no="94", tag=None,
  title_jp="〜て あります",
  title_ro='〜 te arimasu &nbsp;|&nbsp; it has been done (and stays that way) &nbsp;|&nbsp; '
           '<span class="si">කරලා තියෙනවා</span>',
  basic=(f"{MAD}が {AKE} {ARI}。","Mado ga akete arimasu.",
         "The window has been left open.","ජනේලය අරලා තියෙනවා."),
  use=(f'<b>だれかが して、その {JOUT}が のこって いる</b>と いう {r("意味","い み")}です。'
       f'かならず <b>{TADO}</b>（92）と つかいます。'
       f'93「〜て おきます」は {r("動作","どう さ")}、94「〜て あります」は その あとの {JOUT}です。',
       'It means someone did it and <b>the result is still there</b>. It always uses a '
       '<b>transitive</b> verb (92). Unit 93 is the action; 94 is the state left behind.',
       'කවුරු හරි කරලා <b>ඒ තත්ත්වය තාම තියෙනවා</b>. හැමවිටම <b>සකර්මක</b> ක්‍රියාවක් (92). '
       '93 = ක්‍රියාව; 94 = ඉතිරි වුණ තත්ත්වය.'),
  pattern=[[("〜が","~ ga"),"BLANK",("て あります","te arimasu",True)],
           f"NOTE:{TADO}（92）＋て あります。{r('自動詞','じ どう し')}は「〜て います」（16）：",
           f"NOTE:{MAD}が {AKE} あります（だれかが {r('開','あ')}けた）　⇔　"
           f"{MAD}が {r('開','あ')}いて います（ただ {r('開','あ')}いて いる）"],
  examples=[
    (f"{MAD}が {AKE} {ARI}。","Mado ga akete arimasu.","The window has been left open.","ජනේලය අරලා තියෙනවා."),
    (f"{KAB}に {CHIZ}が {HAT} {ARI}。","Kabe ni chizu ga hatte arimasu.","A map has been put up on the wall.","බිත්තියේ සිතියමක් අලවලා තියෙනවා."),
    (f"ここに {NAM}が {KAI} {ARI}。","Koko ni namae ga kaite arimasu.","A name is written here.","මෙතන නමක් ලියලා තියෙනවා."),
    (f"{REI}に {NOM}が {IRE} {ARI}。","Reizouko ni nomimono ga irete arimasu.","Drinks have been put in the fridge.","ශීතකරණයේ බීම දාලා තියෙනවා."),
    (f"{KUR}が ここに {TOM} {ARI}。","Kuruma ga koko ni tomete arimasu.","A car has been parked here.","කාරයක් මෙතන නවත්තලා තියෙනවා."),
    (f"{DEN}が {TSUKE} {ARI}。","Denki ga tsukete arimasu.","The light has been left on.","ලයිට් එක දාලා තියෙනවා."),
    (f"きっぷは もう {r('買','か')}って {ARI}。","Kippu wa mou katte arimasu.","The tickets have already been bought.","ටිකට් දැනටමත් අරගෙන තියෙනවා."),
  ],
  foot="〜て あります",
)

if __name__ == "__main__":
    render(P, "u94_tearu")
