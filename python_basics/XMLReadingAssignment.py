import urllib.parse,urllib.request, urllib.error
import xml.etree.ElementTree as ET

xmlpath='http://py4e-data.dr-chuck.net/comments_2435531.xml'

fData= urllib.request.urlopen(xmlpath).read()
xmlDOM= ET.fromstring(fData)
sumTotal=0

numberElements=xmlDOM.findall('comments/comment/count')
print(len(numberElements))
for elm in numberElements:
    sumTotal=sumTotal+ int(elm.text)

print(f'Total is {sumTotal}')
