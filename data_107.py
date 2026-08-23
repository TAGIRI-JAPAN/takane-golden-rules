from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SUKO = r("少","すこ")+"し"
MAT  = r("待","ま")+"って"
KANJ = r("漢字","かん じ")
YOMK = r("読","よ")+"み"+r("方","かた")
OSHI = r("教","おし")+"えて"
ICHI = r("一度","いち ど")
SETS = r("説明","せつ めい")
SHOR = r("書類","しょ るい")
KAKU = r("確認","かく にん")
ASHI = r("明日","あ した")
HAYA = r("早","はや")+"く"
KIT  = r("来","き")+"て"
SAIN = "サイン"
HAN  = r("話","はな")+"して"
UE   = r("上","うえ")
HITO = r("人","ひと")
KYA  = r("客","きゃく")

P72 = dict(
  no="107", tag=None,
  title_jp="〜して いただけませんか？",
  title_ro='〜 shite itadakemasen ka &nbsp;|&nbsp; Could you please 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කරන්න පුළුවන්ද?</span>',
  basic=(f"すみません、{SUKO} {MAT} いただけませんか。","Sumimasen, sukoshi matte itadakemasen ka.",
         "Excuse me, could you please wait a moment?","සමාවෙන්න, ටිකක් ඉන්න පුළුවන්ද?"),
  use=(f'106より ずっと ていねいな たのみ{r("方","かた")}です。{UE}の {HITO}・お{KYA}さま・'
       f'しごとの メールで つかいます。ぎもんの かたちに する ことで やわらかく なります。',
       'A much politer way to ask than 106. Use it with seniors, customers and in work '
       'emails. Making it a question softens the request.',
       '106ට වඩා ගොඩක් ආචාරශීලීයි. ලොකු අය, ගනුදෙනුකරුවන්, රැකියා ඊමේල් වලට. '
       'ප්‍රශ්නයක් විදිහට කියද්දී මෘදු වෙනවා.'),
  pattern=[["BLANK",("して いただけませんか？","shite itadakemasen ka",True)],
           f"NOTE:ていねいど：しなさい（103）　&lt;　して ください（106）　&lt;　"
           f"して いただけませんか（107）",
           f"NOTE:かるく：「〜して もらえませんか」　/　もっと ていねい：「〜して いただけますでしょうか」"],
  examples=[
    (f"すみません、{SUKO} {MAT} いただけませんか。","Sumimasen, sukoshi matte itadakemasen ka.","Excuse me, could you please wait a moment?","සමාවෙන්න, ටිකක් ඉන්න පුළුවන්ද?"),
    (f"{KANJ}の {YOMK}を {OSHI} いただけませんか。","Kanji no yomikata wo oshiete itadakemasen ka.","Could you tell me how to read this kanji?","මේ කන්ජි අකුර කියවන හැටි කියලා දෙන්න පුළුවන්ද?"),
    (f"もう {ICHI} {SETS}して いただけませんか。","Mou ichido setsumei shite itadakemasen ka.","Could you explain it once more?","තව එක පාරක් පැහැදිලි කරන්න පුළුවන්ද?"),
    (f"この {SHOR}を {KAKU}して いただけませんか。","Kono shorui wo kakunin shite itadakemasen ka.","Could you check this document?","මේ ලියවිල්ල බලන්න පුළුවන්ද?"),
    (f"{ASHI} {HAYA} {KIT} いただけませんか。","Ashita hayaku kite itadakemasen ka.","Could you come early tomorrow?","හෙට ඉක්මනට එන්න පුළුවන්ද?"),
    (f"ここに {SAIN}して いただけませんか。","Koko ni sain shite itadakemasen ka.","Could you sign here?","මෙතන අත්සන් කරන්න පුළුවන්ද?"),
    (f"もう {SUKO} ゆっくり {HAN} いただけませんか。","Mou sukoshi yukkuri hanashite itadakemasen ka.","Could you speak a little more slowly?","තව ටිකක් හෙමින් කතා කරන්න පුළුවන්ද?"),
  ],
  foot="〜して いただけませんか？",
)

if __name__ == "__main__":
    render(P72, "p107_itadakemasenka")
