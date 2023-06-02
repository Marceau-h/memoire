from pathlib import Path
import pickle

import texte
import pickle_test
paths = list(Path("Corpus/Mazarinades").glob("*/*.xml"))

collection_textes = [e for e in texte.corpora(paths) if e.plain]

print(f"sauvegarde de {len(collection_textes)} textes ...")

with open("collection_textes.pickle", mode="wb") as f:
    pickle.dump(collection_textes, f)

if __name__ == "__main__":
    pickle_test.main()
