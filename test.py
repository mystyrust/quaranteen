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

# xs = ['d', 'e']
# urlSet.update(xs)
# print("len is", len(urlSet))
# print(urlSet)

# for url in urls:

    # filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    # print(filename)
    #if not filename:
    #     print("Regex didn't match with the url: {}".format(url))
    #     continue
    #with open(filename.group(1), 'wb') as f:
    #    if 'http' not in url:
    #        # sometimes an image source can be relative 
    #        # if it is provide the base url which also happens 
    #        # to be the site variable atm. 
    #        url = '{}{}'.format(site, url)
    #    response = requests.get(url)
    #    f.write(response.content)

# print(soup) 
# print(soup.find_all("div", class_="amongus-dead"))