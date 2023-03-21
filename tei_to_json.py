import json
from pathlib import Path

import texte

old = Path("Corpus/Mazarinades")
new = Path("JSONS")

files = list(old.glob("**/*.xml"))  # On en fait une liste pour tqdm (progression)

collection_textes = (e for e in texte.corpora(files) if e.plain)

lst = [[files[i], e.header, e.texte] for i, e in enumerate(collection_textes)]

for e in lst:
    file = Path(e[0])
    parent = file.parent.name

    newpath = new.joinpath(parent)
    newpath.mkdir(parents=True, exist_ok=True)

    file = file.with_suffix(".json").name
    newpath = newpath.joinpath(file)

    tempdict = {
        "entête": e[1],
        "texte": e[2]
    }
    with open(newpath, mode="w", encoding="utf-8") as f:
        json.dump(tempdict, f, indent=4, ensure_ascii=False)
