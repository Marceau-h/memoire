from pathlib import Path

fic = Path("../ressources/Morphalou3.1_CSV.csv")

with open(fic, encoding="utf-8") as f:
    content = f.read().split("\n")[15:]

content = "\n".join(content)

newfic = Path("../ressources/morphalou_clean.csv")

with open(newfic, mode="w", encoding="utf-8") as f:
    f.write(content)
