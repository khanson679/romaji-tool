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

うぁ UXA, うぃ UXI,  うぅ UXU,  うぇ UXE, うぉ UXO,
ゔぁ VA,  ゔぃ VI,   ゔ   VU,   ゔぇ VE,  ゔぉ VO,  ゔゃ VYA, ゔゅ VYU, ゔょ VYO,
                              しぇ SYE,
                              じぇ ZYE,
         てぃ TEXI, とぅ TOXU,
                              ちぇ TYE,
つぁ TSA, つぃ TSI,  つぇ TSE,           つぉ TSO,     
         でぃ DEXI, どぅ DOXU,                    ぢゃ DYA, ぢゅ DYU, ぢょ DYO,
ふぁ FA,  ふぃ FI,             ふぇ FE,  ふぉ FO,  ふゃ FYA, ふゅ FYU, ふょ FYO,
         いぃ YI,             いぇ YE,
         ゐ WI,               ゑ WE,

ぁ XA, ぃ XI, ぅ XU, ぇ XE, ぉ XO, ゃ XYA, ゅ XYU, ょ XYO, ゎ XWA,

っ Q,
ー -
"""


#----------------------------------------------------------------------------
# Romaji conversion tables
#----------------------------------------------------------------------------

WAPURO_TAB = """\
a A,   i  I,  u  U,  e  E,  o  O,
ka KA, ki KI, ku KU, ke KE, ko KO, kya KYA, kyu KYU, kyo KYO,
ga GA, gi GI, gu GU, ge GE, go GO, gya GYA, gyu GYU, gyo GYO,
sa SA, si SI, su SU, se SE, so SO, sya SYA, syu SYU, syo SYO,
za ZA, zi ZI, zu ZU, ze ZE, zo ZO, zya ZYA, zyu ZYU, zyo ZYO,
ta TA, ti TI, tu TU, te TE, to TO, tya TYA, tyu TYU, tyo TYO,
da DA, di DI, du DU, de DE, do DO,
na NA, ni NI, nu NU, ne NE, no NO, nya NYA, nyu NYU, nyo NYO,
ha HA, hi HI, fu HU, he HE, ho HO, hya HYA, hyu HYU, hyo HYO,
ba BA, bi BI, bu BU, be BE, bo BO, bya BYA, byu BYU, byo BYO,
pa PA, pi PI, pu PU, pe PE, po PO, pya PYA, pyu PYU, pyo PYO,
ma MA, mi MI, mu MU, me ME, mo MO, mya MYA, myu MYU, myo MYO,
ya YA,        yu YU,        yo YO,
ra RA, ri RI, ru RU, re RE, ro RO, rya RYA, ryu RYU, ryo RYO,
wa WA,                      wo WO,
n N',

uxa UXA, uxi  UXI,   uxu UXU,  uxe UXE,  uxo UXO,
va  VA,  vi   VI,    vu  VU,   ve  VE,   vo  VO,  vya VYA, vyu VYU, vyo VYO,
                               sye SYE,
                               zye ZYE,
         texi TEXI, toxu TOXU,
                               tye TYE,
tsa TSA, tsi  TSI,  tse  TSE,            tso TSO,     
         dexi DEXI, doxu DOXU,                    dya DYA, dyu DYU, dyo DYO,
fa  FA,  fi   FI,              fe  FE,   fo  FO,  fya FYA, fyu FYU, fyo FYO,
         yi   YI,              ye  YE,
         wi   WI,              we  WE,

xa XA, xi XI, xu XU, xe XE, xo XO, xya XYA, xyu XYU, xyo XYO, xwa XWA,

xtu Q,
-   -
"""

NIHON_TAB = """\
a  A,  i  I,  u  U,  e  E,  o  O,
ka KA, ki KI, ku KU, ke KE, ko KO, kya KYA, kyu KYU, kyo KYO,
ga GA, gi GI, gu GU, ge GE, go GO, gya GYA, gyu GYU, gyo GYO,
sa SA, si SI, su SU, se SE, so SO, sya SYA, syu SYU, syo SYO,
za ZA, zi ZI, zu ZU, ze ZE, zo ZO, zya ZYA, zyu ZYU, zyo ZYO,
ta TA, ti TI, tu TU, te TE, to TO, tya TYA, tyu TYU, tyo TYO,
da DA, di DI, du DU, de DE, do DO, dya DYA, dyu DYU, dyo DYO,
na NA, ni NI, nu NU, ne NE, no NO, nya NYA, nyu NYU, nyo NYO,
ha HA, hi HI, hu HU, he HE, ho HO, hya HYA, hyu HYU, hyo HYO,
ba BA, bi BI, bu BU, be BE, bo BO, bya BYA, byu BYU, byo BYO,
pa PA, pi PI, pu PU, pe PE, po PO, pya PYA, pyu PYU, pyo PYO,
ma MA, mi MI, mu MU, me ME, mo MO, mya MYA, myu MYU, myo MYO,
ya YA,        yu YU,        yo YO,
ra RA, ri RI, ru RU, re RE, ro RO, rya RYA, ryu RYU, ryo RYO,
wa WA,                      wo WO,
n N',

