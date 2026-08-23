from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TAN  = "お"+r("誕生日","たん じょう び")
GOK  = r("合格","ごう かく")
NYU  = "ご"+r("入学","にゅう がく")
SOT  = "ご"+r("卒業","そつ ぎょう")
SHUS = "ご"+r("就職","しゅう しょく")
KEK  = "ご"+r("結婚","けっ こん")
TOM  = r("友","とも")+"だち"
MEUE = r("目上","め うえ")
HITO = r("人","ひと")

# ---------------------------------------------------------------- 31 おめでとう
P22 = dict(
  no="31", tag=None,
  title_jp="〜 おめでとう",
  title_ro='〜 omedetou &nbsp;|&nbsp; Congratulations on 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 සුබ පැතුම්</span>',
  basic=(f"{TAN} おめでとう。","Otanjoubi omedetou.",
         "Happy birthday.","සුබ උපන්දිනයක්."),
  use=(f'おいわいの{r("気持","き も")}ちを つたえる ことばです。'
       f'{TOM}には「おめでとう」、{MEUE}の{HITO}には「おめでとうございます」です。',
       'This expresses congratulations. Say <b>omedetou</b> to friends and '
       '<b>omedetou gozaimasu</b> to seniors.',
       'සුබ පැතුම් කියන වචනය. යාළුවන්ට <b>omedetou</b>, වැඩිමහල් අයට <b>omedetou gozaimasu</b>.'),
  pattern=[["BLANK",("おめでとう","omedetou",True)],
           ["BLANK",("おめでとうございます","omedetou gozaimasu",True)],
           f"NOTE:ご ＋ {r('卒業','そつ ぎょう')}・{r('結婚','けっ こん')}・{r('入学','にゅう がく')}　/　"
           f"お ＋ {r('誕生日','たん じょう び')}　（ていねいに なります）",
           f"NOTE:{r('答','こた')}え{r('方','かた')}：ありがとう　/　ありがとうございます　/　おかげさまで　"
           f"（ස්තූතියි　/　ඔබේ උදව්වෙන්）"],
  examples=[
    (f"{TAN} おめでとう。","Otanjoubi omedetou.","Happy birthday.","සුබ උපන්දිනයක්."),
    (f"{GOK} おめでとうございます。","Goukaku omedetou gozaimasu.","Congratulations on passing.","විභාගය සමත් වීම ගැන සුබ පැතුම්."),
    (f"{NYU} おめでとうございます。","Gonyuugaku omedetou gozaimasu.","Congratulations on entering school.","පාසලට ඇතුළු වීම ගැන සුබ පැතුම්."),
    (f"{SOT} おめでとうございます。","Gosotsugyou omedetou gozaimasu.","Congratulations on your graduation.","උපාධිය ගැන සුබ පැතුම්."),
    (f"{SHUS} おめでとうございます。","Goshuushoku omedetou gozaimasu.","Congratulations on your new job.","අලුත් රැකියාව ගැන සුබ පැතුම්."),
    (f"{KEK} おめでとうございます。","Gokekkon omedetou gozaimasu.","Congratulations on your wedding.","විවාහය ගැන සුබ පැතුම්."),
    ("あけまして おめでとうございます。","Akemashite omedetou gozaimasu.","Happy New Year.","සුබ අලුත් අවුරුද්දක්."),
  ],
  foot="〜 おめでとう",
)

if __name__ == "__main__":
    render(P22, "p31_omedetou")
