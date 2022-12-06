class Book:
    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content
    def saveToFile(self, directoryPath):
        self.normalizeAuthorAndTitleForWindows()
        file = open("./"+directoryPath+"/"+self.author + "␞" + self.title, "w")
        file.write(self.content)
        file.close()
    def normalizeAuthorAndTitleForWindows(self):
        ReplaceChars = {
            "\"" : "''",
            "<" : "ᐸ",
            ">" : "ᐳ",
            ":" : "ː",
            "/" : "᜵",
            "\\" : "∖",
            "|" : "∣",
            "*" : "∗"
        }
        for key in ReplaceChars:
            self.author.replace(key, ReplaceChars[key])
            self.title.replace(key, ReplaceChars[key])