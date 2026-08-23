from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SUKO = r("少","すこ")+"し"
HAN  = r("話","はな")+"して"
KANJ = r("漢字","かん じ")
YOM  = r("読","よ")+"んで"
MAD  = r("窓","まど")
SHIM = r("閉","し")+"めて"
ICHI = r("一度","いち ど")
ITT  = r("言","い")+"って"
MAT  = r("待","ま")+"って"
ASHI = r("明日","あ した")
HAYA = r("早","はや")+"く"
KIT  = r("来","き")+"て"
TE   = r("手","て")
ARA  = r("洗","あら")+"って"

P71 = dict(
  no="106", tag=None,
  title_jp="〜して ください",
  title_ro='〜 shite kudasai &nbsp;|&nbsp; Please 〜 &nbsp;|&nbsp; '
           '<span class="si">කරුණාකරලා 〜 කරන්න</span>',
  basic=(f"もう {SUKO} ゆっくり {HAN} ください。","Mou sukoshi yukkuri hanashite kudasai.",
         "Please speak a little more slowly.","තව ටිකක් හෙමින් කතා කරන්න."),
  use=(f'あいてに して ほしい ことを たのむ、いちばん {r("基本","き ほん")}の かたちです。'
       f'105は ものを もらう とき、106は こうい（する こと）を たのむ ときです。',
       'This is the basic way to ask someone to do something. '
       '105 asks for a thing; 106 asks for an action.',
       'අනිත් කෙනාට යමක් කරන්න කියන මූලිකම ආකාරය. '
       '105 = දෙයක්; 106 = ක්‍රියාවක්.'),
  pattern=[["BLANK",("して ください","shite kudasai",True)],
           f"NOTE:ていねいど：{r('待','ま')}ちなさい（103）　&lt;　{MAT} ください（106）　&lt;　"
           f"{MAT} いただけませんか（107）",
           f"NOTE:109の はんたい：{SHIM} ください　⇔　{r('閉','し')}めないで ください"],
  examples=[
    (f"もう {SUKO} ゆっくり {HAN} ください。","Mou sukoshi yukkuri hanashite kudasai.","Please speak a little more slowly.","තව ටිකක් හෙමින් කතා කරන්න."),
    (f"この {KANJ}を {YOM} ください。","Kono kanji wo yonde kudasai.","Please read this kanji.","මේ කන්ජි අකුර කියවන්න."),
    (f"{MAD}を {SHIM} ください。","Mado wo shimete kudasai.","Please close the window.","ජනේලය වහන්න."),
    (f"すみません、もう {ICHI} {ITT} ください。","Sumimasen, mou ichido itte kudasai.","Excuse me, please say it once more.","සමාවෙන්න, තව එක පාරක් කියන්න."),
    (f"ここで {MAT} ください。","Koko de matte kudasai.","Please wait here.","මෙතන ඉන්න."),
    (f"{ASHI} {HAYA} {KIT} ください。","Ashita hayaku kite kudasai.","Please come early tomorrow.","හෙට ඉක්මනට එන්න."),
    (f"{TE}を {ARA} ください。","Te wo aratte kudasai.","Please wash your hands.","අත් හෝදන්න."),
  ],
  foot="〜して ください",
)

if __name__ == "__main__":
    render(P71, "p106_shitekudasai")
