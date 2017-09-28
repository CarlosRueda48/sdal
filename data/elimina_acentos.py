# -*- coding: utf-8 -*-
import unicodedata
text = open("sdal.json").read()
def eliminatildes(s):
    c = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return c.decode()
final_text = eliminatildes(text)
print(final_text)