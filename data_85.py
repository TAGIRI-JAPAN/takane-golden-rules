from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

NIH  = r("日本","に ほん")
RYO  = r("旅行","りょ こう")
IK   = r("行","い")+"く"
KYO  = r("京都","きょう と")
KAN  = r("漢字","かん じ")
JISH = r("辞書","じ しょ")
BEN  = r("便利","べん り")
YASU = r("安","やす")+"い"
MISE = r("店","みせ")
SHIR = r("知","し")+"って"
KAI  = r("買","か")+"う"
ASHI = r("明日","あ した")
HIMA = "ひま"
TETS = r("手伝","て つだ")+"います"
SAKA = r("魚","さかな")
ICHI = r("市場","い ち ば")
DAIG = r("大学","だい がく")
SEN  = r("先生","せん せい")
SOUD = r("相談","そう だん")
WAD  = r("話題","わ だい")

P = dict(
  no="85", tag=None,
  title_jp="〜なら、〜",
  title_ro='〜 nara, 〜 &nbsp;|&nbsp; if it\'s 〜 (then my advice is) &nbsp;|&nbsp; '
           '<span class="si">〜 නම්, 〜</span>',
  basic=(f"{NIH}へ {IK} なら、{KAN}を {r('勉強','べん きょう')}した ほうが いいですよ。",
         "Nihon e iku nara, kanji wo benkyou shita hou ga ii desu yo.",
         "If you're going to Japan, you'd better study kanji.","ජපානෙට යනවා නම් කන්ජි ඉගෙන ගන්න එක හොඳයි."),
  use=(f'あいてが {r("言","い")}った ことを <b>{WAD}に して</b>、'
       f'アドバイスや じょうほうを かえす ときの かたちです。'
       f'82・83・84と ちがい、うしろに <b>アドバイス</b>が 来ます。',
       'Take up what the other person just said as the topic, then give advice or '
       'information. Unlike 82–84, what follows is usually <b>advice</b>.',
       'අනිත් කෙනා කිව්ව දේ මාතෘකාව කරගෙන උපදෙසක් හෝ තොරතුරක් දෙනවා. '
       '82–84 වගේ නෙවෙයි — පස්සේ එන්නේ <b>උපදෙසක්</b>.'),
  pattern=[["BLANK",("なら、","nara",True),("〜が いいですよ","~ ga ii desu yo")],
           f"NOTE:めいし・な けいようしに そのまま つきます（{SAKA}なら／{HIMA}なら）。"
           f"どうしにも つきます（{IK} なら）",
           f"NOTE:「AとB、{r('私','わたし')}なら Aに します」のように "
           f"「{r('私','わたし')}なら」で {r('意見','い けん')}を {r('言','い')}えます"],
  examples=[
    (f"{NIH}へ {IK} なら、{KAN}を {r('勉強','べん きょう')}した ほうが いいですよ。","Nihon e iku nara, kanji wo benkyou shita hou ga ii desu yo.","If you're going to Japan, you'd better study kanji.","ජපානෙට යනවා නම් කන්ජි ඉගෙන ගන්න එක හොඳයි."),
    (f"{JISH}を {KAI} なら、この {MISE}が {BEN}ですよ。","Jisho wo kau nara, kono mise ga benri desu yo.","If you're buying a dictionary, this shop is handy.","ශබ්දකෝෂයක් ගන්නවා නම් මේ කඩේ පහසුයි."),
    (f"{SAKA}なら、あの {ICHI}が {r('安','やす')}いです。","Sakana nara, ano ichiba ga yasui desu.","If it's fish you want, that market is cheap.","මාළු නම් අර වෙළඳපොළ ලාබයි."),
    (f"{ASHI} {HIMA}なら、{TETS}よ。","Ashita hima nara, tetsudaimasu yo.","If you're free tomorrow, I'll help you.","හෙට නිදහස් නම් මම උදව් කරන්නම්."),
    (f"{RYO}に {IK} なら、はやく きっぷを {r('買','か')}って ください。","Ryokou ni iku nara, hayaku kippu wo katte kudasai.","If you're travelling, buy the ticket early.","සංචාරයක් යනවා නම් ටිකට් එක ඉක්මනට ගන්න."),
    (f"わからないなら、{SEN}に {SOUD}して ください。","Wakaranai nara, sensei ni soudan shite kudasai.","If you don't understand, talk to the teacher.","තේරෙන්නේ නැත්නම් ගුරුතුමා එක්ක කතා කරන්න."),
    (f"{r('私','わたし')}なら、こちらに します。","Watashi nara, kochira ni shimasu.","If it were me, I'd choose this one.","මම නම් මේක තෝරගන්නවා."),
  ],
  foot="〜なら、〜",
)

if __name__ == "__main__":
    render(P, "u85_nara")
