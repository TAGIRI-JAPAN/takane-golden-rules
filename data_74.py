from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ONG  = r("音楽","おん がく")
KIKI = r("聞","き")+"きながら"
BEN  = r("勉強","べん きょう")
MIN  = r("見","み")+"ながら"
MITE = r("見","み")+"ては"
TABE = r("食","た")+"べます"
HATA = r("働","はたら")+"きながら"
NHG  = r("日本語","に ほん ご")
ARU  = r("歩","ある")+"きながら"
NOMI = r("飲","の")+"みながら"
HANA = r("話","はな")+"しましょう"
JISH = r("辞書","じ しょ")
KAI  = r("書","か")+"きました"
WARA = r("笑","わら")+"いながら"
HAN  = r("話","はな")+"しました"
ONA  = r("同","おな")+"じ"
HITO = r("人","ひと")

P63 = dict(
  no="74", tag=None,
  title_jp="〜ながら 〜します",
  title_ro='〜 nagara 〜 shimasu &nbsp;|&nbsp; doing 〜 while 〜ing &nbsp;|&nbsp; '
           '<span class="si">〜 කරමින් 〜</span>',
  basic=(f"{ONG}を {KIKI} {BEN}します。","Ongaku wo kikinagara benkyou shimasu.",
         "I study while listening to music.","මම සංගීතය අහමින් ඉගෙන ගන්නවා."),
  use=(f'1{HITO}が {ONA} ときに 2つの ことを する ときの かたちです。'
       f'ますけいの「ます」を とって「ながら」を つけます。',
       'Use it when one person does two things at the same time. '
       'Drop <b>masu</b> from the masu-form and add <b>nagara</b>.',
       'එක් කෙනෙක් එකවර දේවල් දෙකක් කරද්දී. '
       '<b>masu</b> ආකාරයෙන් <b>masu</b> අයින් කරලා <b>nagara</b> දාන්න.'),
  pattern=[["BLANK",("しながら","shinagara",True),("〜します","~ shimasu")],
           f"NOTE:{r('聞','き')}きます → {KIKI}　/　{r('見','み')}ます → {MIN}　/　"
           f"{r('食','た')}べます → {r('食','た')}べながら",
           f"NOTE:{r('大切','たい せつ')}なのは <b>あとの どうし</b>です"
           f"（{ONG}を {KIKI} {BEN}します ＝ {BEN}が メイン）"],
  examples=[
    (f"{ONG}を {KIKI} {BEN}します。","Ongaku wo kikinagara benkyou shimasu.","I study while listening to music.","මම සංගීතය අහමින් ඉගෙන ගන්නවා."),
    (f"テレビを {MIN} ごはんを {TABE}。","Terebi wo minagara gohan wo tabemasu.","I eat while watching TV.","මම රූපවාහිනිය බලමින් කනවා."),
    (f"{HATA} {NHG}を {BEN}して います。","Hatarakinagara nihongo wo benkyou shite imasu.","I study Japanese while working.","මම වැඩ කරමින් ජපන් භාෂාව ඉගෙන ගන්නවා."),
    (f"{ARU} スマホを {MITE} いけません。","Arukinagara sumaho wo mite wa ikemasen.","Don't look at your phone while walking.","ඇවිදිමින් ජංගම දුරකථනය බලන්න එපා."),
    (f"コーヒーを {NOMI} {HANA}。","Koohii wo nominagara hanashimashou.","Let's talk over a coffee.","කෝපි බොමින් කතා කරමු."),
    (f"{JISH}を {MIN} {KAI}。","Jisho wo minagara kakimashita.","I wrote it while looking at a dictionary.","ශබ්දකෝෂය බලමින් ලිව්වා."),
    (f"サマンさんは {WARA} {HAN}。","Saman-san wa warainagara hanashimashita.","Saman spoke with a smile.","සමන් සිනාසෙමින් කතා කළා."),
  ],
  foot="〜ながら 〜します",
)

if __name__ == "__main__":
    render(P63, "u74_nagara")
