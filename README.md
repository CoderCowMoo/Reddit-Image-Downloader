# Reddit-Image-Downloader
This is an image downloader from reddit written in python. Input the subreddit and it will give 7 images from that subreddit. It bypasses the previews and goes straight to the i.redd.it image. I used requests instead of PRAW because PRAW is extremely slow while this works in seconds to download the images. It also doesn't write the image to disk if the image already exists, therefore allowing the script to be run perhaps at startup and only receive the newest images.

## Possible future changes
1. Make it get all the images from the first page of the subreddit.
2. Change the desktop wallpaper randomly to an image.
