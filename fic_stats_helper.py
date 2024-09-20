# python3.9 fic_stats_helper.py

import AO3
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from getpass import getpass

# print(sys.argv)

username = input("Enter username: ")
password = getpass("Enter password: ")

session = AO3.Session(username, password)
session.refresh_auth_token()

def series_info(fic_url):
    page = requests.get(fic_url)
    soup = BeautifulSoup(page.content, "html.parser")
    series_div_list = soup.find_all("div", class_= "series")
    # print(series_div_list)
    if len(series_div_list) > 0:
        # print(series_div_list)
        position = series_div_list[0].find_all("span", class_="position")
        for p in position:
            print(p.get_text())
    else:
        print("no series")
        
ficLinks = [  
    #  "https://archiveofourown.org/works/41220345/chapters/106019919" #10
    # , "https://archiveofourown.org/works/43564573"
]


for url in ficLinks:
    print("------------------------------------------------------------------------------------------------")
    
    workid = AO3.utils.workid_from_url(url)
    work = AO3.Work(workid=workid, session=session)
    # work = AO3.Work(workid=workid)

    print(f"title : \n{work.title}\n")
    print(f"url : \n{url}\n")
    
    authors = ", ".join(work.metadata["authors"])
    print(f"authors : \n{authors}\n") 
    print(f"rating : \n{work.rating}\n")
    
    fandoms = ", ".join(work.fandoms)
    print(f"fandoms : \n{fandoms} \n")

    print(f"words : {work.words}")
    print(f"expected_chapters : {work.expected_chapters}")
    print(f"Chapters: {work.nchapters}")
    
    categories = ", ".join(work.categories)
    print(f"categories : \n{categories}\n")
    
    relationships = ", ".join(work.relationships)
    print(f"ships : \n{relationships} \n")
    
    characters = ", ".join(work.characters)
    print(f"characters : \n{characters} \n")
    
    tags = ", ".join(work.tags)
    print(f"tags : \n{tags} \n") 

    warnings = ", ".join(work.warnings)
    print(f"warnings : {warnings}\n")
    
    # print(f"status : {work.status}")

    series = ", ".join(work.metadata["series"])
    print(f"series : \n{series}\n") 
    
    # print(f"series : {work.series}") 
    for s in work.series:
        print(f"series url = \n{s.url}")
        # series_info(url)
        
print("------------------------------------------------------------------------------------------------")
    