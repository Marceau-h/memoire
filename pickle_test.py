import pickle


def main():
    with open("collection_textes.pickle", mode="rb") as f:
        collection_textes = pickle.load(f)

    print(f"chargement de {len(collection_textes)} textes")

    print(f"collection_textes[0] = \n{collection_textes[0].__dict__}")


if __name__ == "__main__":
    main()
