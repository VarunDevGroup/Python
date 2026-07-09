import json
import urllib.parse, urllib.request, urllib.error


link='http://py4e-data.dr-chuck.net/comments_2435532.json'

try:
    lnkRespons=urllib.request.urlopen(link).read()

    jsonData= json.loads(lnkRespons)
  #  print(jsonData)
    lnCount=len(jsonData["comments"])
    totalCount=0
    print("Total items found:", lnCount)
    if lnCount>0:
        for item in jsonData["comments"]:
            totalCount=totalCount+ int(item["count"])

    print("total count:", totalCount)
except Exception as e:
    print("Error:", e)

