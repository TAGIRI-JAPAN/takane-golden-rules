from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

MON  = r("問題","もん だい")
MUZU = "むずかしくないです"
SHIK = r("試験","し けん")
TAIH = r("大変","たい へん")
KAB  = "かばん"
TAKA = r("高","たか")+"くないです"
GAK  = r("学校","がっ こう")
TOO  = r("遠","とお")+"くないです"
KYO  = r("今日","きょう")
ATSU = r("暑","あつ")+"くないです"
KARE = "カレー"
HEYA = r("部屋","へ や")
HIRO = r("広","ひろ")+"くないです"
YOS  = r("予想","よ そう")

P49 = dict(
  no="118", tag=None,
  title_jp="それほど 〜ないです",
  title_ro='sorehodo 〜 nai desu &nbsp;|&nbsp; not as 〜 as that &nbsp;|&nbsp; '
           '<span class="si">හිතුවා තරම් 〜 නැහැ</span>',
  basic=(f"この {MON}は それほど {MUZU}。","Kono mondai wa sorehodo muzukashikunai desu.",
         "This question isn't as difficult as you think.","මේ ප්‍රශ්නය හිතුවා තරම් අමාරු නැහැ."),
  use=(f'117の「あまり」は ただ {r("少","すく")}ないですが、「それほど」は {YOS}と くらべて '
       f'「{r("思","おも")}った ほどでは ない」と{r("言","い")}う ときに つかいます。',
       'Unlike <b>amari</b> (117), which just means "not much", <b>sorehodo</b> means '
       '"not as much as you (or I) expected".',
       '117 හි <b>amari</b> කියන්නේ "එච්චර නැහැ" විතරයි; <b>sorehodo</b> කියන්නේ '
       '"හිතුවා තරම් නැහැ" — බලාපොරොත්තුව එක්ක සසඳනවා.'),
  pattern=[[("〜は","~ wa"),("それほど","sorehodo",True),"BLANK",("ないです","nai desu",True)],
           f"NOTE:あまり（117）＝ ただ {r('少','すく')}ない　/　それほど（118）＝ {r('思','おも')}った ほどでは ない",
           f"NOTE:へんじに よく つかいます：「むずかしいでしょう？」「いえ、それほど {MUZU}。」"],
  examples=[
    (f"この {MON}は それほど {MUZU}。","Kono mondai wa sorehodo muzukashikunai desu.","This question isn't as difficult as you think.","මේ ප්‍රශ්නය හිතුවා තරම් අමාරු නැහැ."),
    (f"{SHIK}は それほど {TAIH}じゃなかったです。","Shiken wa sorehodo taihen ja nakatta desu.","The exam wasn't as tough as I expected.","විභාගය හිතුවා තරම් අමාරු වුණේ නැහැ."),
    (f"この {KAB}は それほど {TAKA}。","Kono kaban wa sorehodo takakunai desu.","This bag isn't that expensive.","මේ බෑග් එක හිතුවා තරම් ගණන් නැහැ."),
    (f"{GAK}は ここから それほど {TOO}。","Gakkou wa koko kara sorehodo tookunai desu.","The school isn't that far from here.","පාසල මෙතනින් හිතුවා තරම් දුර නැහැ."),
    (f"{KYO}は それほど {ATSU}。","Kyou wa sorehodo atsukunai desu.","It isn't as hot as expected today.","අද හිතුවා තරම් රස්නෙ නැහැ."),
    (f"この {KARE}は それほど からくないです。","Kono karee wa sorehodo karakunai desu.","This curry isn't as spicy as expected.","මේ කරිය හිතුවා තරම් සැර නැහැ."),
    (f"この {HEYA}は それほど {HIRO}。","Kono heya wa sorehodo hirokunai desu.","This room isn't as big as expected.","මේ කාමරය හිතුවා තරම් ලොකු නැහැ."),
  ],
  foot="それほど 〜ないです",
)

if __name__ == "__main__":
    render(P49, "p118_sorehodo")
