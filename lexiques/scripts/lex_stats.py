import json
from pathlib import Path

cwd = Path(__file__).parent

jsons = cwd.parent.glob("*.json")

for json_loc in jsons:
    with open(json_loc, mode="r", encoding="UTF-8") as f:
        lst = json.load(f)
    print(json_loc.stem, len(lst).__format__('_d'))
