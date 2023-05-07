from fixedTime import formattedCurrentTime
import idGeneration
import csv
from fieldnames import *


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
            csvWriter = csv.DictWriter(
                customersFile, fieldnames=customerFieldnames)
            csvWriter.writerow(customer)
        with open('address.csv', 'a', newline='') as addressFile:
            csvWriter = csv.DictWriter(
                addressFile, fieldnames=addressFieldnames)
            csvWriter.writerow(address)
    except Exception as e:
        print(f'An error occurred while adding the customer: {e}')


def deleteCustomer(id=None, name=None):
    customerRows = []
    addressRows = []
    with open('customer.csv', 'r', newline='') as customersFile:
        csvReader = csv.DictReader(
            customersFile, fieldnames=customerFieldnames)
        for row in csvReader:
            if (id is not None and row['ID'] == str(id)) or (name is not None and row['NAME'] == name):
                continue
            customerRows.append(row)

    with open('address.csv', 'r', newline='') as addressFile:
        csvReader = csv.DictReader(addressFile, fieldnames=addressFieldnames)
        for row in csvReader:
            if str(row['ID']) == str(id):
                continue
            addressRows.append(row)

    with open('customer.csv', 'w', newline='') as customersFile:
        csvWriter = csv.DictWriter(
            customersFile, fieldnames=customerFieldnames)
        csvWriter.writerows(customerRows)

    with open('address.csv', 'w', newline='') as addressFile:
        csvWriter = csv.DictWriter(addressFile, fieldnames=addressFieldnames)
        csvWriter.writerows(addressRows)


def registerCustomer(customerId):
    customerFileDir = f'DATABASE/{customerId}.csv'
    with open('customer.csv', 'r', newline='') as customersFile:
        csvReader = csv.DictReader(customersFile)
        for row in csvReader:
            if row['ID'] == customerId:
                print(f"Error: Customer ID {customerId} already exists!")
                return
    with open(customerFileDir, 'w', newline='')as customerPersonalFile:
        csvWriter = csv.DictWriter(
            customerPersonalFile, fieldnames=customerPersonalFieldnames)
        csvWriter.writeheader()
