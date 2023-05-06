# 2. moduł obsługi klienta zawierający 3 funkcje
# funkcja 1: dodawanie (przez administratora) danych
# nowego klienta do bazy tj. do pliku customer.csv i address.csv
# funkcja 2: usuwanie danych klienta względem ID lub NAME

# ID,NAME,E-MAIL,PHONE,CREATED,UPDATED
# ID,STREET,CITY,COUNTRY

from fixedTime import formattedCurrentTime
import idGeneration
import csv
import os


def addCustomer(name, email, phone, street, city, country):    
    try:
        created = formattedCurrentTime()
        updated = created
        identifier = idGeneration.fixedIdGeneration('customer.csv')
        customer = {
            'ID': identifier,
            'NAME': name,
            'E-MAIL': email,
            'PHONE': phone,
            'CREATED': created,
            'UPDATED': updated
        }

        address = {
            'ID': identifier,
            'STREET': street,
            'CITY': city,
            'COUNTRY': country
        }
        with open('customer.csv', 'a', newline='') as customersFile:
            csvWriter = csv.DictWriter(customersFile, fieldnames=[
                                       'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'])
            csvWriter.writerow(customer)
        with open('address.csv', 'a', newline='') as addressFile:
            csvWriter = csv.DictWriter(addressFile, fieldnames=[
                                       'ID', 'STREET', 'CITY', 'COUNTRY'])
            csvWriter.writerow(address)
        databaseDir = os.path.join(os.getcwd(), 'DATABASE')
        with open(os.path.join(databaseDir, identifier + '.csv',), 'w', newline='') as personFile:
            csvWriter = csv.DictWriter(personFile, fieldnames=[
                                       'BOOK', 'HIRED', 'RETURNED'])
            csvWriter.writeheader()
    except Exception as e:
        print(f'An error occurred while adding the customer: {e}')


def deleteCustomer(id=None, name=None):
    customerRows = []
    addressRows = []
    with open('customer.csv', 'r', newline='') as customersFile:
        csvReader = csv.DictReader(customersFile, fieldnames=[
                                   'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'])
        for row in csvReader:
            if (id is not None and row['ID'] == str(id)) or (name is not None and row['NAME'] == name):
                continue
            customerRows.append(row)

    with open('address.csv', 'r', newline='') as addressFile:
        csvReader = csv.DictReader(addressFile, fieldnames=[
                                   'ID', 'STREET', 'CITY', 'COUNTRY'])
        for row in csvReader:
            if str(row['ID']) == str(id):
                continue
            addressRows.append(row)

    with open('customer.csv', 'w', newline='') as customersFile:
        csvWriter = csv.DictWriter(customersFile, fieldnames=[
                                   'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'])
        csvWriter.writerows(customerRows)

    with open('address.csv', 'w', newline='') as addressFile:
        csvWriter = csv.DictWriter(addressFile, fieldnames=[
                                   'ID', 'STREET', 'CITY', 'COUNTRY'])
        csvWriter.writerows(addressRows)

# funkcja 3: rejestracja nowego klienta
# (klient podaje swoje dane, nadawany jest losowo numer ID (3 cyfry))
# w folderze DATABASE utworzony jest plik tekstowy (nazwa pliku to ID klienta)
# do którego będą zapisywane dane wypożyczonej książki oraz
# data wypożyczenia a potem zwrotu książki
