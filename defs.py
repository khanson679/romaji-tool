# -*- coding: utf-8 -*-

import re

from util import *

"""
defs.py

Definitions for mapping between kana/romaji and an internal representation.
"""

#----------------------------------------------------------------------------
# Lemmas
#
# These are unambiguous representations of one or more kana,
#   essentially wapuro-style Kunrei-shiki.
#
# Final data structure is a list of strings.
#----------------------------------------------------------------------------

# lemmas used in native Japanese words
# First section includes base moras, dakuon, handakuon,and youon
# Section section adds dakuon
# dya/dyu/dyo are omitted due to lack of standard use
LEMMA_TAB_BASIC = """\
a i u e o
ka ki ku ke ko kya kyu kyo
ga gi gu ge go gya gyu gyo
sa si su se so sya syu syo
za zi zu ze zo zya zyu zyo
ta ti tu te to tya tyu tyo
da di du de do
na ni nu ne no nya nyu nyo
ha hi hu he ho hya hyu hyo
ba bi bu be bo bya byu byo
pa pi pu pe po pya pyu pyo
ma mi mu me mo mya myu myo
ya    yu    yo
ra ri ru re ro rya ryu ryo
wa          wo
n'

kka kki kku kke kko kkya kkyu kkyo
ssa ssi ssu sse sso ssya ssyu ssyo
tta tti ttu tte tto ttya ttyu ttyo
ppa ppi ppu ppe ppo ppya ppyu ppyo
"""

# lemmas for borrowed words, archaic spellings, etc.
# sections are:
#   -added moras
#   -dakuon for voiced moras
#   -dakuon for added moras
#   -chouon sign
LEMMA_TAB_EXTENDED = """\
    uxi       uxe uxo
va  vi   vu   ve  vo   vya vyu vyo
              sye
              zye
    texi toxu
              tye
tsa tsi       tse tso           
    dexi doxu          dya dyu dyo
fa  fi        fe  fo   fya fyu fyo
              ye
    wi        we

gga ggi ggu gge ggo ggya ggyu ggyo
zza zzi zzu zze zzo zzya zzyu zzyo
dda ddi ddu dde ddo ddya ddyu ddyo
hha hhi hhu hhe hho hhya hhyu hhyo
bba bbi bbu bbe bbo bbya bbyu bbyo

                 ssye
                 zzye
     ttexi ttoxu
                 ttye
ttsa ttsi        ttse ttso           
     ddexi ddoxu            
ffa  ffi         ffe  ffo ffya ffyu ffyo

-
"""

SOKUON_CONSONANTS = "kgsztdhfbp"

# use to handle non-standard use of small kana
WAPURO_SMALL_KANA_PRE =  "xtu"
WAPURO_SMALL_KANA_POST = "xa xi xu xe xo   xya xyu xyo   xwa"


#----------------------------------------------------------------------------
# Kana tables
#
# Used to map kana <-> lemmas
# Derived from python-romkan, itself based on KAKASI
#   <http://kakasi.namazu.org/>
#----------------------------------------------------------------------------

HIRAGANA_TAB = """\
あ a   い i   う u   え e   お o             
か ka  き ki  く ku  け ke  こ ko  きゃ kya  きゅ kyu  きょ kyo
が ga  ぎ gi  ぐ gu  げ ge  ご go  ぎゃ gya  ぎゅ gyu  ぎょ gyo
さ sa  し si  す su  せ se  そ so  しゃ sya  しゅ syu  しょ syo
ざ za  じ zi  ず zu  ぜ ze  ぞ zo  じゃ zya  じゅ zyu  じょ zyo
た ta  ち ti  つ tu  て te  と to  ちゃ tya  ちゅ tyu  ちょ tyo
だ da  ぢ di  づ du  で de  ど do
な na  に ni  ぬ nu  ね ne  の no  にゃ nya  にゅ nyu  にょ nyo
は ha  ひ hi  ふ hu  へ he  ほ ho  ひゃ hya  ひゅ hyu  ひょ hyo
ば ba  び bi  ぶ bu  べ be  ぼ bo  びゃ bya  びゅ byu  びょ byo
ぱ pa  ぴ pi  ぷ pu  ぺ pe  ぽ po  ぴゃ pya  ぴゅ pyu  ぴょ pyo
ま ma  み mi  む mu  め me  も mo  みゃ mya  みゅ myu  みょ myo
や ya         ゆ yu        よ yo
ら ra  り ri  る ru  れ re  ろ ro  りゃ rya  りゆ ryu  りょ ryo
わ wa                      を wo
ん n'

         うぃ uxi             うぇ uxe  うぉ uxo
ゔぁ va   ゔぃ vi    ゔ vu     ゔぇ ve   ゔぉ vo
                             しぇ sye
                             じぇ zye
         てぃ texi  とぅ toxu
                             ちぇ tye
つぁ tsa  つぃ tsi   つぇ tse            つぉ tso     
         でぃ dexi  どぅ doxu                    ぢゃ dya  ぢゅ dyu  ぢょ dyo
ふぁ fa   ふぃ fi              ふぇ fe  ふぉ fo    ふゃ fya  ふゅ fyu  ふょ fyo
                              いぇ ye
         ゐ wi          ゑ we

ー -
"""

