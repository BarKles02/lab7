# 4. moduł wypożyczania książki przez użytkownika 2 funkcje
# funkcja 1 (wielu zmiennych): wypożyczenie książki lub
# kilku książek równocześnie przez klienta
# funkcja 2: zwrot 1 książki przez klienta
import csv
import os
from fixedTime import formattedCurrentTime

# with open('customer.csv', 'r', newline='') as customersFile:
#     csvReader = csv.DictReader(customersFile, fieldnames=[
#                                'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'])
#     for row in csvReader:
#         if (id is not None and row['ID'] == str(id)) or (name is not None and row['NAME'] == name):
#             continue
#         customerRows.append(row)


def lendBooks(customerId, *args):
    booksStayingInLibrary = []
    booksLending = []
    with open('book.csv', 'r', newline='')as bookFile:
        csvReader = csv.DictReader(bookFile, fieldnames=[
                                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'])
        for arg in args:
            bookFile.seek(0)
            for row in csvReader:
                if row['ID'] == arg:
                    booksLending.append(row)
                    continue
                booksStayingInLibrary.append(row)
    customerFileName = f'DATABASE/{customerId}.csv'
    with open(customerFileName, 'a', newline='') as customerFile:
        csvWriter = csv.writer(customerFile)
        for book in booksLending:
            csvWriter.writerow([book['ID'], formattedCurrentTime(),book['CREATED'] ''])
    with open('book.csv', 'w', newline='') as bookFile:
        csvWriter = csv.DictWriter(bookFile, fieldnames=[
                                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'])
        for book in booksStayingInLibrary:
            csvWriter.writerow(book)


def returnBook(customerId, bookId):
    customerFileName = f'DATABASE/{customerId}.csv'
    with open(customerFileName, 'r', newline='')as customerFile:
        csvReader = csv.DictReader(customerFile, fieldnames=[])
