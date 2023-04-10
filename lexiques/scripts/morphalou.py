import pandas as pd
from pathlib import Path
import json

fic = Path("../ressources/morphalou_clean.csv")
newfic = Path("../morphalou.json")

df = pd.read_csv(fic, sep=";", low_memory=False)

df = set(df["GRAPHIE.1"].dropna())

with open(newfic, mode="w", encoding="utf-8") as f:
    json.dump(list(df), f, indent=4, ensure_ascii=False)

