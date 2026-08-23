from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NIH  = r("日本","に ほん")
TABM = r("食","た")+"べ"+r("物","もの")
ATAR = r("新","あたら")+"しい"
TENK = r("天気","てん き")
IMA  = r("今","いま")
DENS = r("電車","でん しゃ")
KAZ  = r("家族","か ぞく")
DOY  = r("土","ど")+"よう"+r("日","び")
MIS  = r("店","みせ")
OCHA = "お"+r("茶","ちゃ")
HITO = r("一","ひと")+"つ"
SEK  = r("席","せき")
KYO  = r("今日","きょう")
KIN  = r("昨日","きのう")
JUG  = r("授業","じゅ ぎょう")
RYO  = r("旅行","りょ こう")
MEN  = r("面接","めん せつ")
SHUM = r("週末","しゅう まつ")
SHOK = "お"+r("食事","しょく じ")

# ---------------------------------------------------------------- 28-1 基本
P21 = dict(
  no="28", tag=None,
  title_jp="〜は どうですか？",
  title_ro='〜 wa dou desu ka &nbsp;|&nbsp; How is 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කොහොමද?</span>',
  basic=(f"{NIH}の {TABM}は どうですか。","Nihon no tabemono wa dou desu ka.",
         "How is Japanese food?","ජපන් කෑම කොහොමද?"),
  use=(f'「どう」は ようすや かんそうを たずねる ことばです。'
       f'「どうですか」より「いかがですか」の ほうが ていねいです。'
       f'{r("目上","め うえ")}の{r("人","ひと")}や おきゃくさんには「いかがですか」を{r("使","つか")}いましょう。',
       '<b>dou</b> asks how something is, or what you think of it. '
       '<b>ikaga desu ka</b> is the polite version of <b>dou desu ka</b> — '
       'use it with seniors and with customers.',
       '<b>dou</b> කියන්නේ තත්ත්වය හෝ හැඟීම අහන එක — <b>dou desu ka</b> = කොහොමද? '
       '<b>ikaga desu ka</b> කියන්නේ ආචාරශීලී ආකාරය — වැඩිමහල් අයට සහ ගනුදෙනුකරුවන්ට ඒක කියන්න.'),
  pattern=[[("〜は","~ wa"),("どう？","dou")],
           [("〜は","~ wa"),("どうですか？","dou desu ka",True)],
           [("〜は","~ wa"),("いかがですか？","ikaga desu ka",True)],
           "NOTE:どう　&#8594;　どうですか　&#8594;　いかがですか　（ていねいさが 上がります）"],
  examples=[
    (f"{NIH}の {TABM}は どうですか。","Nihon no tabemono wa dou desu ka.","How is Japanese food?","ජපන් කෑම කොහොමද?"),
    (f"{ATAR} クラスは どうですか。","Atarashii kurasu wa dou desu ka.","How is the new class?","අලුත් පන්තිය කොහොමද?"),
    ("アルバイトは どうですか。","Arubaito wa dou desu ka.","How is your part-time job?","අර්ධකාලීන රැකියාව කොහොමද?"),
    (f"{NIH}の {TENK}は どうですか。","Nihon no tenki wa dou desu ka.","How is the weather in Japan?","ජපානයේ කාලගුණය කොහොමද?"),
    (f"{IMA}の へやは どうですか。","Ima no heya wa dou desu ka.","How is your room?","දැන් ඉන්න කාමරය කොහොමද?"),
    (f"{NIH}の {DENS}は どうですか。","Nihon no densha wa dou desu ka.","How are the trains in Japan?","ජපානයේ දුම්රිය කොහොමද?"),
    (f"ご{KAZ}は いかがですか。","Gokazoku wa ikaga desu ka.","How is your family?","ඔබේ පවුල කොහොමද?"),
  ],
  foot="〜は どうですか？",
)

