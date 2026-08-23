from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ISS  = r("一緒","いっ しょ")
BEN  = r("勉強","べん きょう")
NOM  = r("飲","の")+"みませんか"
SAN  = r("散歩","さん ぽ")
SHUM = r("週末","しゅう まつ")
KIM  = r("来","き")+"ませんか"
SHA  = r("写真","しゃ しん")
TOS  = r("図書館","と しょ かん")
AIM  = r("会","あ")+"いませんか"
NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"しませんか"
HITE = r("否定","ひ てい")

P26 = dict(
  no="37", tag=None,
  title_jp="〜しませんか？",
  title_ro='〜 shimasen ka &nbsp;|&nbsp; Would you like to 〜? &nbsp;|&nbsp; '
           '<span class="si">〜 කරමුද?</span>',
  basic=(f"{ISS}に {BEN}しませんか。","Isshoni benkyou shimasen ka.",
         "Would you like to study together?","අපි එකට ඉගෙන ගමුද?"),
  use=(f'あいてを さそう ときの ことばです。'
       f'「ません」は{HITE}の{r("形","かたち")}ですが、{r("意味","い み")}は「{ISS}に しましょう」という さそいです。',
       'Use it to invite someone. <b>masen</b> is a negative form, but here it means '
       '"let’s do it together" — a soft, polite invitation.',
       'කෙනෙකුට ආරාධනා කරන්න භාවිතා කරන්න. <b>masen</b> නිශේධන ආකාරය වුණත්, '
       'මෙතන අර්ථය "අපි එකට කරමු" කියන මෘදු ආරාධනාවයි.'),
  pattern=[["BLANK",("しませんか？","shimasen ka",True)],
           f"NOTE:12の「〜したいですか」より、さそう ときは こちらが ていねいです",
           f"NOTE:{r('答','こた')}え{r('方','かた')}：いいですね　/　ぜひ！　/　すみません、ちょっと…　"
           f"（හොඳයි නේ　/　අනිවාර්යයෙන්!）"],
  examples=[
    (f"{ISS}に {BEN}しませんか。","Isshoni benkyou shimasen ka.","Would you like to study together?","අපි එකට ඉගෙන ගමුද?"),
    (f"{ISS}に コーヒーを {NOM}。","Isshoni koohii wo nomimasen ka.","Would you like to have coffee with me?","අපි එකට කෝපි බොමුද?"),
    (f"{SHUM} {SAN}しませんか。","Shuumatsu sanpo shimasen ka.","Would you like to go for a walk at the weekend?","සති අන්තයේ ඇවිදින්න යමුද?"),
    (f"こんど うちに {KIM}。","Kondo uchi ni kimasen ka.","Would you like to come to my place sometime?","කවදා හරි අපේ ගෙදර එනවද?"),
    (f"{ISS}に {SHA}を とりませんか。","Isshoni shashin wo torimasen ka.","Would you like to take a photo together?","අපි එකට ඡායාරූපයක් ගමුද?"),
    (f"あした {TOS}で {AIM}。","Ashita toshokan de aimasen ka.","Would you like to meet at the library tomorrow?","හෙට පුස්තකාලයේ හම්බවෙමුද?"),
    (f"{NHG}で {HAN}。","Nihongo de hanashimasen ka.","Shall we talk in Japanese?","අපි ජපන් භාෂාවෙන් කතා කරමුද?"),
  ],
  foot="〜しませんか？",
)

if __name__ == "__main__":
    render(P26, "p37_shimasenka")
