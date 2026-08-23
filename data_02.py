from build2 import render, lab, tbl, note

GOJU = [
 ["ア行","ア|a","イ|i","ウ|u","エ|e","オ|o"],
 ["カ行","カ|ka","キ|ki","ク|ku","ケ|ke","コ|ko"],
 ["サ行","サ|sa","*シ|shi","ス|su","セ|se","ソ|so"],
 ["タ行","タ|ta","*チ|chi","*ツ|tsu","テ|te","ト|to"],
 ["ナ行","ナ|na","ニ|ni","ヌ|nu","ネ|ne","ノ|no"],
 ["ハ行","ハ|ha","ヒ|hi","*フ|fu","ヘ|he","ホ|ho"],
 ["マ行","マ|ma","ミ|mi","ム|mu","メ|me","モ|mo"],
 ["ヤ行","ヤ|ya","-","ユ|yu","-","ヨ|yo"],
 ["ラ行","ラ|ra","リ|ri","ル|ru","レ|re","ロ|ro"],
 ["ワ行","ワ|wa","-","-","-","*ヲ|o"],
 ["ン","ン|n","-","-","-","-"],
]

DAKU = [
 ["ガ行","ガ|ga","ギ|gi","グ|gu","ゲ|ge","ゴ|go"],
 ["ザ行","ザ|za","*ジ|ji","ズ|zu","ゼ|ze","ゾ|zo"],
 ["ダ行","ダ|da","*ヂ|ji","*ヅ|zu","デ|de","ド|do"],
 ["バ行","バ|ba","ビ|bi","ブ|bu","ベ|be","ボ|bo"],
 ["パ行","パ|pa","ピ|pi","プ|pu","ペ|pe","ポ|po"],
]

HD = ["", "ア a", "イ i", "ウ u", "エ e", "オ o"]

P = dict(
  no="02",
  title_jp="カタカナ",
  title_ro='katakana &nbsp;|&nbsp; the script for foreign words &nbsp;|&nbsp; '
           '<span class="si">කතකනා</span>',
  intro=('音は ひらがなと まったく 同じです。形が ちがうだけです。'
         '外国から 来た ことば・外国の 名前・音を あらわす ことばに つかいます。',
         'The sounds are exactly the same as hiragana — only the shapes differ. '
         'Katakana is used for foreign words, foreign names and sound words.',
         'ශබ්ද හිරගනා වගේමයි — හැඩය විතරයි වෙනස්. විදේශ වචන, විදේශ නම් සහ '
         'ශබ්ද වචන ලියන්න කතකනා යොදනවා.'),
  blocks=[
    lab("五十音", "GOJUON — THE 46 BASIC KANA / මූලික අකුරු 46"),
    tbl(HD, GOJU, kana=True),
    lab("だくおん・はんだくおん", "VOICED SOUNDS / නාද අකුරු"),
    tbl(HD, DAKU, kana=True),
    lab("カタカナだけの ルール", "KATAKANA-ONLY RULES / කතකනා නීති"),
    note('<b>のばす 音は「ー」</b>　コーヒー koohii・ノート nooto・スーパー suupaa・'
         'カレー karee — ひらがなの「あ・い・う」は つかいません。'),
    note('<b>小さい ァ ィ ゥ ェ ォ</b>　ファ fa・フィ fi・ティ ti・ディ di・シェ she・'
         'ジェ je・ウィ wi — 日本語に ない 音を 書く ときに つかいます。'),
    note('<b>よく つかう ことば</b>　スリランカ Suriranka・コロンボ Koronbo・'
         'バス basu・テレビ terebi・パソコン pasokon・アルバイト arubaito・'
         'コンビニ konbini・シャワー shawaa'),
  ],
  foot="カタカナ",
)

if __name__ == "__main__":
    render(P, "u02_katakana")