# ---------------------------------------------------------------- 28-2 応用①
P21B = dict(
  no="28", tag="応用 ①　すすめる・さそう / SUGGESTING",
  title_jp="〜は どうですか？（すすめる）",
  title_ro='〜 wa dou desu ka &nbsp;|&nbsp; How about 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කොහොමද? (යෝජනාව)</span>',
  basic=("あしたは どうですか。","Ashita wa dou desu ka.",
         "How about tomorrow?","හෙට කොහොමද?"),
  use=(f'「どうですか」には ①ようすを{r("聞","き")}く ②すすめる・さそう の 2つの{r("意味","い み")}が あります。'
       f'おきゃくさんに すすめる ときは「いかがですか」です。',
       '<b>dou desu ka</b> has two uses: (1) asking how something is, and (2) suggesting or '
       'inviting. When you offer something to a customer, use <b>ikaga desu ka</b>.',
       '<b>dou desu ka</b> එකට භාවිත දෙකක් තියෙනවා: (1) තත්ත්වය අහන එක, (2) යෝජනා කිරීම / '
       'ආරාධනා කිරීම. ගනුදෙනුකරුවෙකුට යමක් දෙනවා නම් <b>ikaga desu ka</b> කියන්න.'),
  pattern=[[("〜は","~ wa"),("どうですか？","dou desu ka",True)],
           [("〜は","~ wa"),("いかがですか？","ikaga desu ka",True)],
           "NOTE:① ようすを 聞く　「クラスは どうですか」　/　② すすめる　「あしたは どうですか」"],
  examples=[
    ("あしたは どうですか。","Ashita wa dou desu ka.","How about tomorrow?","හෙට කොහොමද?"),
    (f"{DOY}は どうですか。","Doyoubi wa dou desu ka.","How about Saturday?","සෙනසුරාදා කොහොමද?"),
    (f"この {MIS}は どうですか。","Kono mise wa dou desu ka.","How about this shop?","මේ කඩේ කොහොමද?"),
    (f"{OCHA}は いかがですか。","Ocha wa ikaga desu ka.","Would you like some tea?","තේ එකක් කොහොමද?"),
    (f"もう {HITO} いかがですか。","Mou hitotsu ikaga desu ka.","Would you like one more?","තව එකක් කොහොමද?"),
    (f"この {SEK}は いかがですか。","Kono seki wa ikaga desu ka.","How about this seat?","මේ අසුන කොහොමද?"),
    ("サマンさんは どうですか。","Saman-san wa dou desu ka.","How about you, Saman?","සමන්, ඔබ කොහොමද?"),
  ],
  foot="〜は どうですか？（すすめる）",
)

