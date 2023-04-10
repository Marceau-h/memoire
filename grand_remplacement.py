# But : Remplacer les caractères spéciaux par leur équivalent en français dans le LGERM

import json
import re
import string


def custom_make_translation(text, translation):
    regex = re.compile(r'|'.join(map(re.escape, translation)))
    res = regex.sub(lambda match: translation[match.group(0)], text).lower()
    while True:
        symbole_relou = (res.find("ì\x82"), res.find("ì\x81"), res.find("ì\x83"), res.find("ì\x84"), res.find("ì\x80"),
                         res.find("ì\x88"))
        symbole_relou = [e for e in symbole_relou if e != -1]
        if not symbole_relou:
            break
        for e in symbole_relou:
            res = res[:e - 1] + accentue[res[e - 1]] + res[e + 2:]
    return res


def mot_is_french(mot):
    if any(char not in french_chars for char in mot):
        return False
    return True


def mot_is_romain(mot):
    if chriffre_romain.fullmatch(mot):
        return True
    return False


def mot_is_ok(mot):
    if not mot_is_french(mot) and not mot_is_romain(mot):
        return False
    return True


correspondances = {
    "Ã¢": "â",
    "Ã©": "é",
    "Ã¨": "è",
    "Ãª": "ê",
    "Ã«": "ë",
    "Ã®": "î",
    "Ã¯": "ï",
    "Ã´": "ô",
    "Ã¶": "ö",
    "Ã¹": "ù",
    "Ã»": "û",
    "Ã¼": "ü",
    "Ã§": "ç",
    "Å": "œ",
    "â¬": "€",
    "Â°": "°",
    "Ã": "À",
    "Ã": "Â",
    "Ã": "É",
    "Ã": "È",
    "Ã": "Ê",
    "Ã": "Ë",
    "Ã": "Î",
    "Ã": "Ï",
    "Ã": "Ô",
    "Ã": "Ö",
    "Ã": "Ù",
    "Ã": "Û",
    "Ã": "Ü",
    "Ã": "Ç",
    "Å": "Œ",
    "Ã¦": "æ",
    "Â©": "©",
    "Â¤": "¤",
    "à¦": "æ",
    "": "œ"
}

accentue = {
    "a": "à",
    "e": "è",
    "i": "ì",
    "o": "ò",
    "u": "ù",
    "y": "ỳ",
    "v": "v̀",
}

french_chars = {
    'è', 'é', 'ê', 'ë', 'î', 'ï', 'ô', 'œ', 'ù', 'û', 'ü', 'À', 'Â', 'Ä', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Î',
    'Ï', 'Ô', 'Œ', 'Ù', 'Û', 'Ü', 'à', 'â', 'ä', 'æ', 'ç', 'ÿ', '€', '°', 'ß', 'Ò', 'Õ', 'Ý', 'ò', 'ñ', 'ö', "á", "̀",
    "ó", "ì"
}.union(set(string.printable))

chriffre_romain = re.compile("([IVXLCDMivxlcdm]+\.?)|(·[IVXLCDMivxlcdmJjUu]+·)")

with open("correspondances.json", mode="w", encoding="utf-8") as f:
    json.dump(correspondances, f, indent=4, ensure_ascii=False)

with open("lexiques/LGERM.json") as f:
    LGERM = json.load(f)

for i, e in enumerate(LGERM):
    LGERM[i] = custom_make_translation(e, correspondances)

for e in LGERM:
    if not mot_is_ok(e):
        print(e)

with open("lexiques/LGERM.json", mode="w", encoding="utf-8") as f:
    json.dump(LGERM, f, indent=4, ensure_ascii=False)

# Pour l'instant, je ne vois pas comment remplacer les derniers caractères, du coup je les laisse tels quels.
