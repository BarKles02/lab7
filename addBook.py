import idGeneration
import csv
import customerService
from fieldnames import *


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
            bookFile, fieldnames=bookFieldnames)
        csvWriter.writerow(book)
