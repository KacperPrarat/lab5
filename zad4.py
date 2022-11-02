liczba = int(input("Podaj liczbe dodatnia"))

i = 1
suma = 0

while i <= liczba:
    suma = suma + i
    i += 1

wynik = "Suma wszystkich liczb naturalnych niewiekszych niz {} wynosi {}"
wynik = wynik.format(liczba,suma)
print(wynik)