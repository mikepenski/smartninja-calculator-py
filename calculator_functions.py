import math

def addition(zahl1, zahl2):
    print("\n")
    print("Deine Rechnung:", zahl1, " + ", zahl2)
    print("Ergebnis:", zahl1 + zahl2)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Addition: " + str(zahl1 + zahl2))
        f.write("\n")

def subtraktion(zahl1, zahl2):
    print("\n")
    print("Deine Rechnung:", zahl1, " - ", zahl2)
    print("Ergebnis:", zahl1 - zahl2)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Subtraktion: " + str(zahl1 - zahl2))
        f.write("\n")

def division(zahl1, zahl2):
    print("\n")
    print("Deine Rechnung:", zahl1, " / ", zahl2)
    print("Ergebnis:", zahl1 / zahl2)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Division: " + str(zahl1 / zahl2))
        f.write("\n")

def multiplikation(zahl1, zahl2):
    print("\n")
    print("Deine Rechnung:", zahl1, " * ", zahl2)
    print("Ergebnis:", zahl1 * zahl2)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Multiplikation: " + str(zahl1 * zahl2))
        f.write("\n")

def quadrat(zahl1):
    print("\n")
    print("Deine Rechnung:", zahl1," ² ")
    print("Ergebnis:", zahl1 * zahl1)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Quadrat: " + str(zahl1 * zahl1))
        f.write("\n")

def logarithmus(zahl1):
    ergebnis =  math.log(zahl1)
    print("\n")
    print("Deine Zahl:", zahl1)
    print("Ergebnis:", ergebnis)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Logarithmus: " + str(ergebnis))
        f.write("\n")

def wurzel(zahl1):
    ergebnis =  math.sqrt(zahl1)
    print("\n")
    print("Deine Zahl:", zahl1)
    print("Ergebnis:", ergebnis)
    print("-" * 25)
    with open("ergebisse.txt", "a") as f:
        f.write("Ergebnis Wurzel: " + str(ergebnis))
        f.write("\n")