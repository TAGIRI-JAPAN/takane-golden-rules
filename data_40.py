from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SEN  = r("先生","せん せい")
DOKO = "どこ"
SHIR = r("知","し")+"って"
NAN  = r("何","なに")
JI   = r("時","じ")
HAJI = r("始","はじ")+"まる"
OSHI = r("教","おし")+"えて"
ASHI = r("明日","あ した")
KUR  = r("来","く")+"る"
WAK  = "わかりません"
KAI  = r("会議","かい ぎ")
TAS  = r("確","たし")+"かめて"
DAR  = r("誰","だれ")
MICH = r("道","みち")
AT   = r("合","あ")+"って"
GIM  = r("疑問","ぎ もん")+"し"

P = dict(
  no="40", tag=None,
  title_jp="〜か／〜か どうか",
  title_ro='〜 ka / 〜 ka dou ka &nbsp;|&nbsp; (I don\'t know) whether / what … &nbsp;|&nbsp; '
           '<span class="si">〜ද කියලා</span>',
  basic=(f"{SEN}が {DOKO}に いるか {SHIR}いますか。","Sensei ga doko ni iru ka shitte imasu ka.",
         "Do you know where the teacher is?","ගුරුතුමා කොහෙද ඉන්නේ කියලා දන්නවද?"),
  use=(f'{r("質問","しつ もん")}を {r("文","ぶん")}の {r("中","なか")}に {r("入","い")}れる かたちです。'
       f'{GIM}が ある ときは「〜か」、ない ときは「〜か どうか」。',
       'This puts a question inside a sentence. With a question word use <b>~ ka</b>; '
       'without one use <b>~ ka dou ka</b>.',
       'ප්‍රශ්නයක් වාක්‍යයට ඇතුළට දාන ක්‍රමය. ප්‍රශ්න වචනයක් තියෙනවා නම් <b>~ ka</b>; '
       'නැත්නම් <b>~ ka dou ka</b>.'),
  pattern=[[(f"{GIM}＋","gimonshi"),"BLANK",("か","ka",True),("〜ます","~ masu")],
           ["BLANK",("か どうか","ka dou ka",True),("〜ます","~ masu")],
           f"NOTE:{GIM}が ある：{DOKO}に いる<b>か</b>　/　ない：{KUR}<b>か どうか</b>",
           f"NOTE:よく つかう どうし：{SHIR}います　/　{WAK}　/　{OSHI} ください　/　{TAS}"],
  examples=[
    (f"{SEN}が {DOKO}に いるか {SHIR}いますか。","Sensei ga doko ni iru ka shitte imasu ka.","Do you know where the teacher is?","ගුරුතුමා කොහෙද ඉන්නේ කියලා දන්නවද?"),
    (f"じゅぎょうが {NAN}{JI}に {HAJI}か {OSHI} ください。","Jugyou ga nanji ni hajimaru ka oshiete kudasai.","Please tell me what time class starts.","පන්තිය කීයටද පටන් ගන්නේ කියලා කියන්න."),
    (f"{ASHI} サマンさんが {KUR}か どうか {WAK}。","Ashita Saman-san ga kuru ka dou ka wakarimasen.","I don't know whether Saman is coming tomorrow.","හෙට සමන් එනවද කියලා දන්නේ නැහැ."),
    (f"この {MICH}で {AT}いるか どうか {TAS}ましょう。","Kono michi de atte iru ka dou ka tashikamemashou.","Let's check whether this is the right way.","මේ පාර හරිද කියලා බලමු."),
    (f"{DAR}が {KUR}か {SHIR}いますか。","Dare ga kuru ka shitte imasu ka.","Do you know who is coming?","කවුද එන්නේ කියලා දන්නවද?"),
    (f"テストが むずかしいか どうか {WAK}。","Tesuto ga muzukashii ka dou ka wakarimasen.","I don't know whether the test is difficult.","විභාගය අමාරුද කියලා දන්නේ නැහැ."),
    (f"{KAI}が いつか {WAK}。","Kaigi ga itsu ka wakarimasen.","I don't know when the meeting is.","රැස්වීම කවදාද කියලා දන්නේ නැහැ."),
  ],
  foot="〜か／〜か どうか",
)

if __name__ == "__main__":
    render(P, "u40_kadouka")
