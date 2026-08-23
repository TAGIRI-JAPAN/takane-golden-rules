from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KANJ = r("漢字","かん じ")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
SEN  = r("先生","せん せい")
SHIN = r("親切","しん せつ")
KURU = r("来","く")+"る"
KONA = r("来","こ")+"ない"
KAET = r("帰","かえ")+"った"
OMO  = r("思","おも")+"います"
W    = r("私","わたし")
TAIH = r("大変","たい へん")

P28 = dict(
  no="39", tag=None,
  title_jp=f"〜と {OMO}",
  title_ro='〜 to omoimasu &nbsp;|&nbsp; I think 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කියලා හිතනවා</span>',
  basic=(f"この {KANJ}は むずかしいと {OMO}。","Kono kanji wa muzukashii to omoimasu.",
         "I think this kanji is difficult.","මම හිතන්නේ මේ කන්ජි අකුර අමාරුයි කියලා."),
  use=(f'{r("自分","じ ぶん")}の かんがえや よそうを{r("言","い")}う ことばです。'
       f'「と」の{r("前","まえ")}は ふつうけい（じしょけい・ない・た）で、「です」「ます」は つかいません。',
       'Use it to say what you think or expect. Before <b>to</b>, use the plain form '
       '(dictionary / <b>nai</b> / <b>ta</b>) — never <b>desu</b> or <b>masu</b>.',
       'තමන් හිතන දේ හෝ අනුමානය කියන්න. <b>to</b> එකට කලින් සරල ආකාරය '
       '(ශබ්දකෝෂ / <b>nai</b> / <b>ta</b>) දාන්න — <b>desu</b> හෝ <b>masu</b> කවදාවත් නෙවෙයි.'),
  pattern=[["BLANK",("と","to",True),(OMO,"omoimasu",True)],
           f"NOTE:「と」の 前：むずかしい　/　{SHIN}だ　/　{KURU}　/　{KONA}　/　{KAET}",
           f"NOTE:な けいようし・めいしには「だ」を つけます（{SHIN}だ　/　{r('学生','がく せい')}だ）"],
  examples=[
    (f"この {KANJ}は むずかしいと {OMO}。","Kono kanji wa muzukashii to omoimasu.","I think this kanji is difficult.","මම හිතන්නේ මේ කන්ජි අකුර අමාරුයි කියලා."),
    (f"{NHG}の {BEN}は たのしいと {OMO}。","Nihongo no benkyou wa tanoshii to omoimasu.","I think studying Japanese is fun.","මම හිතන්නේ ජපන් භාෂාව ඉගෙන ගන්න එක විනෝදජනකයි කියලා."),
    (f"あの {SEN}は {SHIN}だと {OMO}。","Ano sensei wa shinsetsu da to omoimasu.","I think that teacher is kind.","මම හිතන්නේ අර ගුරුතුමා කරුණාවන්තයි කියලා."),
    (f"サマンさんは {KURU}と {OMO}。","Saman-san wa kuru to omoimasu.","I think Saman will come.","මම හිතන්නේ සමන් එයි කියලා."),
    (f"あした {SEN}は {KONA}と {OMO}。","Ashita sensei wa konai to omoimasu.","I don't think the teacher will come tomorrow.","මම හිතන්නේ හෙට ගුරුතුමා එන්නේ නැහැ කියලා."),
    (f"{SEN}は もう {KAET}と {OMO}。","Sensei wa mou kaetta to omoimasu.","I think the teacher has already gone home.","මම හිතන්නේ ගුරුතුමා දැනටමත් ගෙදර ගිහින් කියලා."),
    (f"{W}も そう {OMO}。","Watashi mo sou omoimasu.","I think so too.","මමත් එහෙම හිතනවා."),
  ],
  foot="〜と 思います",
)

if __name__ == "__main__":
    render(P28, "p39_toomoimasu")
