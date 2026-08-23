from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

KANJ = r("漢字","かん じ")
KAI  = r("書","か")+"いて"
ICHI = r("一度","いち ど")
NHG  = r("日本語","に ほん ご")
HAN  = r("話","はな")+"して"
KUTS = r("靴","くつ")
HAI  = "はいて"
KII  = r("聞","き")+"いて"
TSUK = r("使","つか")+"って"
JIB  = r("自分","じ ぶん")
KANG = r("考","かんが")+"えて"
MIR  = r("見","み")+"る"
TAM  = r("試","ため")+"す"

P68 = dict(
  no="108", tag=None,
  title_jp="〜して みて（ください）",
  title_ro='〜 shite mite (kudasai) &nbsp;|&nbsp; Try 〜ing &nbsp;|&nbsp; '
           '<span class="si">〜 කරලා බලන්න</span>',
  basic=(f"この {KANJ}を {KAI} みて ください。","Kono kanji wo kaite mite kudasai.",
         "Please try writing this kanji.","මේ කන්ජි අකුර ලියලා බලන්න."),
  use=(f'て{r("形","けい")}に つけて「{TAM}」と いう {r("意味","い み")}に なります。'
       f'シンハラ{r("語","ご")}も「කරලා බලන්න」で、{r("同","おな")}じく「{MIR}」を つかいます。',
       'Add it to the te-form to mean "give it a try". Sinhala does the same thing — '
       '<b>karalā balanna</b> also uses the verb "to look".',
       'te-ආකාරයට දාලා "උත්සාහ කරලා බලන්න" කියන අර්ථය. '
       'සිංහලෙනුත් <b>කරලා බලන්න</b> — "බලනවා" කියන ක්‍රියාවම යොදනවා.'),
  pattern=[["BLANK",("して みて","shite mite",True)],
           ["BLANK",("して みて ください","shite mite kudasai",True)],
           f"NOTE:「みて」は ひらがなで {r('書','か')}きます（「{r('見','み')}て」では ありません）",
           f"NOTE:{JIB}が する とき：〜して みます　/　やった あと：〜して みました"],
  examples=[
    (f"この {KANJ}を {KAI} みて ください。","Kono kanji wo kaite mite kudasai.","Please try writing this kanji.","මේ කන්ජි අකුර ලියලා බලන්න."),
    (f"もう {ICHI} やって みて ください。","Mou ichido yatte mite kudasai.","Please try once more.","තව එක පාරක් කරලා බලන්න."),
    (f"{NHG}で {HAN} みて ください。","Nihongo de hanashite mite kudasai.","Try speaking in Japanese.","ජපන් භාෂාවෙන් කතා කරලා බලන්න."),
    (f"この {KUTS}を {HAI} みて ください。","Kono kutsu wo haite mite kudasai.","Please try these shoes on.","මේ සපත්තු දාලා බලන්න."),
    (f"サマンさんに {KII} みて ください。","Saman-san ni kiite mite kudasai.","Try asking Saman.","සමන්ගෙන් අහලා බලන්න."),
    (f"あたらしい アプリを {TSUK} みて ください。","Atarashii apuri wo tsukatte mite kudasai.","Try using the new app.","අලුත් ඇප් එක පාවිච්චි කරලා බලන්න."),
    (f"まず {JIB}で {KANG} みて ください。","Mazu jibun de kangaete mite kudasai.","First, try thinking about it yourself.","මුලින්ම තනියම හිතලා බලන්න."),
  ],
  foot="〜して みて（ください）",
)

if __name__ == "__main__":
    render(P68, "p108_shitemite")
