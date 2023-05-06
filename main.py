# Twoim zadaniem jest utworzenie pakietu obsługi klienta w wypożyczalni
# Utwórz następujące moduły:
# 1. moduł main - moduł główny (administracja zasobami wypożyczalni)

from customerService import *
from addBook import *
from lendBook import *
from idGeneration import findId


def main():
    addCustomer('Tajemniczy Klient', 'jakisemail@gmail.com',
                '696969696', 'Szkolna', 'Whiteslide', 'Poland')


if __name__ == "__main__":
    main()
