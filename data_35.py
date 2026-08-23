from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
SEN  = r("先生","せん せい")
OSHI = r("教","おし")+"えて"
TETS = r("手伝","て つだ")+"って"
NIM  = r("荷物","に もつ")
MOT  = r("持","も")+"って"
KAS  = r("貸","か")+"して"
TSUK = r("作","つく")+"って"
MICH = r("道","みち")
OKU  = r("送","おく")+"って"
KAB  = "かばん"
TOMO = r("友","とも")+"だち"
HAHA = r("母","はは")
KOU  = r("行為","こう い")
NHG_ = r("日本語","に ほん ご")
TETSI= r("手伝","て つだ")+"い"

P = dict(
  no="35", tag=None,
  title_jp="〜て あげます／くれます／もらいます",
  title_ro='te agemasu / kuremasu / moraimasu &nbsp;|&nbsp; doing it for someone &nbsp;|&nbsp; '
           '<span class="si">〜 කරලා දෙනවා</span>',
  basic=(f"{SEN}が {NHG_}を {OSHI} くれました。",
         "Sensei ga nihongo wo oshiete kuremashita.",
         "My teacher taught me Japanese (for me).","ගුරුතුමා මට ජපන් භාෂාව කියලා දුන්නා."),
  use=(f'34は <b>もの</b>、ここは <b>{KOU}</b>の やりとりです。'
       f'て{r("形","けい")}に あげる・くれる・もらう を つけます。',
       'Unit 34 was about giving <b>things</b>; this is about doing <b>actions</b> for someone.',
       '34 කිව්වේ <b>දේවල්</b>; මෙතන <b>ක්‍රියා</b> කරලා දීම.'),
  pattern=[[(f"{W}は","watashi wa"),"BLANK",("て あげます","te agemasu",True)],
           [("〜が","~ ga"),(f"{W}に","watashi ni"),"BLANK",("て くれます","te kuremasu",True)],
           [(f"{W}は","watashi wa"),("〜に","~ ni"),"BLANK",("て もらいます","te moraimasu",True)],
           f"NOTE:くれます＝{r('相手','あい て')}が してくれた（ありがたい）　/　"
           f"もらいます＝{W}が たのんで して もらった",
           f"NOTE:{r('目上','め うえ')}の {r('人','ひと')}に「〜て あげます」は しつれいです。"
           f"「お{TETSI}しましょうか」と {r('言','い')}いましょう"],
  examples=[
    (f"{SEN}が {NHG_}を {OSHI} くれました。","Sensei ga nihongo wo oshiete kuremashita.","My teacher taught me Japanese.","ගුරුතුමා මට ජපන් භාෂාව කියලා දුන්නා."),
    (f"サマンさんが {NIM}を {MOT} くれました。","Saman-san ga nimotsu wo motte kuremashita.","Saman carried my bag for me.","සමන් මගේ බඩු අරන් ගියා."),
    (f"{W}は {TOMO}に ペンを {KAS} あげました。","Watashi wa tomodachi ni pen wo kashite agemashita.","I lent my friend a pen.","මම යාළුවාට පෑනක් දුන්නා."),
    (f"{HAHA}に カレーを {TSUK} もらいました。","Haha ni karee wo tsukutte moraimashita.","My mother made curry for me.","අම්මා මට කරි උයලා දුන්නා."),
    (f"サマンさんに {MICH}を {OSHI} もらいました。","Saman-san ni michi wo oshiete moraimashita.","Saman showed me the way.","සමන් මට පාර කියලා දුන්නා."),
    (f"{TOMO}が {KAB}を {OKU} くれました。","Tomodachi ga kaban wo okutte kuremashita.","My friend sent me a bag.","යාළුවා මට බෑග් එකක් එවලා දුන්නා."),
    (f"{W}が {TETS} あげましょうか。","Watashi ga tetsudatte agemashou ka.","Shall I help you?","මම උදව් කරන්නද?"),
  ],
  foot="〜て あげます／くれます／もらいます",
)

if __name__ == "__main__":
    render(P, "u35_teageru")
