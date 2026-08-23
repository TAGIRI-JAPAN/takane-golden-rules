from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SHIK = r("試験","し けん")
UKA  = r("受","う")+"かる"
TENK = r("天気","てん き")
SHIG = r("仕事","し ごと")
MITS = r("見","み")+"つかる"
NIH  = r("日本","に ほん")
SEIK = r("生活","せい かつ")
KURU = r("来","く")+"る"
AME  = r("雨","あめ")
FURA = r("降","ふ")+"らない"
KANT = r("簡単","かん たん")
HAYA = r("早","はや")+"く"
JIB  = r("自分","じ ぶん")

P29 = dict(
  no="41", tag=None,
  title_jp="〜と いいですね",
  title_ro='〜 to ii desu ne &nbsp;|&nbsp; I hope 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 නම් හොඳයි නේ</span>',
  basic=(f"{SHIK}に {UKA}と いいですね。","Shiken ni ukaru to ii desu ne.",
         "I hope you pass the exam.","විභාගය සමත් වෙනවා නම් හොඳයි නේ."),
  use=(f'{JIB}が のぞむ ことを{r("言","い")}う ことばです。39と{r("同","おな")}じで「と」の{r("前","まえ")}は ふつうけいです。'
       f'あいてに{r("言","い")}うと「うまく いって ほしい」という{r("気持","き も")}ちが つたわります。',
       'Use it to say what you hope for. As in pattern 39, the part before <b>to</b> is in the '
       'plain form. Said to someone else, it means "I hope it goes well for you".',
       'තමන් බලාපොරොත්තු වන දේ කියන්න. 39 වගේම <b>to</b> එකට කලින් සරල ආකාරය. '
       'අනිත් කෙනාට කිව්වොත් "හොඳින් වේවා" කියන හැඟීම යනවා.'),
  pattern=[["BLANK",("と","to",True),("いいですね","ii desu ne",True)],
           f"NOTE:39と 同じ：「と」の 前は ふつうけい（{UKA}　/　いい　/　{FURA}　/　{KANT}だ）",
           f"NOTE:{r('答','こた')}え{r('方','かた')}：ありがとうございます　/　そうですね　/　がんばります　"
           f"（ස්තූතියි　/　මම උත්සාහ කරන්නම්）"],
  examples=[
    (f"{SHIK}に {UKA}と いいですね。","Shiken ni ukaru to ii desu ne.","I hope you pass the exam.","විභාගය සමත් වෙනවා නම් හොඳයි නේ."),
    (f"あした {TENK}が いいと いいですね。","Ashita tenki ga ii to ii desu ne.","I hope the weather is good tomorrow.","හෙට කාලගුණය හොඳ නම් හොඳයි නේ."),
    (f"いい {SHIG}が {MITS}と いいですね。","Ii shigoto ga mitsukaru to ii desu ne.","I hope you find a good job.","හොඳ රැකියාවක් හම්බවුණා නම් හොඳයි නේ."),
    (f"{NIH}の {SEIK}が たのしいと いいですね。","Nihon no seikatsu ga tanoshii to ii desu ne.","I hope life in Japan is fun.","ජපානයේ ජීවිතය විනෝදජනක නම් හොඳයි නේ."),
    (f"バスが {HAYA} {KURU}と いいですね。","Basu ga hayaku kuru to ii desu ne.","I hope the bus comes soon.","බස් එක ඉක්මනට එනවා නම් හොඳයි නේ."),
    (f"{AME}が {FURA}と いいですね。","Ame ga furanai to ii desu ne.","I hope it doesn't rain.","වැස්ස වහින්නේ නැත්නම් හොඳයි නේ."),
    (f"つぎの テストが {KANT}だと いいですね。","Tsugi no tesuto ga kantan da to ii desu ne.","I hope the next test is easy.","ඊළඟ විභාගය ලේසි නම් හොඳයි නේ."),
  ],
  foot="〜と いいですね",
)

if __name__ == "__main__":
    render(P29, "p41_toiidesune")
