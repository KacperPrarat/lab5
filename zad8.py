import random
losowaliczba = random.randint(0,100)
liczbapodana = int(input("Podaj losowa liczbe"))
liczbastrzalow = 0
while liczbapodana != losowaliczba:
    liczbapodana = int(input("Podaj losowa liczbe"))
    liczbastrzalow = liczbastrzalow + 1
if liczbapodana == losowaliczba:
    print("Gratulacje wygrales")
    print("Liczba strzalow ",liczbastrzalow)

