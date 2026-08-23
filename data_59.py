from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

SOTO = r("外","そと")
AME  = r("雨","あめ")
KITA = r("来","き")+"た"
KYOU = r("教室","きょう しつ")
KARE = "カレー"
SUKO = r("少","すこ")+"し"
SEN  = r("先生","せん せい")
MISE = r("店","みせ")
KYO  = r("今日","きょう")
HITO = r("人","ひと")
ATAR = r("新","あたら")+"しい"
ASHI = r("明日","あ した")
MIM  = r("見","み")+"て"
KII  = r("聞","き")+"いて"

P39 = dict(
  no="59", tag=None,
  title_jp="〜のようです〔〜のようだ〕",
  title_ro='〜 no you desu &nbsp;|&nbsp; It looks like 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වගේ පේනවා</span>',
  basic=(f"{SOTO}は {AME}のようです。","Soto wa ame no you desu.",
         "It looks like it's raining outside.","එළියේ වහිනවා වගේ."),
  use=(f'{r("自分","じ ぶん")}が {MIM}・{KII} かんじた ことから すいそくする ときに つかいます。'
       f'めいしには「の」が {r("入","はい")}ります。',
       'Use it to guess from what you yourself see, hear or feel. '
       'After a noun you need <b>no</b>.',
       'තමන් දකින, අහන, දැනෙන දෙයින් අනුමාන කරන්න. '
       'නාම පදයකට පස්සේ <b>no</b> දාන්න.'),
  pattern=[[("〜は","~ wa"),"BLANK",("のようです","no you desu",True)],
           [("〜は","~ wa"),"BLANK",("するようです","suru you desu",True)],
           [("〜は","~ wa"),"BLANK",("したようです","shita you desu",True)],
           f"NOTE:{ASHI}は {AME}だそうです（57＝{KII}）　/　{AME}らしいです（58＝{KII}＋すいそく）　/　"
           f"{SOTO}は {AME}のようです（59＝{MIM} すいそく）"],
  examples=[
    (f"{SOTO}は {AME}のようです。","Soto wa ame no you desu.","It looks like it's raining outside.","එළියේ වහිනවා වගේ."),
    (f"だれか {KITA}ようです。","Dareka kita you desu.","It seems someone has come.","කවුරු හරි ඇවිත් වගේ."),
    (f"サマンさんは まだ {KYOU}に いるようです。","Saman-san wa mada kyoushitsu ni iru you desu.","It seems Saman is still in the classroom.","සමන් තාම පන්ති කාමරයේ ඉන්නවා වගේ."),
    (f"この {KARE}は {SUKO} からいようです。","Kono karee wa sukoshi karai you desu.","This curry seems a little spicy.","මේ කරිය ටිකක් සැරයි වගේ."),
    (f"{SEN}は いそがしいようです。","Sensei wa isogashii you desu.","The teacher seems busy.","ගුරුතුමා කාර්යබහුලයි වගේ."),
    (f"この {MISE}は {KYO} やって いないようです。","Kono mise wa kyou yatte inai you desu.","This shop doesn't seem to be open today.","මේ කඩේ අද වහලා වගේ."),
    (f"あの {HITO}は {ATAR} {SEN}のようです。","Ano hito wa atarashii sensei no you desu.","That person seems to be the new teacher.","අර කෙනා අලුත් ගුරුතුමා වගේ."),
  ],
  foot="〜のようです",
)

if __name__ == "__main__":
    render(P39, "p59_noyoudesu")
