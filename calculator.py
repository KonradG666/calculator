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