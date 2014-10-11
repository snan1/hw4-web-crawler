import urllib.request
import json
from pprint import pprint

query=input("query: ")
query = query.strip(" ").split() #get rid of the front and rear spaces, space being the delimiter
query = list(set(query))
str1="http://api.openweathermap.org/data/2.5/weather?q="
a=len(query)
if (len(query)<=1):
    str2=query[0]
elif(len(query)>1):
    str2 = query[0]+query[1]
str3=str1+str2    
page = urllib.request.urlopen(str3)
code=page.getcode()
print(code)
if (code==200):
    content=page.read()
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    if(json_data["weather"] in json_data[""]):
        print(json_data["weather"][0]["main"])
    else:
        content=page.read()
