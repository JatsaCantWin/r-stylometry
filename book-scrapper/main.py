import requests
import re

import Book

books = []

for i in range(1700, 1701):
    url = "https://www.gutenberg.org/cache/epub/{}/pg{}.txt".format(i, i)
    print(url)
    downloadedData = r = requests.get(url)
    decodedData = downloadedData.text
    #Author = re.search(r'Author:.*$', decodedData, flags=re.MULTILINE).string
    Title = re.search("Author:.*", decodedData).string
    print(type(Title))

    #print(Author)
    print(Title)
