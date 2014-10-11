import urllib.request
import json
from pprint import pprint
import pickle
import shelve

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
content=page.read()
if (code == 200):
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    pprint(json_data)

def process_data(pickle_file, shelve_file):
    global dict_words
    dict_words = {}
    wordList=[]
    i=0
    h=open(pickle_file,"br")
    mylist2=pickle.load(h)
    shelve_file = shelve.open(shelve_file)
    for quote_tuple in mylist2:
        quote_list=list(quote_tuple[1:])
        for quote_string in quote_list:
            words = quote_string.split()
            for word in words:
                dict_words.setdefault(word,[]).append(quote_tuple[0:1])
   

                    
    for key,value in dict_words.items():
        shelve_file[key]=(value)
    h.close
    shelve_file.close()
    
process_data("raw_data.txt","shelve_file")
