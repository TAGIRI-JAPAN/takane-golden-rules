from build2 import render, lab, tbl, note, exs

ROWS = [
 ["は","テーマ（〜については）","わたし<b>は</b> 学生です。","topic marker"],
 ["が","しゅご・あたらしい じょうほう","だれ<b>が</b> 来ましたか。","subject / new info"],
 ["を","どうさの あいて（もくてきご）","ごはん<b>を</b> 食べます。","object"],
 ["に","時・ばしょ（いる/ある）・あいて","7時<b>に</b> 学校<b>に</b> 行きます。","time / place / target"],
 ["で","どうさの ばしょ・どうぐ・ほうほう","きょうしつ<b>で</b> バス<b>で</b>","where you act / by means of"],
 ["へ","ほうこう（〜のほうへ）","日本<b>へ</b> 行きます。","direction"],
 ["と","いっしょに・と（and）","友だち<b>と</b> 話します。","with / and"],
 ["も","〜も（also）","わたし<b>も</b> 行きます。","also"],
 ["から／まで","はじめ／おわり","9時<b>から</b> 3時<b>まで</b>","from / until"],
 ["の","もちぬし・せつめい","わたし<b>の</b> かばん","of / 's"],
]

P = dict(
  no="20",
  title_jp="助詞の つかい分け",
  title_ro='particles &nbsp;|&nbsp; wa, ga, wo, ni, de … &nbsp;|&nbsp; '
           '<span class="si">නිපාත</span>',
  intro=('助詞は ことばと ことばを つなぐ、日本語の ほねです。'
         'シンハラ語にも ට・න්・ෙන් などが あるので かんがえ方は 同じですが、'
         'どれを えらぶかが むずかしい ところです。ここで 一度 せいりしましょう。',
         'Particles are the skeleton of a Japanese sentence. Sinhala has particles too '
         '(ṭa, en …), so the idea is familiar — the hard part is choosing the right one.',
         'නිපාත කියන්නේ ජපන් වාක්‍යයේ අස්ථි. සිංහලෙත් නිපාත තියෙනවා (ට, න්, ෙන්) — '
         'අදහස එකයි; අමාරුව තමයි හරි එක තෝරගන්න එක.'),
  blocks=[
    lab("よく つかう 助詞", "THE MAIN PARTICLES / ප්‍රධාන නිපාත"),
    tbl(["助詞","はたらき","れい","English"], ROWS, small=True),
    lab("まちがえやすい ところ", "EASY TO CONFUSE / පටලවා ගන්නා තැන්"),
    note('<b>は と が</b>　「は」は<b>もう 知って いる こと</b>、「が」は<b>あたらしい こと</b>。'
         '「わたし<b>は</b> サマンです」（自分の 話）／「だれ<b>が</b> サマンさんですか」'
         '（あたらしい じょうほうを たずねる）。'
         'こたえも「サマンさん<b>が</b> …」に なります。'),
    note('<b>に と で</b>　「に」は <b>いる・ある・行く</b> ばしょ、「で」は <b>どうさを する</b> ばしょ。'
         'きょうしつ<b>に</b> います。／ きょうしつ<b>で</b> 勉強します。'),
    note('<b>へ と に（ほうこう）</b>　どちらも つかえますが、'
         '「へ」は <b>ほうこう</b>、「に」は <b>とうちゃくてん</b>の 気もちです。'
         '「へ」は「え」と 読みます（01の じょしの ルール）。'),
    note('<b>を と が</b>　好き・ほしい・できる・じょうずの 前は '
         '<b>かならず「が」</b>です（42・43・44・45）。カレー<b>が</b> 好きです。○'),
    lab("言ってみよう！", "LET'S SAY IT / අපි කියමු"),
    exs([
      ("わたしは 毎日 学校へ 行きます。","Watashi wa mainichi gakkou e ikimasu.",
       "I go to school every day.","මම හැමදාම පාසලට යනවා."),
      ("としょかんで 日本語を 勉強します。","Toshokan de nihongo wo benkyou shimasu.",
       "I study Japanese at the library.","මම පුස්තකාලයේ ජපන් භාෂාව ඉගෙන ගන්නවා."),
      ("きょうしつに 学生が います。","Kyoushitsu ni gakusei ga imasu.",
       "There are students in the classroom.","පන්ති කාමරයේ ශිෂ්‍යයෝ ඉන්නවා."),
      ("サマンさんと バスで 帰りました。","Saman-san to basu de kaerimashita.",
       "I went home by bus with Saman.","මම සමන් එක්ක බස් එකෙන් ගෙදර ගියා."),
      ("じゅぎょうは 9時から 3時までです。","Jugyou wa kuji kara sanji made desu.",
       "Class is from nine to three.","පන්ති 9 සිට 3 දක්වා."),
      ("これは わたしの かばんです。","Kore wa watashi no kaban desu.",
       "This is my bag.","මේක මගේ බෑග් එක."),
    ]),
  ],
  foot="助詞の つかい分け",
)

if __name__ == "__main__":
    render(P, "u20_joshi")
