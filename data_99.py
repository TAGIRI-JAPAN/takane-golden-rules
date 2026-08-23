from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KANE = r("金","かね")
ARI  = "ありません"
HYAK = r("百円","ひゃく えん")
JIK  = r("時間","じ かん")
FUN  = r("分","ふん")
NHG  = r("日本語","に ほん ご")
SUKO = r("少","すこ")+"し"
HAN  = r("話","はな")+"せません"
KYO  = r("教室","きょう しつ")
HITO = r("人","ひと")
IMAS = "いません"
NON  = r("飲","の")+"みません"
MIZU = r("水","みず")
TAB  = r("食","た")+"べません"
KAI  = r("回","かい")
ITT  = r("行","い")+"った ことが"
HITEI= r("否定","ひ てい")
NIH_ = r("日本","に ほん")
TABD = r("食","た")+"べませんでした"

P = dict(
  no="99", tag=None,
  title_jp="〜しか ありません",
  title_ro='〜 shika arimasen &nbsp;|&nbsp; only 〜 (and that\'s not much) &nbsp;|&nbsp; '
           '<span class="si">〜 විතරයි</span>',
  basic=(f"{HYAK}しか {ARI}。","Hyakuen shika arimasen.",
         "I only have a hundred yen.","මට යෙන් 100ක් විතරයි තියෙන්නේ."),
  use=(f'「〜だけ」と {r("同","おな")}じ「only」ですが、'
       f'「しか」は かならず <b>{HITEI}</b>と いっしょに つかい、'
       f'「それだけ しか ない＝すくない」と いう <b>ざんねんな {r("気持","き も")}ち</b>が {r("入","はい")}ります。',
       'Like <b>dake</b> it means "only", but <b>shika</b> must be paired with a '
       '<b>negative</b>, and it adds the feeling that this is <b>not enough</b>.',
       '<b>dake</b> වගේම "විතරයි"; හැබැයි <b>shika</b> හැමවිටම <b>නෙගටිව්</b> එකක් එක්ක, '
       'සහ "මේ ටික විතරයි, මදි" කියන හැඟීම එනවා.'),
  pattern=[["BLANK",("しか","shika",True),("ありません／〜ません","arimasen",True)],
           f"NOTE:だけ（ただの only）　⇔　しか 〜ない（すくない、たりない、と いう {r('気持','き も')}ち）",
           f"NOTE:「を」「が」は きえます：{MIZU}<b>を</b> しか ×　→　{MIZU}しか {NON} ○"],
  examples=[
    (f"{HYAK}しか {ARI}。","Hyakuen shika arimasen.","I only have a hundred yen.","මට යෙන් 100ක් විතරයි තියෙන්නේ."),
    (f"{JIK}が 10{FUN}しか {ARI}。","Jikan ga jippun shika arimasen.","We only have ten minutes.","විනාඩි 10ක් විතරයි තියෙන්නේ."),
    (f"{NHG}は {SUKO}しか {HAN}。","Nihongo wa sukoshi shika hanasemasen.","I can only speak a little Japanese.","මට ජපන් භාෂාව ටිකක් විතරයි කතා කරන්න පුළුවන්."),
    (f"{KYO}に 3{r('人','にん')}しか {IMAS}。","Kyoushitsu ni sannin shika imasen.","There are only three people in the classroom.","පන්ති කාමරයේ තුන්දෙනෙක් විතරයි ඉන්නේ."),
    (f"{r('私','わたし')}は {MIZU}しか {NON}。","Watashi wa mizu shika nomimasen.","I only drink water.","මම වතුර විතරයි බොන්නේ."),
    (f"{NIH_}へ 1{KAI}しか {ITT} {ARI}。","Nihon e ikkai shika itta koto ga arimasen.","I've only been to Japan once.","ජපානෙට එක වතාවක් විතරයි ගිහින් තියෙන්නේ."),
    (f"きょうは カレーしか {TABD}。","Kyou wa karee shika tabemasen deshita.","Today I only ate curry.","අද කරි විතරයි කෑවේ."),
  ],
  foot="〜しか ありません",
)

if __name__ == "__main__":
    render(P, "u99_shika")
