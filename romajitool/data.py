"""
Raw data sources for lemma lists and mappings.
"""

# lemmas used in native Japanese words
# includes base moras, dakuon, handakuon,and youon
# dya/dyu/dyo are omitted due to lack of standard use
LEMMA_TAB_BASE = """\
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
Q
-
"""

# lemmas for borrowed words
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
"""

# lemmas for archaic kana
LEMMA_TAB_ARCHAIC = """\
    WI        WE
"""

# lemmas for rarely used kana
LEMMA_TAB_RARE = """\
UXA    UXU
               VYA VYU VYO
               DYA DYU DYO
               FYA FYU FYO
    YI
"""

# use to handle non-standard use of small kana
LEMMA_TAB_SMALL_KANA = "XA XI XU XE XO   XYA XYU XYO   XWA"

# special lemmas
# SOKUON = "Q"
# CHOUON = "-"


# ---------------------------------------------------------------------------
# Support data
# ---------------------------------------------------------------------------

SOKUON_CONSONANTS = "KGSZTDHFBP"


# ---------------------------------------------------------------------------
# Kana conversion tables
#
# Used to map kana <-> lemmas
# Derived from python-romkan, itself based on KAKASI
#   <http://kakasi.namazu.org/>
# ---------------------------------------------------------------------------

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

KATAKANA_TAB = """\
ア A,  イ I,  ウ U,  エ E,  オ O,
カ KA, キ KI, ク KU, ケ KE, コ KO, キャ KYA, キュ KYU, キョ KYO,
ガ GA, ギ GI, グ GU, ゲ GE, ゴ GO, ギャ GYA, ギュ GYU, ギョ GYO,
サ SA, シ SI, ス SU, セ SE, ソ SO, シャ SYA, シュ SYU, ショ SYO,
ザ ZA, ジ ZI, ズ ZU, ゼ ZE, ゾ ZO, ジャ ZYA, ジュ ZYU, ジョ ZYO,
タ TA, チ TI, ツ TU, テ TE, ト TO, チャ TYA, チュ TYU, チョ TYO,
ダ DA, ヂ DI, ヅ DU, デ DE, ド DO,
ナ NA, ニ NI, ヌ NU, ネ NE, ノ NO, ニャ NYA, ニュ NYU, ニョ NYO,
ハ HA, ヒ HI, フ HU, ヘ HE, ホ HO, ヒャ HYA, ヒュ HYU, ヒョ HYO,
バ BA, ビ BI, ブ BU, ベ BE, ボ BO, ビャ BYA, ビュ BYU, ビョ BYO,
パ PA, ピ PI, プ PU, ペ PE, ポ PO, ピャ PYA, ピュ PYU, ピョ PYO,
マ MA, ミ MI, ム MU, メ ME, モ MO, ミャ MYA, ミュ MYU, ミョ MYO,
ヤ YA,        ユ YU,       ヨ YO,
ラ RA, リ RI, ル RU, レ RE, ロ RO, リャ RYA, リュ RYU, リョ RYO,
ワ WA,                     ヲ WO,
ン N',

ウァ UXA, ウィ UXI,  ウゥ UXU,  ウェ UXE, ウォ UXO,
ゔァ VA,  ゔィ VI,   ゔ   VU,   ゔェ VE,  ゔォ VO,  ゔャ VYA, ゔュ VYU, ゔョ VYO,
                              シェ SYE,
                              ジェ ZYE,
         ティ TEXI, トゥ TOXU,
                              チェ TYE,
ツァ TSA, ツィ TSI,  ツェ TSE,           ツォ TSO,
         ディ DEXI, ドゥ DOXU,                    ヂャ DYA, ヂュ DYU, ヂョ DYO,
ファ FA,  フィ FI,             フェ FE,  フォ FO,  フャ FYA, フュ FYU, フョ FYO,
         イィ YI,             イェ YE,
         ヰ WI,               ヱ WE,

