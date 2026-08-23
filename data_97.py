from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SHUM = r("趣味","しゅ み")
HON  = r("本","ほん")
YOM  = r("読","よ")+"む"
KOTO = "こと"
UTA  = r("歌","うた")+"う"
SUKI = r("好","す")+"き"
TSUK = r("使","つか")+"い"
KATA = r("方","かた")
OSHI = r("教","おし")+"えて"
YOMK = r("読","よ")+"み"
TAKA = r("高","たか")+"さ"
NAGA = r("長","なが")+"さ"
OOK  = r("大","おお")+"きさ"
NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"す"
MUZU = "むずかしいです"
WASU = r("忘","わす")+"れました"
DAS  = r("出","だ")+"す"
MEIS = r("名詞","めい し")

P = dict(
  no="97", tag=None,
  title_jp="名詞に する（〜こと・〜の・〜方・〜さ）",
  title_ro='making nouns &nbsp;|&nbsp; koto / no / kata / sa &nbsp;|&nbsp; '
           '<span class="si">නාම පද හදන හැටි</span>',
  basic=(f"{SHUM}は {HON}を {YOM} {KOTO}です。","Shumi wa hon wo yomu koto desu.",
         "My hobby is reading books.","මගේ විනෝදාංශය පොත් කියවීම."),
  use=(f'どうしや けいようしを <b>{MEIS}</b>に かえると、'
       f'「〜は …です」（06）や「〜が {SUKI}です」（42）の 中に 入れられます。'
       f'これで {r("言","い")}える ことが 一気に ふえます。',
       'Turning a verb or adjective into a <b>noun</b> lets you drop it into patterns like '
       '06 and 42. This suddenly widens what you can say.',
       'ක්‍රියාවක් හෝ විශේෂණයක් <b>නාම පදයක්</b> කළාම, 06 සහ 42 වගේ රටාවලට දාන්න පුළුවන්. '
       'ඒකෙන් කියන්න පුළුවන් දේ එකපාරටම වැඩි වෙනවා.'),
  pattern=[[("じしょけい","dict. form"),"BLANK",("こと／の","koto / no",True)],
           [("ますけい","masu stem"),"BLANK",(f"{KATA}（〜し方）","kata",True)],
           f"NOTE:こと＝かたい・{r('書','か')}きことば　/　の＝かいわ。"
           f"「{HON}を {YOM} <b>の</b>が {SUKI}です」も {r('同','おな')}じ {r('意味','い み')}です",
           f"NOTE:い けいようし ＋ さ：{r('高','たか')}い → {TAKA}　/　"
           f"{r('長','なが')}い → {NAGA}　/　{r('大','おお')}きい → {OOK}"],
  examples=[
    (f"{SHUM}は {HON}を {YOM} {KOTO}です。","Shumi wa hon wo yomu koto desu.","My hobby is reading books.","මගේ විනෝදාංශය පොත් කියවීම."),
    (f"{UTA}のが {SUKI}です。","Utau no ga suki desu.","I like singing.","මම සිංදු කියන්න කැමතියි."),
    (f"{NHG}を {HAN} {KOTO}は {MUZU}。","Nihongo wo hanasu koto wa muzukashii desu.","Speaking Japanese is difficult.","ජපන් භාෂාව කතා කරන එක අමාරුයි."),
    (f"この きかいの {TSUK}{KATA}を {OSHI} ください。","Kono kikai no tsukaikata wo oshiete kudasai.","Please show me how to use this machine.","මේ යන්ත්‍රය පාවිච්චි කරන හැටි කියලා දෙන්න."),
    (f"この {r('漢字','かん じ')}の {YOMK}{KATA}が わかりません。","Kono kanji no yomikata ga wakarimasen.","I don't know how to read this kanji.","මේ කන්ජි කියවන හැටි දන්නේ නැහැ."),
    (f"レポートを {DAS} {KOTO}を {WASU}。","Repooto wo dasu koto wo wasuremashita.","I forgot to hand in the report.","වාර්තාව දෙන එක අමතක වුණා."),
    (f"この かばんの {OOK}が ちょうど いいです。","Kono kaban no ookisa ga choudo ii desu.","The size of this bag is just right.","මේ බෑග් එකේ ප්‍රමාණය හරියටම හොඳයි."),
  ],
  foot="名詞に する（〜こと・〜の・〜方・〜さ）",
)

if __name__ == "__main__":
    render(P, "u97_meishika")
