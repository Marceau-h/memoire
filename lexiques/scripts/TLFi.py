import json

with open("../ressources/Tlfi.txt", mode="r", encoding="UTF-8") as f:
    lst = f.read().split("\n")

with open("../tlfi.json", mode="w", encoding="UTF-8") as f:
    json.dump(lst, f, indent=4, ensure_ascii=False)
