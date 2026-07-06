import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138.0 Safari/537.36"
}


url='https://www.ltm.com/'

req = urllib.request.Request(url, headers=headers)



fhand=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(fhand,'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('href',None))


#
#for line in fhand:
#    print(line.decode().strip())