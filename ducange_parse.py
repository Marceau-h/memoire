from pathlib import Path
import re
from bs4 import BeautifulSoup
from tqdm.auto import tqdm
import json

xmldir = Path("ducange_xmls")
jsondir = Path("ducange_json")
jsondir.mkdir(exist_ok=True)

xmls = list(xmldir.glob("*.xml"))

cleaner = re.compile(r"(\t+)|(\n+)|(\d+.?)|(\.)|(-)")

for xml in tqdm(xmls):
    print(xml)
    with open(xml, mode="r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml")
        soup = soup.find("body")

    forms = (e.text.lower() for e in soup.find_all("form"))
    forms = (f for form in forms for f in form.split(","))
    forms = (re.sub(cleaner, "", form) for form in forms)
    forms = (re.sub(r" +", " ", form) for form in forms)
    forms = (form.strip() for form in forms)
    forms = (form for form in forms if form)





    forms = sorted(list(set(forms)))

    with open(jsondir / (xml.stem + ".json"), mode="w", encoding="utf-8") as f:
        json.dump(list(forms), f, indent=4, ensure_ascii=False)

allforms = []
for jsonfile in jsondir.glob("*.json"):
    with open(jsonfile, mode="r", encoding="utf-8") as f:
        allforms.extend(json.load(f))

allforms = sorted(list(set(allforms)))

allforms = json.dumps(allforms, indent=4, ensure_ascii=False)

files = (jsondir / "allforms.json", Path("ducange.json"))

for file in files:
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(allforms)




