from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MAT  = r("待","ま")+"って"
KAS  = r("貸","か")+"して"
SAS  = r("誘","さそ")+"って"
SHIN = r("心配","しん ぱい")
NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"して"
SHA  = r("写真","しゃ しん")
TOT  = r("撮","と")+"って"
SAI  = r("最後","さい ご")
KII  = r("聞","き")+"いて"
W    = r("私","わたし")
MEUE = r("目上","め うえ")
HITO = r("人","ひと")

P24 = dict(
  no="33", tag=None,
  title_jp="〜して くれて ありがとう",
  title_ro='〜 shite kurete arigatou &nbsp;|&nbsp; Thank you for 〜ing (for me) &nbsp;|&nbsp; '
           '<span class="si">〜 කළාට ස්තූතියි</span>',
  basic=(f"{MAT} くれて ありがとう。","Matte kurete arigatou.",
         "Thank you for waiting.","ඉන්න එකට ස්තූතියි."),
  use=(f'15の「て」に「くれて ありがとう」を つけます。'
       f'「くれる」は「あいてが {W}に して くれた」という{r("意味","い み")}です。',
       'Take the <b>te</b> form from pattern 15 and add <b>kurete arigatou</b>. '
       '<b>kureru</b> means "the other person did it for me".',
       '15 හි <b>te</b> ආකාරයට <b>kurete arigatou</b> දාන්න. '
       '<b>kureru</b> කියන්නේ "අනිත් කෙනා මට ඒක කළා" කියන එකයි.'),
  pattern=[[("〜して","~ shite"),("くれて","kurete",True),("ありがとう","arigatou",True)],
           [("〜して","~ shite"),("くれて","kurete",True),("ありがとうございます","arigatou gozaimasu",True)],
           f"NOTE:くれる = あいてが {W}に して くれた（මට කළා）　/　{MEUE}の {HITO}には「ございます」",
           f"NOTE:{r('答','こた')}え{r('方','かた')}：どういたしまして　/　いいえ　/　こちらこそ　（කමක් නැහැ）"],
  examples=[
    (f"{MAT} くれて ありがとう。","Matte kurete arigatou.","Thank you for waiting.","ඉන්න එකට ස්තූතියි."),
    (f"{KAS} くれて ありがとう。","Kashite kurete arigatou.","Thank you for lending it to me.","ණයට දුන්නාට ස්තූතියි."),
    (f"{SAS} くれて ありがとう。","Sasotte kurete arigatou.","Thank you for inviting me.","ආරාධනා කළාට ස්තූතියි."),
    (f"{SHIN}して くれて ありがとう。","Shinpai shite kurete arigatou.","Thank you for worrying about me.","මා ගැන හිතුවාට ස්තූතියි."),
    (f"{NHG}で {HAN} くれて ありがとう。","Nihongo de hanashite kurete arigatou.","Thank you for speaking in Japanese.","ජපන් භාෂාවෙන් කතා කළාට ස්තූතියි."),
    (f"{SHA}を {TOT} くれて ありがとうございます。","Shashin wo totte kurete arigatou gozaimasu.","Thank you for taking the photo.","ඡායාරූපය ගත්තාට ස්තූතියි."),
    (f"{SAI}まで {KII} くれて ありがとうございます。","Saigo made kiite kurete arigatou gozaimasu.","Thank you for listening to the end.","අන්තිම වෙනකන් අහගෙන හිටියාට ස්තූතියි."),
  ],
  foot="〜して くれて ありがとう",
)

if __name__ == "__main__":
    render(P24, "p33_kurete")
