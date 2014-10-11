import searcher
import indexer
from indexer import query
import data_load
import crawler_new

indexer.process_data("raw_data.txt","shelve_file")
indexer.process_data("raw_data1.txt","shelve_file")

searcher.search("shelve_file",query)
