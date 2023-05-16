from pathlib import Path
import pickle

import texte

paths = list(Path("Corpus/Mazarinades").glob("*/*.xml"))

collection_textes = [e for e in texte.corpora(paths) if e.plain]

print("save")

with open("collection_textes.pickle", mode="wb") as f:
    pickle.dump(collection_textes, f)