# ---------------------------------------------------------------- 28-3 応用②
P21C = dict(
  no="28", tag="応用 ②　〜は どうでしたか？ / PAST",
  title_jp="〜は どうでしたか？",
  title_ro='〜 wa dou deshita ka &nbsp;|&nbsp; How was 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කොහොමද තිබුණේ?</span>',
  basic=(f"{KYO}の テストは どうでしたか。","Kyou no tesuto wa dou deshita ka.",
         "How was today's test?","අද විභාගය කොහොමද තිබුණේ?"),
  use=(f'「です」を「でした」に かえるだけです。21〜29と{r("同","おな")}じです。'
       f'ていねいに{r("聞","き")}くときは「いかがでしたか」を{r("使","つか")}います。',
       'Just change <b>desu</b> to <b>deshita</b>, exactly as in patterns 21–29. '
       'The polite version is <b>ikaga deshita ka</b>.',
       '<b>desu</b> එක <b>deshita</b> කරන්න විතරයි — 21–29 වගේමයි. '
       'ආචාරශීලී ආකාරය <b>ikaga deshita ka</b>.'),
  pattern=[[("〜は","~ wa"),("どうでしたか？","dou deshita ka",True)],
           [("〜は","~ wa"),("いかがでしたか？","ikaga deshita ka",True)],
           "NOTE:です → でした　/　いかがですか → いかがでしたか"],
  examples=[
    (f"{KYO}の テストは どうでしたか。","Kyou no tesuto wa dou deshita ka.","How was today's test?","අද විභාගය කොහොමද තිබුණේ?"),
    (f"{KIN}の {JUG}は どうでしたか。","Kinou no jugyou wa dou deshita ka.","How was yesterday's class?","ඊයේ පන්තිය කොහොමද තිබුණේ?"),
    (f"{NIH}の {RYO}は どうでしたか。","Nihon no ryokou wa dou deshita ka.","How was your trip in Japan?","ජපානයේ ගමන කොහොමද තිබුණේ?"),
    (f"アルバイトの {MEN}は どうでしたか。","Arubaito no mensetsu wa dou deshita ka.","How was your part-time job interview?","අර්ධකාලීන රැකියා සම්මුඛ පරීක්ෂණය කොහොමද තිබුණේ?"),
    (f"{SHUM}は どうでしたか。","Shuumatsu wa dou deshita ka.","How was your weekend?","සති අන්තය කොහොමද තිබුණේ?"),
    (f"{NIH}の {TABM}は どうでしたか。","Nihon no tabemono wa dou deshita ka.","How was the Japanese food?","ජපන් කෑම කොහොමද තිබුණේ?"),
    (f"{SHOK}は いかがでしたか。","Oshokuji wa ikaga deshita ka.","How was your meal?","ඔබේ කෑම කොහොමද තිබුණේ?"),
  ],
  foot="〜は どうでしたか？",
)

# ---------------------------------------------------------------- 28-4 / 28-5 答え方
_USE = (f'「どう」の{r("質問","しつ もん")}には けいようしで{r("答","こた")}えます。'
        f'「はい」「いいえ」では{r("答","こた")}えません。'
        f'06・07で ならった たのしい・むずかしい・いそがしい などが そのまま{r("使","つか")}えます。',
        'Answer a <b>dou</b> question with an adjective — never with <b>hai</b> or <b>iie</b>. '
        'The adjectives from patterns 06 and 07 (<b>tanoshii</b>, <b>muzukashii</b>, '
        '<b>isogashii</b> …) work here as they are.',
        '<b>dou</b> ප්‍රශ්නයකට විශේෂණ පදයකින් උත්තර දෙන්න — <b>hai</b>/<b>iie</b> නෙවෙයි. '
        '06, 07 වලදී ඉගෙන ගත්ත <b>tanoshii</b>, <b>muzukashii</b>, <b>isogashii</b> '
        'වගේ ඒවා එහෙමම භාවිතා කරන්න.')

_PAT = ["NOTE:【 ちゅうい 】「はい / いいえ」では 答えません　/　never answer yes or no",
        [("どうですか？","dou desu ka"),"TO",("けいようし ＋ です","adjective + desu",True)],
        "NOTE:かこ：むずかしい → むずかしかったです　　　すすめられたとき：いいですね　/　すみません、ちょっと…"]

