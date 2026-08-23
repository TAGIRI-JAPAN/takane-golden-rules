from build2 import render, lab, tbl, note

GOJU = [
 ["あ行","あ|a","い|i","う|u","え|e","お|o"],
 ["か行","か|ka","き|ki","く|ku","け|ke","こ|ko"],
 ["さ行","さ|sa","*し|shi","す|su","せ|se","そ|so"],
 ["た行","た|ta","*ち|chi","*つ|tsu","て|te","と|to"],
 ["な行","な|na","に|ni","ぬ|nu","ね|ne","の|no"],
 ["は行","は|ha","ひ|hi","*ふ|fu","へ|he","ほ|ho"],
 ["ま行","ま|ma","み|mi","む|mu","め|me","も|mo"],
 ["や行","や|ya","-","ゆ|yu","-","よ|yo"],
 ["ら行","ら|ra","り|ri","る|ru","れ|re","ろ|ro"],
 ["わ行","わ|wa","-","-","-","*を|o"],
 ["ん","ん|n","-","-","-","-"],
]

DAKU = [
 ["が行","が|ga","ぎ|gi","ぐ|gu","げ|ge","ご|go"],
 ["ざ行","ざ|za","*じ|ji","ず|zu","ぜ|ze","ぞ|zo"],
 ["だ行","だ|da","*ぢ|ji","*づ|zu","で|de","ど|do"],
 ["ば行","ば|ba","び|bi","ぶ|bu","べ|be","ぼ|bo"],
 ["ぱ行","ぱ|pa","ぴ|pi","ぷ|pu","ぺ|pe","ぽ|po"],
]

HD = ["", "あ a", "い i", "う u", "え e", "お o"]

P = dict(
  no="01",
  title_jp="ひらがな",
  title_ro='hiragana &nbsp;|&nbsp; the basic Japanese syllabary &nbsp;|&nbsp; '
           '<span class="si">හිරගනා</span>',
  intro=('1つの 字が「子音＋母音」で 1つの 音に なります。シンハラ語の ක・කි・කු と '
         '同じ しくみなので、シンハラ語を 話す 人には おぼえやすい 文字です。',
         'Each character is one syllable — a consonant plus a vowel. Sinhala works the '
         'same way (ක ka, කි ki, කු ku), so hiragana comes easily to Sinhala speakers.',
         'එක් අකුරක් = හල් අකුරක් + ස්වරයක්. සිංහලෙත් එහෙමයි (ක, කි, කු) — '
         'ඒ නිසා සිංහල දන්න අයට හිරගනා ලේසියි.'),
  blocks=[
    lab("五十音", "GOJUON — THE 46 BASIC KANA / මූලික අකුරු 46"),
    tbl(HD, GOJU, kana=True),
    lab("だくおん・はんだくおん", "VOICED SOUNDS / නාද අකුරු"),
    tbl(HD, DAKU, kana=True),
    lab("おぼえる ポイント", "POINTS TO REMEMBER / මතක තබාගන්න"),
    note('<b>ようおん（小さい や・ゆ・よ）</b>　'
         'きゃ kya・きゅ kyu・きょ kyo　／　しゃ sha・しゅ shu・しょ sho　／　'
         'ちゃ cha・ちゅ chu・ちょ cho　／　にゃ nya・ひゃ hya・みゃ mya・りゃ rya　／　'
         'ぎゃ gya・じゃ ja・びゃ bya・ぴゃ pya'),
    note('<b>じょしの とき 音が かわります</b>　'
         'は → <b>wa</b>（わたし<b>は</b>）　／　へ → <b>e</b>（がっこう<b>へ</b>）　／　'
         'を → <b>o</b>（ごはん<b>を</b>）。この 3つだけ、書き方と 読み方が ちがいます。'),
    note('<b>小さい っ</b> きって kitte・がっこう gakkou　／　'
         '<b>のばす 音</b> おか<b>あ</b>さん・おに<b>い</b>さん・せんせ<b>い</b>　／　'
         '<span class="si">තද පාට කොටු විශේෂයි (shi, chi, tsu, fu, o).</span>'),
  ],
  foot="ひらがな",
)

if __name__ == "__main__":
    render(P, "u01_hiragana")
