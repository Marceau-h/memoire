from pathlib import Path
import json

cwd = Path(__file__).parent

glaff = cwd / "../ressources/glaff-1.2.2.txt"
json_loc = cwd / "../glaff.json"

with open(glaff, mode="r", encoding="UTF-8") as f:
    lst = f.read().split("\n")

lst = [elt.strip() for elt in lst]


lst = [e[0] for elt in lst for e in elt.split("|", 1) if elt]

lst = [elt for elt in lst if elt]

with open(json_loc, mode="w", encoding="UTF-8") as f:
    json.dump(lst, f, ensure_ascii=False, indent=4)


