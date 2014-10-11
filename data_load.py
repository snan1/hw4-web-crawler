import os
import pickle
import fnmatch

def get_traversal_data():
    mylist = []
    mytuple=()
    start_dir = "fortune1"
    for dirpath, sub_dirs, files in os.walk(start_dir):
        for single_file in files:
            file_path = os.path.abspath(os.path.join(dirpath, single_file))
            if (fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log")):
                f = open(os.path.join(dirpath, single_file))
                data=f.read()
                mytuple=(file_path, data)
                mylist.append(mytuple)
    g=open("raw_data.txt","bw")
    pickle.dump(mylist,g)
    g.close()

get_traversal_data()

