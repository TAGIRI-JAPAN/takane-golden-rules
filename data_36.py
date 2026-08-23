from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

CHI  = r("遅刻","ち こく")
YAS  = r("休","やす")+"んで"
MACH = r("間違","まちが")+"えて"
SHU  = r("宿題","しゅく だい")
WAS  = r("忘","わす")+"れて"
HEN  = r("返事","へん じ")
REN  = r("連絡","れん らく")
KIN  = r("昨日","きのう")
MEUE = r("目上","め うえ")
HITO = r("人","ひと")
SHIG = r("仕事","し ごと")
JIB  = r("自分","じ ぶん")

P25 = dict(
  no="36", tag=None,
  title_jp="〜（して）ごめんなさい",
  title_ro=("〜 (shite) gomennasai &nbsp;|&nbsp; I&#39;m sorry for 〜 &nbsp;|&nbsp; "
            '<span class="si">〜 ට සමාවෙන්න</span>'),
  basic=(f"{CHI}して ごめんなさい。","Chikoku shite gomennasai.",
         "I'm sorry I was late.","පරක්කු වුණාට සමාවෙන්න."),
  use=(f'{JIB}が した ことを あやまる ときの ことばです。'
       f'「して」は した こと、「しなくて」は しなかった こと、「できなくて」は できなかった ことです。',
       'Use it to apologize for what you did. <b>shite</b> = for what you did, '
       '<b>shinakute</b> = for what you did NOT do, <b>dekinakute</b> = for what you could not do.',
       'තමන් කළ දෙයකට සමාව අයදින වචනය. <b>shite</b> = කළ දෙයට, '
       '<b>shinakute</b> = නොකළ දෙයට, <b>dekinakute</b> = කරන්න බැරි වුණු දෙයට.'),
  pattern=[[("〜して","~ shite"),("ごめんなさい","gomennasai",True)],
           [("〜しなくて","~ shinakute"),("ごめんなさい","gomennasai",True)],
           [("〜できなくて","~ dekinakute"),("ごめんなさい","gomennasai",True)],
           f"NOTE:【 ちゅうい 】{MEUE}の {HITO}・{SHIG}では　ごめんなさい &#8594; すみません / "
           f"もうしわけありません"],
  examples=[
    (f"{CHI}して ごめんなさい。","Chikoku shite gomennasai.","I'm sorry I was late.","පරක්කු වුණාට සමාවෙන්න."),
    (f"{YAS} ごめんなさい。","Yasunde gomennasai.","I'm sorry I was absent.","නිවාඩු ගත්තාට සමාවෙන්න."),
    ("うるさくして ごめんなさい。","Urusaku shite gomennasai.","I'm sorry for being noisy.","ශබ්ද කළාට සමාවෙන්න."),
    (f"{SHU}を {WAS} ごめんなさい。","Shukudai wo wasurete gomennasai.","I'm sorry I forgot my homework.","ගෙදර වැඩ අමතක වුණාට සමාවෙන්න."),
    (f"{MACH} ごめんなさい。","Machigaete gomennasai.","I'm sorry, I made a mistake.","වැරදුණාට සමාවෙන්න."),
    (f"{HEN}を しなくて ごめんなさい。","Henji wo shinakute gomennasai.","I'm sorry I didn't reply.","උත්තර නොදුන්නාට සමාවෙන්න."),
    (f"{KIN} {REN}が できなくて ごめんなさい。","Kinou renraku ga dekinakute gomennasai.","I'm sorry I couldn't contact you yesterday.","ඊයේ සම්බන්ධ වෙන්න බැරි වුණාට සමාවෙන්න."),
  ],
  foot="〜（して）ごめんなさい",
)

if __name__ == "__main__":
    render(P25, "p36_gomennasai")
