import requests
from bs4 import BeautifulSoup
a = input('What subreddit? ').lower()
site = requests.get('https://reddit.com/r/' + a + '/',  headers={'User-Agent': 'Chrome/91.0.4389.114'})
print(site)
g = 0
soup = BeautifulSoup(site.text, features='html.parser')
for img in soup.find_all('img', class_ = "ImageBox-image"):
    imgSrc = img['src']
    if 'external' in imgSrc:
        link = imgSrc
    else:
        c = imgSrc.split('/')
        d = c[3].split('?')
        link = "https://i.redd.it/" + d[0]
    newName = soup.findAll('h3',{'class' : '_eYtD2XCVieq6emjKBH3m'})[g].text + '.jpg'
    imgBytes = requests.get(link, stream= True, headers={'User-Agent': 'Chrome/89.0.4389.114'})
    file = open(newName, 'wb')
    file.write(imgBytes.content)
    file.close()
    g += 1
