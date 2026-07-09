import json, urllib.parse, urllib.request, urllib.error

link='http://py4e-data.dr-chuck.net/opengeo?'

city=input("Enter Location:")

try:
    param=dict()
    param['q']=city.strip()
    param['key']=42
    updatedURL= link + urllib.parse.urlencode(param)

    print(updatedURL)
    responseData=urllib.request.urlopen(updatedURL).read()
    jsonData=json.loads(responseData)
    print(f"Retrieved {len(responseData)} characters")

    print(jsonData["features"][0]["properties"]["plus_code"])

except Exception as e:
    print("Error :" , e)
