import re
from pathlib import Path

import requests
from tqdm.auto import tqdm

link = re.compile(r'<a href="(.*)">')


def get_links(url):
    r = requests.get(url)
    return link.findall(r.text)


def get_xmls(url):
    return [x for x in get_links(url) if x.endswith(".xml")]


def xml_download(url, path):
    r = requests.get(url)
    with open(path, mode="wb") as f:
        f.write(r.content)


def main(path: Path, url, renew=False):
    if renew:
        try:
            past = [x.name for x in path.iterdir()]
        except FileNotFoundError:
            past = []
    else:
        past = []

    xmls = get_xmls(url)
    for xml in tqdm(xmls):
        if xml in past:
            continue
            
        xml_download(url + xml, path / xml)


if __name__ == "__main__":
    path = Path("ducange_xmls")
    path.mkdir(exist_ok=True)

    url = "http://svn.code.sf.net/p/ducange/code/xml/"
    main(path, url)