_QA = [
  ("QA", (f"{NIH}の {TABM}は どうですか。","Nihon no tabemono wa dou desu ka.","How is Japanese food?","ජපන් කෑම කොහොමද?"),
         ("とても おいしいです。","Totemo oishii desu.","It's very good.","ගොඩක් රසයි.")),
  ("QA", (f"{ATAR} クラスは どうですか。","Atarashii kurasu wa dou desu ka.","How is the new class?","අලුත් පන්තිය කොහොමද?"),
         ("たのしいです。","Tanoshii desu.","It's fun.","විනෝදජනකයි.")),
  ("QA", ("アルバイトは どうですか。","Arubaito wa dou desu ka.","How is your part-time job?","අර්ධකාලීන රැකියාව කොහොමද?"),
         (f"ちょっと {r('忙','いそが')}しいです。","Chotto isogashii desu.","It's a bit busy.","ටිකක් කාර්යබහුලයි.")),
  ("QA", (f"{IMA}の へやは どうですか。","Ima no heya wa dou desu ka.","How is your room?","දැන් ඉන්න කාමරය කොහොමද?"),
         ("しずかです。","Shizuka desu.","It's quiet.","නිශ්ශබ්දයි.")),
  ("QA", ("あしたは どうですか。","Ashita wa dou desu ka.","How about tomorrow?","හෙට කොහොමද?"),
         ("いいですね。","Ii desu ne.","Sounds good.","හොඳයි නේ.")),
  ("QA", (f"{OCHA}は いかがですか。","Ocha wa ikaga desu ka.","Would you like some tea?","තේ එකක් කොහොමද?"),
         ("はい、おねがいします。","Hai, onegaishimasu.","Yes, please.","ඔව්, කරුණාකරලා.")),
  ("QA", (f"この {MIS}は どうですか。","Kono mise wa dou desu ka.","How about this shop?","මේ කඩේ කොහොමද?"),
         ("すみません、ちょっと…。","Sumimasen, chotto…","Sorry, I'd rather not.","සමාවෙන්න, ඒක ටිකක්…")),
  ("QA", (f"{KYO}の テストは どうでしたか。","Kyou no tesuto wa dou deshita ka.","How was today's test?","අද විභාගය කොහොමද තිබුණේ?"),
         ("むずかしかったです。","Muzukashikatta desu.","It was difficult.","අමාරු වුණා.")),
  ("QA", (f"{SHUM}は どうでしたか。","Shuumatsu wa dou deshita ka.","How was your weekend?","සති අන්තය කොහොමද තිබුණේ?"),
         ("たのしかったです。","Tanoshikatta desu.","It was fun.","විනෝදජනක වුණා.")),
]

_TITLE_RO = ('Dou no shitsumon no kotaekata &nbsp;|&nbsp; Answering a "how" question &nbsp;|&nbsp; '
             '<span class="si">"කොහොමද?" ප්‍රශ්නයට උත්තර දීම</span>')

P21A = dict(
  no="28", tag="応用 ③　答え方 / HOW TO ANSWER",
  title_jp="どう の 質問の 答え方",
  title_ro=_TITLE_RO,
  basic=("クラスは どうですか。　&#8594;　たのしいです。",
         "Kurasu wa dou desu ka. → Tanoshii desu.",
         "How is the class? → It's fun.","පන්තිය කොහොමද? → විනෝදජනකයි."),
  use=_USE, pattern=_PAT,
  examples=_QA[:4],
  foot="どう の 質問の 答え方",
)

P21A2 = dict(
  no="28", tag="応用 ③　答え方（つづき）/ HOW TO ANSWER (cont.)",
  title_jp="どう の 質問の 答え方",
  title_ro=_TITLE_RO,
  skip=("basic","use","pattern"), start=4,
  basic=P21A["basic"], use=_USE, pattern=_PAT,
  examples=_QA[4:],
  answers_label=("そのほかの 答え方","OTHER REPLIES / වෙනත් පිළිතුරු"),
  answers=[
    ("いいですね。","Ii desu ne.","Sounds good.","හොඳයි නේ."),
    ("とても いいです。","Totemo ii desu.","Very good.","ගොඩක් හොඳයි."),
    ("まあまあです。","Maamaa desu.","So-so.","හරි හරි."),
    (f"ちょっと {r('大変','たい へん')}です。","Chotto taihen desu.","It's a bit tough.","ටිකක් අමාරුයි."),
  ],
  foot="どう の 質問の 答え方",
)

if __name__ == "__main__":
    for p, stem in [(P21,"p28_1_dou"), (P21B,"p28_2_susumeru"), (P21C,"p28_3_past"),
                    (P21A,"p28_4_answer"), (P21A2,"p28_5_answer2")]:
        render(p, stem)
