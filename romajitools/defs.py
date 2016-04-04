#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
defs.py

Definitions for mapping between kana/romaji and an internal representation.
"""

#----------------------------------------------------------------------------
# Lemmas
#
# These are unambiguous representations of one or more kana,
#   essentially wapuro-style Kunrei-shiki.
# Implementated as space-separated lists, which can be easily parsed
#   into lists of strings.
#----------------------------------------------------------------------------

# lemmas used in native Japanese words
# Includes base moras, handakuon,and youon
# dya/dyu/dyo are omitted due to lack of standard use
LEMMA_TAB_BASIC = """\
A  I  U  E  O
KA KI KU KE KO KYA KYU KYO
GA GI GU GE GO GYA GYU GYO
SA SI SU SE SO SYA SYU SYO
ZA ZI ZU ZE ZO ZYA ZYU ZYO
TA TI TU TE TO TYA TYU TYO
DA DI DU DE DO
NA NI NU NE NO NYA NYU NYO
HA HI HU HE HO HYA HYU HYO
BA BI BU BE BO BYA BYU BYO
PA PI PU PE PO PYA PYU PYO
MA MI MU ME MO MYA MYU MYO
YA    YU    YO
RA RI RU RE RO RYA RYU RYO
WA          WO
N'
"""

# lemmas for borrowed words, archaic spellings, etc.
LEMMA_TAB_EXTENDED = """\
    UXI       UXE UXO
VA  VI   VU   VE  VO
              SYE
              ZYE
    TEXI TOXU
              TYE
TSA TSI       TSE TSO
    DEXI DOXU
FA  FI        FE  FO
              YE
    WI        WE
"""

# lemmas for Kana that are rarely used, for completeness
LEMMA_TAB_EXTRA = """\
UXA    UXU
               VYA VYU VYO
               DYA DYU DYO
               FYA FYU FYO
    YI
"""

# use to handle non-standard use of small kana
LEMMA_TAB_SMALL_KANA_POST = "XA XI XU XE XO   XYA XYU XYO   XWA"

# special lemmas
LEMMA_SOKUON = "Q"
LEMMA_CHOUON = "-"


#----------------------------------------------------------------------------
# Support data
#----------------------------------------------------------------------------

SOKUON_CONSONANTS = "KGSZTDHFBP"


#----------------------------------------------------------------------------
# Romaji conversion tables
#----------------------------------------------------------------------------

WAPURO_TAB = """\
kk QK,
gg QG,
ss QS,
zz QZ,
tt QT,
dd QD,
hh QH,
ff QF,
bb QB,
pp QP
"""


#----------------------------------------------------------------------------
# Kana conversion tables
#
# Used to map kana <-> lemmas
# Derived from python-romkan, itself based on KAKASI
#   <http://kakasi.namazu.org/>
#----------------------------------------------------------------------------

HIRAGANA_TAB = """\
あ A,  い I,  う U,  え E,  お O,
か KA, き KI, く KU, け KE, こ KO, きゃ KYA, きゅ KYU, きょ KYO,
が GA, ぎ GI, ぐ GU, げ GE, ご GO, ぎゃ GYA, ぎゅ GYU, ぎょ GYO,
さ SA, し SI, す SU, せ SE, そ SO, しゃ SYA, しゅ SYU, しょ SYO,
ざ ZA, じ ZI, ず ZU, ぜ ZE, ぞ ZO, じゃ ZYA, じゅ ZYU, じょ ZYO,
た TA, ち TI, つ TU, て TE, と TO, ちゃ TYA, ちゅ TYU, ちょ TYO,
だ DA, ぢ DI, づ DU, で DE, ど DO,
な NA, に NI, ぬ NU, ね NE, の NO, にゃ NYA, にゅ NYU, にょ NYO,
は HA, ひ HI, ふ HU, へ HE, ほ HO, ひゃ HYA, ひゅ HYU, ひょ HYO,
ば BA, び BI, ぶ BU, べ BE, ぼ BO, びゃ BYA, びゅ BYU, びょ BYO,
ぱ PA, ぴ PI, ぷ PU, ぺ PE, ぽ PO, ぴゃ PYA, ぴゅ PYU, ぴょ PYO,
ま MA, み MI, む MU, め ME, も MO, みゃ MYA, みゅ MYU, みょ MYO,
や YA,        ゆ YU,       よ YO,
ら RA, り RI, る RU, れ RE, ろ RO, りゃ RYA, りゅ RYU, りょ RYO,
わ WA,                     を WO,
ん N',

うぁ UXA, うぃ UXI,  うぅ UXU,   うぇ UXE, うぉ UXO,
ゔぁ VA,  ゔぃ VI,   ゔ VU,    ゔぇ VE,  ゔぉ VO,   ゔゃ VYA, ゔゅ VYU, ゔょ VYO,
                             しぇ SYE,
                             じぇ ZYE,
         てぃ TEXI, とぅ TOXU,
                             ちぇ TYE,
つぁ TSA, つぃ TSI,  つぇ TSE,           つぉ TSO,     
         でぃ DEXI, どぅ DOXU,                   ぢゃ DYA, ぢゅ DYU, ぢょ DYO,
ふぁ FA,  ふぃ FI,             ふぇ FE,  ふぉ FO,  ふゃ FYA, ふゅ FYU, ふょ FYO,
         いぃ  YI,            いぇ YE,
         ゐ WI,         ゑ WE,

ぁ XA, ぃ XI, ぅ XU, ぇ XE, ぉ XO, ゃ XYA, ゅ XYU, ょ XYO, ゎ XWA,

っ Q,
ー -
"""


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
#     print list(groups(re.split('\s', "a 1 b 2 cc 33,\nddd 444\teee 555")))