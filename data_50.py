from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

HAYA = r("早","はや")+"く"
NET  = r("寝","ね")+"た"
HOU  = r("方","ほう")
ISH  = r("医者","い しゃ")
IT   = r("行","い")+"った"
YASU = r("休","やす")+"んだ"
MUR  = r("無理","む り")
KIP  = "きっぷ"
KAT  = r("買","か")+"った"
KASA = "かさ"
MOT  = r("持","も")+"って"
IKA  = r("行","い")+"かない"
TAB  = r("食","た")+"べない"
RENR = r("連絡","れん らく")
KYO_ = r("今日","きょう")
SEN_ = r("先生","せん せい")

P = dict(
  no="50", tag=None,
  title_jp="〜した ほうが いいです",
  title_ro='〜 shita hou ga ii desu &nbsp;|&nbsp; You had better 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 කරන එක හොඳයි</span>',
  basic=(f"{HAYA} {NET} {HOU}が いいですよ。","Hayaku neta hou ga ii desu yo.",
         "You had better go to bed early.","ඉක්මනට නිදාගන්න එක හොඳයි."),
  use=(f'あいてに アドバイスを する ときの かたちです。'
       f'「する {HOU}が いい」より <b>「した {HOU}が いい」</b>（た{r("形","けい")}）の ほうが しぜんです。'
       f'ひていは「〜ない {HOU}が いい」です。',
       'Use it to give advice. The <b>ta-form</b> + <b>hou ga ii</b> sounds more natural '
       'than the dictionary form. The negative is <b>~ nai hou ga ii</b>.',
       'උපදෙසක් දෙන්න. ශබ්දකෝෂ ආකාරයට වඩා <b>ta-ආකාරය</b> + <b>hou ga ii</b> ස්වාභාවිකයි. '
       'නෙගටිව් එක <b>~ nai hou ga ii</b>.'),
  pattern=[["BLANK",(f"した {HOU}が いいです","shita hou ga ii desu",True)],
           ["BLANK",(f"しない {HOU}が いいです","shinai hou ga ii desu",True)],
           f"NOTE:た{r('形','けい')}＋ほうが いい（{r('休','やす')}んだ ほうが いい）　/　"
           f"ない{r('形','けい')}＋ほうが いい（{IKA} ほうが いい）",
           f"NOTE:49の「〜の ほうが」（くらべる）とは ちがい、ここは <b>アドバイス</b>です"],
  examples=[
    (f"{HAYA} {NET} {HOU}が いいですよ。","Hayaku neta hou ga ii desu yo.","You had better go to bed early.","ඉක්මනට නිදාගන්න එක හොඳයි."),
    (f"{ISH}に {IT} {HOU}が いいです。","Isha ni itta hou ga ii desu.","You had better see a doctor.","දොස්තර ළඟට යන එක හොඳයි."),
    (f"{KYO_}は {YASU} {HOU}が いいですよ。","Kyou wa yasunda hou ga ii desu yo.","You had better rest today.","අද විවේක ගන්න එක හොඳයි."),
    (f"{KIP}は はやく {KAT} {HOU}が いいです。","Kippu wa hayaku katta hou ga ii desu.","You had better buy the ticket early.","ටිකට් එක ඉක්මනට ගන්න එක හොඳයි."),
    (f"{KASA}を {MOT} {IT} {HOU}が いいです。","Kasa wo motte itta hou ga ii desu.","You had better take an umbrella.","කුඩය අරන් යන එක හොඳයි."),
    (f"{MUR}を しない {HOU}が いいです。","Muri wo shinai hou ga ii desu.","You had better not overdo it.","වැඩිය මහන්සි නොවෙන එක හොඳයි."),
    (f"{SEN_}に {RENR}した {HOU}が いいですよ。","Sensei ni renraku shita hou ga ii desu yo.","You had better contact the teacher.","ගුරුතුමාට කතා කරන එක හොඳයි."),
  ],
  foot="〜した ほうが いいです",
)

if __name__ == "__main__":
    render(P, "u50_hougaii")
