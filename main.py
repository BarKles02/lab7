# Twoim zadaniem jest utworzenie pakietu obsługi klienta w wypożyczalni
# Utwórz następujące moduły:
# 1. moduł main - moduł główny (administracja zasobami wypożyczalni)

from customerService import *
from addBook import *
from lendBook import *
from idGeneration import findId


def main():
    # addCustomer('Bartłomiej Kleszczewski', 'pulpecikpucipuci@gmail.com',
    #  '795318141', 'Pogodna 2', 'Białystok', 'Poland')
    # deleteCustomer(id=451)
    # addBook('Adam Mickiewicz', 'Dziady', '290')
    lendBooks(577, findId(
    'book.csv', 'TITLE', 'Dziady'))
    # returnBook(577, 138)


if __name__ == "__main__":
    main()
