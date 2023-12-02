# installs
# pip3 install beautifulsoup4
# pip3 install pathlib2 ???

# to run: python3 test.py

import urllib.request 
from bs4 import BeautifulSoup
from pathlib2 import Path 

quarnateensFilePaths = ["./Quaranteens/quarantine-3.html"]
            # ["./Quaranteens/quarantine-1.html"
            #  "./Quaranteens/quarantine-2.2.html", 
            #  "./Quaranteens/quarantine-3.html", 
            #  "./Quaranteens/quarantine-4.html", 
            #  "./Quaranteens/quarantine-6.html",
            #  "./Quaranteens/quarantine-7v2.html"]

urlSet = set()

for filePath in quarnateensFilePaths:
    currentFile = open(filePath, "r") 
    contents = currentFile.read() 
    soup = BeautifulSoup(contents, 'html.parser') 
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    urlSet.update(urls)

print("len is", len(urlSet))

urlRefs = {}

for url in urlSet:
    # ignore progress-tracker and github images
    print(url)
    filename="Test/" + url.split('/')[-1] 
    urllib.request.urlretrieve(url, filename) 
    urlRefs.update({ url : filename })
print(urlRefs)

for filePath in quarnateensFilePaths:
    file = Path(filePath) 
    data = file.read_text() 
    # get the urlRefs for THIS file only, at this step
    for url, location in urlRefs.items():

        data = data.replace(url, "../"+location)
        # todo , use github raw location
        # format -> https://raw.githubusercontent.com/mystyrust/quaranteen/master/[path/to/file.png/jpg/etc]
        # example -> https://raw.githubusercontent.com/mystyrust/quaranteen/master/Images/Gifs/portal.webp
    
    file.write_text(data) # write back to the same file
    
    # todo update url ref in quarnateensFilePaths
    # maybe create a dict { key = url, value = new downloaded path }
    # then open each file , create the set for just that file, 
    # use that set to select only the keys you need from the dict, update refs in place

# figure out how to modularize this ^^^^
# maybe later

# todo maaaybe organize??
# after downloading and updating refs for all 7 ch
# visually sort into folders by character
# update file name and ref in html concurrently 
# something like , all the danny images in 1 folder, name them numberically, 
# keep dict of updated names,
# update ref in html at the same time.