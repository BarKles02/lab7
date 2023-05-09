import csv
from fixedTime import formattedCurrentTime
from fieldnames import *




def lendBooks(customerId, *args):
    booksStayingInLibrary = []
    booksLending = []
    with open('book.csv', 'r', newline='')as bookFile:
        csvReader = csv.DictReader(bookFile, fieldnames=bookFieldnames)
        lista=[wiersz for wiersz in csvReader]
        for arg in args:
            # bookFile.seek(0)
            for row in lista:
                if row['ID'] == arg:
                    booksLending.append(row)
                    continue
                booksStayingInLibrary.append(row)
    customerFileName = f'DATABASE/{customerId}.csv'
    with open(customerFileName, 'a', newline='')as customerFile:
        csvWriter = csv.DictWriter(
            customerFile, fieldnames=customerPersonalFieldnames)
        for book in booksLending:
            csvWriter.writerow({
                'ID': book['ID'],
                'AUTHOR': book['AUTHOR'],
                'TITLE': book['TITLE'],
                'PAGES': book['PAGES'],
                'CREATED': book['CREATED'],
                'HIRED': formattedCurrentTime(),
                'RETURNED': 'Not yet returned'
            })
    with open('book.csv', 'w', newline='') as bookFile:
        csvWriter = csv.DictWriter(bookFile, fieldnames=bookFieldnames)
        for book in booksStayingInLibrary:
            csvWriter.writerow(book)



def returnBook(customerId, bookId):
    booksReturning = []
    restOfTheBooks = []
    customerFileName = f'DATABASE/{customerId}.csv'
    with open(customerFileName, 'r', newline='')as customerFile:
        csvReader = csv.DictReader(
            customerFile, fieldnames=customerPersonalFieldnames)
        for row in csvReader:
            if row['ID'] == bookId:
                row['RETURNED'] = formattedCurrentTime()
                booksReturning.append(row)
                continue
            restOfTheBooks.append(row)
    with open(customerFileName, 'r', newline='')as customerFile:
        csvWriter = csv.DictWriter(
            customerFile, fieldnames=customerPersonalFieldnames)
        for book in restOfTheBooks:
            csvWriter.writerow(book)
        csvWriter.writerow(booksReturning)

    with open('book.csv', 'a', newline='') as bookFile:
        csvWriter = csv.DictWriter(bookFile, fieldnames=bookFieldnames)
        book = {
            'ID': booksReturning['ID'],
            'AUTHOR': booksReturning['AUTHOR'],
            'TITLE': booksReturning['TITLE'],
            'PAGES': booksReturning['PAGES'],
            'CREATED': booksReturning['CREATED'],
            'UPDATED': formattedCurrentTime()
        }
        csvWriter.writerow(book)
