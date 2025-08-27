# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

POSITION_TO_GET = 18
ITERATIONS = 7
FIRST_URL = "http://py4e-data.dr-chuck.net/known_by_Lowena.html"

for i in range(ITERATIONS):
    if i == 0:
        url = FIRST_URL

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    pos = 0
    for tag in tags:
        pos = pos + 1
        if pos == POSITION_TO_GET:
            print(f"{tag['href']} {tag.text}")
            url = tag['href']
            break
