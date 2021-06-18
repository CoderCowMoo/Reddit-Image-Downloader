import requests # Import requests for getting html and bs4 for parsing
from bs4 import BeautifulSoup
a = input('What subreddit? ').lower() #grab the lowered string of the subreddit.
site = requests.get('https://reddit.com/r/' + a + '/',  headers={'User-Agent': 'Chrome/91.0.4389.114'}) # Sending the request without the user agent header gives a 502 response
print(site) # Print the response for debugging purposes.
g = 0 # Initialise a counter.
soup = BeautifulSoup(site.text, features='html.parser') # Initialise the soup object
for img in soup.find_all('img', class_ = "ImageBox-image"): # for every img element with class ... do:
    imgSrc = img['src'] # Give imgSrc the value of the source image
    if 'external' in imgSrc: # If external is in the src, that means the preview and hosted image are the same
        link = imgSrc
    else: # Else, parse the image for the middle part which can be concatenated with 
        c = imgSrc.split('/')
        d = c[3].split('?')
        link = "https://i.redd.it/" + d[0] # this
    newName = soup.findAll('h3',{'class' : '_eYtD2XCVieq6emjKBH3m'})[g].text + '.jpg' # The name for the image will be its order in the page.
                                                                                      # Because the img name and the img are not relative
                                                                                      # there may be problems with syncing it.
    imgBytes = requests.get(link, stream= True, headers={'User-Agent': 'Chrome/91.0.4389.114'}) # Make another request to the direct image.
    file = open(newName, 'wb') # Open a file in write in binary mode
    file.write(imgBytes.content) # Write the image into it.
    file.close() # close it
    g += 1 #increment the counter
