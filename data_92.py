from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

DOA  = "ドア"
AKI  = r("開","あ")+"きます"
AKE  = r("開","あ")+"けます"
DEN  = r("電気","でん き")
TSUK = "つきます"
TSUKE= "つけます"
MAD  = r("窓","まど")
SHIM = r("閉","し")+"まります"
SHIME= r("閉","し")+"めます"
KURU = r("車","くるま")
TOM  = r("止","と")+"まります"
TOME = r("止","と")+"めます"
KOD  = r("子","こ")+"ども"
OKI  = r("起","お")+"きます"
OKO  = r("起","お")+"こします"
HAJI = r("始","はじ")+"まります"
HAJM = r("始","はじ")+"めます"
JUG  = r("授業","じゅ ぎょう")
JITA = r("自動詞","じ どう し")
TADO = r("他動詞","た どう し")
KOWA = "こわれます"
KOWS = "こわします"

P = dict(
  no="92", tag=None,
  title_jp="自動詞・他動詞",
  title_ro='intransitive &amp; transitive verbs &nbsp;|&nbsp; it opens / I open it &nbsp;|&nbsp; '
           '<span class="si">ඉබේ වෙනවා / කෙනෙක් කරනවා</span>',
  basic=(f"{DOA}が {AKI}。　/　{DOA}を {AKE}。","Doa ga akimasu. / Doa wo akemasu.",
         "The door opens. / I open the door.","දොර ඇරෙනවා. / මම දොර අරිනවා."),
  use=(f'日本語には <b>{r("同","おな")}じ {r("意味","い み")}で かたちが ちがう どうし</b>が ペアで あります。'
       f'<b>{JITA}</b>は「〜が」＝ひとりでに おこる、'
       f'<b>{TADO}</b>は「〜を」＝{r("人","ひと")}が する。助詞で 見分けます（20）。',
       'Japanese has pairs of verbs with the same meaning but different forms. '
       'The <b>intransitive</b> takes <b>ga</b> (it happens by itself); the '
       '<b>transitive</b> takes <b>wo</b> (someone does it). Tell them apart by the particle.',
       'ජපන් භාෂාවේ එකම අර්ථය ඇති, හැඩය වෙනස් ක්‍රියා යුගල තියෙනවා. '
       '<b>අකර්මක</b> එකට <b>ga</b> (ඉබේ වෙනවා); <b>සකර්මක</b> එකට <b>wo</b> (කෙනෙක් කරනවා).'),
  pattern=[[("〜が","~ ga"),"BLANK",(f"{JITA}","jidoushi",True)],
           [("〜を","~ wo"),"BLANK",(f"{TADO}","tadoushi",True)],
           f"NOTE:{AKI}／{AKE}　{TSUK}／{TSUKE}　{SHIM}／{SHIME}　{TOM}／{TOME}　"
           f"{HAJI}／{HAJM}　{KOWA}／{KOWS}",
           f"NOTE:94「〜て あります」は かならず <b>{TADO}</b>、"
           f"16「〜て います」（じょうたい）は <b>{JITA}</b>と つかいます"],
  examples=[
    (f"{DOA}が {AKI}。","Doa ga akimasu.","The door opens.","දොර ඇරෙනවා."),
    (f"サマンさんが {DOA}を {AKE}。","Saman-san ga doa wo akemasu.","Saman opens the door.","සමන් දොර අරිනවා."),
    (f"{DEN}が {TSUK}。","Denki ga tsukimashita.","The light came on.","ලයිට් එක පත්තු වුණා."),
    (f"{DEN}を {TSUKE}。","Denki wo tsukemashita.","I turned the light on.","මම ලයිට් එක පත්තු කළා."),
    (f"{KURU}が {TOM}。","Kuruma ga tomarimashita.","The car stopped.","කාරය නැවතුණා."),
    (f"ここに {KURU}を {TOME}ないで ください。","Koko ni kuruma wo tomenaide kudasai.","Please don't park your car here.","මෙතන කාරය නවත්තන්න එපා."),
    (f"{JUG}が {HAJI}。","Jugyou ga hajimarimashita.","The class has started.","පන්තිය පටන් ගත්තා."),
  ],
  foot="自動詞・他動詞",
)

if __name__ == "__main__":
    render(P, "u92_jitadoushi")
