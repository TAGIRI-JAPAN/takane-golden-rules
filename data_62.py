from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

GAK  = r("学校","がっ こう")
DEN  = r("電車","でん しゃ")
SHIR = r("知","し")+"らない"
MON  = r("問題","もん だい")
KANT = r("簡単","かん たん")
OKU  = r("遅","おく")+"れる"
FUN  = r("分","ふん")
OMO  = r("思","おも")+"います"
ASHI = r("明日","あ した")
HARE = r("晴","は")+"れる"

P63 = dict(
  no="62", tag=None,
  title_jp="たぶん 〜でしょう",
  title_ro='tabun 〜 deshou &nbsp;|&nbsp; probably 〜 &nbsp;|&nbsp; '
           '<span class="si">බොහෝවිට 〜 ඇති</span>',
  basic=(f"サマンさんは たぶん {GAK}に いるでしょう。","Saman-san wa tabun gakkou ni iru deshou.",
         "Saman is probably at school.","සමන් බොහෝවිට පාසලේ ඇති."),
  use=(f'よそうを {r("言","い")}う ことばで、60〜80パーセントぐらいの きもちです。'
       f'「でしょう」は ていねい、「だろう」は ふつうけいです。',
       'It states an expectation — about 60–80% sure. '
       '<b>deshou</b> is the polite form; <b>darou</b> is the plain form.',
       'අනුමානයක් කියනවා — 60–80%ක් විතර විශ්වාසයි. '
       '<b>deshou</b> ආචාරශීලීයි; <b>darou</b> සරල ආකාරයයි.'),
  pattern=[[("たぶん","tabun",True),"BLANK",("でしょう","deshou",True)],
           f"NOTE:つよさ：きっと 〜はずです（64）　&gt;　たぶん 〜でしょう（62）　&gt;　"
           f"〜かもしれません（65）",
           f"NOTE:ていねい：でしょう　/　ふつう：だろう（ともだちと {r('話','はな')}す とき）"],
  examples=[
    (f"サマンさんは たぶん {GAK}に いるでしょう。","Saman-san wa tabun gakkou ni iru deshou.","Saman is probably at school.","සමන් බොහෝවිට පාසලේ ඇති."),
    (f"たぶん この {DEN}は こんで いるでしょう。","Tabun kono densha wa konde iru deshou.","This train is probably crowded.","බොහෝවිට මේ දුම්රියේ මිනිස්සු ගොඩක් ඇති."),
    (f"たぶん サマンさんは まだ {SHIR}でしょう。","Tabun Saman-san wa mada shiranai deshou.","Saman probably doesn't know yet.","බොහෝවිට සමන් තාම දන්නේ නැති ඇති."),
    (f"たぶん この {MON}は {KANT}でしょう。","Tabun kono mondai wa kantan deshou.","This question is probably easy.","බොහෝවිට මේ ප්‍රශ්නය ලේසි ඇති."),
    (f"たぶん バスは {OKU}でしょう。","Tabun basu wa okureru deshou.","The bus will probably be late.","බොහෝවිට බස් එක ප්‍රමාද වේවි."),
    (f"たぶん 20{FUN}ぐらい かかると {OMO}。","Tabun nijippun gurai kakaru to omoimasu.","I think it will probably take about 20 minutes.","බොහෝවිට විනාඩි 20ක් විතර යාවි කියලා හිතනවා."),
    (f"{ASHI}は たぶん {HARE}でしょう。","Ashita wa tabun hareru deshou.","It will probably be sunny tomorrow.","බොහෝවිට හෙට අව්ව ඇති."),
  ],
  foot="たぶん 〜でしょう",
)

if __name__ == "__main__":
    render(P63, "p62_tabun")
