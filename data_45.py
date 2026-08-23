from build import render

def r(k, y): return f"<ruby>{k}<rt>{y}</rt></ruby>"

W    = r("私","わたし")
TOK  = r("得意","とく い")
NIG  = r("苦手","にが て")
UTA  = r("歌","うた")
ANI  = r("兄","あに")
SUG  = r("数学","すう がく")
SAM  = r("寒","さむ")+"い"
TEN  = r("天気","てん き")
OTO  = r("弟","おとうと")
ASA  = r("朝","あさ")
KANJ = r("漢字","かん じ")
JOZ  = r("上手","じょう ず")
SUKI = r("好","す")+"き"
HITO = r("人","ひと")

P56 = dict(
  no="45", tag=None,
  title_jp=f"〜が {TOK}です　/　〜が {NIG}です",
  title_ro='〜 ga tokui / nigate desu &nbsp;|&nbsp; good at / not good at 〜 &nbsp;|&nbsp; '
           '<span class="si">දක්ෂයි / දුර්වලයි</span>',
  basic=(f"{W}は クリケットが {TOK}です。","Watashi wa kuriketto ga tokui desu.",
         "I'm good at cricket.","මම ක්‍රිකට් වලට දක්ෂයි."),
  use=(f'{TOK}＝じょうずに できる、{NIG}＝うまく できない・あまり {SUKI}じゃない。'
       f'42の「{SUKI}です」は きもちで、こちらは {r("力","ちから")}の {r("話","はなし")}です。',
       '<b>tokui</b> = you can do it well; <b>nigate</b> = you can\'t do it well or don\'t like it. '
       'Pattern 42 <b>suki</b> is about feeling; this is about ability.',
       '<b>tokui</b> = හොඳට පුළුවන්; <b>nigate</b> = හොඳට බැහැ / එච්චර කැමති නැහැ. '
       '42 හි <b>suki</b> කැමැත්ත ගැන; මේක හැකියාව ගැන.'),
  pattern=[[("〜は","~ wa"),"BLANK",("が","ga",True),(f"{TOK}です","tokui desu",True)],
           [("〜は","~ wa"),"BLANK",("が","ga",True),(f"{NIG}です","nigate desu",True)],
           f"NOTE:{r('自分','じ ぶん')}には「{TOK}です」、ほかの {HITO}を ほめる ときは「{JOZ}ですね」",
           f"NOTE:{NIG}です は「きらいです」より やわらかくて ていねいです"],
  examples=[
    (f"{W}は クリケットが {TOK}です。","Watashi wa kuriketto ga tokui desu.","I'm good at cricket.","මම ක්‍රිකට් වලට දක්ෂයි."),
    (f"サマンさんは {UTA}が {TOK}です。","Saman-san wa uta ga tokui desu.","Saman is good at singing.","සමන් සිංදු කියන්න දක්ෂයි."),
    (f"{ANI}は パソコンが {TOK}です。","Ani wa pasokon ga tokui desu.","My older brother is good with computers.","අයියා පරිගණක වලට දක්ෂයි."),
    (f"{W}は {SUG}が {NIG}です。","Watashi wa suugaku ga nigate desu.","I'm not good at maths.","මම ගණිතයට දුර්වලයි."),
    (f"サマンさんは {SAM} {TEN}が {NIG}です。","Saman-san wa samui tenki ga nigate desu.","Saman doesn't do well in cold weather.","සමන්ට සීතල කාලගුණය අමාරුයි."),
    (f"{OTO}は {ASA}が {NIG}です。","Otouto wa asa ga nigate desu.","My little brother is not a morning person.","මල්ලිට උදේ නැගිටින්න අමාරුයි."),
    (f"{KANJ}は {NIG}ですが、ひらがなは {TOK}です。","Kanji wa nigate desu ga, hiragana wa tokui desu.","I'm weak at kanji, but good at hiragana.","කන්ජි අමාරුයි, ඒත් හිරගනා හොඳට පුළුවන්."),
  ],
  foot="〜が 得意です / 〜が 苦手です",
)

if __name__ == "__main__":
    render(P56, "p45_tokui_nigate")
