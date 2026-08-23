from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KAB  = "かばん"
OMO  = r("重","おも")+"すぎます"
NAGA = r("長","なが")+"すぎます"
KUTS = r("靴","くつ")
TAKA = r("高","たか")+"すぎます"
MON  = r("問題","もん だい")
MUZU = "むずかしすぎます"
KYOU = r("今日","きょう")
ATSU = r("暑","あつ")+"すぎます"
HAYA = r("早","はや")+"く"
HANA = r("話","はな")+"しすぎます"
KINO = r("昨日","きのう")
NOMI = r("飲","の")+"みすぎました"
TAKI = r("高","たか")+"い"

P42 = dict(
  no="52", tag=None,
  title_jp="〜すぎます",
  title_ro='〜 sugimasu &nbsp;|&nbsp; too 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 වැඩියි</span>',
  basic=(f"この {KAB}は {OMO}。","Kono kaban wa omosugimasu.",
         "This bag is too heavy.","මේ බෑග් එක බර වැඩියි."),
  use=(f'「ちょうど いい」を こえて {r("困","こま")}る ときに つかいます。'
       f'シンハラ{r("語","ご")}の「වැඩියි」と{r("同","おな")}じで、いつも わるい{r("気持","き も")}ちです。',
       'Use it when something goes past "just right" and becomes a problem. '
       'Like the Sinhala <b>vædiyi</b>, it always sounds negative.',
       '"හරියටම හොඳයි" කියන එක පනිද්දී පාවිච්චි කරන්න. '
       'සිංහල <b>වැඩියි</b> වගේම හැමවිටම නරක අර්ථයක්.'),
  pattern=[[("〜は","~ wa"),"BLANK",("すぎます","sugimasu",True)],
           [("〜は","~ wa"),"BLANK",("すぎました","sugimashita",True)],
           f"NOTE:{TAKI} → {r('高','たか')}すぎる　/　しずかな → しずかすぎる　/　"
           f"{r('飲','の')}みます → {r('飲','の')}みすぎる",
           f"NOTE:とくべつ：いい → よすぎる　/　ない → なさすぎる"],
  examples=[
    (f"この {KAB}は {OMO}。","Kono kaban wa omosugimasu.","This bag is too heavy.","මේ බෑග් එක බර වැඩියි."),
    (f"この シャツは {NAGA}。","Kono shatsu wa nagasugimasu.","This shirt is too long.","මේ කමිසය දිග වැඩියි."),
    (f"その {KUTS}は {TAKA}。","Sono kutsu wa takasugimasu.","Those shoes are too expensive.","ඒ සපත්තු ගණන් වැඩියි."),
    (f"この {MON}は {MUZU}。","Kono mondai wa muzukashisugimasu.","This question is too difficult.","මේ ප්‍රශ්නය අමාරු වැඩියි."),
    (f"{KYOU}は {ATSU}。","Kyou wa atsusugimasu.","It is too hot today.","අද රස්නෙ වැඩියි."),
    (f"サマンさんは {HAYA} {HANA}。","Saman-san wa hayaku hanashisugimasu.","Saman speaks too fast.","සමන් ඉක්මනට කතා කරනවා වැඩියි."),
    (f"{KINO} コーヒーを {NOMI}。","Kinou koohii wo nomisugimashita.","I drank too much coffee yesterday.","ඊයේ මම කෝපි වැඩිපුර බිව්වා."),
  ],
  foot="〜すぎます",
)

if __name__ == "__main__":
    render(P42, "p52_sugimasu")