ァ XA, ィ XI, ゥ XU, ェ XE, ォ XO, ャ XYA, ュ XYU, ョ XYO, ヮ XWA,

ッ Q,
ー -
"""


# ---------------------------------------------------------------------------
# Romaji conversion tables
# ---------------------------------------------------------------------------

# WAPURO_TAB = """\
# a A,   i  I,  u  U,  e  E,  o  O,
# ka KA, ki KI, ku KU, ke KE, ko KO, kya KYA, kyu KYU, kyo KYO,
# ga GA, gi GI, gu GU, ge GE, go GO, gya GYA, gyu GYU, gyo GYO,
# sa SA, si SI, su SU, se SE, so SO, sya SYA, syu SYU, syo SYO,
# za ZA, zi ZI, zu ZU, ze ZE, zo ZO, zya ZYA, zyu ZYU, zyo ZYO,
# ta TA, ti TI, tu TU, te TE, to TO, tya TYA, tyu TYU, tyo TYO,
# da DA, di DI, du DU, de DE, do DO,
# na NA, ni NI, nu NU, ne NE, no NO, nya NYA, nyu NYU, nyo NYO,
# ha HA, hi HI, fu HU, he HE, ho HO, hya HYA, hyu HYU, hyo HYO,
# ba BA, bi BI, bu BU, be BE, bo BO, bya BYA, byu BYU, byo BYO,
# pa PA, pi PI, pu PU, pe PE, po PO, pya PYA, pyu PYU, pyo PYO,
# ma MA, mi MI, mu MU, me ME, mo MO, mya MYA, myu MYU, myo MYO,
# ya YA,        yu YU,        yo YO,
# ra RA, ri RI, ru RU, re RE, ro RO, rya RYA, ryu RYU, ryo RYO,
# wa WA,                      wo WO,
# n N',

# uxa UXA, uxi  UXI,   uxu UXU,  uxe UXE,  uxo UXO,
# va  VA,  vi   VI,    vu  VU,   ve  VE,   vo  VO,  vya VYA, vyu VYU, vyo VYO,
#                                sye SYE,
#                                zye ZYE,
#          texi TEXI, toxu TOXU,
#                                tye TYE,
# tsa TSA, tsi  TSI,  tse  TSE,            tso TSO,
#          dexi DEXI, doxu DOXU,                    dya DYA, dyu DYU, dyo DYO,
# fa  FA,  fi   FI,              fe  FE,   fo  FO,  fya FYA, fyu FYU, fyo FYO,
#          yi   YI,              ye  YE,
#          wi   WI,              we  WE,

# xa XA, xi XI, xu XU, xe XE, xo XO, xya XYA, xyu XYU, xyo XYO, xwa XWA,

# xtu Q,
# -   -
# """

ROMAJI_TAB_BASE = """\
a  A,  i  I,  u  U,  e  E,  o  O,
ka KA, ki KI, ku KU, ke KE, ko KO, kya KYA, kyu KYU, kyo KYO,
ga GA, gi GI, gu GU, ge GE, go GO, gya GYA, gyu GYU, gyo GYO,
sa SA,        su SU, se SE, so SO,
za ZA, zi ZI, zu ZU, ze ZE, zo ZO,
ta TA,               te TE, to TO,
da DA,               de DE, do DO,
na NA, ni NI, nu NU, ne NE, no NO, nya NYA, nyu NYU, nyo NYO,
ha HA, hi HI,        he HE, ho HO, hya HYA, hyu HYU, hyo HYO,
ba BA, bi BI, bu BU, be BE, bo BO, bya BYA, byu BYU, byo BYO,
pa PA, pi PI, pu PU, pe PE, po PO, pya PYA, pyu PYU, pyo PYO,
ma MA, mi MI, mu MU, me ME, mo MO, mya MYA, myu MYU, myo MYO,
ya YA,        yu YU,        yo YO,
ra RA, ri RI, ru RU, re RE, ro RO, rya RYA, ryu RYU, ryo RYO,
wa WA,
n' N'
"""

