import requests
import re

from Book import Book

downloaded = 0

FIRST_BOOK_ID = 2000
BOOK_COUNT = 50

for i in range(FIRST_BOOK_ID, FIRST_BOOK_ID+BOOK_COUNT+1):
    url = "https://www.gutenberg.org/cache/epub/{}/pg{}.txt".format(i, i)
    downloadedData = r = requests.get(url)
    decodedData = downloadedData.text
    Author = re.search("(?<=Author: ).*", decodedData)
    Title = re.search("(?<=Title: ).*", decodedData)
    Content = re.search("\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*.*End of the Project Gutenberg", decodedData, flags=re.DOTALL)

    if (Author != None) and (Title != None) and (Content != None):
        Author = Author.group(0)
        Title = Title.group(0)
        Content = Content.group(0)
        Content = Content[Content.find('\n'):Content.rfind('\n')].strip()
        currentBook = Book(Author, Title, Content)
        currentBook.saveToFile('./corpora/corpus-a/corpus')
        downloaded += 1

print(downloaded)