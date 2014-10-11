import os
import shelve
def search(d, query):				#search function
    def file_size(FilePath):            #function to get file size
        for FilePath_str in FilePath:
                    print("Found in: ... ", FilePath)
                    print("File Size: ", os.path.getsize(FilePath_str))

    def last_modified_date(FilePath):       #function to get file's last modified date
        for FilePath_str in FilePath:
            print("Last Modified Date: ", os.path.getmtime(FilePath_str),'\n')

    Found_List=[]
    dict_words=shelve.open(d)

    if ("or" in query) and ("and" not in query): #"OR" search
        query.remove("or")
        print("Performing OR search for: ", query)
        for item in query:
            if (item in dict_words):
                query_list=[]
                query_list=query_list+dict_words[item]
                query_list=list(set(query_list))
                for item in query_list: 
                    print("Found in ... ",item,'\n')
                    #file_size(item)
                    #last_modified_date(item)

        #if(query[0] in dict_words):
            #search_logic_OR(dict_words,query)
        #elif(query[1] in dict_words):
                #search_logic_OR(dict_words,query)
        #else:
            #print("keyword not found in dictionary")

#        else:
#            print( "'{keyword}' Not Found... Please Enter Valid Keyword!".format(keyword=item))
            

    elif("and" in query) or (len(query)>1 and ("and" not in query)and("or" not in query)):
        if "and" in query:
            query.remove("and")
        if "or" in query:
            query.remove("or")
        print ("Performing AND search for: ",query)
        list_dict1=dict_words[query[0]]
        for a in query[1:]:
            list_dict2=dict_words[a]
            list_dict1=list(set(list_dict1).intersection(list_dict2))
        for thing in list_dict1:
            print("Found in ...", thing, '\n')
            #file_size(thing)
            #last_modified_date(thing)
            
    elif((len(query)==1) and ("and" not in query)and("or" not in query)):
        print ("Searching for: ",query)
        dict_words[query[0]]=list(set(dict_words[query[0]]))
        for value in dict_words[query[0]]:
            print("Found in...", value,'\n')
            #file_size(value)
            #last_modified_date(value)


