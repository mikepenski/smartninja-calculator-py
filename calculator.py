"""
Homework 7.3: Calculator

Write a program that does the basic arithmetic operations:

addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
"""

from calculator_functions import addition, subtraktion, division, multiplikation, logarithmus, quadrat, wurzel

print("\n")
print("Taschenrechner App")
print("#"*25)
print("#"*25)
print("\n")


zahl1 = 0
zahl2 = 0
operator = None
bedingung = True

while bedingung:

    operator = input("Welche Rechenart möchtest du durchführen? (' + ' - ' / ' * ' x² ' log ' wurzel') ").strip()

    if operator in ["+", "-", "/", "*"]:

        try:
            zahl1 = int(input("Wie lautet die erste Zahl? ").strip())
            zahl2 = int(input("Wie lautet die zweite Zahl? ").strip())
        except:
                    print("\n")
                    print("Es ist ein Fehler aufgetreten! Bitte überprüfe deine Eingaben")


    elif operator in ["log", "wurzel", "x²"]:

        try:
            zahl1 = int(input("Wie lautet Ihre Zahl: ").strip())
        except Exception as error:
            print("Es ist ein Fehler aufgetreten! Bitte überprüfe deine Eingaben")
            continue

    if (operator == "+") :
            addition(zahl1, zahl2)

    elif (operator == "-"):
            subtraktion(zahl1, zahl2)

    elif (operator == "/"):
            division(zahl1, zahl2)

    elif (operator == "*"):
            multiplikation(zahl1, zahl2)

    elif operator == "log":
            logarithmus(zahl1)

    elif operator == "x²":
            quadrat(zahl1)

    elif operator == "wurzel":
            wurzel(zahl1)

    decision = input("Möchtest du weiter rechnen? (Bestätigen mit: ja / nein) ")

    if decision != 'ja':
        print("\n")
        print("Taschenrechner beendet")
        bedingung = False
