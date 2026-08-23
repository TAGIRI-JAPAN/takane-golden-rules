from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
NAKA = r("中","なか")
SUKI = r("好","す")+"き"
NHG  = r("日本語","に ほん ご")
JOZ  = r("上手","じょう ず")
MISE = r("店","みせ")
YASU = r("安","やす")+"いです"
ATSU = r("暑","あつ")+"いです"
NEN  = r("年","ねん")
KAZ  = r("家族","か ぞく")
CHIC = r("父","ちち")
HAYA = r("早","はや")+"く"
OKI  = r("起","お")+"きます"
TAIH = r("大変","たい へん")
MACH = r("町","まち")

P45 = dict(
  no="51", tag=None,
  title_jp="〜が いちばん 〜です",
  title_ro='〜 ga ichiban 〜 desu &nbsp;|&nbsp; 〜 is the most 〜 &nbsp;|&nbsp; '
           '<span class="si">〜 ම වැඩියි</span>',
  basic=(f"くだものの {NAKA}で マンゴーが いちばん {SUKI}です。",
         "Kudamono no naka de mangoo ga ichiban suki desu.",
         "Of all fruit I like mango best.","පලතුරු අතරින් මම අඹ වලට වැඩියෙන්ම කැමතියි."),
  use=(f'3つ{r("以上","い じょう")}を くらべて、1つを えらぶ ときの ことばです。'
       f'48の「より」は 2つ、51の「いちばん」は 3つ{r("以上","い じょう")}です。',
       'Use it to pick one out of three or more. <b>yori</b> (48) compares two things; '
       '<b>ichiban</b> compares three or more.',
       'තුනකට වඩා අතරින් එකක් තෝරද්දී. 48 හි <b>yori</b> දෙකක් සසඳනවා; '
       '<b>ichiban</b> තුනකට වඩා.'),
  pattern=[[(f"〜の {NAKA}で","~ no naka de"),"BLANK",("が いちばん","ga ichiban",True),
            ("〜です","~ desu")],
           f"NOTE:シンハラ{r('語','ご')}は ことばの さいごに「ම」を つけますが、"
           f"日本語は {r('前','まえ')}に「いちばん」を おきます",
           f"NOTE:しつもん：{r('何','なに')}が／どれが／だれが／どこが／いつが いちばん 〜ですか"],
  examples=[
    (f"くだものの {NAKA}で マンゴーが いちばん {SUKI}です。","Kudamono no naka de mangoo ga ichiban suki desu.","Of all fruit I like mango best.","පලතුරු අතරින් මම අඹ වලට වැඩියෙන්ම කැමතියි."),
    (f"クラスで サマンさんが いちばん {NHG}が {JOZ}です。","Kurasu de Saman-san ga ichiban nihongo ga jouzu desu.","Saman is the best at Japanese in the class.","පන්තියේ සමන් ජපන් භාෂාවට වැඩියෙන්ම දක්ෂයි."),
    (f"この {MACH}で この {MISE}が いちばん {YASU}。","Kono machi de kono mise ga ichiban yasui desu.","This shop is the cheapest in this town.","මේ නගරයේ මේ කඩේ ලාබම."),
    (f"1{NEN}で 8{r('月','がつ')}が いちばん {ATSU}。","Ichinen de hachigatsu ga ichiban atsui desu.","August is the hottest month of the year.","අවුරුද්දේ අගෝස්තු වැඩියෙන්ම රස්නෙයි."),
    (f"スポーツの {NAKA}で クリケットが いちばん おもしろいです。","Supootsu no naka de kuriketto ga ichiban omoshiroi desu.","Cricket is the most interesting sport.","ක්‍රීඩා අතරින් ක්‍රිකට් වැඩියෙන්ම රසවත්."),
    (f"{r('何','なに')}が いちばん {TAIH}ですか。","Nani ga ichiban taihen desu ka.","What is the hardest part?","වැඩිම අමාරුව මොකක්ද?"),
    (f"{KAZ}の {NAKA}で {CHIC}が いちばん {HAYA} {OKI}。","Kazoku no naka de chichi ga ichiban hayaku okimasu.","In my family my father gets up earliest.","පවුලේ තාත්තා තමයි කලින්ම නැගිටින්නේ."),
  ],
  foot="〜が いちばん 〜です",
)

if __name__ == "__main__":
    render(P45, "u51_ichiban")
