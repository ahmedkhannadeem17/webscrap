from urllib.request import urlopen

from bs4 import BeautifulSoup

import re
from data.prjct_vars import *



html_page=urlopen(murl)

bsobj=BeautifulSoup(html_page,features=bsfeature)

#to find all images
for x in bsobj.find_all('img'):
    print(x)

#filter imgX.jpg using re module
for x in bsobj.find_all('img',{'src':re.compile('.*\/img\d.jpg.*')}):
    print(x.parent)


