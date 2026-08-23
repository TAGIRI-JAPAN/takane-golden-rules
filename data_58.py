from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

DAI  = r("大学","だい がく")
NIH  = r("日本","に ほん")
IKU  = r("行","い")+"く"
SEN  = r("先生","せん せい")
CHIK = r("近","ちか")+"く"
ATAR = r("新","あたら")+"しい"
DEKI = "できる"
MISE = r("店","みせ")
NINK = r("人気","にん き")
KUNI = r("国","くに")
KAET = r("帰","かえ")+"った"
HITO = r("人","ひと")
KYOU = r("今日","きょう")
KONA = r("来","こ")+"ない"
BYOU = r("病気","びょう き")
JIN  = r("人","じん")

P38 = dict(
  no="58", tag=None,
  title_jp="〜らしいです〔〜らしい〕",
  title_ro='〜 rashii desu &nbsp;|&nbsp; It seems / I hear 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වගේ</span>',
  basic=("サマンさんは "+NIH+"の "+DAI+"に "+IKU+"らしいです。",
         "Saman-san wa Nihon no daigaku ni iku rashii desu.",
         "It seems Saman is going to a university in Japan.","සමන් ජපානේ විශ්වවිද්‍යාලයට යනවා වගේ."),
  use=(f'{r("聞","き")}いた ことや まわりの ようすから すいそくする ときに つかいます。'
       f'57の「そうです」より すこし よわい{r("言","い")}い{r("方","かた")}です。',
       'Use it to guess from what you heard or from the situation around you. '
       'It is a little weaker than <b>sou desu</b> in 57.',
       'අහපු දේවලින් හෝ වටපිටාවෙන් අනුමාන කරන්න. '
       '57 හි <b>sou desu</b> වලට වඩා ටිකක් දුර්වල කීමක්.'),
  pattern=[[("〜は","~ wa"),"BLANK",("らしいです","rashii desu",True)],
           [("〜は","~ wa"),"BLANK",("するらしいです","suru rashii desu",True)],
           [("〜は","~ wa"),"BLANK",("したらしいです","shita rashii desu",True)],
           f"NOTE:めいし・な けいようしに「だ」は つきません（{BYOU}らしい　○　/　{BYOU}だらしい　×）"],
  examples=[
    ("サマンさんは "+NIH+"の "+DAI+"に "+IKU+"らしいです。",
     "Saman-san wa Nihon no daigaku ni iku rashii desu.",
     "It seems Saman is going to a university in Japan.","සමන් ජපානේ විශ්වවිද්‍යාලයට යනවා වගේ."),
    (f"あの {SEN}は とても きびしいらしいです。","Ano sensei wa totemo kibishii rashii desu.","I hear that teacher is very strict.","අර ගුරුතුමා ගොඩක් දරුණුයි වගේ."),
    (f"{CHIK}に {ATAR} スーパーが {DEKI}らしいです。","Chikaku ni atarashii suupaa ga dekiru rashii desu.","It seems a new supermarket is opening near here.","මේ ළඟ අලුත් සුපිරි වෙළඳසැලක් හදනවා වගේ."),
    (f"あの {MISE}の パンは {NINK}らしいです。","Ano mise no pan wa ninki rashii desu.","I hear the bread at that shop is popular.","අර කඩේ පාන් ජනප්‍රියයි වගේ."),
    (f"サマンさんは もう {KUNI}へ {KAET}らしいです。","Saman-san wa mou kuni e kaetta rashii desu.","It seems Saman has already gone back home.","සමන් දැනටමත් රටට ගිහින් වගේ."),
    (f"あの {HITO}は スリランカ{JIN}らしいです。","Ano hito wa Suriranka-jin rashii desu.","It seems that person is Sri Lankan.","අර කෙනා ශ්‍රී ලාංකිකයෙක් වගේ."),
    (f"{KYOU}は バスが {KONA}らしいです。","Kyou wa basu ga konai rashii desu.","It seems the bus isn't coming today.","අද බස් එන්නේ නැහැ වගේ."),
  ],
  foot="〜らしいです",
)

if __name__ == "__main__":
    render(P38, "p58_rashii")
