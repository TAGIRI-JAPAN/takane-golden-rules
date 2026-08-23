from build2 import render, lab, tbl, note, exs

ROWS = [
 ["もの<br><small>thing</small>","これ|kore","それ|sore","あれ|are","どれ|dore"],
 ["場所<br><small>place</small>","ここ|koko","そこ|soko","あそこ|asoko","どこ|doko"],
 ["＋めいし<br><small>+ noun</small>","この 本|kono","その 本|sono","あの 本|ano","どの 本|dono"],
 ["ていねい<br><small>polite</small>","こちら|kochira","そちら|sochira","あちら|achira","どちら|dochira"],
 ["ようす<br><small>kind of</small>","こんな|konna","そんな|sonna","あんな|anna","どんな|donna"],
 ["シンハラ語","මේ|mē","ඔය|oya","අර|ara","කො…|ko…"],
]

P = dict(
  no="08",
  title_jp="こそあど ことば",
  title_ro='ko-so-a-do words &nbsp;|&nbsp; this / that / that over there / which &nbsp;|&nbsp; '
           '<span class="si">මේ / ඔය / අර / කො…</span>',
  intro=('日本語は「近い・すこし 遠い・とても 遠い・しつもん」の 4つに 分けます。'
         'シンハラ語の මේ・ඔය・අර と 分け方が ぴったり 同じなので、'
         'シンハラ語を 話す 人には いちばん わかりやすい ところです。',
         'Japanese splits these words four ways: near me, near you, far from both, and '
         'the question word. Sinhala divides them the same way (mē / oya / ara), so this '
         'is one of the easiest points for Sinhala speakers.',
         'ජපන් භාෂාව මේවා කොටස් 4කට බෙදනවා: මට ළඟ, ඔයාට ළඟ, දෙන්නාටම දුර, ප්‍රශ්නය. '
         'සිංහලෙනුත් හරියටම එහෙමයි (මේ / ඔය / අර) — ඒ නිසා මේක ලේසිම තැන.'),
  blocks=[
    lab("こそあど 一覧", "THE KO-SO-A-DO TABLE / සම්පූර්ණ වගුව"),
    tbl(["", "こ　near me", "そ　near you", "あ　far from both", "ど　question"], ROWS),
    lab("つかい方の ポイント", "HOW TO USE / භාවිතය"),
    note('<b>だれの そばに あるか</b>で えらびます。　'
         '<b>こ</b>＝話す 人の そば　/　<b>そ</b>＝聞く 人の そば　/　'
         '<b>あ</b>＝どちらからも 遠い　/　<b>ど</b>＝しつもん。'
         '手に 持って いる ものは いつも「これ」です。'),
    note('<b>ていねいに 言う とき</b>　ここ → <b>こちら</b>　/　どこ → <b>どちら</b>　/　'
         'だれ → <b>どなた</b>。お店や 会社では こちらを つかいます'
         '（23「〜は どこですか？」も 見て ください）。'),
    note('<b>話に 出て きた こと</b>を さす ときは「<b>それ</b>」です。'
         '「きのう 本を 買いました。」「<b>それ</b>は 何の 本ですか。」'),
    note('<b>これ・この の ちがい</b>　「これ」は それ 1つで 名詞。'
         '「この」は うしろに かならず 名詞が 来ます。'
         '<b>これ</b>は 本です。○　/　<b>この</b>は 本です。×　/　<b>この 本</b>は…○'),
    lab("言ってみよう！", "LET'S SAY IT / අපි කියමු"),
    exs([
      ("これは わたしの かばんです。","Kore wa watashi no kaban desu.",
       "This is my bag.","මේක මගේ බෑග් එක."),
      ("それを ください。","Sore wo kudasai.",
       "Please give me that one.","ඔය එක දෙන්න."),
      ("あの 人は サマンさんです。","Ano hito wa Saman-san desu.",
       "That person over there is Saman.","අර කෙනා සමන්."),
      ("トイレは どこですか。","Toire wa doko desu ka.",
       "Where is the toilet?","වැසිකිළිය කොහෙද?"),
      ("こちらへ どうぞ。","Kochira e douzo.",
       "This way, please.","මෙහාට වඩින්න."),
      ("どんな カレーが 好きですか。","Donna karee ga suki desu ka.",
       "What kind of curry do you like?","ඔයා කැමති මොන වගේ කරි වලටද?"),
    ]),
  ],
  foot="こそあど ことば",
)

if __name__ == "__main__":
    render(P, "u08_kosoado")
