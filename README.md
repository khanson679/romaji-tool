# romaji-tools

Python library to convert between different forms of Japanese Kana and romanization via an intermediate representation based on "wapuro" style romaji.

```python
>>> import romajitools as rt
>>> rt.convert(u"はんおう", in_fmt="hiragana", out_fmt="wapuro")
u"han'ou"
```


## Features

When complete, will convert between the following formats to the greatest extent possible:
- Hiragana
- Katakana (+ half width)
- Kunrei romaji
- Hepburn romaji (traditional, modern, wapuro-style vowels)
- An extreme form of "wapuro" romaji (keystrokes typically entered into an IME, e.g. "texi" to produce "ティ")

Will also allow the user to specify various options for details like the spelling of long vowels, and will include a command line interface for easy use from a Unix shell.

Mapping rules mostly encoded in plain text tables rather than code for maximum simplicity and clarity.


## Status

Pre-alpha. Currently, only the Hiragana format is fully implemented. Only tested on Python 2.7 on Ubuntu (14.04 LTS, 15.10).


[rk]: https://github.com/soimort/python-romkan "python-romkan"
