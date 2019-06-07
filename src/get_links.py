from urllib.request import urlopen
from data.prjct_vars import bsfeature
from bs4 import BeautifulSoup

murl='https://en.wikipedia.org/wiki/Microscope'
html_page=urlopen(murl)
bsobj=BeautifulSoup(html_page,bsfeature)


"""
Get All links from Wikipedia page excluding all translated versions
"""
for eachlink in bsobj.find_all('a'):
    if 'href' in eachlink.attrs:
        link=eachlink.attrs['href']
        if 'https' in link and 'wikipedia' not in link:
            print(link)
