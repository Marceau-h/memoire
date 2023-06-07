import pickle
import re

with open("collection_textes.pickle", mode="rb") as f:
    collection_textes = pickle.load(f)
crade = re.compile(r"([liIba1]* ?)+")


for txt in collection_textes:
    texte = txt.texte
    if not texte: continue

    for page in texte:
        for line in page:
            if re.fullmatch(crade, line):
                print(line)


                
                
                
                
