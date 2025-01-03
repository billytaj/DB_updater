import os
import sys
import urllib
import urllib.request
import json
import xmltojson
#https://www.geeksforgeeks.org/convert-html-source-code-to-json-object-using-python/
#----------------------------------------------
#webscraper to automate DB updates from various sources.
#https://realpython.com/python-web-scraping-practical-introduction/
if __name__ == "__main__":
    place_to_pull = "https://huttenhower.sph.harvard.edu/humann2_data/chocophlan/"
    ncbi = "https://ftp.ncbi.nlm.nih.gov/blast/db/"
    
    #page_obj = urllib.request.urlopen(ncbi)
    page_obj = urllib.request.urlopen(place_to_pull) 
   
    page_bytes = page_obj.read()
    html = page_bytes.decode("utf-8")

    line = html.split("\t")
    
    print(line)
    for item in line:
        count = 0
        if(".tar.gz" in item):
            cleaned_line = item.strip("\n")
            #cleaned_line = cleaned_line.strip(" ")
            #cleaned_line = cleaned_line.strip("\t")
            #cleaned_line = cleaned_line.split("</a>")
            print(count, cleaned_line)
            count += 1
            #for i in cleaned_line:
            #    print(count, i)
            #    count += 1
