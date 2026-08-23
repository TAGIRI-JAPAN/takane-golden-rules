from build2 import render, lab, tbl, note, exs

ROWS = [
 ["そして","そのあと・ならべる","and, and then","ごはんを 食べました。<b>そして</b> ねました。"],
 ["それから","じゅんばん（そのつぎ）","after that","そうじを して、<b>それから</b> 出かけます。"],
 ["でも","はんたい（かいわ）","but","つかれました。<b>でも</b> たのしかったです。"],
 ["しかし","はんたい（かたい）","however","やすいです。<b>しかし</b> よくないです。"],
 ["だから","りゆう → けっか","so, therefore","雨です。<b>だから</b> 行きません。"],
 ["それで","りゆう → けっか（じじつ）","and so","バスが おくれました。<b>それで</b> ちこくしました。"],
 ["それに","つけたす","besides, and also","やすいです。<b>それに</b> おいしいです。"],
 ["じゃあ／では","はなしを つぎへ","well then","<b>じゃあ</b>、また あした。"],
]

P = dict(
  no="88",
  title_jp="つなぎことば",
  title_ro='connecting words &nbsp;|&nbsp; soshite, demo, dakara … &nbsp;|&nbsp; '
           '<span class="si">සම්බන්ධක වචන</span>',
  intro=('75〜87で ならった つなぎ方は <b>1つの 文の 中</b>でした。'
         'ここは <b>文と 文の あいだ</b>に おく ことばです。'
         '「〜が、〜」（87）は 文の 中、「でも」は 文の はじめ、と おぼえて ください。',
         'Units 75–87 joined clauses <b>inside one sentence</b>. These words go '
         '<b>between two sentences</b>. Remember: <b>ga</b> (87) sits inside a sentence, '
         '<b>demo</b> starts a new one.',
         '75–87 වල සම්බන්ධ කළේ <b>එක වාක්‍යයක් ඇතුළේ</b>. මේවා <b>වාක්‍ය දෙකක් අතර</b> '
         'දාන වචන. <b>ga</b> (87) වාක්‍යය ඇතුළේ; <b>demo</b> අලුත් වාක්‍යයක් පටන් ගන්නවා.'),
  blocks=[
    lab("よく つかう つなぎことば", "THE MAIN CONNECTORS / ප්‍රධාන සම්බන්ධක"),
    tbl(["ことば","はたらき","English","れい"], ROWS, small=True),
    lab("まちがえやすい ところ", "EASY TO CONFUSE / පටලවා ගන්නා තැන්"),
    note('<b>でも と 〜が</b>　「でも」は <b>文の はじめ</b>、「〜が」は <b>文の 中</b>です。'
         '「やすいです。<b>でも</b>、よくないです。」○　/　'
         '「やすいです<b>が</b>、よくないです。」○　/　'
         '「やすいです。<b>が</b> よくないです。」×'),
    note('<b>だから と ので・から</b>　「だから」は <b>あたらしい 文</b>の はじめ。'
         '「〜ので」（78）「〜から」（29）は <b>1つの 文</b>の 中です。'
         '「雨です。<b>だから</b> 行きません。」＝「雨<b>なので</b> 行きません。」'),
    note('<b>そして と それから</b>　どちらも「そのあと」ですが、'
         '「それから」の ほうが <b>じゅんばん</b>を はっきり させます。'),
    note('<b>ていねいな 文では</b>　「でも」より「しかし」、'
         '「だから」より「そのため」を つかうと かたい 文に なります。'
         'しごとの メールでは こちらです。'),
    lab("言ってみよう！", "LET'S SAY IT / අපි කියමු"),
    exs([
      ("きのう 図書館へ 行きました。そして、日本語を 勉強しました。",
       "Kinou toshokan e ikimashita. Soshite, nihongo wo benkyou shimashita.",
       "I went to the library yesterday. And I studied Japanese.",
       "ඊයේ පුස්තකාලයට ගියා. ඊට පස්සේ ජපන් භාෂාව ඉගෙන ගත්තා."),
      ("この カレーは からいです。でも、おいしいです。",
       "Kono karee wa karai desu. Demo, oishii desu.",
       "This curry is spicy. But it's delicious.",
       "මේ කරිය සැරයි. ඒත් රසයි."),
      ("雨が ふって います。だから、今日は 行きません。",
       "Ame ga futte imasu. Dakara, kyou wa ikimasen.",
       "It's raining. So I won't go today.",
       "වහිනවා. ඒ නිසා අද යන්නේ නැහැ."),
      ("この 店は やすいです。それに、近いです。",
       "Kono mise wa yasui desu. Sore ni, chikai desu.",
       "This shop is cheap. And it's close, too.",
       "මේ කඩේ ලාබයි. ඒ විතරක් නෙවෙයි, ළඟයි."),
      ("じゃあ、また あした。",
       "Jaa, mata ashita.",
       "Well then, see you tomorrow.",
       "එහෙනම්, හෙට හම්බවෙමු."),
    ]),
  ],
  foot="つなぎことば",
)

if __name__ == "__main__":
    render(P, "u88_setsuzoku")
