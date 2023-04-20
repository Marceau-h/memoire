import pickle

with open("collection_textes.pickle", mode="rb") as f:
    collection_textes = pickle.load(f)

print(collection_textes[0].__dict__)