HIRAGANA_SOKUON = "っ"
HIRAGANA_SMALL_POST = "ぁ ぃ ぅ ぇ ぉ ゃ ゅ ょ ゎ"


# KATAKANA_TAB = """ァ  xa ア  a  ィ  xi イ  i  ゥ  xu
# ウ  u  ヴ  vu ヴァ va ヴィ vi ヴェ ve
# ヴォ vo ェ  xe エ  e  ォ  xo オ  o 

# カ  ka ガ  ga キ  ki キャ kya   キュ kyu 
# キョ kyo   ギ  gi ギャ gya   ギュ gyu   ギョ gyo 
# ク  ku グ  gu ケ  ke ゲ  ge コ  ko
# ゴ  go 

# サ  sa ザ  za シ  si シャ sya   シュ syu 
# ショ syo   シェ  sye
# ジ  zi ジャ zya   ジュ zyu   ジョ zyo 
# ス  su ズ  zu セ  se ゼ  ze ソ  so
# ゾ  zo 

# タ  ta ダ  da チ  ti チャ tya   チュ tyu 
# チョ tyo   ヂ  di ヂャ dya   ヂュ dyu   ヂョ dyo 
# ティ  ti

# ッ  xtu 
# ッヴ vvu   ッヴァ   vva   ッヴィ   vvi 
# ッヴェ   vve   ッヴォ   vvo 
# ッカ kka   ッガ gga   ッキ kki   ッキャ   kkya 
# ッキュ   kkyu  ッキョ   kkyo  ッギ ggi   ッギャ   ggya 
# ッギュ   ggyu  ッギョ   ggyo  ック kku   ッグ ggu 
# ッケ kke   ッゲ gge   ッコ kko   ッゴ ggo   ッサ ssa 
# ッザ zza   ッシ ssi   ッシャ   ssya 
# ッシュ   ssyu  ッショ   ssyo  ッシェ   ssye
# ッジ zzi   ッジャ   zzya  ッジュ   zzyu  ッジョ   zzyo
# ッス ssu   ッズ zzu   ッセ sse   ッゼ zze   ッソ sso 
# ッゾ zzo   ッタ tta   ッダ dda   ッチ tti   ッティ tti
# ッチャ   ttya  ッチュ   ttyu  ッチョ   ttyo  ッヂ ddi 
# ッヂャ   ddya  ッヂュ   ddyu  ッヂョ   ddyo  ッツ ttu 
# ッヅ ddu   ッテ tte   ッデ dde   ット tto   ッド ddo 
# ッドゥ ddu
# ッハ hha   ッバ bba   ッパ ppa   ッヒ hhi 
# ッヒャ   hhya  ッヒュ   hhyu  ッヒョ   hhyo  ッビ bbi 
# ッビャ   bbya  ッビュ   bbyu  ッビョ   bbyo  ッピ ppi 
# ッピャ   ppya  ッピュ   ppyu  ッピョ   ppyo  ッフ hhu   ッフュ ffu
# ッファ   ffa   ッフィ   ffi   ッフェ   ffe   ッフォ   ffo 
# ッブ bbu   ップ ppu   ッヘ hhe   ッベ bbe   ッペ  ppe
# ッホ hho   ッボ bbo   ッポ ppo   ッヤ yya   ッユ yyu 
# ッヨ yyo   ッラ rra   ッリ rri   ッリャ   rrya 
# ッリュ   rryu  ッリョ   rryo  ッル rru   ッレ rre 
# ッロ rro 

# ツ  tu ヅ  du テ  te デ  de ト  to
# ド  do ドゥ  du

# ナ  na ニ  ni ニャ nya   ニュ nyu   ニョ nyo 
# ヌ  nu ネ  ne ノ  no 

# ハ  ha バ  ba パ  pa ヒ  hi ヒャ hya 
# ヒュ hyu   ヒョ hyo   ビ  bi ビャ bya   ビュ byu 
# ビョ byo   ピ  pi ピャ pya   ピュ pyu   ピョ pyo 
# フ  hu ファ fa フィ fi フェ fe フォ fo
# フュ  fu
# ブ  bu プ  pu ヘ  he ベ  be ペ  pe
# ホ  ho ボ  bo ポ  po 

# マ  ma ミ  mi ミャ mya   ミュ myu   ミョ myo 
# ム  mu メ  me モ  mo 

# ャ  xya   ヤ  ya ュ  xyu   ユ  yu ョ  xyo
# ヨ  yo

# ラ  ra リ  ri リャ rya   リュ ryu   リョ ryo 
# ル  ru レ  re ロ  ro 

# ヮ  xwa   ワ  wa ウィ  wi ヰ wi ヱ  we ウェ we
# ヲ  wo ウォ  wo ン n 

# ン   n'
# ディ  dyi
# ー   -
# チェ  tye
# ッチェ   ttye
# ジェ zye
# """


#
# Tests
#

# if __name__ == "__main__":
#     print list(groups(re.split('\s', "a 1 b 2 cc 33\nddd 444\teee 555")))