def calculate():
    operation = int(input("""
    Podaj działanie: 
    1 Dodawanie, 
    2 Odejmowanie, 
    3 Mnożenie, 
    4 Dzielenie, 
    5 Exit: 
    """))

    if operation in (1, 2, 3, 4, 5):

        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if operation == 1:
            print("Dodaję %s i %s" % (num1, num2))
            print("Wynik to: ", (num1 + num2))
        elif operation == 2:
            print("Odejmuję %s i %s" % (num1, num2))
            print("Wynik to: ", (num1 - num2))
        elif operation == 3:
            print("Mnożę %s i %s" % (num1, num2))
            print("Wynik to: ", (num1 * num2))
        elif operation == 4:
            print("Dzielę %s i %s" % (num1, num2))
            print("Wynik to: ", (num1 / num2))
        elif operation == 5:
            end()

    repeat()


def repeat():
    text = input("Czy chcesz liczyć dalej? Y/N: ")
    if text == "Y":
        calculate()
    elif text == "N":
        end()


def end():
    print("End of counting")
    exit()

calculate()

import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("debug")


def calculate():
    operation = int(input("""
    Podaj działanie: 
    1 Dodawanie, 
    2 Odejmowanie, 
    3 Mnożenie, 
    4 Dzielenie, 
    5 Exit: 
    """))

    if operation in (1, 2, 3, 4, 5):

        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if operation == 1:
            logging.debug("Dodaję %s i %s" % (num1, num2))
            logging.debug("Wynik to: ", (num1 + num2))
        elif operation == 2:
            logging.debug("Odejmuję %s i %s" % (num1, num2))
            logging.debug("Wynik to: ", (num1 - num2))
        elif operation == 3:
            logging.debug("Mnożę %s i %s" % (num1, num2))
            logging.debugt("Wynik to: ", (num1 * num2))
        elif operation == 4:
            logging.debug("Dzielę %s i %s" % (num1, num2))
            logging.debug("Wynik to: ", (num1 / num2))
        elif operation == 5:
            end()

    repeat()


if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    string = sys.argv[1]


def repeat():
    text = input("Czy chcesz liczyć dalej? Y/N: ")
    if text == "Y":
        calculate()
    elif text == "N":
        end()


def end():
    print("End of counting")
    exit()


calculate()