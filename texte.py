import contextlib
import glob
import json
import re
from collections import Counter

import xmltodict
from bs4 import BeautifulSoup
from numpy import mean
from tqdm import tqdm


def eval_sub_type(str_):
    if str_ == "no":
        return False
    elif str_ == "yes":
        return True
    else:
        return str_


with open("LGERM.json", encoding="utf-8") as f:
    LGERM = json.load(f)
mots_LGERM = set(LGERM)


def corpora(path):
    if isinstance(path, str):
        path = glob.glob(path)

    for file in tqdm(path):
        yield Texte(file)


class Texte:
    lexique = mots_LGERM

    def __init__(self, path):
        self.elts = None

        self.ttrs = None
        self.ttr = None

        self.hapaxes = None
        self.hapax = None
        self.hapax_ratio = None

        self.texte = None
        self.plain = None
        self.pages = None

        self.lexicalites = None
        self.lexicalite = None
        self.lignes_non_lexicalisees = 0

        self.n_words = None
        self.n_lines = None
        self.n_pages = None
        self.n_chars = None

        self.path = path

        with open(path, encoding="utf-8") as f:
            self.txt = f.read()

            self.header = self.process_header()

            self.process_body()

    def get_txt(self):
        return self.txt

    def __repr__(self):
        return f"{self.__class__.__name__}({self.txt!r})"

    def __str__(self):
        return self.txt

    def __len__(self):
        return len(self.txt)

    def process_header(self):
        dict_ = xmltodict.parse(self.txt)
        dict_ = dict_["TEI"]["teiHeader"]

        header = dict_["profileDesc"]["textClass"]["keywords"]["term"]
        header = [{header["@type"]: header["#text"] if "#text" in header else eval_sub_type(
            header["@subtype"]) if "@subtype" in header else None} for header in header]

        dict_header = {}
        for dicts in header:
            for k, v in dicts.items():
                if k not in dict_header:
                    dict_header[k] = []
                dict_header[k].append(v)

        dict_header = {k: v if len(v) > 1 else v[0] for k, v in dict_header.items()}

        with contextlib.suppress(KeyError):
            creation = dict_["profileDesc"]["settingDesc"]["setting"]["date"]
            if creation is None:
                dict_header["creation"] = "00-00-0000"
            else:
                dict_header["creation"] = creation["@when"] if "@when" in creation else creation["#text"]

        dict_header["change"] = dict_["revisionDesc"]["change"]

        titre = dict_["fileDesc"]["titleStmt"]["title"]
        titre = [e for e in titre if e["@type"] == "main"][0]["#text"]
        dict_header["titre"] = titre if isinstance(titre, str) else " ".join(titre)

        dict_header["dates"] = dict_["fileDesc"]["publicationStmt"]["date"]

        return dict_header

    def get_header(self):
        return self.header

    def process_body(self):
        tei_head = re.search(r"<teiHeader>.*?</teiHeader>", self.txt, re.DOTALL).group()

        soup = BeautifulSoup(tei_head, "html.parser")

        elts = {
            e.tag: e.text
            for e in soup.find_all()
        }

        txt = re.split(r"(?:<pb .*?>)", self.txt)[1:]
        txt = [re.split(r"\n|<lb/>|<l>", line) for line in txt]
        txt = [[re.sub(r"<.*?>|  |\t", "", line) for line in page] for page in txt]
        txt = [[line for line in page if line.strip()] for page in txt]
        txt = [page for page in txt if page]

        pages = [' '.join(line for line in page) for page in txt]

        plain = ' '.join(mot for page in txt for line in page for mot in line)

        if not plain:
            print(f"Empty file: {self.path = }")
            return

        self.texte = txt

        self.elts = elts

        self.n_pages = len(self.txt)
        self.n_lines = sum(len(page) for page in txt)
        self.n_words = len(plain.split())
        self.n_chars = sum(len(line) for page in txt for line in page)

        # if self.n_words == 0:
        #     print(f"Empty file: {self.path = }")
        #     print(f"{self.n_lines = }")
        #     print(f"{self.n_words = }")
        #     print(f"{self.n_chars = }")
        #     print(f"{self.n_pages = }")

        self.ttrs = [self.mesurer_ttr(page) for page in pages]
        self.ttr = mean(self.ttrs)

        self.lexicalites = [self.mesurer_lexicalite(page) for page in pages]
        self.lexicalite = mean(self.lexicalites)

        self.hapaxes = [self.mesurer_hapax(page) for page in pages]
        self.hapax = sum(self.hapaxes)
        self.hapax_ratio = self.hapax / self.n_words

        self.pages = pages
        self.plain = plain

    def mesurer_ttr(self, text):
        mots = text.split()
        vocabulaire = set(mots)
        if not mots:
            raise ValueError(f"Empty string, {self.path = }")
        return len(vocabulaire) / len(mots)

    def mesurer_lexicalite(self, text):
        tokens = text.split()
        mots_LGERM = self.lexique

        mots = [mot for mot in tokens if mot in mots_LGERM]

        if not mots:
            self.lignes_non_lexicalisees += 1
            return 0 # -1  a retester

        return len(mots) / len(tokens)

    @staticmethod
    def mesurer_hapax(text):
        mots = text.split()
        count = Counter(mots)
        return sum(1 for mot, occurrences in count.items() if occurrences == 1)


if __name__ == "__main__":
    path = "Corpus/Mazarinades/*/*.xml"

    testfile = "Corpus/Mazarinades/1-100/Moreau3_MAZ.xml"

    texte = Texte(testfile)
    print(texte.__dict__)

    liste = list(corpora(path))
