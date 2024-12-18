import os
import sys
import urllib
import urllib.request

#----------------------------------------------
#webscraper to automate DB updates from various sources.
#https://realpython.com/python-web-scraping-practical-introduction/
if __name__ == "__main__":
    place_to_pull = "https://huttenhower.sph.harvard.edu/humann2_data/chocophlan/"
    page_obj = urllib.request.urlopen(place_to_pull)
     
    page_bytes = page_obj.read()
    html = page_bytes.decode("utf-8")

    