kwa KWA,
gwa GWA
"""

KUNREI_TAB = """\
a  A,  i  I,  u  U,  e  E,  o  O,
ka KA, ki KI, ku KU, ke KE, ko KO, kya KYA, kyu KYU, kyo KYO,
ga GA, gi GI, gu GU, ge GE, go GO, gya GYA, gyu GYU, gyo GYO,
sa SA, si SI, su SU, se SE, so SO, sya SYA, syu SYU, syo SYO,
za ZA, zi ZI, zu ZU, ze ZE, zo ZO, zya ZYA, zyu ZYU, zyo ZYO,
ta TA, ti TI, tu TU, te TE, to TO, tya TYA, tyu TYU, tyo TYO,
da DA, di DI, du DU, de DE, do DO, dya ZYA, dyu ZYU, dyo ZYO,
na NA, ni NI, nu NU, ne NE, no NO, nya NYA, nyu NYU, nyo NYO,
ha HA, hi HI, fu HU, he HE, ho HO, hya HYA, hyu HYU, hyo HYO,
ba BA, bi BI, bu BU, be BE, bo BO, bya BYA, byu BYU, byo BYO,
pa PA, pi PI, pu PU, pe PE, po PO, pya PYA, pyu PYU, pyo PYO,
ma MA, mi MI, mu MU, me ME, mo MO, mya MYA, myu MYU, myo MYO,
ya YA,        yu YU,        yo YO,
ra RA, ri RI, ru RU, re RE, ro RO, rya RYA, ryu RYU, ryo RYO,
wa WA,                      wo WO,
n N'
"""

HEPBURN_TAB_BASE = """\
a  A,  i   I,  u   U,  e  E,  o  O,
ka KA, ki  KI, ku  KU, ke KE, ko KO, kya KYA, kyu KYU, kyo KYO,
ga GA, gi  GI, gu  GU, ge GE, go GO, gya GYA, gyu GYU, gyo GYO,
sa SA, shi SI, su  SU, se SE, so SO, sha SYA, shu SYU, sho SYO,
za ZA, zi  ZI, zu  ZU, ze ZE, zo ZO, ja  ZYA, ju  ZYU, jo  ZYO,
ta TA, chi TI, tsu TU, te TE, to TO, cha TYA, chu TYU, cho TYO,
da DA, di  DI, du  DU, de DE, do DO, ja  ZYA, ju  ZYU, jo  ZYO,
na NA, ni  NI, nu  NU, ne NE, no NO, nya NYA, nyu NYU, nyo NYO,
ha HA, hi  HI, fu  HU, he HE, ho HO, hya HYA, hyu HYU, hyo HYO,
ba BA, bi  BI, bu  BU, be BE, bo BO, bya BYA, byu BYU, byo BYO,
pa PA, pi  PI, pu  PU, pe PE, po PO, pya PYA, pyu PYU, pyo PYO,
ma MA, mi  MI, mu  MU, me ME, mo MO, mya MYA, myu MYU, myo MYO,
ya YA,         yu  YU,        yo YO,
ra RA, ri RI,  ru  RU, re RE, ro RO, rya RYA, ryu RYU, ryo RYO,
wa WA,
n N'
"""

HEPBURN_TAB_EXTENDED = """\
         wi  UXI,   wu UXU,  we  UXE, wo   UXO,
va  VA,  vi   VI,   vu  U,   ve  VE,  vo   VO,   vya VYA, vyu VYU, vyo VYO,
                             she SYE,
                             je  ZYE,
         texi ti,   toxu tu,
                             che TYE,
tsa TSA, tsi  TSI,           tse TSE, tso  TSO,     
         dexi DEXI,                   doxu DOXU,
fa  FA,  fi   FI,            fe  FE,  fo   FO,   fya FYA, fyu FYU, fyo FYO,
         yi   YI,            ye  YE,
"""

SOKUON_BASE = """\
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

SOKUON_HEPBURN = """\
tch QCH
ssh QSH
"""

SOKUON_WAPURO = """\
cch QCH
SSH QSH
"""

YOUON_MACRON = """\
ā A-,
ī I-,
ū U-,
ē E-,
ō O-
"""

YOUON_CIRCUMFLEX = """\
â A-,
î I-,
û U-,
ê E-,
ô O-
"""

YOUON_DOUBLE_VOWEL = """\
aa A-
ii I-
uu U-
ee E-
oo O-
"""


#
# init lemma data
#

LEMMAS_BASIC    = LEMMA_TAB_BASIC.split()
LEMMAS_EXTENDED = LEMMA_TAB_EXTENDED.split()
LEMMAS_EXTRA    = LEMMA_TAB_EXTRA.split()
LEMMAS_SMALL_KANA_POST = LEMMA_TAB_SMALL_KANA_POST.split()
LEMMAS = (LEMMAS_BASIC + LEMMAS_EXTENDED + LEMMAS_EXTRA +
        LEMMAS_SMALL_KANA_POST + [LEMMA_SOKUON, LEMMA_CHOUON])