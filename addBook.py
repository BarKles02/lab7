# ID,AUTHOR,TITLE,PAGES,CREATED,UPDATED
# 3. moduł obsługi książek zawierający 1 funkcję:
# funkcja 1: dodanie nowej książki do bazy (book.csv)
import idGeneration
import csv
import customerService


def addBook(author, title, pages):
    created = customerService.formattedCurrentTime()
    updated = created
    book = {
        'ID': idGeneration.fixedIdGeneration('book.csv'),
        'AUTHOR': author,
        'TITLE': title,
        'PAGES': pages,
        'CREATED': created,
        'UPDATED': updated
    }
    with open('book.csv', 'a', newline='')as bookFile:
        csvWriter = csv.DictWriter(
            bookFile, fieldnames=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'])
        csvWriter.writerow(book)
