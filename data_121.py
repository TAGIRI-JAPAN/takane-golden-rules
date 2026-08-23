from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KYO  = r("今日","きょう")
SAM  = r("寒","さむ")+"いです"
HON  = r("本","ほん")
SHIN = r("親切","しん せつ")
NHG  = r("日本語","に ほん ご")
BEN  = r("勉強","べん きょう")
KINO = r("昨日","きのう")
MUZU = "むずかしかったです"
KANT = r("簡単","かん たん")
DEK  = "できません"
NIM  = r("荷物","に もつ")
HITO = r("一人","ひと り")
MOT  = r("持","も")+"てません"
ZEN  = r("全然","ぜん ぜん")

P61 = dict(
  no="121", tag=None,
  title_jp="とても 〜",
  title_ro='totemo 〜 &nbsp;|&nbsp; very 〜 / (with neg.) simply cannot &nbsp;|&nbsp; '
           '<span class="si">ගොඩක් 〜</span>',
  basic=(f"{KYO}は とても {SAM}。","Kyou wa totemo samui desu.",
         "It is very cold today.","අද ගොඩක් සීතලයි."),
  use=(f'ふつうは「very」の {r("意味","い み")}ですが、ひていと いっしょに つかうと '
       f'「どうしても できない」と いう {r("強","つよ")}い {r("意味","い み")}に なります。',
       'Normally it means "very". But together with a negative it means '
       '"simply cannot, no matter what".',
       'සාමාන්‍යයෙන් "ගොඩක්" කියන අර්ථය. හැබැයි නෙගටිව් එකක් එක්ක ආවොත් '
       '"කොහොම වුණත් බැහැ" කියන ශක්තිමත් අර්ථය.'),
  pattern=[[("とても","totemo",True),"BLANK"],
           [("とても","totemo",True),"BLANK",("ない","nai",True)],
           f"NOTE:あまり 〜ない（117・{r('少','すく')}ない）　/　まったく 〜ない（120・0％）　/　"
           f"とても 〜ない（121・できない）",
           f"NOTE:かいわでは「とっても」と {r('言','い')}う ことも あります"],
  examples=[
    (f"{KYO}は とても {SAM}。","Kyou wa totemo samui desu.","It is very cold today.","අද ගොඩක් සීතලයි."),
    (f"この {HON}は とても おもしろいです。","Kono hon wa totemo omoshiroi desu.","This book is very interesting.","මේ පොත ගොඩක් රසවත්."),
    (f"サマンさんは とても {SHIN}です。","Saman-san wa totemo shinsetsu desu.","Saman is very kind.","සමන් ගොඩක් කරුණාවන්තයි."),
    (f"{NHG}の {BEN}は とても たのしいです。","Nihongo no benkyou wa totemo tanoshii desu.","Studying Japanese is very fun.","ජපන් භාෂාව ඉගෙන ගන්න එක ගොඩක් විනෝදජනකයි."),
    (f"{KINO}の テストは とても {MUZU}。","Kinou no tesuto wa totemo muzukashikatta desu.","Yesterday's test was very difficult.","ඊයේ විභාගය ගොඩක් අමාරු වුණා."),
    (f"そんなに {KANT}には とても {DEK}。","Sonna ni kantan ni wa totemo dekimasen.","I simply can't do it that easily.","ලේසියෙන් නම් කිසිසේත්ම කරන්න බැහැ."),
    (f"この {NIM}は {HITO}では とても {MOT}。","Kono nimotsu wa hitori de wa totemo mochimasen.","I simply can't carry this luggage alone.","මේ බඩු එක්කෙනෙකුට කිසිසේත්ම අරන් යන්න බැහැ."),
  ],
  foot="とても 〜",
)

if __name__ == "__main__":
    render(P61, "p121_totemo")
