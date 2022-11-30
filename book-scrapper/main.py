import  urllib.request
from bs4 import BeautifulSoup
import re
file_name = "demostenes-wybor-mow"
text = urllib.request.urlopen("https://wolnelektury.pl/media/book/txt/"+file_name+".txt")
txt_str = BeautifulSoup(text)

file_to_save =open("../Corpuses/corpus_a/corpus/"+file_name+".txt", "w")

print(txt_str)
#file_to_save.write(txt_str.prettify())

#file_to_save.write(str(txt_str.html.encode('utf8')))
