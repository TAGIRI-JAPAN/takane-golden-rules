from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SAM  = r("寒","さむ")+"く"
NAR  = "なりました"
NHG  = r("日本語","に ほん ご")
JOZ  = r("上手","じょう ず")
W    = r("私","わたし")
SEN  = r("先生","せん せい")
HEYA = r("部屋","へ や")
SAI  = r("歳","さい")
KO   = r("子","こ")
OOK  = r("大","おお")+"きく"
DEN  = r("電車","でん しゃ")
TAKA = r("高","たか")+"く"
HAYA = r("早","はや")+"く"
OKI  = r("起","お")+"きます"
SHIZ = r("静","しず")+"かに"

P47 = dict(
  no="53", tag=None,
  title_jp="〜く なります／〜に なります",
  title_ro='〜 ku narimasu / 〜 ni narimasu &nbsp;|&nbsp; becomes 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වෙනවා</span>',
  basic=(f"{SAM} {NAR}。","Samuku narimashita.",
         "It has got cold.","සීතල වෙලා."),
  use=(f'ようすが かわる ことを {r("言","い")}います。い けいようしは 「い」を「く」に、'
       f'な けいようしと めいしには 「に」を つけます。',
       'Use it when something changes. i-adjectives change their <b>i</b> to <b>ku</b>; '
       'na-adjectives and nouns take <b>ni</b>.',
       'තත්ත්වයක් වෙනස් වෙනවා කියද්දී. i-විශේෂණවල <b>i</b> එක <b>ku</b> වෙනවා; '
       'na-විශේෂණ සහ නාම පදවලට <b>ni</b> දානවා.'),
  pattern=[[("い けいようし","i-adj"),"BLANK",("く なります","ku narimasu",True)],
           [("な けいようし・めいし","na-adj / noun"),"BLANK",("に なります","ni narimasu",True)],
           f"NOTE:{TAKA}い → {TAKA} なる　/　{SHIZ}な → {SHIZ} なる　/　{SEN} → {SEN}に なる　"
           f"/　とくべつ：いい → よく なります",
           f"NOTE:この かたちは ふくしにも なります：{HAYA} {OKI}　/　{SHIZ} して ください"],
  examples=[
    (f"{SAM} {NAR}。","Samuku narimashita.","It has got cold.","සීතල වෙලා."),
    (f"{NHG}が {JOZ}に {NAR}。","Nihongo ga jouzu ni narimashita.","My Japanese has got better.","මගේ ජපන් භාෂාව හොඳ වෙලා."),
    (f"{W}は {SEN}に なりたいです。","Watashi wa sensei ni naritai desu.","I want to become a teacher.","මට ගුරුවරයෙක් වෙන්න ඕනේ."),
    (f"{HEYA}が きれいに {NAR}。","Heya ga kirei ni narimashita.","The room has got clean.","කාමරය පිරිසිදු වෙලා."),
    (f"もうすぐ 21{SAI}に なります。","Mousugu hatachi ni narimasu.","I will turn twenty soon.","මට ඉක්මනට අවුරුදු 21 වෙනවා."),
    (f"{KO}どもが {OOK} {NAR}。","Kodomo ga ookiku narimashita.","The children have grown up.","දරුවෝ ලොකු වෙලා."),
    (f"{DEN}が {TAKA} {NAR}。","Densha ga takaku narimashita.","Train fares have got expensive.","දුම්රිය ගාස්තු ගණන් වෙලා."),
  ],
  foot="〜く なります／〜に なります",
)

if __name__ == "__main__":
    render(P47, "u53_narimasu")
