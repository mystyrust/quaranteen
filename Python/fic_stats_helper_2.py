# python3.9 Python/fic_stats_helper.py

import AO3
import json
import sys
import string
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


# todo, get wordcounts for singular chapters? 
# support multiple series entries in the future

def getSession():
    with open('./Python/sandbox-test-credential.json', 'r') as config_file:
        config = json.load(config_file)

    username = config['ao3_username']
    password = config['ao3_password']

    session = AO3.Session(username, password)
    session.refresh_auth_token()
    return session

def ratingsHelper(rating):
    if rating == "General Audiences":
        return "G"
    elif rating == "Teen And Up Audiences":
        return "T"
    elif rating == "Mature":
        return "M"
    elif rating == "Explicit":
        return "E"
    else: 
        return "Not Rated"

def warningsHelper(warningString):
    warning1 = warningString.replace("Graphic Depictions Of Violence", "Graphic Depictions of Violence")
    warning2 = warning1.replace("Rape/Non-Con", "Rape/Non-con")
    warning3 = warning2.replace("Creator Chose Not To Use Archive Warnings", "Creator Chose Not to Use Archive Warnings")
    return warning3

def seriesHelper1(ao3work):
    soup = ao3work.request(ao3work.url)
    # print("using series helper to get part in series")
    
    dd = soup.find("dd", {"class": "series"})
    if dd is None: 
        return ()
    if dd is not None:
        first_span = dd.find("span", {"class": "position"})
        seriesname = first_span.a.getText()
        seriespart = first_span.getText().replace("Part ", "").replace(f" of {seriesname}", "")
        seriesid = int(first_span.a.attrs["href"].split("/")[-1])
        seriesurl = f"https://archiveofourown.org/series/{seriesid}"
        
        # '=HYPERLINK("https://www.example.com", "Example Link")
        seriesurlInput = f'=HYPERLINK("{seriesurl}", "{seriesname}")'
        return (seriesurlInput, seriespart, seriesname, seriesurl)
       
def ficStatsHelper(ficLinks, session, month="October"):   
    allStats = []

    for url in ficLinks:
        
        ficStats = []
        print("------------------------------------------------------------------------------------------------")
        
        # session = getSession()
        workid = AO3.utils.workid_from_url(url)
        work = AO3.Work(workid=workid, session=session)
        # work = AO3.Work(workid=workid)
        
        completionStatus = "Complete" if work.expected_chapters == work.nchapters else "Awaiting new chapter"
        ficStats.append(completionStatus)

        print(f"title : \n{work.title}\n")
        print(f"url : \n{url}\n")
        
        ficStats.append(f'=HYPERLINK("{url}", "{work.title}")')
        
        authors = ", ".join(work.metadata["authors"])
        print(f"authors : \n{authors}\n") 
        ficStats.append(authors)
        ficStats.append("")
        
        print(f"rating : \n{work.rating}\n")
        ficStats.append(ratingsHelper(work.rating))
        
        fandoms = ", ".join(work.fandoms)
        print(f"fandoms : \n{fandoms} \n")
        ficStats.append(fandoms)

        print(f"words : {work.words}")
        ficStats.append(work.words)
        print(f"expected_chapters : {work.expected_chapters}")
        print(f"Chapters: {work.nchapters}")
        ficStats.append(work.expected_chapters)
        ficStats.append(work.nchapters)
        print(f"words : {work.words}")
        ficStats.append(work.words)
        
        categories = ", ".join(work.categories)
        print(f"categories : \n{categories}\n")
        ficStats.append(categories.split(",")[0])
        
        relationships = ", ".join(work.relationships)
        print(f"ships : \n{relationships} \n")
        ficStats.append('')
        ficStats.append(relationships)
        
        characters = ", ".join(work.characters)
        print(f"characters : \n{characters} \n")
        ficStats.append(characters)
        
        tags = ", ".join(work.tags)
        print(f"tags : \n{tags} \n") 
        ficStats.append(tags)

        warnings = ", ".join(work.warnings)
        print(f"warnings : {warnings}\n")
        ficStats.append(warningsHelper(warnings))
        
        # print(f"status : {work.status}")

        series = ", ".join(work.metadata["series"])
        print(f"series : \n{series}\n") 
        
        seriesData = seriesHelper1(work)
        if len(seriesData) > 0:
            ficStats.append(seriesData[0])
            ficStats.append(seriesData[1])
        else:
            ficStats.append("")
            ficStats.append("")
            
        # for s in work.series:
        #     print(f"series url = \n{s.url}")
        #     # series_info(url)
            
        # notes col, fill in manually later
        ficStats.append("")
        
        # print(ficStats)
        # print(f"series : {work.series}") 
        isBookmarked = work._bookmarkid

        ficStats.append("Yes" if isBookmarked is not None else "No")
        ficStats.append(month)
        
        allStats.append(ficStats)
    print("------------------------------------------------------------------------------------------------")
    return allStats
