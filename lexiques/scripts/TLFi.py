import json
from pathlib import Path

cwd = Path(__file__).parent

tlfi = cwd / "../ressources/tlfi.txt"
json_loc = cwd / "../tlfi.json"


with open(tlfi, mode="r", encoding="UTF-8") as f:
    lst = f.read().split("\n")


with open(json_loc, mode="w", encoding="UTF-8") as f:
    json.dump(lst, f, indent=4, ensure_ascii=False)

print(len(lst))
