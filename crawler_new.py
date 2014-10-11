import urllib.request
from urllib.error import  URLError
import re
import pickle
import shelve

web_tuple=()
web_list=[]
def visit_url(url, domain, web_tuple, web_list):
    global crawler_backlog
    if(len(crawler_backlog)>10):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        #print("Processing:", url)
        #url_list.append(url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>.*)</title>')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")

            result = regexp_title.search(content_string, re.IGNORECASE)
            
            if result:
                title = result.group("title")
                title=title[26:]
                title=title.lower()
                title_list=title.split()
                for title_word in title_list:
                    web_tuple=(url, title_word)
                    web_list.append(web_tuple)
                    #url_dict.setdefault(title_word,[]).append(url)                
                #print(title,'\n')


            for (urls) in re.findall(regexp_url, content_string):
                    if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                        crawler_backlog[urls] = 0
                        visit_url(urls, domain, web_tuple, web_list)

                        
    except URLError as e:
        print("error")

    x = open("raw_data1.txt","bw")
    pickle.dump(web_list,x)
    x.close
    
    #shelve_web = shelve.open("web_shelve")
    #for key,value in url_dict.items():
        #shelve_web[key]=(value)
    
    #shelve_web.close()
        
crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu", web_tuple, web_list)

#y=open("raw_data1.txt","br")
#z=pickle.load(y)
#print(z)
