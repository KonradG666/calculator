

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
        nums = input("Podaj liczby (oddzielone spacją): ").split()
        # print(type(nums))
        # nums = num.split(",")

        wynik = 0

        for num in nums:
            wynik += int(num)
        print(f"Dodaje: {nums}")
        print(f'Wynik to {wynik}')

        # print(f"Wynik to: ", sum(num))

    elif more_digits == "N":
        num1, num2 = set_input()
        print(f"Dodaje {num1} i {num2}")
        print(f"Wynik to: ", num1 + num2)


def multi_more():
    more_digits2 = input("Chcesz pomnożyć więcej cyfr jednocześnie? Y/N:")
    if more_digits2 == "Y":
        nums = input("Podaj liczby (oddzielone spacją): ").split()

        wynik = 1

        for num in nums:
            wynik *= int(num)
        print(f"Mnożę: {nums}")
        print(f'Wynik to {wynik}')


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