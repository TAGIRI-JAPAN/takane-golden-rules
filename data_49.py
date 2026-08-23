from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

DEN  = r("電車","でん しゃ")
HOU  = r("方","ほう")
HAYA = r("速","はや")+"いです"
NIH  = r("日本","に ほん")
SAM  = r("寒","さむ")+"いです"
NHG  = r("日本語","に ほん ご")
EIG  = r("英語","えい ご")
MUZU = "むずかしいです"
NIKU = r("肉","にく")
SAKA = r("魚","さかな")
SUKI = r("好","す")+"き"
KYO  = r("今日","きょう")
KINO = r("昨日","きのう")
ISO  = "いそがしいです"
KAB  = "かばん"
YASU = r("安","やす")+"いです"
DOCH = "どちら"

P = dict(
  no="49", tag=None,
  title_jp="…より 〜の ほうが 〜です",
  title_ro='... yori 〜 no hou ga 〜 desu &nbsp;|&nbsp; 〜 is more 〜 than ... &nbsp;|&nbsp; '
           '<span class="si">... ට වඩා 〜 වැඩියි</span>',
  basic=(f"バスより {DEN}の {HOU}が {HAYA}。","Basu yori densha no hou ga hayai desu.",
         "The train is faster than the bus.","බස් එකට වඩා දුම්රිය වේගවත්."),
  use=(f'48と {r("同","おな")}じ くらべ方ですが、「〜の {HOU}が」を つけると '
       f'<b>えらんだ ほう</b>が はっきりします。しつもんは「AとB、{DOCH}が 〜ですか」です。',
       'Same comparison as 48, but adding <b>no hou ga</b> makes the chosen side clear. '
       'The question form is <b>A to B, dochira ga ~ desu ka</b>.',
       '48 වගේම සංසන්දනයක්; <b>no hou ga</b> දැම්මම තෝරගත්ත පැත්ත පැහැදිලියි. '
       'ප්‍රශ්නය: <b>A to B, dochira ga ~ desu ka</b>.'),
  pattern=[[("Aより","A yori"),("Bの ほうが","B no hou ga",True),"BLANK",("です","desu")],
           [("AとB、","A to B"),(f"{DOCH}が","dochira ga",True),"BLANK",("ですか","desu ka")],
           f"NOTE:{r('答','こた')}え{r('方','かた')}：「Bの ほうが 〜です」　/　"
           f"どちらも {r('同','おな')}じ ときは「どちらも 〜です」",
           f"NOTE:{r('人','ひと')}や ばしょでも「どちら」を つかいます（どっちは かいわ）"],
  examples=[
    (f"バスより {DEN}の {HOU}が {HAYA}。","Basu yori densha no hou ga hayai desu.","The train is faster than the bus.","බස් එකට වඩා දුම්රිය වේගවත්."),
    (f"スリランカより {NIH}の {HOU}が {SAM}。","Suriranka yori Nihon no hou ga samui desu.","Japan is colder than Sri Lanka.","ශ්‍රී ලංකාවට වඩා ජපානය සීතලයි."),
    (f"{EIG}より {NHG}の {HOU}が {MUZU}。","Eigo yori nihongo no hou ga muzukashii desu.","Japanese is harder than English.","ඉංග්‍රීසියට වඩා ජපන් භාෂාව අමාරුයි."),
    (f"{NIKU}と {SAKA}と、{DOCH}が {SUKI}ですか。","Niku to sakana to, dochira ga suki desu ka.","Which do you like better, meat or fish?","මස්ද මාළුද, මොකටද වැඩිය කැමති?"),
    (f"— {SAKA}の {HOU}が {SUKI}です。","— Sakana no hou ga suki desu.","— I like fish better.","— මම මාළු වලට වැඩිය කැමතියි."),
    (f"{KINO}より {KYO}の {HOU}が {ISO}。","Kinou yori kyou no hou ga isogashii desu.","Today is busier than yesterday.","ඊයේට වඩා අද කාර්යබහුලයි."),
    (f"この {KAB}の {HOU}が {YASU}。","Kono kaban no hou ga yasui desu.","This bag is the cheaper one.","මේ බෑග් එක ලාබයි."),
  ],
  foot="…より 〜の ほうが 〜です",
)

if __name__ == "__main__":
    render(P, "u49_houga")
