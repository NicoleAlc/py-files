# import your functions here
from utils import files
book1=files.readFile("el_quijote.txt")
book2=files.readFile("el_quijote_ii.txt")
print(book1 +book2)
# read the quijote here


# Word Count
# print('Word Count: ', files.wordCount(book))

# Unique Word Count
# print('Unique Word Count: ', files.uniqueWordCount(book))

# Quijote count
# print('find Content: ', files.findContent(book, 'quijote'))
# print('find Content: ', files.findContent(book, 'sancho'))

# Change Quijote to Quixote and write it to a new file "el_quixote.txt"
# print('Change Quijote to Quixote: ', files.changeQuijoteToQuixote(book))