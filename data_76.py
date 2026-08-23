from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

ASA  = r("朝","あさ")
TAB  = r("食","た")+"べないで"
GAK  = r("学校","がっ こう")
KI   = r("来","き")+"ました"
JISH = r("辞書","じ しょ")
TSUK = r("使","つか")+"わないで"
KOTA = r("答","こた")+"えて"
SAT  = r("砂糖","さ とう")
IRE  = r("入","い")+"れないで"
NOM  = r("飲","の")+"みます"
DEN  = r("電気","でん き")
KES  = r("消","け")+"さないで"
NER  = r("寝","ね")+"ました"
KASA = "かさ"
MOT  = r("持","も")+"たないで"
DE   = r("出","で")+"かけました"
MEG  = r("眼鏡","め がね")
KAK  = r("書","か")+"きました"
FUKU = r("服","ふく")
KI2  = r("着","き")+"た"

P = dict(
  no="76", tag=None,
  title_jp="〜ないで、〜／〜ずに",
  title_ro='〜 naide / 〜 zu ni &nbsp;|&nbsp; without doing 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 නොකර</span>',
  basic=(f"{ASA}ごはんを {TAB}、{GAK}へ {KI}。","Asagohan wo tabenaide, gakkou e kimashita.",
         "I came to school without eating breakfast.","උදේ කෑම නොකා පාසලට ආවා."),
  use=(f'「A しないで B する」＝ ふつうは する Aを <b>しないまま</b> Bを する、と いう {r("意味","い み")}です。'
       f'{r("書","か")}きことばでは「〜ずに」に なります（する → せずに）。',
       '"A naide B" means you do B <b>without</b> doing A, which you normally would. '
       'In writing it becomes <b>~ zu ni</b> (suru → sezu ni).',
       '"A naide B" කියන්නේ සාමාන්‍යයෙන් කරන A <b>නොකර</b> B කරනවා. '
       'ලිවීමේදී <b>~ zu ni</b> (suru → sezu ni).'),
  pattern=[["BLANK",("ないで、","naide",True),("〜します","~ shimasu")],
           f"NOTE:ない{r('形','けい')}＋で：{TAB}　/　{TSUK}　/　{IRE}。"
           f"{r('書','か')}きことば：〜ずに（する → せずに）",
           f"NOTE:にた かたち：「〜<b>たまま</b>」＝ した じょうたいの まま"
           f"（{MEG}を かけた まま ねました）"],
  examples=[
    (f"{ASA}ごはんを {TAB}、{GAK}へ {KI}。","Asagohan wo tabenaide, gakkou e kimashita.","I came to school without eating breakfast.","උදේ කෑම නොකා පාසලට ආවා."),
    (f"{JISH}を {TSUK}、{KOTA} ください。","Jisho wo tsukawanaide, kotaete kudasai.","Please answer without using a dictionary.","ශබ්දකෝෂය පාවිච්චි නොකර උත්තර දෙන්න."),
    (f"{SAT}を {IRE}、コーヒーを {NOM}。","Satou wo irenaide, koohii wo nomimasu.","I drink coffee without sugar.","සීනි නොදා කෝපි බොනවා."),
    (f"{DEN}を {KES}、{NER}。","Denki wo kesanaide, nemashita.","I went to sleep without turning off the light.","ලයිට් නිවන්නේ නැතුව නිදාගත්තා."),
    (f"{KASA}を {MOT}、{DE}。","Kasa wo motanaide, dekakemashita.","I went out without taking an umbrella.","කුඩය අරන් නොගිහින් එළියට ගියා."),
    (f"なにも {r('言','い')}わずに、{r('帰','かえ')}りました。","Nani mo iwazu ni, kaerimashita.","He went home without saying anything.","මොකුත් නොකියා ගෙදර ගියා."),
    (f"{FUKU}を {KI2} まま、ねて しまいました。","Fuku wo kita mama, nete shimaimashita.","I fell asleep with my clothes on.","ඇඳුම් ඇඳගෙනම නිදාගත්තා."),
  ],
  foot="〜ないで、〜／〜ずに",
)

if __name__ == "__main__":
    render(P, "u76_naide")
