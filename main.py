# Twoim zadaniem jest utworzenie pakietu obsługi klienta w wypożyczalni
# Utwórz następujące moduły:
# 1. moduł main - moduł główny (administracja zasobami wypożyczalni)

from customerService import *
from addBook import *
from lendBook import *
from idGeneration import findId


def main():
    # addBook('Autor', 'Książka', '69')
    lendBooks(577, '040')


if __name__ == "__main__":
    main()
