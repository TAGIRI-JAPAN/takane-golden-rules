from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

TEG  = "お"+r("手紙","て がみ")
DEN  = r("電話","でん わ")
SHIN = "ご"+r("親切","しん せつ")
TETS = "お"+r("手伝","て つだ")+"い"
KYO  = r("今日","きょう")
TOM  = r("友","とも")+"だち"
MEUE = r("目上","め うえ")
HITO = r("人","ひと")

# ---------------------------------------------------------------- 32 ありがとう
P23 = dict(
  no="32", tag=None,
  title_jp="〜 ありがとう",
  title_ro='〜 arigatou &nbsp;|&nbsp; Thank you for 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 ට ස්තූතියි</span>',
  basic=(f"{TEG}を ありがとう。","Otegami wo arigatou.",
         "Thank you for your letter.","ලිපියට ස්තූතියි."),
  use=(f'おれいの{r("気持","き も")}ちを つたえる ことばです。'
       f'{TOM}には「ありがとう」、{MEUE}の{HITO}には「ありがとうございます」です。',
       'This expresses thanks. Say <b>arigatou</b> to friends and '
       '<b>arigatou gozaimasu</b> to seniors.',
       'ස්තූතිය කියන වචනය. යාළුවන්ට <b>arigatou</b>, වැඩිමහල් අයට <b>arigatou gozaimasu</b>.'),
  pattern=[[("〜を","~ wo"),("ありがとう","arigatou",True)],
           [("〜を","~ wo"),("ありがとうございます","arigatou gozaimasu",True)],
           "NOTE:おわった ことには「ありがとうございました」（かこ）",
           f"NOTE:{r('答','こた')}え{r('方','かた')}：どういたしまして　/　いいえ　/　こちらこそ　"
           f"（කමක් නැහැ　/　මමත් ස්තූතියි）"],
  examples=[
    (f"{TEG}を ありがとう。","Otegami wo arigatou.","Thank you for your letter.","ලිපියට ස්තූතියි."),
    (f"{DEN}を ありがとう。","Denwa wo arigatou.","Thank you for calling.","කතා කිරීමට ස්තූතියි."),
    ("アドバイスを ありがとうございます。","Adobaisu wo arigatou gozaimasu.","Thank you for your advice.","උපදෙස් වලට ස්තූතියි."),
    (f"{SHIN}に ありがとうございます。","Goshinsetsu ni arigatou gozaimasu.","Thank you for your kindness.","ඔබේ කරුණාවට ස්තූතියි."),
    (f"{TETS}を ありがとうございます。","Otetsudai wo arigatou gozaimasu.","Thank you for your help.","උදව්වට ස්තූතියි."),
    ("いつも ありがとうございます。","Itsumo arigatou gozaimasu.","Thank you, as always.","හැමවෙලේම ස්තූතියි."),
    (f"{KYO}は ありがとうございました。","Kyou wa arigatou gozaimashita.","Thank you for today.","අදට ස්තූතියි."),
  ],
  foot="〜 ありがとう",
)

if __name__ == "__main__":
    render(P23, "p32_arigatou")
