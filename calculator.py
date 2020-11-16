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


def calculate():
    operation = int(input("""
Wybierz funkcję, posługując się adekwatną liczbą:
1-Dodawanie
2-Odejmowanie
3-Mnożenie
4-Dzielenie
5-Exit
"""))


    if operation in (1, 2, 3, 4, 5):


        if operation == 1:
            print("Dodawanie")
            add_more_numbers()
        elif operation == 2:
            print("Odejmowanie")
            num1, num2 = set_input()
            print(f"Odejmuję {num1} i {num2}")
            print(f"Wynik to: ", num1 - num2)
        elif operation == 3:
            print("Mnożenie")
            multi_more()
        elif operation == 4:
            print("Dzielenie")
            num1, num2 = set_input()
            print(f"Dzielę {num1} i {num2}")
            print(f"Wynik to: ", num1 / num2)
        elif operation == 5:
            end()

    repeat()


def repeat():
    text = input("Czy chcesz liczyć dalej? Y/N: ")
    if text == "Y":
        calculate()
    elif text == "N":
        end()


def add_more_numbers():
    more_digits = input("Chcesz dodać więcej cyfr jednocześnie? Y/N:")
    if more_digits == "Y":
        num = int(input("Podaj liczby: "))
        print(f"Dodaje: {num}")
        print(f"Wynik to: ", sum(num))
        # TU COS NIE ŚMIGA Z 3 LINIJEK OSTATNICH
    elif more_digits == "N":
        num1, num2 = set_input()
        print(f"Dodaje {num1} i {num2}")
        print(f"Wynik to: ", num1 + num2)


def multi_more():
    more_digits2 = input("Chcesz pomnożyć więcej cyfr jednocześnie? Y/N:")
    if more_digits2 == "Y":
        num = int(input("Podaj liczby: "))
        print(f"Mnożę: {num} przez {num}")
        print(f"Wynik to: ", num * num)
        # TU COS NIE ŚMIGA Z 3 LINIJEK OSTATNICH
    elif more_digits2 == "N":
        num1, num2 = set_input()
        print(f"Mnożę {num1} i {num2}")
        print(f"Wynik to: ", num1 * num2)


def set_input():
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    return num1, num2


def end():
    print("Do widzenia.")
    exit()


calculate()