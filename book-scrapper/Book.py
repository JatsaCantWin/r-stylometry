class Book:
    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content
    def saveToFile(self, directoryPath):
        file = open("./"+directoryPath+"/"+self.author + "|" + self.title, "w")
        file.write(self.content)
        file.close()
