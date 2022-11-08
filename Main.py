import os
import io
import urllib.parse

from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.parse import urlparse
from urllib.request import Request

url = "https://www.datasciencecentral.com/top-10-projects-for-data-science-and-machine-learning/"
#url = "https://www.techopedia.com/definition/26184/c-plus-plus-programming-language"
####################################################################################################
# https://understandingdata.com/python-for-seo/how-to-extract-text-from-multiple-webpages-in-python/
# https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

url = "https://www.labri.fr/perso/nrougier/from-python-to-numpy/"


train_db = open("train-db.txt", 'w', encoding='utf-8')

# kill all root-nodes in DOM-model: script and style elements
for node in raw(["script", "style", "header", "footer", "noscript", "iframe", "svg", "button", "img", "span"]):
    node.extract()   # cut it out


def parseURL(url, train_db):
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    html = urllib.request.urlopen(req).read()
    raw = BeautifulSoup(html, features="html.parser")
    
    parse(raw, train_db)

    # get text
    text = raw.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)

def parse(soup, train_db):
    h1 = False
    for item in soup(["h1", "h2", "h3", "h4", "p", "a"]):
        if item.name == 'h1':
            h1 = True
        if h1 == True:
            txt = item.get_text().replace('\n', ' ')
            print(txt)
            
 def parseFile(filename, train_db):
    soup = BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")
    parse(soup, train_db)
            
 def list_dir(dir_path):
    i = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if (file.endswith(".html")):
                print(os.path.join(root, file))
                parseFile(os.path.join(root, file), train_db)
                i += 1
                print(i)

# clean raw text
parse(url, "")