NIHON_TAB = """\
si SI,
zi ZI,
ti TI, tu TU,
di DI, du DU,
hu HU,

sya SYA, syu SYU, syo SYO,
zya ZYA, zyu ZYU, zyo ZYO,
tya TYA, tyu TYU, tyo TYO,
dya DYA, dyu DYU, dyo DYO
"""

KUNREI_TAB = """\
si SI,
zi ZI,
ti TI, tu TU,
hu HU,

sya SYA, syu SYU, syo SYO,
zya ZYA, zyu ZYU, zyo ZYO,
tya TYA, tyu TYU, tyo TYO
"""

KUNREI_TAB_OUTONLY = """\
zi DI, zu DU, zya DYA, zyu DYU, zyu DYO
"""

HEPBURN_TAB = """\
shi SI,
ji  ZI,
chi TI, tsu TU,
fu  HU,

sha SYA, shu SYU, sho SYO,
ja  ZYA, ju  ZYU, jo  ZYO,
cha TYA, chu TYU, cho TYO
"""

HEPBURN_TAB_OUTONLY = """\
ji DI, zu DU, ja DYA, ju DYU, jo DYO
"""

ROMAJI_TAB_HEPBURN_EXTENDED = """\
         wi  UXI,           we  UXE, wo   UXO,
va  VA,  vi  VI,   vu VU,   ve  VE,  vo   VO,
                            she SYE,
                            je  ZYE,
         ti  TEXI, tu TOXU,
                            che TYE,
tsa TSA, tsi TSI,           tse TSE, tso  TSO,
         di  DEXI, du DOXU,
fa  FA,  fi  FI,            fe  FE,  fo   FO,
                            ye  YE
"""

ROMAJI_TAB_HEPBURN_EXTRA = """\
wu UXU,
vya VYA, vyu VYU, vyo VYO,
fya FYA, fyu FYU, fyo FYO,
yi  YI
"""

ROMAJI_TAB_HEPBURN_EXTRA_OUTONLY = """\
wa  UXA
"""

ARCHAIC_WAGYO_RETAIN_W = "wi WI, we WE, wo WO"

ARCHAIC_WAGYO_DROP_W = "i WE, e WE, o WO"

SOKUON_TAB_BASE = """\
kk QK,
gg QG,
ss QS,
zz QZ,
tt QT,
dd QD,
hh QH,
bb QB,
pp QP
"""

SOKUON_TAB_HEPBURN = """\
tch QCH
"""

SOKUON_TAB_HEPBURN_EXTENDED = """\
jj  QJ,
ff  QF
"""

SOKUON_TAB_HEPBURN_ALTERNATE = """\
cch QCH
"""

CHOUON_MACRON = """\
ā A-,
ī I-,
ū U-,
ē E-,
ō O-
"""

CHOUON_CIRCUMFLEX = """\
â A-,
î I-,
û U-,
ê E-,
ô O-
"""

CHOUON_DOUBLE_VOWEL = """\
aa A-,
ii I-,
uu U-,
ee E-,
oo O-
"""

# character mapping tables turn out not to work for nasal spelling,
#  because end of word/string needs to be referenced

# NASAL_BASE = """\
# n'a N'A,
# n'i N'I,
# n'u N'U,
# n'e N'E,
# n'o N'U,
# nk  N'K,
# ng  N'G,
# ns  N'S,
# nz  N'Z,
# nt  N'T,
# nd  N'D,
# nn  N'N,
# nh  N'H,
# nm  N'M,
# n'y N'Y,
# nr  N'R,
# nw  N'W,
# n   N'
# """

# NASAL_HEPBURN = """\
# nch n'CH
# nj N'J
# """

# NASAL_EXTENDED = """\
# nf N'F,
# nv N'V
# """

# NASAL_ALTERNATE = """\
# mp N'P,
# mb N'B,
# mm N'M
# """
