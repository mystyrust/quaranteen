import AO3
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

# print(sys.argv)

# username = input("Enter username: ")
# password = input("Enter password: ")

# session = AO3.Session(username, password)
# session.refresh_auth_token()


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
    "https://archiveofourown.org/works/19643287"
    , "https://archiveofourown.org/works/56373862"
]

for url in ficLinks:
    print("------------------------------------------------------------------------------------------------")
    
    workid = AO3.utils.workid_from_url(url)
    work = AO3.Work(workid=workid)

    print(f"title : {work.title} - {url}")
    
    authors = ", ".join(work.metadata["authors"])
    print(f"authors : {authors}") 
    print(f"rating : {work.rating}")
    
    fandoms = ", ".join(work.fandoms)
    print(f"fandoms : {fandoms}")

    print(f"words : {work.words}")
    print(f"expected_chapters : {work.expected_chapters}")
    print(f"Chapters: {work.nchapters}")
    
    categories = ", ".join(work.categories)
    print(f"categories : {categories}")
    
    relationships = ", ".join(work.relationships)
    print(f"ships : {relationships}")
    
    characters = ", ".join(work.characters)
    print(f"characters : {characters}")
    
    tags = ", ".join(work.tags)
    print(f"tags : {tags}") 

    warnings = ", ".join(work.warnings)
    print(f"warnings : {warnings}")
    
    # print(f"status : {work.status}")

    series = ", ".join(work.metadata["series"])
    print(f"series : {series}") 
    
    print(f"series : {work.series}") 
    for s in work.series:
        print(f"series url = {s.url}")
        series_info(url)
        
print("------------------------------------------------------------------------------------------------")
    